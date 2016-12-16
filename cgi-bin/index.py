#!/usr/bin/python2.4
# -*- coding: UTF-8 -*-
#!c:/Python24/python.exe

import sys

from quixote.publish import Publisher
from quixote.directory import Directory, Resolving
from quixote.util import StaticDirectory, StaticFile
from quixote import get_field, get_response, redirect, get_request, get_session

from session2.SessionManager import SessionManager

from quixote.directory import Directory
from quixote.form import Form, StringWidget

import kid, Image, smtplib
from cStringIO import StringIO

from baseconfig import *
from classes import *


class RootDirectory(Directory):

    _q_exports = ['', 'about', 'prices', 'addinfo', 'fulllist', 'mostviewed', 'search',
        'image', 'login', 'logout', 'edit', 'sendMessage', 'mostviewedcategories']

    def page(self, title='', breadcrumbs=None, message='', content='', **kwargs):
        return kid.Template(
            file=templatesDir+'main.kid',
            title = TITLE + title,
            news = NEWS,
            nav_links = NAV_LINKS,
            popular_links = POPULAR_LINKS,
            advert_links = ADVERT_LINKS,
            last_changed_links = database.getLastChanged(),
            breadcrumbs = breadcrumbs,
            message = message,
            page_content = content,
            database = database,
            COLUMNS_ORDER = COLUMNS_ORDER,
            is_logged = self.is_authorised(),
            query = kwargs.get('query', '')
        ).serialize(output='html')


    def _q_index(self):
        """ Render site homepage """
        content = kid.Template(
            file=templatesDir+'homepage.kid',
            COLUMNS_ORDER=COLUMNS_ORDER,
            database=database
        ).serialize(output='html', fragment=1)
        return self.page(title=u"Главная страница", content=content)


    def _q_lookup(self, component):
        obj = database.get_object(component)
        if obj:
            session = get_session()
            if session.addToVisited(component):
                obj.counter = int(obj.counter) + 1
#               database.save()
            content = obj.as_html(database, self.is_authorised())
            return self.page(title=database.get_full_title(obj.oid), breadcrumbs=obj.get_parents(database), content=content)
        else:
            return self.page(title=u'Ошибка', content='Объект %s не существует' % component)


    def edit(self):
        if not self.is_authorised():
            return self.page(title=u'Редактирование объекта', content='Вы должны пройти авторизацию для получения возможности редактировать контент.')

        # we get data from URL:
        # action : del | edit | update | new
        # object_kind : category | entity
        # parent : oid of parent object

        oid  = str(get_field('oid'))
        action = get_field('action')
        object_kind = get_field('object_kind')
        parent = get_field('parent')

        if not oid and not action:
            return "No required fields detected"

        try:
            obj = database.get_object(oid)
        except:
            return "Can't get object with ID '%s' from database." % oid


        # DELETE ACTION

        if action == 'del':
            wheretoback = obj.parent
            if database.delObject(oid):
                # We don't need link to this object in last_changed more
                if oid in database.last_changed:
                    database.last_changed.remove(oid)
                database.save()
                redirect("/%s" % wheretoback)
#               return self.page(title=u'Результат удаления объекта - Успешно', content=u'Удалён из каталога объёкт с идентификатором &quot;%s&quot;.' % obj.oid)
            else:
                content = obj.as_html(database, self.is_authorised())
                return self.page(
                    title=obj.title,
                    breadcrumbs=obj.get_parents(database),
                    message = u'Произошла ошибка при попытке удалить объёкт с идентификатором "%s".' % obj.oid,
                    content=content)

