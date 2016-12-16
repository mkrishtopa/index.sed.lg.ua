<?xml version='1.0' encoding='utf-8'?>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:py="http://purl.org/kid/ns#">
<head>
<title py:content="XML(title)">Template</title>
<meta name="description" content="Index - Северодонецкий городской информационный каталог" />
<meta name="keywords" content="Северодонецк, index, индекс, каталог, предприятия, организации, фирмы, гостиницы, банки, такси, телефоны, недвижимость, сайт, желтые страницы, severodonetsk" />
<meta name="verify-v1" content="l/FbwzAUHqkuv8G8pdYbxTuKKjJG+LQ/91E/1ZOu570=" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" media="screen" href="/styles/styles.css" />
<link rel="stylesheet" type="text/css" media="print" href="/styles/print.css" />
<link rel="stylesheet" type="text/css" media="handheld" href="/styles/handheld.css" />
<script type="text/javascript" language="javascript1.2" src="/javascripts/javascripts.js" > </script>
<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" />
</head>

<body>

<div id="wrapper">

<!--! LEFT COLUMN -->
<div id="column_left">

	<img src="/images/logo.jpg" height="130" width="300" alt="Логотип" usemap="#logomap" />
	<map name="logomap">
	<area shape="circle" coords="279,21,13" href="/" alt="На главную страницу" title="На главную страницу" />
	<area shape="poly" coords="29,43,17,71,30,108,54,92,86,83,99,90,162,69,150,58,129,64,125,45,46,63,40,45" href="/" alt="На главную страницу" title="На главную страницу" />
	</map>
			
	<!--! NEWS -->
	<img src="/images/news.gif" width="300" height="45" alt="Раздел новостей" />
	<div class="infobox" id="news">
	<dl>
	<span py:for="(date, newsbody, hotnews) in news" py:strip="">
	<dt py:content="date"></dt>
	<dd py:if="hotnews" py:attrs='class="hotnews"' py:content='XML(newsbody)'></dd>
	<dd py:if="not hotnews" py:content='XML(newsbody)'></dd>
	</span>
	</dl>
	</div>
			
	<!--! SEARCH FORM -->
	<img src="/images/search.gif" width="300" height="24" alt="Поиск по каталогу" />
	<div class="infobox">
	<form action="/search" name="searchform" method="get" id="searchform">
	<input type="text" name="query" value="${query}" id="textfield" onKeyUp="search_check(this);" />
	<input type="submit" value="Найти" id="submit" />
	<input name="where" type="radio" value="intitles" id="searchswitcher1" checked="checked" />
	<label for="searchswitcher1">Искать в названии</label>
	<input name="where" type="radio" value="everywhere" id="searchswitcher2" />
	<label for="searchswitcher2">Искать везде</label>
	</form>
	</div>
	
	<!--! NAVIGATION LINKS -->
	<img src="/images/navigation.gif" width="300" height="24" alt="Навигация по каталогу" />
	<div class="infobox">
	<ul>
	<li py:for="(url, content, title) in nav_links">
	<a href="#" py:content="content" py:attrs="href=url, title=title"></a>
	</li>
	</ul>
	</div>
	
	<!--! ADVERT LINKS -->
	<img src="/images/recommended.gif" width="300" height="24" alt="Рекомендуем посмотреть" />
	<div class="infobox" id="portlet-advert">
	<ul>
	<li py:for="(url,lcontent,ltitle) in advert_links">
	<a href="#" py:content="lcontent" py:attrs="href=url, title=ltitle"></a>
	</li>
	</ul>
	</div>
	
	<!--! POPULAR LINKS -->
	<img src="/images/popular.gif" width="300" height="24" alt="Популярные ссылки" />
	<div class="infobox">
	<ul>
	<li py:for="(url,lcontent,ltitle) in popular_links">
	<a href="#" py:content="lcontent" py:attrs="href=url, title=ltitle"></a>
	</li>
	</ul>
	</div>
	
	<!--! LAST CHANGED OBJECTS -->
	<img src="/images/lastadded.gif" width="300" height="24" alt="Последние изменения" />
	<div class="infobox" id="lastadded">
	<ul>
	<li py:for="oid in last_changed_links">
	<a href="#" py:attrs="href='/%s' % oid" py:content="XML(database.get_full_title(oid))"></a>
	</li>
	</ul>
	</div>
	
	<!--! PARTNERS LINKS -->
	<img src="/images/partners.png" width="300" height="24" alt="Партнёрские ссылки" />
	<div class="infobox" id="partners-links">
	  <a href="http://www.is.ua/index.php?page=is-price-bunkernet" title="">
	    <img src="/images/banners/bn_banner.png" alt="" />
	  </a>
	</div>

	<!--! ADMINISTRATIVE LINKS -->
	<div class="infobox" id="admin">
	<ul>
	<li py:if="not is_logged"><a href="/login" accesskey="l">Вход администратора</a></li>
	<li py:if="is_logged"><a href="/logout" accesskey="l">Выйти из системы</a></li>
	</ul>
	</div>
	
