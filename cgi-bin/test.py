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
    f = u"<!---->-!.,��������QWErty"
    print clearString(f).encode('koi8-r')

def test_search():
    query = u"����"
    res = db.search(query)
#    print res
#    print len(res)
    for i in res:
        print i.oid

def test_stemmerString():
    st = u"������ ������"
#   st = '''������ ������ �������������� ����������� ������� �� �.���������� ������� ��.������� 10 43443 45247 43443 ������� ���� ������� 1966 ���� ������: ���������� ����������� �������� ����������� ����������� ������� ������� ����������� �������� ����������� ������� ������������� ������ ������ �������������� ����������: �������� ��������� ������� ������� �������� ����������� ������� �������� ������������ ��� ������� ���� ������� ���������� ��� �� 500 ������� ����� ��� ��� ���������� ������������� ��������� ���������� ��� ������� ����� ���������� ��������� ����� �� 50 ������� 12 ������� ��� ��������� 30 ������� ��� �������������� ������� ������������ ���������� ��� �� ������ ����� ��������� �������� '������ �����' ����������� �������� �������������� ������ ��������� �� 80 ���� �������� ����� �� 3 �������� ����������� ������ ������� ���� ���������� ���� ������� ��� �������������� �� ������ ������ ������� �������� ������� ���������� ������� ������ ������������'''
    print st.encode('koi8-r')
    print " ".join(stemString(st)).encode('koi8-r')

def test_stemmerList():
    sl = [u'������', u'������']
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