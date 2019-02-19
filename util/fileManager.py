import config.fileConfig as fileC
import requests as re
class fileManager:
    def __init__(self,con):
        self.con = con

    def Begin(self):
        #connect = 'http://127.0.0.1:8080/index.php'
        connect = self.con.getUrl()
        #connect = connect + self.getBaseCode()
        #print(connect)
        date = {'key':self.getBaseCode()}
        firstURL=re.post(connect,date)
        #print(firstURL.text)
        print(firstURL.text)


    def getBaseCode(self):
        baseCodeForFile=fileC.PHP_fileBaseCode
        #print(baseCodeForFile)
        return baseCodeForFile
