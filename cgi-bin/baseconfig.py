# -*- coding: UTF-8 -*-

from os import name as platform

# Site title
TITLE = u'Северодонецкий городской каталог &#8220;Index&#8221; - '
IndexURL = 'http://www.index.sed.lg.ua'

# Locations of static files
if platform == 'nt':
    location = "Q:\\LocalSites\\index\\"        #Where's catalogue files are placed
    mapbigFile = location+'images_map\\citymap.png'
    mapaimFile = location+'images_map\\aim.png'
    mapsignFile = location+'images_map\\indexmapsign.png'
    mapPiecesDir = location+'images_map\\map_pieces\\'
    databaseDir = location+'cgi-bin\\database\\'
    templatesDir = location + 'cgi-bin\\templates\\'
    sessionsDir = location + 'cgi-bin\\sessions\\'
else:
    location = "/home/theo/Index/"
    mapbigFile = location+'images_map/citymap.png'
    mapaimFile = location+'images_map/aim.png'
    mapsignFile = location+'images_map/indexmapsign.png'
    mapPiecesDir = location+'images_map/map_pieces/'
    databaseDir = location+'cgi-bin/database/'
    templatesDir = location + 'cgi-bin/templates/'
    sessionsDir = location + 'cgi-bin/sessions/'


# Site news
NEWS = (
    # date, description, is the news is hot (True/False)
    ('09.02.2009', u'''Функция поиска по сайту каталога снова работает''', 0),
    ('22.08.2008', u'''На сайте sed.lg.ua убрали ссылку на каталог INDEX. Добавьте наш сайт в закладки, пожалуйста.''', 1),
    ('20.01.2008', u'''<a href="/prices" title="Открыть прайс-лист">Изменение в расценках на услуги: оплата за размещение в каталоге теперь вносится единоразово: всего 100грн</a>.''', 0),
    ('11.07.2007', u'''<a href="/prices" title="Открыть прайс-лист">Оптовая скидка -50% при размещении более одной фирмы в каталоге INDEX!</a>.''', 0),
    ('3.07.2007', u'''Обращаем внимание на работающий <strong><a href="http://www.homelan.lg.ua/our-projects/sites-catalog" title="Перейти к каталогу">каталог Северодонецких веб-сайтов</a></strong>.''', 0),
#   ('16.05.2007', u'''И снова спасибо посетителю Алёне за новую информацию об <a href="/pharmacy" title="Перейти в раздел аптек">аптеках</a>.''', 0),
#   ('4.04.2007', u'''Добавлена <a href="/pharmacy" title="Перейти в раздел аптек">информацию об аптеках</a> - добавились в каталог новые, добавлены недостающие телефоны. Спасибо посетителю Алёне за оставленный в <a href="http://gb.com.ua/?id=index&amp;act=show">гостевой книге</a> список.''', 0),
#   ('12.03.2007', u'''<a href="/routes" title="Список маршрутов">С 12 марта продлён маршрут 102/12 по улицам: Сметанина, Советский, Энергетиков, 2-я проходная СГПП "Азот", 1-я проходная СГПП "Азот".</a>''', 0),
#   ('12.03.2007', u'''Каталог снова доступен как городской ресурс.''', 0),
#   ('19.02.2007', u'''Из-за проблем с хостером каталог временно доступен только для внутригородских посетителей. Приносим извинения.''', 0),
#   ('1.01.2007', u'''1 февраля каталог не работал - шли работы по модернизации сервера. Приносим извинения за доставленные неудобства.''', 0),
#   ('29.01.2007', u'''<a href="/xenon">Установка ксенонового света на автомобили - взгляните на дорогу по-новому!. <strong>Посетителям каталога скидки...</strong></a>''', 0),
#   ('22.01.2007', u'''Обновился каталог туров турагентства "Гамалия".  <a href="/hamalia">Смотрите зимний каталог туров</a>.''', 0),
#   ('12.01.2007', u'''Нужна юридическая помощь? В городе работает <a href="/chernobay">"Северодонецкая  коллегия  адвокатов"</a>.''', 0),
#   ('11.01.2007', u'''Обратите внимание: изменился контактный телефон администратора. <strong>Новый телефон: +38(063)1755807</strong>.''', 0),
#   ('27.12.2006', u'''Открылся супермаркет "<a href="/semja">Семья</a>" по Космонавтов 17.''', 0),
#   ('23.12.2006', u'''Нужен Дед Мороз со Снегурочкой на праздники? Звоните 24693.''', 0),
#   ('27.11.2006', u'''<a href="http://help.is.ua/">Требуется помощь в спасении ребёнка - дочери Павла Игнатенко! Все кто может - откликнитесь!</a>''', 0),
#   ('27.11.2006', u'''Сдаются в аренду помещения (для производства/хранения) общей площадью 4500 кв.м с возможностью обустройства отдельного офиса. Тел.: (06452)31015, (050)5948421''', 0),
#   ('14.11.2006', u'''Сдаётся комната под офис: ул.Донецкая д.50 (перекрёсток ул.Донецкой и пр.Гвардейского), 1 этаж, офисный ремонт, крыльцо. 8(050)7418778, 8(095)5335058''', 0),
#   ('2.11.2006', u'''Сдаётся помещение под офис. <strong>93 кв.м.</strong>, ул.Гоголя д.24 (3 этаж, р-н центр.рынка). т.53450''', 1),
#   ('31.10.2006', u'''Изменился телефон "Городского такси" (с 95900 на 66900) в связи со сменой АТС.''', 0),
#   ('25.10.2006', u'''При салоне "Glamour" действует выставочный <a href="/glamour#nugabest" title="массажёры Nuga Best">зал массажёров компании Nuga Best</a>.''', 0),
#   ('22.09.2006', u'''Внесена <a href="/clubs" title="Смотреть подробее">подробная информация о детско-юношеских клубах</a>.''', 0),
#   ('20.09.2006', u'''Выставка репродукций картин Н.Рериха в <a href="/exposition" title="Смотреть подробее">выставочном зале</a>.''', 0),
#   ('4.09.2006', u'''Охотничий магазин <a href="/krechet2" title="Смотреть страницу магазина">&quot;Кречет-2&quot;</a> - всё для удачной охоты!''', 0),
#   ('1.09.2006', u'''Добавлена кнопка для быстрого вывода страниц на печать.''', 0),
#   ('30.08.2006', u'''Добавлена подробная информация о <a href="/cronashop" title="Смотреть страницу салона">мебельном салоне &quot;Крона&quot;</a>.''', 0),
#   ('30.08.2006', u'''В связи со сбоем в работе сервера каталог не функционировал сутки. Утерянные данные восстанавливаются. Приносим свои извинения посетителям.''', 0),
#   ('3.08.2006', u'''Все поступающие заявки будут обработаны после 14 августа в связи с отпуском администратора.''', 0),
#   ('5.07.2006', u'''Значительно пополнен раздел "Рынок транспорта". Внесены автогаражные кооперативы, заправки, стоянки, СТО.''', 0),
#   ('30.06.2006', u'''Сегодня нашему каталогу исполнился год! Спасибо всем, кто принимал и принимает участие в его развитии.''', 0),
#   ('22.06.2006', u'''Реализована возможность размещения баннеров или рекламной информации в разделах каталога. <a href="/prices" title="Смотреть прайс-лист">Заказывайте себе рекламу!</a>''', 0),
#   ('21.06.2006', u'''Добавлены <a href="/cashmachines" title="Перейти в раздел">банкоматы городских банков</a>.'''),
#   ('20.06.2006', u'''Добавлены <a href="/communal" title="Перейти в раздел">ЖЭКи</a>.'''),
#   ('19.06.2006', u'''Добавлена информация о первой в городе <a href="/filletstudio" title="Открыть страницу">багетной мастерской</a>.'''),
#   ('15.06.2006', u'''<span style="color:red">Добавлен раздел <a href="/mobilemarket" title="Перейти в раздел">&quot;Рынок мобильной связи&quot;</a>. Приглашаем все салоны мобильной связи вносить о себе информацию!</span>'''),
#   ('15.06.2006', u'''Добавлен раздел <a href="/automarket" title="Перейти в раздел">&quot;Рынок транспорта&quot;</a>.'''),
#   ('13.06.2006', u'''Добавлен летний каталог туров <a href="/hamalia" title="Смотреть страницу турагентства">туристического агентства Гамалия</a>.'''),
#   ('3.06.2006', u'''В городе Северодонецке <a href="/cafes" title="Перейти в раздел" style="color:red">100 баров</a>!'''),
#   ('29.05.2006', u'''В братском городе Рубежное 1-го мая студией дизайна "Vita" был запущен свой <a href="http://index.lg.ua">городской каталог</a>. Поздравляем их с почином. Успеха в развитии!'''),
#   ('23.05.2006', u'''Теперь каталог можно смотреть с помощью мобильного телефона. <a href="http://mini.opera.com" title="Перейти на сайт браузера">Рекомендуемый браузер - Opera</a>. Милости просим! Отзывы оставляйте в гостевой.'''),
#   ('17.05.2006', u'''Добавлена информация о <a href="/glamour" title="Перейти">парикмахерской "Glamour"</a>.'''),
#   ('16.05.2006', u'''<span style="color:red">Если у Вас возникли проблемы с отображением сайта, перегрузите страницу нажав Ctrl+F5 чтобы обновить кеш броузера.</span>'''),
#   ('14.05.2006', u'''Добавлены <a href="/policlinic">телефоны городских больниц и их отделений</a>. Спасибо Олегу Стрельченко за информацию.'''),
#   ('27.04.2006', u'''Движок каталога обновлён и находится в стадии финального тестирования. О замеченных ошибках сообщайте в <a href="http://gb.com.ua/?id=index&amp;act=show">гостевой книге</a>.'''),
#   ('25.04.2006', u'''Внимание! С 1 мая изменяются условия внесения информации в каталог - каталог становится полностью <a href="/prices" title="Смотреть прайс-лист">платным</a>.'''),
#   ('25.10.2005', """Добавлена информация о <a href="/sanatoriums">городских санаториях</a>."""),
#   ('25.10.2005', """Добавлена подробная информация о турагентстве <a href="/universaltouragency">&quot;УниверсалТур&quot;</a>."""),
#   ('13.10.2005', """Добавлен <a href="/nurseries">полный список</a> работающих детских садов (ясель). Благодарим ГОРОНО."""),
#   10.10.2005  Запущена <a href="http://gb.com.ua/?id=index&amp;act=show" title="Перейти к гостевой книге">гостевая книга сайта</a>.</dd>
#   20.09.2005  С 20 сентября расширен спектр предоставляемых услуг и изменены <a href="/prices">расценки</a>.</dd>
#   11.09.2005  Новая выставка в <a href="/exposition" title="">Выставочном Зале Народного Творчества</a>.</dd>
#   16.08.2005  Улучшен <a href="/search" title="Перейти на страницу поиска">поиск по каталогу</a> - теперь он нечувствителен к регистру.</dd>
#   16.08.2005  Внесены изменения для корректной <a href="javascript:this.print();" title="Распечатать страницу">распечатки страниц</a> каталога на принтере (оформление при печати не выводится).</dd>
#   15.08.2005  Добавлена подробная информация о <a href="/exposition" title="">Выставочном Зале Народного Творчества</a>.</dd>
#   13.07.2005  Добавлена возможность <a href="/search" title="Перейти на страницу поиска">поиска по каталогу</a>.</dd>
#   11.07.2005  Внесена информация о <a href="/economic/banks">городских банках</a>.</dd>
#   01.07.2005  <strong>Внимание!</strong> Первым десяти клиентам - 6 месяцев размещения бесплатно! Подробности по размещению информации читайте <a href="/prices">тут</a>.</dd>
#   30.06.2005  Внесена информация. Проект запущен.</dd>
#   07.06.2005  Добавлены все <a href="/entertainments/cafes">кафе и рестораны города</a>.</dd>
)

