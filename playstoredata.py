#! python2
# coding=utf-8

from apprepos import apprepos
from datagetter import appmonsta
import re
import math

keynames = (
	"uniq_name",
	"name",
	"price"
)
def get_all_uniqname():
	apprepos.connect()
	apps = apprepos.get_all_uniqname()
	apprepos.commit_and_close()
	return apps

def get_app_detail(uniq_name):
	apprepos.connect()
	rst = apprepos.get_appdetail_by_uniqname(uniq_name)
	apprepos.commit_and_close()
	
	if rst is not None:
		return {
			keynames[0]:uniq_name,
			keynames[1]:rst.name, 
			keynames[2]:rst.price
		}
	else:
		return update_data_from_appmonsta(uniq_name)

def update_data_from_appmonsta(uniq_name):
	detail = appmonsta.get_detail_by_uniqname(uniq_name)
	if detail is None:
		return None	
	_insert_or_update_data(
		uniq_name,detail["name"],
		_doller_to_float(detail["price"])
	)
	return {
		keynames[0]:uniq_name, 
		keynames[1]:detail["name"], 
		keynames[2]: _doller_to_float(detail["price"])
	}

def update_all_data_from_appmonsta():
	apprepos.connect()
	lst = apprepos.get_all_uniqname()
	if None == lst:
		apprepos.commit_and_close()
		return None
	else:
		import time
		for row in lst:
			#row is a  tuple =>("com.xxx.xxx",)
			uniq_name = row[0]
			dict = appmonsta.get_detail_by_uniqname(uniq_name)
			if None != dict:
				apprepos.insert_or_update_appdetail(
					uniq_name,
					dict[keynames[1]],
					_doller_to_float(dict[keynames[2]])
				)
			time.sleep(5)
		apprepos.commit_and_close()

def get_notice_apps():
	apprepos.connect()
	apps = apprepos.get_notice_apps_detail()
	apprepos.commit_and_close()
	return apps
	
def clean_notice_apps():
	apprepos.connect()
	apprepos.clean_notice_apps()
	apprepos.commit_and_close()

def _insert_or_update_data(uniq_name,name,price):
	apprepos.connect()
	apprepos.insert_or_update_appdetail(uniq_name,name,price)
	apprepos.commit_and_close()

def _doller_to_float(str):
	p = re.compile(r"\d+\.?\d{0,2}")
	m = p.search(str)
	if m:
		return float(m.group())
	else:
		return 0.0



#test case
#if __name__ == "__main__":
#1. exist in mysql
	#r = get_app_detail("com.noodlecake.chameleonrun")
	#print(r)
#2. not exist in mysql
	#r = get_app_detail("")
	#print(r)
#3. no such app
	#r = get_app_detail("")
	#print(r)
	
	#update_all_data_from_appmonsta()

	#_insert_or_update_data("com.noodlecake.chameleonrun","Chameleonrun",0.1)