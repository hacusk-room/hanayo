# coding: utf-8
import urllib.request
import json
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE stock(category_id, name_text)''')

def yahooapi():
  load_setting = open("setting.json")
  json_setting = json.load(load_setting)

  host = "https://shopping.yahooapis.jp"
  path = "/ShoppingWebService/V1/json/itemSearch?"

  # Query parameter
  appid = format(json_setting["appid"])
  sort = "&sort=%2bprice"
  jan = input(">> ")

  # Request URL
  url = host + path + "appid=" + appid + "&jan=" + jan + sort
  response = urllib.request.urlopen(url)

  return response.read()

def do_json(s):
  json_dict = json.loads(s)
  print("商品名: {}".format(json_dict["ResultSet"]["0"]["Result"]["0"]["Name"]))
  c.execute("INSERT INTO stock VALUES (?, ?)", (1, json_dict["ResultSet"]["0"]["Result"]["0"]["Name"]))
  conn.commit()

if __name__ == '__main__':
  json_str = yahooapi()
  do_json(json_str)

conn.close()