# Navigation links
NAV_LINKS = (
        ('/prices', u'Прайс-лист на услуги каталога', u'Стоимость размещения информации в каталоге'),
        ('/addinfo', u'Добавить свою информацию', u'Внесение информации в каталог - страница отправки заявок'),
#       ('/advanced_search', u'Расширенный поиск', ''),
        ('/mostviewed', u'Рейтинг популярности фирм', ''),
        ('/mostviewedcategories', u'Рейтинг популярности категорий', ''),
        ('/fulllist', u'Просмотреть весь каталог таблицей', ''),
        ('http://gb.com.ua/?id=index&amp;act=show', u'Гостевая книга', u'С исправлениями и пожеланиями - сюда'),
        ('/about', u'О каталоге', u'Общая информация о сайте'),
)
# Most popular links (on left column) : ((id, title, alt), (...), ...)
POPULAR_LINKS = (
    ('computerselling', u'Магазины компьютерной техники', ''),
    ('electonic4home', u'Магазины бытовой техники', u''),
#   ('taxies', u'Такси, грузоперевозки', u'Список всех служб такси'),
    ('cafes', u'Рестораны, бары, ночные клубы', ''),
#   ('trading', u'Торговля', ''),
)

# Advertisement links
ADVERT_LINKS = (
    ('heddex', u'Студия HedDex - разработка веб-сайтов', u'Сайты "под ключ"'),
#   ('rmservcentre', u'Сервисный центр РМ - Авторизованный сервисный центр и продавец оргтехники (принтеры, копиры, МФУ)', u''),
#    ('chernobay', u'Северодонецкая коллегия адвокатов', u'Юридическя помощь'),
    ('hitfm', u'Радио Хит FM (103.8FM)', u''),
#   ('hamalia', u'"Гамалия" - туристическое агентство', u''),
#   ('xenon', u'Установка ксенонового света на авто', u'Установка ксенона'),
#   ('bps', u'Ремонт, сопровождение, обслуживание компьютерной техники', u'Сервисный центр "Best Print Sevice"'),
#   ('homelan', u'HomeLan - Первая городская домашняя сеть', u''),
)

