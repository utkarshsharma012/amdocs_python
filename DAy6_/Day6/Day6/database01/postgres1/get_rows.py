from db_connect import connect 
conn,cur=connect()
if conn!=None:
    #Sql_Inj
    sql="select * from amd01 order by id"
#     sql="select name,salary,age from amd01 order by id"
    cur.execute(sql)
#     for i in enumerate(cur): # [(0,row1),(1,row2),...]
#         print(f"{i[0]+1}.",i[1])
#     f=cur.fetchone() #one row
#     f=cur.fetchmany() #List of one row
#     f=cur.fetchmany(3) #List of 3 rows
#     f=cur.fetchmany(-1) #List of all the rows
    f=cur.fetchall() #List of all the rows
    print(f)
   
    conn.close()
else:
    print("Conn. Failed")