from db_connect import connect 
conn,cur=connect()
if conn!=None:
    #Sql_Inj
    #python Data Type List of Tuples
    rows=[(1891,'Manisha',14,None,None),(111,'Dongli',54,"florida us",34556.799),
             (121,'Mr.Wu',38,"near lake,Boston",34.908),(131,'Manisha',14,None,None),
             (141,'Rajesh',98,None,45.798),(151,'Jhon',94,None,None)]
    
    sql="insert into amd01 (id,name,age,address,salary) values (%s,%s,%s,%s,%s)"
    cur.executemany(sql,rows)
    conn.commit()
    conn.close()
else:
    print("Conn. Failed")