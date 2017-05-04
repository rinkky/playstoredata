#! python2
# coding=utf-8

import MySQLdb
import dbconfig as cfg
from appdetail import AppDetail

tb_apps_col_names = (
	"app_uniq_name", 
	"app_name", 
	"app_isfree", 
	"app_price_id", 
	"app_price"
)

conn = None

def connect():
	global conn
	conn = MySQLdb.connect(
		host=cfg.host,
		port=cfg.port,
		user=cfg.user,
		passwd=cfg.passwd,
		db=cfg.db
	)

def commit():
	if conn:
		conn.commit()
		
def commit_and_close():
	if conn:
		conn.commit()
		conn.close()

def insert_or_update_appdetail(uniq_name,name,price):
	cur = conn.cursor()
	sqli = (
		"select * from tb_apps where app_uniq_name = \'{0}\'"
	).format(uniq_name)
	r = cur.execute(sqli)
	isonsale = False
	if 0 == r:
		sqli = (
			"insert into tb_apps({0},{1},{2},{3},{4}) values"
			"(\'{5}\',\'{6}\',{7},{8},{9})"
		).format(
			tb_apps_col_names[0],tb_apps_col_names[1],
			tb_apps_col_names[2],tb_apps_col_names[3],
			tb_apps_col_names[4], uniq_name, name, 
			isfree(price), "NULL", price
		)
	else:
		sqli = (
			"update tb_apps set app_name = \'{0}\', app_isfree = \'{1}\',"
			" app_price = \'{2}\' where app_uniq_name = \'{3}\'"
		).format(
			name, isfree(price), price, uniq_name
		)
		detail = cur.fetchone()
		if(detail[5] > price):
			isonsale = True
			sqli1 = (
				"replace into tb_apps_notice(app_id, time) values"
				"(\'{0}\' , curdate())"
			).format(detail[0])
			cur.execute(sqli1)
	r = cur.execute(sqli)
	cur.close()
	return isonsale

def get_appdetail_by_uniqname(uniq_name):
	cur = conn.cursor()
	sqli = (
		"select * from tb_apps where app_uniq_name"
		" = \'{0}\'"
	).format(uniq_name)
	r = cur.execute(sqli)
	if 0 == r:
		rst = None
	else:
		appdata = cur.fetchone()
		rst = AppDetail(appdata[1],appdata[2],appdata[5])
	cur.close()
	return rst

def get_appdetail_by_uniqnames(uniq_names):
	cur = conn.cursor()
	rst = []
	for uniq_name in uniq_names:
		sqli = ("select * from tb_apps where app_uniq_name = \'{0}\'"
		).format(uniq_name)
		r = cur.execute(sqli)
		if 0 != r:
			appdata = cur.fetchone()
			item = AppDetail(appdata[1],appdata[2],appdata[5])
			rst.append(item)
	cur.close()
	return rst

def get_appdetail_by_appids(ids):
	cur = conn.cursor()
	apps = []
	for appid in ids:
		sqli = "select * from tb_apps where app_id = {0}".format(str(appid))
		r = cur.execute(sqli)
		if 0 != r:
			appdata = cur.fetchone()
			item = AppDetail(appdata[1],appdata[2],appdata[5])
			apps.append(item)
	cur.close()
	return apps

def get_notice_apps_detail():
	cur = conn.cursor()
	sqli = "select app_id from tb_apps_notice"
	r = cur.execute(sqli)
	ids = []
	if r == 0:
		cur.close()
		return None
	else:
		ids = cur.fetchall()
		cur.close()
		return get_appdetail_by_appids([x[0] for x in ids])

def clean_notice_apps():
	cur = conn.cursor()
	sqli = "delete from tb_apps_notice"
	cur.execute(sqli)
	cur.close()

def get_all_uniqname():
	cur = conn.cursor()
	sqli = "select app_uniq_name from tb_apps"
	r = cur.execute(sqli)
	rst = []
	if r > 0:
		rst = cur.fetchall()
	cur.close()
	return [x[0] for x in rst]

def set_notice(app_id):
	cur = conn.cursor()
	sqli = (
		"replace into tb_apps_notice(app_id, time) "
		"values (\'{0}\' , getdate())"
	).format(app_id)
	cur.execute(sqli)
	cur.close()

def isfree(price):
	if price == 0:
		return 1
	else:
		return 0

