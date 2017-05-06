#! python2
# coding=utf-8

import requests
import appmonsta_auth as my_auth

def get_detail_by_uniqname(uniq_name):
    payload = {"country": "US"}
    # This header turns on compression to reduce 
    # the bandwidth usage and transfer time.
    headers = {'Accept-Encoding': 'deflate, gzip'}
    r = requests.get(
        "https://api.appmonsta.com/v1/stores/android/details/{0}.json".format(
            uniq_name
        ),
        auth = my_auth.appmonsta_auth,
        params = payload,
        headers = headers,
        stream = True
    )
    if r.status_code == 200:
        data = r.json()
        return {
            "uniq_name":uniq_name, 
            "name":data["app_name"], 
            "price":data["price"] 
        }
    else:
        return None