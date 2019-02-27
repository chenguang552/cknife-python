"""
    作者：李晨光
    日期：2018 12 20
"""
import sys
from util.connect import connect
from util.shellManager import shellManager
from util.fileManager import fileManager
from util.databaseManager import databaseManager
REC_SYS = sys.argv
try:
    URL = None
    KEY = None
    TYP = None
    CONNECT = connect()
    #CONNECT = connect()
    for i in range(len(REC_SYS)):
        if REC_SYS[i] == '-u':
            #global URL
            URL = REC_SYS[i+1]
            #把url写入connect.url
            i = i + 2
        if REC_SYS[i] == '-k':
            #global KEY
            KEY = REC_SYS[i+1]
            #把key写入connect.key
            i = i + 2
        if REC_SYS[i] == '-t':
            TYP = REC_SYS[i+1]
            i = i + 2
        if URL != None and KEY != None and TYP != None:
            CONNECT.setUrl(URL)
            CONNECT.setKey(KEY)
            CONNECT.setTyp(TYP)
            #print(CONNECT.getUrl(),CONNECT.getKey(),CONNECT.getTyp())
            #print(URL,KEY,TYP)
            break
    for j in range(len(REC_SYS)):
        #shell命令处理程序
        if REC_SYS[j] == '--shell':
            SHELL = shellManager(CONNECT)
            SHELL.Begin()
            quit()
        #文件管理命令处理程序
        if REC_SYS[j] == '--file':
            FILE = fileManager(CONNECT)
            FILE.Begin()
            quit()
        #数据库管理命令处理程序
        if REC_SYS[j] == '--database' or REC_SYS[j] == '--db':
            DB = databaseManager(CONNECT)
            DB.Begin()
            quit()
except:
    pass
