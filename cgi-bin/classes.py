# -*- coding: UTF-8 -*-

import random, cPickle, string, kid, re, logging
from time import time, gmtime, localtime, strftime, struct_time
from BeautifulSoup import BeautifulSoup
from quixote.form import Form, StringWidget, TextWidget # CheckboxWidget, SingleSelectWidget, MultipleSelectWidget,
from baseconfig import *

from session2.Session import Session

try:
	import Stemmer
except ImportError:
	Stemmer = False

class IndexSession(Session):
	def __init__(self, id):
		Session.__init__(self, id)
		self.visitedPages = {}
		
	def has_info(self):
		if self.user!=None or len(self.visitedPages)!=0:
			return True
		else:
			return False
		
	def addToVisited(self, oid):
		if oid not in self.visitedPages:
			self.visitedPages[oid] = time()
			return True
		else:
			if (time() - self.visitedPages[oid]) <= 7200:		# if the difference more than 2 hours (7200 secs)
				self.visitedPages[oid] = time()
				return False
			else:
				self.visitedPages[oid] = time()
				return True
	
class DataBase:
	
	def __init__(self):
		self.data = {}	# format: { oid1 : class instance, oid2 : class instance, ... }
		self.load()
		self.load_changed_objects()
		
	def addObject(self, obj):
		""" Add object (entity or category) to database """
		oid = obj.oid
		if self.data.has_key(oid) == False:
			self.data[oid] = obj
			return True
		else:
			return False
		
	def delObject(self, oid):
		""" Delete entity object by given ID """
		obj = self.get_object(oid)
		if not obj:
			return False		
		if obj.object_kind == 'entity':
			del self.data[oid]
			return True
		else:
			if len(self.get_by_parent(oid)) > 0:	# Category contain subojects and can't be deleted
				return False
			else:
				del self.data[oid]
				return True
				
	def save(self):
		f = file(databaseDir+'pickled.bin', 'wb')
		cPickle.dump(self.data, f, protocol=2)
		f.close()
		f = file(databaseDir+'last_changed_objects.bin', 'wb')
		cPickle.dump(self.last_changed, f, protocol=2)
		f.close()
		
	def load(self):
		f = file(databaseDir+'pickled.bin', 'rb')
		self.data = cPickle.load(f)

		
	def load_changed_objects(self):
		try:
			f = file(databaseDir+'last_changed_objects.bin', 'rb')
			self.last_changed = cPickle.load(f)
			f.close()
		except:
			self.last_changed = LAST_CHANGED_LINKS

	def addToChanged(self, oid):
		if oid not in self.last_changed:
			self.last_changed.insert(0,oid)
			if len(self.last_changed) > 4:
				del self.last_changed[-1]

	def getLastChanged(self):
		if (len(self.last_changed) >= 4):
			return self.last_changed[:4]
		else:
			return self.last_changed

	def delFromChanged(self, oid):
		if oid in self.last_changed:
			self.last_changed.remove(oid)


	def get_full_title(self, oid):
		obj = self.get_object(oid)
		if len(obj.sort)>1 and len(obj.title)>0:
			return '%s &#8221;%s&#8221;' % (obj.sort, obj.title)
		if len(obj.title)>0:
			return '%s' % obj.title
		return 'Без названия'

		
	def get_object(self, oid):
		if self.data.has_key(oid):
			return self.data[oid]
		else:
			return False

			
	def get_by_parent(self, parent, object_kind=None, sorted=False):
		""" Return list of objects with common parent """
		objects = []
		for obj in self.data.itervalues():
			if obj.parent == parent:
				if object_kind:
					if obj.object_kind == object_kind:
						objects.append(obj)
				else:
					objects.append(obj)
		if sorted:
			return sort(objects)
		else:
			return objects


	def search(self, query='', searcharea='intitles'):
		""" Query param must be in unicode """
		result = []
		
		f = open('temp.txt','w')
		if len(query) > 0:
			
			# What we search
			stemmer = Stemmer.Stemmer('russian')
#			print query.encode('koi8-r')
			query = stemmer.stemWord(query)			# Stemming request
#			print query.encode('koi8-r')
#			print query.encode('koi8-r')
#			print query[0].encode('koi8-r')
			
			for obj in self.data.itervalues():
