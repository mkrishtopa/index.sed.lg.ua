<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:strip="">

<h1 py:content="obj.title"></h1>

<table id="objectinfo">
<tbody>

<tr py:if="obj.sort">
<td>Тип:</td>
<td class="databit" py:content="obj.sort"></td>
</tr>

<tr py:if="obj.address">
<td>Адрес:</td>
<td class="databit" py:content="obj.address"></td>
</tr>

<tr py:if="obj.map_xy != ['','']  and obj.map_visib == 'yes'">
<td>Карта:</td>
<td class="databit">
<a href="#" title="Смотреть на карте города (объект в центре карты)"
	onClick="newWindow('/image?oid=${obj.oid}', 425, 425)">Смотреть карту</a></td>
</tr>

<tr py:if="obj.phones">
<td>Телефоны:</td>
<td class="databit" py:content="obj.phones"></td>
</tr>

<tr py:if="obj.faxes">
<td>Факсы:</td>
<td class="databit" py:content="obj.faxes"></td>
</tr>

<tr py:if="obj.timetable">
<td>Время работы:</td>
<td class="databit" py:content="obj.timetable"></td>
</tr>

<tr py:if="obj.url">
<td>Веб-сайт:</td>
<td class="databit"><a href="#" py:attrs="href=obj.url" py:content="obj.url"></a></td>
</tr>

<tr py:if="obj.email and obj.email_visib == 'yes'">
<td>E-mail:</td>
<td class="databit" py:content="XML(obj.noSpamEmail())"></td>
</tr>

<tr py:if="obj.license">
<td>Лицензия:</td>
<td class="databit" py:content="obj.license"></td>
</tr>

</tbody>
</table>

<span py:if="obj.description and obj.description != ' ' and obj.description_visib == 'yes'" py:omit="">
<h3>Дополнительная информация:</h3>
<div id="description" py:content="XML(obj.description)">Some description text</div>
</span>

<div py:if="is_logged" id="pageControl">
<h1>Управление объектом</h1>
<ul>
<li><a href="/edit?oid=${obj.oid}&amp;action=edit" accesskey="e">Редактировать объект</a></li>
<li><a href="javascript:if(confirm('Удалить объект?'))window.location='/edit?oid=${obj.oid}&amp;action=del'" accesskey="d">Удалить объект</a></li>
</ul>
</div>

<div id="index_advert" py:if="not is_logged">
Пожалуйста, оставляйте свои отзывы о каталоге в <a href="http://gb.com.ua/?id=index&amp;act=show" title="Открыть гостевую книгу каталога">гостевой книге</a>.
<br />
Хотите, чтобы и Ваша фирма была представлена в каталоге? <a href="/prices">Тогда Вам сюда</a>.
<br />
Нашли неточность в представленной информации? Отошлите правильные данные с <a href="/addinfo" title="Послать исправление">этой страницы</a>.
</div>

<div class="advertBlock" py:if="not is_logged" py:content="XML(obj.getAdvertBlock())">
</div>

<p id="viewcounter">
<!--!Страница просмотрена <span py:replace="obj.counter"></span> раз.<br />-->
Дата последнего обновления: <span py:replace="obj.get_change_date()"></span><br />
Страница добавлена: <span py:replace="obj.get_create_date()"></span>
</p>

</html>