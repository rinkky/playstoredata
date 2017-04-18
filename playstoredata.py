#! python2
# coding: utf-8

from apprepos import apprepos
from datagetter import appmonsta
import re
import math

keynames = ("uniq_name","name","price")

def get_app_detail(uniq_name):
	apprepos.connect()
	rst = apprepos.get_appdetail_by_uniqname(uniq_name)
	apprepos.commit_and_close()
	
	#1. 
	if rst != None :
		return {keynames[0]:uniq_name,keynames[1]:rst.name, keynames[2]:rst.price}

	#2.
	dict = appmonsta.get_detail_by_uniqname(uniq_name)
	if None == dict :
		return None;
	#3.
	insert_or_update_data(uniq_name,dict["name"],doller_to_float(dict["price"]))
	return {keynames[0]:uniq_name, keynames[1]:dict["name"], keynames[2]: doller_to_float(dict["price"])}

def insert_or_update_data(uniq_name,name,price):
	apprepos.connect()
	apprepos.insert_or_update_appdetail(uniq_name,name,price)
	apprepos.commit_and_close()

def doller_to_float(str):
	p = re.compile(r"\d+\.?\d{0,2}")
	m = p.search(str)
	if m :
		return float(m.group())
	return 0.0



#test case
if __name__ == "__main__":
#1. exist in mysql
#2. not exist in mysql
#3. no such app
	r = get_app_detail("com.noodlecake.chameleonrun")
	print(r)