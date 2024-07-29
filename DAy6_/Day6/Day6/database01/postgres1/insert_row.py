from db_connect import connect 
conn,cur=connect()
if conn!=None:
    #Sql_Inj
    row=(6,'Raj',45,None,None)#python Data Type
    sql="insert into amd01 (id,name,age,address,salary) values (%s,%s,%s,%s,%s)"
    cur.execute(sql,row)
    conn.commit()
    conn.close()
else:
    print("Conn. Failed")