# Order of columns on homepage
COLUMNS_ORDER = (
    ('humanservices', 'trading', 'entertainments', 'economic', 'computermarket',
     'mobilemarket', 'automarket', 'buildingmarket', 'industrialmarket', 'health',
     'science',  'art', 'government', 'massmedia', 'sport','organizations')
)

# Last changed object, initial list
LAST_CHANGED_LINKS = ['heddex', 'homelan', 'zonewm', 'zonewm', 'zonewm']

LOGIN = u'admin'
PASSWORD = u'ob]zdktybz7'


# Block of advert data
advertData = {
    'providers':        """<a href="/homelan"><img src="/images/banners/homelan.gif" alt="Homelan banner" width="468" height="60" /></a>""",
    'flowers':          """<a href="/charivnykvity" title="Выберите цветы для своих любимых!"><img src="/images/banners/char_kviti1.jpg" alt="Баннер салона цветов" width="468" height="60" /></a>""",
    'gambles':          '',
    'parlay':           '',
    'tv':               """<a href="/hitfm"><img src="/images/banners/hitfm-banner.png" alt="HitFM Banner" width="468" height="60" /></a>""",
    'touringagencies':  """<a href="/hitfm"><img src="/images/banners/hitfm-banner.png" alt="HitFM Banner" width="468" height="60" /></a>""",
#   'common': '',
#    'common':       """<h3>Реклама от Google:</h3>
#    <script type="text/javascript"><!--
#    google_ad_client = "pub-3556605310537490";
#    google_ad_width = 468;
#    google_ad_height = 60;
#    google_ad_format = "468x60_as";
#    google_ad_type = "text_image";
#    google_ad_channel ="3593784427";
#    google_color_border = "FFFFFF";
#    google_color_link = "0000FF";
#    google_color_bg = "FFFFFF";
#    google_color_text = "000000";
#    google_color_url = "008000";
#    //--></script>
#    <script type="text/javascript"
#      src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
#    </script>"""    # Common advert block, if no other advert for object
    'common': """<script type="text/javascript"><!--
                 google_ad_client = "pub-3556605310537490";
                 //468x60, created 15.01.08
                 google_ad_slot = "0115630333";
                 google_ad_width = 468;
                 google_ad_height = 60;
                 //--></script>
                 <script type="text/javascript"
                 src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
                 </script>

<script type="text/javascript"><!--
yandex_partner_id = 32252;
yandex_site_charset = 'utf-8';
yandex_ad_format = 'direct';
yandex_font_size = 1;
yandex_direct_type = 'horizontal';
yandex_direct_border_type = 'block';
yandex_direct_limit = 2;
yandex_direct_bg_color = 'FFF9F0';
yandex_direct_border_color = 'FBE5C0';
yandex_direct_header_bg_color = 'FEEAC7';
yandex_direct_title_color = '0000CC';
yandex_direct_url_color = '006600';
yandex_direct_all_color = '0000CC';
yandex_direct_text_color = '000000';
yandex_direct_site_bg_color = 'FFFFFF';
document.write('<sc'+'ript type="text/javascript" src="http://an.yandex.ru/resource/context.js?rnd=' + Math.round(Math.random() * 100000) + '"></sc'+'ript>');
//--></script>

    """
}
