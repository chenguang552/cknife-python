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
            pass
        #print(baseCodeForFile)
        return baseCodeForFile

    def check(self,text):
        if len(text)<2:
            print('缺少参数')
        return len(text)

    def path(self,re):
        if self.con.getTyp()=="php":
            getpath = fileC.PHP_GETPATH
            getpath = getpath.replace('@@',self.changePath(),1)
            date = { self.key : getpath }
            commit = re.post(self.connect,date)
            return commit.text
        if self.con.getTyp()=="jsp":
            getpath = fileC.JSP_GETPATH
            #date = { self.key : 'file','ds':getpath}
            date = { self.key : "file",'cpath':self.changePath(),'ds':getpath}
            commit = re.post(self.connect,date)
            return commit.text
        if self.con.getTyp()=="asp":
            pass
        

    def changePath(self):
        j = 0
        str = self.CHANGE_PATH[0]
        
        if self.con.getTyp()=="php":
            line='/'
        if self.con.getTyp()=="jsp":
            line='\\'
        while j!=self.i:
            j = j + 1
            str = str + self.CHANGE_PATH[j]+ line 
        if self.con.getTyp()=="php":
            changePach_ = fileC.PHP_CHDIR.replace('##',str,1)
        if self.con.getTyp()=="jsp":
            changePach_ = str
        if self.con.getTyp()=="asp":
            pass
        return changePach_

    def FileMain(self,re):
        self.i = 0
        self.CHANGE_PATH = dict.fromkeys(range(1024),'')
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
                            date = { self.key : CD }
                            commit = re.post(self.connect,date)
                        if self.con.getTyp()=="jsp":
                            pass
                        if self.con.getTyp()=="asp":
                            pass
                        
                        # print(commit.text)
                    elif flag[1] != '.' and self.i != 0:
                        self.i = self.i - 1
                    continue
                else:
                    continue

            if flag[0] == 'read':
                if self.check(flag)>1:
                    if self.con.getTyp()=="php":
                        READ_r = fileC.PHP_READ.replace('##',flag[1],1)
                        READ_r = READ_r.replace('@@',self.changePath(),1)
                        date = { self.key : READ_r }
                    if self.con.getTyp()=="jsp":
                        READ_r = fileC.JSP_READ
                        date = { self.key : "file",'cpath':self.changePath(),'ds':READ_r,'c1':flag[1]}
                    if self.con.getTyp()=="asp":
                        pass
                   
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'delete' or flag[0] == 'rm':
                if self.check(flag)>1:
                    if self.con.getTyp()=="php":
                        delete = fileC.PHP_DELETE.replace('##',flag[1],1)
                        delete = delete.replace('@@',self.changePath(),1)
                        date = { self.key : delete }
                    if self.con.getTyp()=="jsp":
                        delete = fileC.JSP_DELETE
                        date = { self.key : "file",'cpath':self.changePath(),'ds':delete,'c1':flag[1]}
                    if self.con.getTyp()=="asp":
                        pass
                    
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'mkdir':
                if self.check(flag)>1:
                    if self.con.getTyp()=="php":
                        mkdir = fileC.PHP_MKDIR.replace('##',flag[1],1)
                        mkdir = mkdir.replace('@@',self.changePath(),1)
                        date = { self.key : mkdir }
                    if self.con.getTyp()=="jsp":
                        mkdir = fileC.JSP_MKDIR
                        date = { self.key : "file",'cpath':self.changePath(),'ds':mkdir,'c1':flag[1]}
                    if self.con.getTyp()=="asp":
                        pass
                    
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'rmdir':
                if self.check(flag)>1:
                    if self.con.getTyp()=="php":
                        rmdir = fileC.PHP_RMDIR.replace('##',flag[1],1)
                        rmdir = rmdir.replace('@@',self.changePath(),1)
                        date = { self.key : rmdir }
                    if self.con.getTyp()=="jsp":
                        rmdir = fileC.JSP_RMDIR
                        date = { self.key : "file",'cpath':self.changePath(),'ds':rmdir,'c1':flag[1]}
                    if self.con.getTyp()=="asp":
                        pass
                    
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'mkfile':
                if self.check(flag)>1:
                    if self.con.getTyp()=="php":
                        mkfile = fileC.PHP_MKFILE.replace('##',flag[1],1)
                        mkfile = mkfile.replace('@@',self.changePath(),1)
                        date = { self.key : mkfile }
                    if self.con.getTyp()=="jsp":
                        mkfile = fileC.JSP_MKFILE
                        date = { self.key : "file",'cpath':self.changePath(),'ds':mkfile,'c1':flag[1]}
                    if self.con.getTyp()=="asp":
                        pass
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'ls' or flag[0] == 'dir':
                if self.con.getTyp()=="php":
                    dir = fileC.PHP_GETDIR
                    dir = dir.replace('@@',self.changePath(),1)
                    date = { self.key : dir }
                if self.con.getTyp()=="jsp":
                    dir = fileC.JSP_GETDIR
                    date = { self.key : "file",'cpath':self.changePath(),'ds':dir}
                if self.con.getTyp()=="asp":
                    pass
                commit = re.post(self.connect,date)
                print(commit.text,"\n")
                continue

            if flag[0] == 'pwd' or flag[0] == 'cwd':
                if self.con.getTyp()=="php":
                    pwd = fileC.PHP_GETPATH
                    pwd = pwd.replace('@@',self.changePath(),1)
                    date = { self.key : pwd }
                if self.con.getTyp()=="jsp":
                    pwd = fileC.JSP_GETPATH
                    date = { self.key : "file",'cpath':self.changePath(),'ds':pwd}
                if self.con.getTyp()=="asp":
                    pass
                
                commit = re.post(self.connect,date)
                print(commit.text,"\n")
                continue

            if flag[0] == 'rename':
                if self.check(flag)>2:
                    if self.con.getTyp()=="php":
                        rename = fileC.PHP_RENAME.replace('#1',flag[1],1)
                        rename = rename.replace("#2",flag[2])
                        rename = rename.replace('@@',self.changePath(),1)
                        date = { self.key : rename }
                    if self.con.getTyp()=="jsp":
                        rename = fileC.JSP_RENAME
                        date = { self.key : "file",'cpath':self.changePath(),'ds':rename,'c1':flag[1],'c2':flag[2] }
                    if self.con.getTyp()=="asp":
                        pass
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'copy':
                if self.check(flag)>2:
                    if self.con.getTyp()=="php":
                        copy = fileC.PHP_COPY.replace('#1',flag[1],1)
                        copy = copy.replace("#2",flag[2])
                        copy = copy.replace('@@',self.changePath(),1)
                        date = { self.key : copy }
                    if self.con.getTyp()=="jsp":
                        copy = fileC.JSP_COPY
                        date = { self.key : "file",'cpath':self.changePath(),'ds':copy,'c1':flag[1],'c2':flag[2] }
                    if self.con.getTyp()=="asp":
                        pass
                    
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'write':
                if self.check(flag)>2:
                    num = len(flag)
                    strw = flag[2]
                    n = 3
                    while  n != num:
                        strw = strw + ' ' + flag[n]
                        n = n + 1
                    print(strw)
                    if self.con.getTyp()=="php":
                        write = fileC.PHP_WRITE.replace('#1',flag[1],1)
                        write = write.replace("#2",strw,1)
                        write = write.replace('@@',self.changePath(),1)
                        date = { self.key : write }
                    if self.con.getTyp()=="jsp":
                        write = fileC.JSP_WRITE
                        date = { self.key : "file",'cpath':self.changePath(),'ds':write,'c1':flag[1],'c2':strw }
                    if self.con.getTyp()=="asp":
                       pass
                    
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'writeto':
                if self.check(flag)>2:
                    num = len(flag)
                    str1 = flag[2]
                    n = 3
                    while  n != num:
                        str1 = str1 + ' ' + flag[n]
                        n = n + 1
                    print(str1)
                    if self.con.getTyp()=="php":
                        writeto = fileC.PHP_WRITETO.replace('#1',flag[1],1)
                        writeto = writeto.replace("#2",str1)
                        writeto = writeto.replace('@@',self.changePath(),1)
                        date = { self.key : writeto }
                    if self.con.getTyp()=="jsp":
                        writeto = fileC.JSP_WRITETO
                        date = { self.key : "file",'cpath':self.changePath(),'ds':writeto,'c1':flag[1],'c2':flag[2] }
                    if self.con.getTyp()=="asp":
                        pass
                    
                    commit = re.post(self.connect,date)
                    print(commit.text,"\n")
                    continue
                else:
                    continue

            if flag[0] == 'upload':
                if self.check(flag)>1:
                    print(flag[1])
                    file1 = open(flag[1],'rb')
                    strofupdate = file1.read()
                    print("upload....")
                    if self.con.getTyp()=="php":
                        update = fileC.PHP_UPLOAD.replace('#1',flag[1],1)
                        update = update.replace('#2',strofupdate,1)
                        update = update.replace('@@',self.changePath(),1)
                        date = { self.key : update }
                    if self.con.getTyp()=="jsp":
                        update = fileC.JSP_UPLOAD
                        date = { self.key : "file",'cpath':self.changePath(),'ds':update,'c1':flag[1],'c2':strofupdate }
                    if self.con.getTyp()=="asp":
                        pass
                    #将本地路径所指文件读出到strofupdate
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
                        download = download.replace('##',flag[1],1)
                        date = { self.key : download }
                    if self.con.getTyp()=="jsp":
                        download = fileC.JSP_READ
                        date = { self.key : "file",'cpath':self.changePath(),'ds':download,'c1':flag[1]}
                    if self.con.getTyp()=="asp":
                        pass
                   
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

            print('指令错误 !')
