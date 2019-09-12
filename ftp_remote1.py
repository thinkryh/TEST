# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @thinkryh 2019/5/22

import os,datetime,zipfile,re,shutil
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
import requests
import json

now_date=(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y%m%d')
localfiles = 'E:/FTP/DataConnect/' # 文件储存本地根目录
local = localfiles+'report%s.zip' %now_date # 压缩包文件地址

def ftp_download():
    # FTP地址;files(username:password@ip:port);  name(指定文件);  local(本地地址）；
    FTP = 'ftp://ftpuser-readonly:udz4djp8xeid@public.dc.tcy365.net:53186'
    name = '/playgame/report81.zip'
    download_file=FTP+name+' -o '+local
    print(download_file)
    print(os.popen('curl %s' %FTP).readlines())
    print('****start curl ftp****')
    DownLoad_remote = os.popen('curl %s' %download_file).readlines()
    print('----DownLoad is ok---- \n****start zipfile****')

def un_downloadzip():
    '''
    1.找到压缩包中指定文件，并进行解压
    2.将对应文件放到指定文件夹中
    3.删除源文件夹
    '''
    f = zipfile.ZipFile(local,'r')
    # un_zipfile为解压文件将要解压后的默认文件名 f.namelist为解压文件的列表信息
    for un_zipfile in f.namelist():
        # ssllcc 包含指定字符的列表
        ssllcc = ['start','showcards','login','logout','customization','combatgains']
        for z_files in ssllcc:
            # z_files 包含ssllcc列表中字符以及后缀为.csvde的
            if z_files in un_zipfile and un_zipfile.endswith('.csv'):
                print ('prodcess:   '+un_zipfile)
                # 解压后文件夹地址（根据解压后文件路径信息所变化)
                un_zipfiles=localfiles+un_zipfile
                # 创建根目录下的子文件夹
                move_zipfiles=localfiles+"%s"%(z_files)
                if not os.path.exists(move_zipfiles):
                    os.mkdir(move_zipfiles)
                # 定义解压后文件储存位置
                gamefiles= move_zipfiles+'/%s_%s.csv'%(z_files,now_date)
                # 解压文件到根目录，localfiles为默认的路径
                f.extract(un_zipfile, localfiles)
                # 移动解压后的文件到指定位置，gamefiles为创建的制定文件夹及名称
                shutil.move('%s' %un_zipfiles,'%s' %gamefiles)
                # 删除源文件地址（./date/)
                shutil.rmtree('%sdata/'%localfiles)
    print('----UnZip is ok----')


# def upload_mysql():
#     '''
#     将数据上传到mysql中
#     连接mysql
#     '''
#     host = 'mysql9.tcy365.org'
#     user = 'chunk81'
#     password = '74avuwsxnpC5'
#     database = 'chunk81logdb'
#     port = 3306
#     charset = 'gb2312'
#     engine = create_engine('mysql+mysqlconnector://%s:%s@%s:%s/%s'%(user,password,host,port,database))
#     # con = engine.connect()
#     df = pd.read_csv('E:/FTP/DataConnect/start/start_201905201.csv','enconding=utf-8',',')
#     # df = pd.DataFrame([[1,2,3],[2,3,4]],columns=list('abc'))
#     df.to_sql('start_2019052011',engine,index=False)
#
#     config1 = {'host':'192.168.8.173',
#               'user':'root',
#               'password':'123',
#               'database':'221',
#               'charset':'gb2312'}
#     cnn = mysql.connector.connect(**config1)
#     cursor = cnn.cursor()
#     sql = "select * from custom limit 1;"
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     print(data)
#     cursor.close()
#     cnn.close()

#access_token
def dingtoken():
    url = 'https://oapi.dingtalk.com/robot/send?access_token=\
b69e8c5ad93a94628c79d4b0a25d74a7939c578ab81d692c5a375982ceb26fc7'
    #数据发送
    title = 'FTP'
    s = 'Fine'
    HEADERS = {'Content-Type': "application/json ;charset=utf-8 "}
    String_textMsg = {"msgtype": "markdown","markdown": {"title": title,"text":s}}
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.text)

if __name__ == '__main__':
    ftp_download()
    un_downloadzip()
    dingtoken()
print("All Izz Well")