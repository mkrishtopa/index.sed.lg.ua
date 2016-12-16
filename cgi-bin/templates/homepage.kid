<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:strip="">
			<div id="homepage">
				<div py:for="category in COLUMNS_ORDER" py:strip="">
				<h1><a href="#"	py:content="database.get_object(category).title"
						py:attrs="href='/'+database.get_object(category).oid">Section</a></h1>
				<ul>
					<li py:for="subcategory in database.get_by_parent(category, 'category', True)"><a 
						href="#1" py:attrs="href='/'+subcategory.oid, title=subcategory.sort"><span 
							py:replace="subcategory.title"></span> (<span 
								py:replace="len(database.get_by_parent(subcategory.oid, object_kind='entity')) + len(database.get_by_parent(subcategory.oid, object_kind='category'))"></span>)</a><span> • </span></li>
				</ul>
				</div>
			</div>
</html>