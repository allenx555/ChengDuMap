# 放到api目录下跑
from scipy import spatial
import numpy as np
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_login import LoginManager
from flask_login import current_user
from Map import db
from Map import app
import json
from Map.user.models import User
from Map.event.models import Event
from Map.comment.models import Comment
from datetime import datetime

forward = ([1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1])

def fetch_usr():                                        #得到主用户的数据
    user = current_user
    cosx = list()
    numlist = to_numlist(user.likelist)
    for i in numlist:                          #获取用户的个性向量
        cosx.append(i)
    return cosx

def fetch_other(uid):                                      #得到其他用户的数据
    #uid2 = FromComment_eventid_GetUserid(eventid)
    user2 = User.query.filter_by(id=uid.first())
    cosy = list()
    numlist = to_numlist(user2.likelist)
    for i in numlist:
        cosy.append(i)
    return cosy

def like_rate():                              #计算出兴趣的相似程度
    x = np.array(fetch_usr)
    y = np.array(fetch_other)
    user = current_user
    dic = {"uid":user.id,"uphone":user.phone,"like_rate":1 - spatial.distance.cosine(x,y)}
    js = json.dumps(dic,indent=4)
    return js

def get_recomment_pow():                                #计算出最接近用户兴趣的三种类别
    x = np.array(fetch_usr())
    result = list()
    for i in forward:
        y = np.array(i)
        result.append(1 - spatial.distance.cosine(x,y))
    power = ger3(result)
    return power

def ger3(result):                                       #辅助计算公式
    j = 0
    maxnum = 0
    while j < 10:
        if maxnum == 0:
            maxnum = result[j]
            index1 = j
        elif maxnum < result[j]:
            maxnum = result[j]
            index1 = j
        j = j + 1
    result.pop(index1)
    j = 0
    maxnum = 0
    while j < 9:
        if maxnum == 0:
            maxnum = result[j]
            index2 = j
        if maxnum < result[j]:
            maxnum = result[j]
            index2 = j
        j = j + 1
    result.pop(index2)
    j = 0
    maxnum = 0
    while j < 8:
        maxnum = result[0]
        index3 = 0
        if maxnum < result[j]:
            maxnum = result[j]
            index3 = j
        j = j + 1
    result.pop(j)
    return index1,index2,index3

def recomment():                       #返回推荐地图的经纬度,list
    '''搜索数据库中的对应的信息
    返回一个地图list'''
    rec, index = CFr(fetch_usrMain())
    user = current_user
    numlist = to_numlist(user.likelist)
    numlist[index] = rec
    rec_list = list(get_recomment_pow())
    event = Event.query.filter_by(id=rec_list[0]).all()
    if len(event) < 10 :
        event.bak = Event.query.filter_by(id=rec_list[1]).all()
        for e in event.bak:
            event.append(e)
            if len(event) > 10:
                break
    if len(event) < 10 :
        event.bak = Event.query.filter_by(id=rec_list[2]).all()
        for e in event.bak:
            event.append(e)
            if len(event) > 10:
                break
    map_list = list()
    for e in event:
        map_list.append([e.x,e.y])
    return map_list

def fetch_usrMain():                                    #获取主用户的比重在0.3以上的方向,索引,辅助计算值
    user = current_user
    '''uid = user.id
    userdata = User.query.filter_by(id=uid).first()'''
    cosx = list()
    numlist = to_numlist(user.likelist)
    for i in numlist:                          #获取用户的个性向量
        cosx.append(i)
    sumlike = sum(cosx)
    filt = list()
    index = list()
    j = 0
    for i in cosx:
        if i/sumlike > 0.3:
            filt.append(i)
            index.append(j)
        j = j + 1
    return filt,index,sumlike/len(filt)

def CFr(filt,index,avr):                                #基于用户的协同过滤算法,在推荐活动时一定程度上修正用户的倾向
    user = current_user
    uid = user.id
    userdata = User.query.all()
    j = 0
    for i in userdata:
        if i.id == uid:
            userdata.pop(j)
            break
        j = j + 1

    cosx = np.array(filt)
    maxlike = 0
    numlist = to_numlist(user.likelist)
    for u in userdata:          #计算相似度最大
        l = list()
        ulist = to_numlist(u.likelist)
        for i in index:
            l.append(ulist[i])
        cosy = np.array(l)
        result = adjust_cosine(cosx, cosy)
        if maxlike == 0:
            maxlike = result
            des = u
        if maxlike < result:
            maxlike = result
            des = u
    j = 0
    maxm = 0
    deslist = to_numlist(des.likelist)
    for i in deslist:
        flag = 0
        for a in index:
            if j == a:
                flag = 1
                break
        if flag == 1:
            continue
        if maxm == 0:
            maxm = deslist[j]
            index_b = j
        elif maxm < deslist[j]:
            maxm = deslist[j]
            index_b = j
        j = j + 1
    rec = avr + maxlike*(numlist[index_b] - deslist[index_b])
    return rec, index_b

def adjust_cosine(cosx, cosy):                              #计算调整后的余弦相似度
    sumnumber = sum(cosx) + sum(cosy)
    lenth = len(cosx) + len(cosy)
    mean = sumnumber / lenth
    j = 0
    for i in cosx:
        cosx[j] = i - mean
        j = j + 1
    j = 0
    for i in cosy: 
        cosy[j] = i - mean
        j = j + 1
    return 1 - spatial.distance.cosine(cosx,cosy)

def to_numlist(string):
    string = string.replace("'","").replace(",","")
    numbers = list()
    for i in string:
        numbers.append(int(i))
    return numbers

x = np.array(to_numlist(User.query.filter_by(id=1).first().likelist))
y = np.array(to_numlist(User.query.filter_by(id=2).first().likelist))
print(1 - spatial.distance.cosine(x,y))
