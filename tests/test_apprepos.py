# coding=utf-8

import unittest
from apprepos import dbconfig
from apprepos import apprepos

class TestApprepos(unittest.TestCase):

	def setUp(self):
		dbconfig.db = "noticemetest"
		apprepos.connect()
		self._clear_all_table()


	def tearDown(self):
		apprepos.commit_and_close()
		print("tearDown")


	def test_app_detail(self):
		uniq_name="com.test.test"
		name="test"
		price=1.99
		apprepos.insert_or_update_appdetail(
			uniq_name=uniq_name,
			name=name,
			price=price
		)
		apprepos.commit()
		apprepos.insert_or_update_appdetail(
			uniq_name=uniq_name,
			name=name,
			price=price
		)
		apprepos.commit()
		app = apprepos.get_appdetail_by_uniqname(uniq_name)
		map(
			self.assertEqual,
			[uniq_name, name, price],
			[app.uniq_name, app.name, app.price]
		)
		apps = apprepos.get_appdetail_by_uniqnames([uniq_name])
		map(
			self.assertEqual,
			[uniq_name, name, price],
			[apps[0].uniq_name, apps[0].name, apps[0].price]
		)


	def test_app_notice(self):
		uniq_name="com.test.test1"
		name="test"
		price=1.99
		apprepos.insert_or_update_appdetail(
			uniq_name,
			name,
			price
		)
		apprepos.commit()
		price = 0.99
		apprepos.insert_or_update_appdetail(
			uniq_name,
			name,
			price
		)
		apprepos.commit()
		apps = apprepos.get_notice_apps_detail()
		map(
			self.assertEqual,
			[uniq_name, name, price],
			[apps[0].uniq_name, apps[0].name, apps[0].price]
		)

		apprepos.clean_notice_apps()
		apprepos.commit()
		apps = apprepos.get_notice_apps_detail()
		self.assertTrue(apps is None)


	def _clear_all_table():
		cur = apprepos.conn.cursor()
		sqlis = [
			"delete from tb_apps",
			"delete from tb_apps_notice",
			"delete from tb_prices"
		]
		map(cur.execute,sqlis)
		cur.cose()