#               return self.page(title=u'Результат удаления объекта - Ошибка', content=u'Произошла ошибка при попытке удалить объёкт с идентификатором &quot;%s&quot;.' % obj.oid)

        # EDIT ACTION

        if action == 'edit':
            return self.page(title=u'Редактирование объекта', content=obj.as_form())

        # UPDATE OBJECT ACTION

        if action == 'update':
            fields = get_request().form

            if not (oid and get_field('title') and parent):
                return "Necessary fields not found."
            if not database.get_object(parent):
                return "Parent not found. Any object in catalog must have a parent container."

            result = obj.import_data(fields)
            if type(result) == 'str':
                return result   #some error occured

            # If oid was changed
            oidnew = fields['oidnew']
            if oid != oidnew:
                # oid changed - delete old object and replace with new one
                if database.delObject(oid):
                    database.delFromChanged(oid)
                    obj.oid = oidnew
                    oid = oidnew
                    database.addObject(obj)
                else:
                    return 'some error occured'

            database.addToChanged(oid)
            database.save()
            redirect("/%s" % obj.oid)

        # ADD OBJECT ACTION

        if action == 'new' and not obj:
        # Object not found in database, so this in new object, create it.
            if object_kind == 'category':
                obj = Category(parent, 'temporarycategory', 'temporaryCategory')
            if object_kind == 'entity':
                obj = Entity(parent, 'temporaryentity', 'temporaryEntity')
            if database.addObject(obj):
                database.save()
                return self.page(title=u'Редактирование объекта', content=obj.as_form())
            else:
                return self.page(title=u'Ошибка при создании объекта',
                    message=u'Ошибка при создании объекта',
                    content=u"Возможно такой объект уже существует")



    # LOGIN PAGE

    def login(self):
        login = get_field('login')
        password = get_field('password')
        if not login and not password:
            came_from = get_request().environ.get('HTTP_REFERER')
            login_form = """
                <h1>Страница авторизации</h1>
                <form method="post" action="/login">
                    Login: <input type="text" name="login" size="10" /><br />
                    Password: <input type="password" name="password" size="10" /><br />
                    <input type="hidden" name="came_from" value="%s" />
                    <input type="submit" value="Login" />
                </form>""" % came_from
            return self.page(title = u"Страница авторизации", content=login_form)
        else:
            came_from = get_field('came_from')
            if login == LOGIN and password.encode('utf-8') == PASSWORD:
                session = get_session()
                session.user = LOGIN
                redirect(came_from)
            else:
                return self.page(title = u"Страница авторизации - Ошибка авторизации", message="Авторизация не пройдена", content=login_form)

    def is_authorised(self):
        session = get_session()
        if session.get_user() == LOGIN:
            return True
        return False

    def logout(self):
        session = get_session()
        session.user = None
        return self.page(title = u"Страница авторизации", content='Вы вышли из системы')


    # STATIC INFO PAGES

    def about(self):
        content = open(location+'content/about.html').read()
        content += """<p>Проект был запущен 30.06.2005</p>"""
        content += """<p>На данный момент каталог содержит %s объектов в %s категориях.</p>""" % (
            len(database.get_by_kind()), len(database.get_by_kind(object_kind="category")) )
        return self.page(title = u'О проекте', content=content)

    def prices(self):
        content = open(location+'content/prices.html').read()
        return self.page(title = u"Расценки на услуги", content=content)

    def addinfo(self):
        content = open(location+'content/addinfo.html').read()
        return self.page(title = u"Добавить информацию в каталог", content=content)

    def mostviewed(self):
        content = '<h1>Рейтинг популярности</h1>\n<ol>'
        objects = database.get_by_popularity(howmuch=30)
        for oid in objects:
            obj = database.get_object(oid[1])
            content += '''<li><a href="/%s">&quot;%s&quot; %s</a> (%s просмотров)</li>\n''' % (
                oid[1].encode('utf-8'),
                obj.title.encode('utf-8'),
                obj.sort.encode('utf-8'),
                oid[0])
        content += '</ol>'
        return self.page(title = u"Рейтинг популярности", content=content)

    def mostviewedcategories(self):
        content = '<h1>Рейтинг популярности категорий каталога</h1>\n<ol>'
        objects = database.get_by_popularity(howmuch=30, object_kind='category')
        for oid in objects:
            obj = database.get_object(oid[1])
            content += '''<li><a href="/%s">%s</a> (%s просмотров)</li>\n''' % (
                oid[1].encode('utf-8'),
                obj.title.encode('utf-8'),
                oid[0])
        content += '</ol>'
        return self.page(title = u"Рейтинг популярности категорий каталога", content=content)

    def fulllist(self, sorted='title'):
        sorted = get_field('sorted')
        if not sorted:
            sorted = 'title'
        content = '<h1>Каталог в одной таблице</h1>\n'
        content += '<table border="0" cellspacing="0" cellpadding="0" id="fulllist">\n'
        content += '<tr>\n'
        content += '<th><a href="/fulllist?sorted=title">Название</a></th>\n'
        content += '<th><a href="/fulllist?sorted=sort">Тип</a></th>\n'
        content += '<th><a href="/fulllist?sorted=address">Адрес</a></th>\n'
        content += '<th><a href="/fulllist?sorted=phones">Телефоны</a></th>\n'
        content += '</tr>\n'
        for n, obj in enumerate(database.get_by_kind(sorted=sorted)):
            if obj.object_kind == 'entity':
                content += '<tr class="%s">\n'  % (n%2 and 'even' or 'odd')
                content += '''<td><a href="/%s">%s</a></td>\n''' % (obj.oid.encode('utf-8'), obj.title.encode('utf-8'))
                content += '<td>%s</td>\n' % obj.sort.encode('utf-8')
                content += '<td>%s</td>\n' % obj.address.encode('utf-8')
                content += '<td>%s</td>\n' % obj.phones.encode('utf-8')
                content += '</tr>\n'
        content += "</table>\n"
        return self.page(title = u"Весь каталог", content=content)

    def search(self):
        query = get_field('query')
        searcharea = get_field('where')

        # Write request into log file (for statistic)
        try:
            qf = open('queries.txt','a')
            qf.write("%s\n" % query.encode('koi8-r'))
            qf.close()
        except:
            pass

        if query == None:   # if visited just a page without any query
            query = ''

        result = database.search(query, searcharea)
        message = ''
        content = '''<h1>Результаты поиска:</h1>\n<p>Найдено %s объектов.</p>\n''' % len(result)
        if len(result) == 0:
            message = u"Попробуйте изменить поисковый запрос."
        if len(result) > 50:
            result = result[:50]
            message = u"Найдено слишком много объектов. Будут отображены только первые пятьдесят."
        if len(result) <= 50:
            content += "<ol>"
            for obj in result:
                var1 = obj.oid
                var2 = obj.title
                if obj.object_kind == 'entity':
                    var3 = obj.sort
                else:
                    var3 = u'Категория'
                content += """<li><a href="/%s">%s - %s</a></li>""" % (var1.encode('utf-8'), var2.encode('utf-8'), var3.encode('utf-8'))
            content += "</ol>"
        return self.page(title = u"Поиск по сайту", message=message, content=content, query=query)

    def sendMessage(self):
        """ Send message on administrator's email """
        From = get_field('From')
        Name = get_field('Name')
        Text = get_field('Text')
        To = 'admin@index.sed.lg.ua'
        Subject = 'From Index AddInfo Page'
        body = """From: "%s" <%s>\nTo: %s\nSubject: %s\n\n%s""" % (Name, From, To, Subject, Text)

        body = body.encode('koi8-r')

        try:
            server = smtplib.SMTP("smtp.sed.lg.ua")
            server.sendmail(From, To, body)
            server.quit()
            return self.page(title=u"Результат отправки сообщения", message=u"Сообщение отправлено",
                content=u"""Было отправлено сообщение:<br />"""+Text)
        except:
            return self.page(title=u"Результат отправки сообщения", message=u"Ошибка при отправке сообщения",
                content=u"""<p><a href="javascript:history.go(-1)">Вернуться к отправке сообщения</a>.</p>""")

    def image(self):
        if get_field('oid'):
            oid = str(get_field('oid'))
            get_response().set_content_type('image/png')
            try:
                #if cropped image exist
                croppedImage = Image.open(mapPiecesDir+oid+'.png')
                f = StringIO()
                croppedImage.save(f, 'PNG', optimize=1)
                return f.getvalue()
            except:
                #no cropped image present, cropping proceed...
                obj = database.get_object(oid)
                mapbig = Image.open(mapbigFile)
                mapaim = Image.open(mapaimFile)
                mapsign = Image.open(mapsignFile)

                x = int(obj.map_xy[0])
                y = int(obj.map_xy[1])

                x1 = x-200
                y1 = y-200
                x2 = x+200
                y2 = y+200

                # crop region from global city map
                cropped = mapbig.crop( (x1, y1, x2, y2) ).convert('RGB')

                # make the transparent mask
                colorTable = [255]*256
                colorTable[0] = 0
                aimmask = mapaim.point (colorTable, '1') #mask for map aim
                signmask = mapsign.point (colorTable, '1') #mask for map sign 'Index'

                #paste aim to the map
                cropped.paste( mapaim, (168, 168), aimmask )
                cropped.paste( mapsign, (20, 350), signmask )

                #save to file if not present
                cropped = cropped.convert('P', palette=1, colors=64)
                cropped.save(mapPiecesDir+oid+'.png', 'PNG', optimize=1)

                #save to virtual file and return it
                f = StringIO()
                cropped.save(f, 'PNG', optimize=1)
                return f.getvalue()


def create_publisher():
    # create the session manager.
    from os import name as platform

    if platform == 'nt':
        from session2.store.ShelveSessionStore import ShelveSessionStore
        store_type = ShelveSessionStore(sessionsDir+'sessions.shelf')
    else:
        from session2.store.DirectorySessionStore import DirectorySessionStore
        store_type = DirectorySessionStore(sessionsDir)

    session_manager = SessionManager(store_type, session_class=IndexSession)

    return Publisher(
        RootDirectory(),
        session_manager=session_manager,
        display_exceptions='plain',
        error_log="index_errors.log",
        access_log="index_access.log"
        )


if __name__ == "__main__":
    database = DataBase()

#   for i in database.data.values():
#       try:
#           i.created = str(i.created)
#           i.modified = str(i.modified)
#       except:
#           pass
#   database.save()

    if '-p' in sys.argv:
        from quixote.server.simple_server import run
        print 'Starting server'
        run(create_publisher, host='localhost', port=8080)
    else:
        # run as cgi
        from quixote.server.cgi_server import run
        run(create_publisher)