#				print obj.oid, (obj.title).encode('koi8-r')
			
				if obj.object_kind == 'entity':
					commonData = [obj.oid, obj.title, obj.sort, obj.address, obj.phones, obj.faxes, obj.timetable, obj.license]
#					print (obj.oid)
					if searcharea=='intitles':
						where = commonData
					if searcharea=='everywhere':
						where = commonData + BeautifulSoup(obj.description).fetchText(re.compile('.*'))
					where.extend( (obj.url, obj.email) )	# Now we have list of stemmed words
				else:
					where = [obj.oid, obj.title, obj.sort]
					where = string.join(where, ' ')
					where = stemmer.stemWord(where)
					
				searchword = query
#				print type(searchword)
#				searchword = searchword.decode('koi8-r')
#				print type(searchword)
#				print type(where)
				
				for word in where:
					word = string.lower(word)
#					print word
#					print word.encode('koi8-r')
#					f.write(word)
#					f.write(searchword)
					if word.find(searchword) != -1:
						if obj not in result:
							result.append(obj)
			return sort(result)
		else:
			return ()
			
			
		
	def get_by_kind(self, object_kind='entity', sorted=False):	# sorted - field name to sort on
		"""
			Get object by kind: category or entity.
			Result can be sorted by name.
				object_kind = entity|category
				sorted = False|True
		"""
		objects = []
		for obj in self.data.itervalues():
			if obj.object_kind == object_kind:
				objects.append(obj)
		if sorted:
			li = []
			for i in objects:
				li.append( (getattr(i, sorted), i) )
			li.sort()
			li2 = []
			for i in li:
				li2.append(i[1])
			return li2
		else:
			return objects			
		
			
	def get_by_popularity(self, howmuch=10, object_kind='entity'):
		""" Return 10 most viewed objects """
		_list = []
		for obj in self.get_by_kind(object_kind=object_kind):
			_list.append( (int(obj.counter),obj.oid) )
		_list.sort()
		_list = _list[-howmuch:]
		_list.reverse()
		return _list
		
		
	def get_top_categories(self):
		cat_list = []
		for category in COLUMNS_ORDER:
			cat_list.append(database.get_object(category).title)
		return cat_list
		
		
#	def add_category(self, oid, title, description, parent):
#		""" Add new category object """
#		if self.data.has_key(oid) == False:
#			obj = Category()
#			obj.oid = str(oid)
#			obj.title = title
# 			obj.description = description
#			obj.parent = parent
#			self.data[oid] = obj
#			return obj
#		else:
#			return False

			
#	def add_entity(self, oid, title, entityType, address='', phones='', faxes='', \
#					timetable='', url='', description='', parent=None, x='', y='', vip=0):
#		""" Add new entity object """
#		if self.data.has_key(oid) == False:
#			obj = Entity()
#			obj.oid = str(oid)
#			obj.title = title
#			obj.entityType = entityType
#			obj.address = address
#			obj.phones = phones
#			obj.faxes = faxes
#			obj.timetable = timetable
#			obj.url = url
#			obj.description = description
#			obj.parent = parent
#			obj.x = x
#			obj.y = y
#			obj.vip = vip
#			self.data[oid] = obj
#			return obj
#		else:
#			return False
		
			

class Object:
	"""Common object, only for subclassing
	
	Instance attributes:
		parent : string			Point out to the container object
		object_kind : string	'entity' or 'category' type
		oid : string			An identificator - part of URL
		title : string			Human-readable title
		sort : string			What kind of the object? (advocate, taxi etc)
		created : time			Creation date/time
		modified : time			Last modification date/time
		counter : int			Visits counter
	"""

	def __init__(self):
		self.parent = None
		self.object_kind = ''
		self.oid = generate_oid()
		self.title = generate_oid()
		self.sort = ''
		self.created = str(localtime())
		self.modified = self.created
		self.counter = 0
		
		
	def get_parents(self, database):
		""" Return 'objects' list - objects in path to current object """
		obj = self
		objects = []
		while 1:
			objects.append(obj)
			obj = database.get_object(obj.parent)
			if not obj:
				break
		objects.reverse()
		del objects[0:1]		# we dont need link to homepage in breadcrumbs
		return objects
		
		
	def as_html(self, database='', is_logged=False):
		""" Return an HTML representation of this object """
		
		if self.object_kind == 'category':
			template_name = 'category.kid'
		if self.object_kind == 'entity':
			template_name = 'entity.kid'
			
		return kid.Template(
			file=templatesDir+template_name, 
			obj=self,
			is_logged=is_logged,
			database=database
		).serialize(output='xhtml', fragment=1)
		
	def get_change_date(self):
		try:
			a = string_to_date(self.modified)
			a = strftime('%d.%m.%Y', a)
		except:
			a = 'Undefined'
		return a 

	def get_create_date(self):
		try:
			a = string_to_date(self.created)
			a = strftime('%d.%m.%Y', a)
		except:
			a = 'Undefined'
		return a
		
	def getAdvertBlock(self):
		""" Get advert block for object """
		oid = self.oid
		if oid in advertData.keys():
			return advertData[oid]
		else:
			return advertData['common']

		
