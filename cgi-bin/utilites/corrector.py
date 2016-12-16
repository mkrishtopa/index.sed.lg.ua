# -*- coding: UTF-8 -*-

from classes import DataBase


if __name__ == "__main__":
	db = DataBase()
	print db.delObject('cashmachines_privatbank')
#	obj = Category('root', 'automarket', '123', '')
#	db.addObject(obj)
	db.save()

