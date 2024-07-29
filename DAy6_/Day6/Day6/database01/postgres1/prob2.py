from db_connect import connect 
conn,cur=connect()
if conn!=None:
    #Sql_Inj
    #python Data Type List of Tuples
    rows=[(None,14,None,'Manisha'),(34556.799,54,"florida us",'Dongli'),
             (34.908,38,"near lake,Boston",'Mr.Wu'),(None,14,None,'Manisha'),
             (45.798,98,None,'Rajesh'),(None,94,None,'Jhon')]
    
    sql="insert into amd02 (salary,age,address,name) values (%s,%s,%s,%s)"
    cur.executemany(sql,rows)
    conn.commit()
    conn.close()
else:
    print("Conn. Failed")