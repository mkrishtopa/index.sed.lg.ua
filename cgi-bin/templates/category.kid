<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:strip="">
<h1 py:content="obj.title"></h1>

<p py:if="database.get_by_parent(obj.oid)">В этой категории находятся такие элементы:</p>
<p py:if="not database.get_by_parent(obj.oid)">В этой категории пусто.</p>

<ol py:if="database.get_by_parent(obj.oid, 'category')">
<li py:for="subcategory in database.get_by_parent(obj.oid, 'category', True)">
<a href="#" py:attrs="href='/%s' % subcategory.oid, title=subcategory.sort"
py:content="subcategory.title">Category title</a>
(<span py:replace="len(database.get_by_parent(subcategory.oid))">Amount of entities inside</span>)</li>
</ol>

<dl py:if="database.get_by_parent(obj.oid, 'entity')">
<span py:for="entity in enumerate(database.get_by_parent(obj.oid, 'entity', True))" py:strip="">
<dt><span py:replace="entity[0]+1"></span>. <a href="#" py:attrs="href='/%s' % entity[1].oid"><span py:replace="entity[1].title"></span><span py:if="entity[1].sort" py:omit=""> - </span><span py:replace="entity[1].sort"></span></a></dt>
<dd><span py:if="entity[1].address" py:replace="entity[1].address+'; '">address</span><span py:if="entity[1].phones" py:replace="entity[1].phones"></span></dd>
</span>
</dl>

<div py:if="is_logged" id="pageControl">
<h1>Управление объектом</h1>
<ul>
<li><a href="/edit?action=new&amp;object_kind=entity&amp;parent=${obj.oid}">Добавить новый объект в текущую категорию</a></li>
<li><a href="/edit?action=new&amp;object_kind=category&amp;parent=${obj.oid}">Добавить новую категорию</a></li>
<li><a href="/edit?oid=${obj.oid}&amp;action=edit" accesskey="e">Редактировать текущую категорию</a></li>
<li><a href="javascript:if(confirm('Удалить категорию?'))window.location='/edit?oid=${obj.oid}&amp;action=del'">Удалить текущую категорию</a></li>
</ul>
</div>

<div class="advertBlock" py:if="not is_logged" py:content="XML(obj.getAdvertBlock())">
</div>
<!--
<p id="viewcounter">Страница просмотрена <span py:replace="obj.counter"></span> раз.</p>
-->
</html>