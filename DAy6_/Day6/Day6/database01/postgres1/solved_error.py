from db_connect import connect
import psycopg2 as pg
conn,cur=connect()
if conn!=None:
    #Sql_Inj
    #python Data Type List of Tuples
    
    try:
        rows=[(18911,None,14,None,'Manisha'),(1111,34556.799,54,"florida us",'Dongli'),
             (1211,34.908,38,"near lake,Boston",'Mr.Wu'),(1311,None,14,None,'Manisha'),
             (1411,45.798,98,None,'Rajesh'),(901,None,94,None,'Jhon')]
    
        sql="insert into amd01 (id,salary,age,address,name) values (%s,%s,%s,%s,%s) on conflict do nothing"
        cur.executemany(sql,rows)
    except pg.IntegrityError as e:
        conn.rollback()
        print(e)
    else:
        conn.commit()
    conn.close()
    
else:
    print("Conn. Failed")