</div>

<!--! RIGHT COLUMN -->
<div id="column_right">
<div class="visualWrapper">

	<!--! PRINT PAGE BUTTON -->
	<a href="javascript:this.print();" 
	   id="print_page" 
	   title="Печать страницы"
	   py:if="breadcrumbs">
		<img src="/images/print_icon.gif" alt="Печать страницы" />
	</a>

	<!--! BREADCRUMBS BLOCK -->
	<div py:if="breadcrumbs" id="breadcrumbs">
	Вы тут: 
	<a href="/" title="На главную">Главная</a> &gt;  
	<span py:for="obj in breadcrumbs[0:-1]" py:omit="">
	<a py:attrs="href='/'+obj.oid" py:content="obj.title">Object title</a> &gt; 
	</span>
	<span py:content="breadcrumbs[-1].title" py:strip=''></span>
	</div>
	
	<!--! CONTENT BLOCK -->
	<div class="content">
		<div id="message" py:if="message" py:content="message"></div>
		<span py:replace="XML(page_content)"></span>
	</div>

</div>
</div>

<div class="visualClear"> </div>

<!--! FOOTER -->

<table border="0" cellspacing="0" cellpadding="0" id="footer">
<tr>
<td id="copyrights">
  &copy; 2005-2007 <a href="http://www.heddex.biz/" title="Перейти на сайт студии &quot;HedDex&quot;">HedDex Design Studio</a><br />
  При поддержке 
  <a href="http://www.homelan.lg.ua/" title="Перейти на сайт сети">сети HomeLan</a>.<br />
  Для просмотра рекомендуем <a href="http://www.mozilla.com/firefox/central/" title="Официальный сайт браузера FireFox">браузер FireFox</a>.<br />
</td>
<td valign="middle" id="counter">

<!-- StarCounter -->
<script language="javascript" type="text/javascript"><![CDATA[
  ck=document.cookie; ck="SC=1;"; tr="";tr="&amp;cook="+(ck?"Y":"N");
]]></script>
<script language="javascript" type="text/javascript"><![CDATA[
  document.write("<a href='http://counter.star.lg.ua/stats.cgi?id=18' target='_blank'><img src='http://counter.star.lg.ua/star.fcgi?id=18&amp;t="+Math.random()+tr+"&amp;ck="+escape(ck)+"' border='0' width='88' height='31' alt='StarCounter' /><"+"/a>");
]]></script>
<noscript><a href='http://counter.star.lg.ua/stats.cgi?id=18' target='_blank'><img src="http://counter.star.lg.ua/star.fcgi?id=18" border="0" width="88" height="31" alt="StarCounter" /></a></noscript>
<!-- StarCounter -->

</td>
<td valign="middle" id="banner">

<div py:if="not is_logged" py:omit="">

<!-- Another Banner Network -->
<script language="javascript" type="text/javascript"><![CDATA[
  bn_id='105289';
  bn_url='http://a.abnad.net';
  bn_rnd=Math.round((Math.random()*10000000));
  bn_addurl='?t=468&w=468&h=60&id='+bn_id;
  if(window.screen) bn_addurl+='&c='+screen.colorDepth+'&cw='+screen.width;
  if(document.referrer) bn_addurl+='&ref='+escape(document.referrer);
  bn_addurl+='&tz='+(new Date()).getTimezoneOffset()+'&r='+bn_rnd;
  document.write('<iframe src="'+bn_url+'/iframe'+bn_addurl+'" width="468" height="60" frameborder="0" vspace="0" hspace="0" marginwidth="0" marginheight="0" scrolling=no><a href="'+bn_url+'/nsanchor'+bn_addurl+'" target=_top><img src="'+bn_url+'/nsimg'+bn_addurl+'" width="468" height="60" border=0 /></a></iframe>');
]]></script>
<noscript><a href="http://a.abnad.net/nsanchor?t=468&amp;id=105289" target="_top"><img src="http://a.abnad.net/nsimg?t=468&amp;w=468&amp;h=60&amp;id=105289" width="468" height="60" border="0" alt=""/></a></noscript>

</div>
<div py:if="is_logged" py:omit="">&nbsp;</div>

</td>
</tr>
</table>

</div>

</body>
</html>