class Category(Object):
	"""A category in the tree of links
	
	Instance attributes:
		parent : string			Point out to the container object
		oid : string			An identificator - part of URL
		title : string			Human-readable title
		sort : string			What kind of the object? (advocate, taxi etc)
	"""
	
	def __init__ (self, parent, oid, title, sort=''):
		Object.__init__(self)
		self.parent = parent
		self.object_kind = 'category'
		self.oid = oid
		self.title = title
		self.sort = sort
		
		
	def as_form(self):
		""" Render edit form for the object """
		form = Form(action=IndexURL+"/edit", method="post")
		
		form.add_hidden("action", value='update')
		form.add_hidden("oid", value=self.oid)
		
		form.add_string("parent", title='Parent object ID (dont touch this)', value=self.parent, required=True)
		form.add_hidden("object_kind", value=self.object_kind)
		form.add_string("oidnew", title='ID', value=self.oid, required=True)
		form.add_string("title", title='Title', value=self.title, required=True)
		form.add_string("sort", title='Sort of object (taxi, cafe etc)', value=self.sort)
		form.add_int("counter", title='Visits counter', value=int(self.counter))
		form.add_string("created", title='Creation date/time', value=self.created)
		form.add_string("modified", title='Last modification date/time', value=self.modified)
		form.add_submit("save", "Save")
		return unicode(form.render())

		
	def import_data(self, a):
		''' Update object fields from dictionary '''
		if a.has_key('parent'): self.parent = a['parent']
		else: return 'Error in import_data() function: "parent" field absent.'
		if a.has_key('object_kind'): self.object_kind = a['object_kind']
		else: return 'Error in import_data() function: "object_kind" field absent.'
		if a.has_key('oid'): self.oid = a['oid']
		else: return 'Error in import_data() function: "oid" field absent.'
		if a.has_key('title'): self.title = a['title']
		else: return 'Error in import_data() function: "title" field absent.'
		if a.has_key('sort'): self.sort = a['sort']
		else: self.sort = None
		if a.has_key('created'): self.created = a['created']
		else: self.created = str(localtime())
		if a.has_key('modified'): self.modified = a['modified']
		else: self.created = str(localtime())
		if a.has_key('counter'): self.counter = int(a['counter'])
		else: self.counter = 0
		self.modified = str(localtime())
		return True

		
	def export_data(self):
		''' Export all object fields to dictionary '''
		a = {}
		a['parent'] = self.parent
		a['object_kind'] = self.object_kind
		a['oid'] = self.oid
		a['title'] = self.title
		a['sort'] = self.sort
		a['created'] = self.created
		a['modified'] = self.modified
		a['counter'] = self.counter
		return a


	def __str__(self):
		out = "parent: %s\n" % self.parent
		out += "kind: %s\n" % self.object_kind
		out += "oid: %s\n" % self.oid
		out += "title: %s\n" % self.title
		out += "sort: %s\n" % self.sort
		out += "created: %s\n" % self.created
		out += "modified: %s\n" % self.modified
		out += "counter: %s\n" % self.counter
		return out



