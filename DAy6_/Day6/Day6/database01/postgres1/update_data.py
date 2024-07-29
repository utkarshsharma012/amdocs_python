from db_connect import *
import time
conn,cur=connect()
if conn !=None:
    try:
        sql="select * from amd01"
        cur.execute(sql)
        print("====Rows Before Update==================")
        for row in enumerate(cur):
            print(f"{row[0]+1}. ",row[1])
        print("========rows updating================")
#         sql="update amd01 set name=%s where name=%s"
#         data=('Nishant',"Manish")
        sql="update amd01 set name=%s,age=%s where name=%s or age=%s"
        data=('Nishant',45,"Manisha",67)
        cur.execute(sql,data)



        conn.commit()
        time.sleep(4)
        print("========rows updated==================")

        time.sleep(1)
        sql="select * from amd01"
        cur.execute(sql)
        print("====Rows After Update==================")
        for row in enumerate(cur):
            print(f"{row[0]+1}. ",row[1])
            
        conn.close()    
    except Exception as e:
        print(e.__class__.__name__,"Error Solved!",e)