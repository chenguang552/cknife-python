Mysql_BaseCode='''echo php_uname('s');'''
#Mysql_Connect='''$sql=mysqli_connect("#1","#2","#3","information_schema");
#                 $result = mysqli_query($sql,"SELECT a,b FROM a");
#                 while($row = mysqli_fetch_assoc($result)){
#                       echo $row["a"] . " " . $row["b"];
#                    }
#                 mysqli_close($sql);'''
Mysql_Connect='''$sql=mysqli_connect("#1","#2","#3","#4");'''
# Mysql_ShowDBs='''@@$result = mysqli_query($sql,"show databases");\
#     while($row = mysqli_fetch_assoc($result)){echo $row["Database"].'\n';}mysqli_close($sql);'''
Mysql_ShowDBs='''@@$searchcode="##";\
    $result=mysqli_query($sql,$searchcode);\
    $result2=mysqli_query($sql,$searchcode);\
    $row_1 = mysqli_fetch_assoc($result2);\
    $id_1=array_keys($row_1);\
    foreach($id_1 as $j=>$key){\
            print($key);\
            echo "\t";\
            }\
    echo "\n";\
    echo "--------\t-------\t---------\t-------->>>\n";\
    while($row = mysqli_fetch_assoc($result)){\
        $id=array_keys($row);\
        foreach($id as $i=>$k){\
            print($row[$k]);\
                echo "\t";\
            }\
        echo "\n";\
    }\
    mysqli_close($sql);'''