class Entity(Object):
	"""Parental class for any entity object.
	
	Instance attributes:
		address : string			Address of the firm
		phones : string				Phones (if any)
		faxes : string				Faxes (if any)
		timetable : string			Time-table of the firm
		url : string				URL of site (if present)
		email : string				E-mail address
		email_visib : boolean		Is the email address visible?
		description : string		Long description (may contain prices etc)
		description_visib : boolean	Is the description field visible?
		map_xy : (int, int)			X,Y coordinates on big city map
		map_visib : boolean			Is the map should be displayed for this object?
		contact_name : string		Name of contact person (for email sending)
		visibility : boolean		Is this object should be displayed for site visitors?
		license : string			License number, if it's necessary for this sort of business
    """
	
	def __init__(self, parent, oid, title, sort='', address='', phones='', faxes='',
			timetable='', url='', email='', description='', map_xy=['',''], license=''):
		Object.__init__(self)
		self.parent = parent
		self.object_kind = 'entity'
		self.oid = oid
		self.title = title
		self.sort = sort
		self.address = address
		self.phones = phones
		self.faxes = faxes
		self.timetable = timetable
		self.url = url
		self.email = email
		self.email_visib = True
		self.description = description
		self.description_visib = True
		self.map_xy = map_xy
		self.map_visib = True
		self.contact_name = ''
		self.visibility = True
		self.license = license
		
		
	def as_form(self):
		""" Render edit form for the object """
		form = Form(action=IndexURL+"/edit", method="post")
		
		form.add_hidden("action", value='update')
		form.add_hidden("oid", value=self.oid)
		
		form.add_string("parent", title='Parent object ID (dont touch this)', value=self.parent, required=True)
		form.add_hidden("object_kind", value=self.object_kind)
		form.add_string("oidnew", title='ID', value=self.oid, required=True)
		form.add_string("title", title='Title', value=self.title, required=True)
		form.add_string("sort", title='Sort of object (taxi, cafe etc)', value=self.sort)
		form.add_string("address", title='Address of the firm', value=self.address)
		form.add_string("phones", title='Phones (if any)', value=self.phones)
		form.add_string("faxes", title='Faxes (if any)', value=self.faxes)
		form.add_string("timetable", title='Time-table of the firm', value=self.timetable)
		form.add_string("url", title='URL of site (if present)', value=self.url)
		form.add_string("email", title='E-mail address', value=self.email)
		form.add_checkbox("email_visib", title='Is the email address visible?', value=self.email_visib)
		form.add_text("description", title='Long description (may contain prices etc)', value=self.description, cols=62, rows=17)
		form.add_checkbox("description_visib", title='Is the description field visible?', value=self.description_visib)
		form.add_string("map_x", title='X coordinate on big city map', value=self.map_xy[0])
		form.add_string("map_y", title='Y coordinate on big city map', value=self.map_xy[1])		
		form.add_checkbox("map_visib", title='Is the map should be displayed for this object?', value=self.map_visib)
		form.add_string("contact_name", title='Name of contact person (for email sending)', value=self.contact_name)
		form.add_checkbox("visibility", title='Is this object should be displayed for site visitors?', value=self.visibility)
		form.add_string("license", title='License number, if it is necessary for this sort of business', value=self.license)		
		form.add_int("counter", title='Visits counter', value=int(self.counter))
		form.add_string("created", title='Creation date/time', value=self.created)
		form.add_string("modified", title='Last modification date/time', value=self.modified)
		form.add_submit("save", "Save")
		return unicode(form.render())

		
	def import_data(self, a):
		''' Update object fields from dictionary '''
		self.parent = a['parent']
		self.object_kind = a['object_kind']
		self.oid = a['oid']
		self.title = a['title']
		self.sort = a['sort']
		self.address = a['address']
		self.phones = a['phones']
		self.faxes = a['faxes']
		self.timetable = a['timetable']
		self.url = a['url']
		if a.has_key('email'):
			self.email = a['email']
		if a.has_key('email_visib'):
			self.email_visib = a['email_visib']
		else:
			self.email_visib = False
		self.description = a['description']
		if a.has_key('description_visib'):
			self.description_visib = a['description_visib']
		else:
			self.description_visib = False
		if a.has_key('map_x'):
			self.map_xy[0] = a['map_x']
			if a.has_key('map_y'): 
				self.map_xy[1] = a['map_y']
		if a.has_key('map_visib'):
			self.map_visib = a['map_visib']
		else:
			self.map_visib = False
		if a.has_key('contact_name'):
			self.contact_name = a['contact_name']
		if a.has_key('visibility'):
			self.visibility = a['visibility']
		else:
			self.visibility = False
		if a.has_key('license'):
			self.license = a['license']
		if a.has_key('created'):
			self.created = a['created']
		if a.has_key('modified'):
			self.modified = a['modified']
		self.counter = a['counter']
		
		self.modified = str(localtime())
		
		return self

		
	def export_data(self):
		''' Export all object fields to dictionary '''
		a = {}
		a['parent'] = self.parent
		a['object_kind'] = self.object_kind
		a['oid'] = self.oid
		a['title'] = self.title
		a['sort'] = self.sort
		a['address'] = self.address
		a['phones'] = self.phones
		a['faxes'] = self.faxes
		a['timetable'] = self.timetable
		a['url'] = self.url
		a['email'] = self.email
		a['email_visib'] = self.email_visib
		a['description'] = self.description
		a['description_visib'] = self.description_visib
		a['map_xy'] = self.map_xy
		a['map_visib'] = self.map_visib
		a['contact_name'] = self.contact_name
		a['visibility'] = self.visibility
		a['license'] = self.license
		a['created'] = self.created
		a['modified'] = self.modified
		a['counter'] = self.counter
		return a
		
		
	def __str__(self):
		out = u"parent: %s\n" % self.parent
		out += "kind: %s\n" % self.object_kind
		out += "oid: %s\n" % self.oid
		out += "title: %s\n" % self.title
		out += "sort: %s\n" % self.sort
		out += 'address: %s\n' % self.address
		out += 'phones: %s\n' % self.phones
		out += 'faxes: %s\n' % self.faxes
		out += 'timetable: %s\n' % self.timetable
		out += 'url: %s\n' % self.url
		out += 'email: %s\n' % self.email
		out += 'email_visib: %s\n' % self.email_visib
		out += 'description: %s\n' % self.description
		out += 'description_visib: %s\n' % self.description_visib
		out += 'map_xy: %s\n' % self.map_xy
		out += 'map_visib: %s\n' % self.map_visib
		out += 'contact_name: %s\n' % self.contact_name
		out += 'visibility: %s\n' % self.visibility
		out += 'license: %s\n' % self.license
		out += "created: %s\n" % self.created
		out += "modified: %s\n" % self.modified
		out += "counter: %s\n" % self.counter
		return out

		
	def noSpamEmail(self):
		''' Return email link like: <a href="&#0109;ailto&#0058;admin&#0064;homelan.lg.ua">admin&#0064;homelan.lg.ua</a>'''
		(name,server) = self.email.split('@')
		return '<a href="&#0109;ailto&#0058;%s&#0064;%s">%s&#0064;%s</a>' % (name, server, name, server)
		
	def splitEmail(self):
		return self.email.split('@')

		
