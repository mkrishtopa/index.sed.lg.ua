#
# Convert Index old database (in text format) to new format
#

import cPickle
from configobj import ConfigObj
from classes import *

def save_pickle():

	a = {}

	for (oid, d) in DB.items():

		if d['object_kind'] == 'Category':
			obj = Category('someparent', 'foo', 'Foo')

		if d['object_kind'] == 'Entity':
			obj = Entity('someparent', 'foo', 'Foo')

		for (k,v) in d.iteritems():		# We should store data in unicode
			try:
				d[k] = unicode(v, 'utf-8')
			except:
				pass

		obj.import_data(d)
		obj.object_kind = string.lower(obj.object_kind)
		obj.description_visib = 'yes'
		obj.email_visib = 'yes'
		obj.map_visib = 'yes'
		obj.visibility = 'yes'

		if obj.object_kind == 'entity':
			obj.map_xy = d['map_xy']

		a[str(oid)] = obj
#		obj = None

	f = file('database\\pickled.bin', 'wb')
	cPickle.dump(a, f, protocol=2)
	f.close()

	print len(a)



if __name__ == "__main__":

	DB = ConfigObj('data.ini')

	save_pickle()

