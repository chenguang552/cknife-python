PHP_Mysql_BaseCode='''echo php_uname('s');'''
#Mysql_Connect='''$sql=mysqli_connect("#1","#2","#3","information_schema");
#                 $result = mysqli_query($sql,"SELECT a,b FROM a");
#                 while($row = mysqli_fetch_assoc($result)){
#                       echo $row["a"] . " " . $row["b"];
#                    }
#                 mysqli_close($sql);'''
PHP_Mysql_Connect='''$sql=mysqli_connect("#1","#2","#3","#4");'''
# Mysql_ShowDBs='''@@$result = mysqli_query($sql,"show databases");\
#     while($row = mysqli_fetch_assoc($result)){echo $row["Database"].'\n';}mysqli_close($sql);'''
PHP_Mysql_ShowDBs='''@@$searchcode="##";\
    $result=mysqli_query($sql,$searchcode);\
    $result2=mysqli_query($sql,$searchcode);\
    $row_1 = mysqli_fetch_assoc($result2);\
    $id_1=array_keys($row_1);\
    foreach($id_1 as $j=>$key){\
            echo "\t|\t";\
            print($key);\
            echo " \t|\t";\
            }\
    echo "\n";\
    while($row = mysqli_fetch_assoc($result)){\
        $id=array_keys($row);\
        foreach($id as $i=>$k){\
            echo "\t|\t";\
            print($row[$k]);\
            echo "\t|\t";\
            }\
        echo "\n";\
    }\
    mysqli_close($sql);'''

JSP_Mysql_BaseCode='''uname'''
JSP_Mysql_Connect='''databaseconnect'''

ASP_Mysql_BaseCode=''''''
ASP_Mysql_Connect=''''''
ASP_Mysql_ShowDBs=''''''