def sort(objects):
	""" Sort objects by title """
	li = []
	for i in objects:
		li.append( (i.title, i) )
	li.sort()
	li2 = []
	for i in li:
		li2.append(i[1])
	return li2		

def generate_oid():
	oid = int(random.uniform(1000000, 2000000))
	return str(oid)


def clearString(s):
	""" Filter content from some symbols """
	s = re.sub('<!--|-->', '', s)
	s = re.sub(' \S |-|!|\. |,', ' ', s)
	s = re.sub(' \S ', ' ', s)
	s = re.sub('\s+', ' ', s)
	s = string.lower(s)
	return s
	
def stemString(s):
	""" 
		Get a string, cut some symbols 
		and return list of stemmed words
	"""
	s = clearString(s)
	return stemList(s.split())
	

def stemList(seq):
	"""
		Return list of stemmed words. Incoming list 
		must be already prepaired for stemming.
	"""
	if Stemmer:
		ST = Stemmer.Stemmer('russian')
		rseq = []
		for word in seq:
			word = string.lower(word)
			try:
				word = word.encode('koi8-r')
				word = ST.stem(word)
				word = word.decode('koi8-r')
				rseq.append(word)				
			except:
				rseq.append(word)
		return rseq
	else:
		return None

def string_to_date(a):
	""" Get the string like "(2006, 6, 10, 15, 44, 20, 5, 161, 1)"
		and convert it to time format
	"""
	a = a[1:-1].split(',')
	b = []
	for i in a:
		b.append(int(i))
	a = struct_time(b)
	return a
	
