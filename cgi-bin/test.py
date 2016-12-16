#!/usr/bin/python2.4
# -*- coding: KOI8-R -*-

from classes import *
#from quixote import *
import string


def test_saved():
    f = file('database\\pickled.bin', 'rb')
    a = cPickle.load(f)
    f.close()

    print len(a)

    return a

def test_sort():
    for obj in db.get_by_kind(object_kind='category', sorted='title'):
        print obj.title

def test_asform():
    obj = db.get_object('providers')
    print obj.as_form()

def test_passallobjects():
    for obj in db.data.values():
        print 'Testing: ', obj.oid
        print obj.as_html(database=db)

def test_clearString():
    f = u"<!---->-!.,ЙЦУккенгQWErty"
    print clearString(f).encode('koi8-r')

def test_search():
    query = u"миры"
    res = db.search(query)
#    print res
#    print len(res)
    for i in res:
        print i.oid

def test_stemmerString():
    st = u"Студии студия"
#   st = '''студии студия Северодонецкое музыкальное училище им С.Прокофьева училище ул.Химиков 10 43443 45247 43443 Училище было открыто 1966 году Отделы: фортепиано оркестровые струнные инструменты оркестровые духовые ударные инструменты народные инструменты хоровое дирижирование теория музыки Художественные коллективы: ансамбль скрипачей духовой оркестр ансамбль бандуристов оркестр народных инструментов хор училище есть большой концертный зал на 500 человек малый зал для проведения академических концертов спортивный зал хоровой класс библиотека читальным залом на 50 человек 12 классов для групповых 30 классов для индивидуальных занятий оригинальный самобытный хол на первом этаже небольшим фонтаном 'зимним садом' Иногородние студенты обеспечиваются жильем общежитии на 80 мест комнатах живут по 3 человека практически каждой комнате есть фортепиано Есть комнаты для самоподготовки На данный момент училище является учебным заведением первого уровня аккредитации'''
    print st.encode('koi8-r')
    print " ".join(stemString(st)).encode('koi8-r')

def test_stemmerList():
    sl = [u'Студия', u'студии']
    print ' '.join(sl).encode('koi8-r')
    print ' '.join(stemList(sl)).encode('koi8-r')

def test_getObject():
    obj = db.get_object('laguna')
    print obj.__str__().encode('koi8-r')

#def test_template():
#   import kid
#   return kid.Template(
#       file='templates\main.kid',
#   ).serialize(output='html')


if __name__ == "__main__":
    db = DataBase()
    print "test started:"
#    print db
#   obj = db.get_object('laguna')
#   print obj.oid
#   obj = db.get_object('heddex').map_xy
#   print obj.__str__()
    test_search()
#   test_stemmerList()
#   test_clearString()
#   test_getObject()
#   test_template()
    print "test finished"