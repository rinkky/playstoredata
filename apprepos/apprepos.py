#! python2
# coding: utf-8

import MySQLdb
import dbconfig as cfg
from appdetail import AppDetail

tb_apps_col_names = ("app_uniq_name", "app_name", "app_isfree", "app_price_id", "app_price")
conn = None

def connect():
	global conn
	conn = MySQLdb.connect(
		host = cfg.host,
		port = cfg.port,
		user = cfg.user,
		passwd = cfg.passwd,
		db = cfg.db
		)

def commit_and_close():
	if conn :
		conn.commit()
		conn.close()

def insert_or_update_appdetail(uniq_name,name,price):
	cur = conn.cursor()
	sqli = "select * from tb_apps where app_uniq_name = \'{0}\'".format(uniq_name)
	r = cur.execute(sqli)
	if 0 == r:
		sqli = "insert into tb_apps({0},{1},{2},{3},{4}) values(\'{5}\',\'{6}\',{7},{8},{9})".format(tb_apps_col_names[0],tb_apps_col_names[1],tb_apps_col_names[2],tb_apps_col_names[3],tb_apps_col_names[4], uniq_name, name, isfree(price), "NULL", price)
	else:
		sqli = "update tb_apps set app_name = \'{0}\', app_isfree = \'{1}\', app_price = \'{2}\' where app_uniq_name = \'{3}\'".format(name, isfree(price), price, uniq_name)
	r = cur.execute(sqli)
	cur.close()
	return r != 0

def get_appdetail_by_uniqname(uniq_name):
	cur = conn.cursor()
	sqli = "select * from tb_apps where app_uniq_name = \'{0}\'".format(uniq_name)
	r = cur.execute(sqli)
	if 0 == r:
		rst = None
	else:
		appdata = cur.fetchone()
		rst = AppDetail(appdata[1],appdata[2],appdata[5])
	cur.close()
	return rst

def isfree(price):
	if price == 0:
		return 1
	else:
		return 0