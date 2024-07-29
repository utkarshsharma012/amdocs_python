from db_connect import connect 
conn,cur=connect()
if conn!=None:
    #Sql_Inj
#     sql="select * from amd01 where id=%s"
#     row=(111,)
#     sql="select * from amd01 where name=%s"
#     row=("Manisha",)
    sql="select * from amd01 where name=%s and age=%s"
    row=("Manisha",23)
#     sql="select name,salary,age from amd01 order by id"
    cur.execute(sql,row)
#     for i in enumerate(cur): # [(0,row1),(1,row2),...]
#         print(f"{i[0]+1}.",i[1])
    f=cur.fetchall() #List of all the rows
    print(f)
   
    conn.close()
else:
    print("Conn. Failed")