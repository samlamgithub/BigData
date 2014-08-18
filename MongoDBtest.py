import pymongo
from pymongo import Connection
import simplejson
import json
import random

#####Variables for Mongo Connections#####

mongoHost = ''
mongoPort = ''
db_name = ''
username = ''
password = ''
collnection_Name = ['BrowserHistory']

conn = Connection("127.0.0.1",27017)
db = conn[db_name] #连接库
db.authenticate(username,password) #用户认证

AccountId = []
TYPEID = []
cName = []
new_sub = []
uid = ''

id = ''

#top ten websites for this id#
toptenforthisid = [u'',u'',u'',u'',u'',u'',u'',u'',u'',u'']

dateandhistory = []

count = 0

import datetime

for data in db.BrowserHistory.find({"AccountId": id}):
    
    count += 1
    
    if data['Host'] in toptenforthisid:
        dateandhistory.append([data['VisitTime'].year, data['VisitTime'].month, data['VisitTime'].day, data['VisitTime'].hour, data['VisitTime'].minute, str(data['Host'])])
    
    print count 
    
print dateandhistory



#example of writing csv
def writecsvforlistelment(data,csvname):#data = [['None', 'need to decide!'], ['Sharing', 'need to decide!'], ['Shopping', 'need to decide!'], ['Storage', 'need to decide!'], ['Applications', 'need to decide!'], ['Services', 'need to decide!'], ['Networking', 'need to decide!'], ['None', 'need to decide!'], ['Forums', 'need to decide!'], ['Software', 'need to decide!']]

    import csv

    with open('%s.csv'%csvname, 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(data)


writecsvforlistelment(dateandhistory,'datetimeandtop10')


db.user.save({'id':1,'name':'kaka','sex':'male'})
#插入一个数据
for id in range(2,10):
    name = random.choice(['steve','koby','owen','tody','rony'])
    sex = random.choice(['male','female'])
    db.user.insert({'id':id,'name':name,'sex':sex}) 
#通过循环插入一组数据
content = db.user.find()
#打印所有数据
for i in content:
    print i


#
#
#

from pymongo import Connextion #import module
con = Connection()
db = con.test # connext to test database
posts = db.post # connect to post set in test database

import datetime

post1 = {"title":"I Love Python",
           "slug":"i-love-python",
           "author":"SErHo",
           "content":"I Love Python....",
           "tags":["Love","Python"],
           "time":datetime.datetime.now()}
   
post2 = {"title":"Python and MongoDB",
          "slug":"python-mongodb",
          "author":"SErHo",
          "content":"Python and MongoDB....",
          "tags":["Python","MongoDB"],
          "time":datetime.datetime.now()}
  
post3 = {"title":"SErHo Blog",
          "slug":"serho-blog",
          "author":"Akio",
          "content":"SErHo Blog is OK....",
          "tags":["SErHo","Blog"],
          "time":datetime.datetime.now()}
  
posts.insert(post1)
posts.insert(post2)
posts.insert(post3)
