from db_connect import *
import time
conn,cur=connect()
if conn !=None:
    try:
        sql="select * from amd01"
        cur.execute(sql)
        print("====Rows Before delete==================")
        for row in enumerate(cur):
            print(f"{row[0]+1}. ",row[1])
        print("========rows deleting================")
#         sql="delete from amd01 where id=%s"
#         data=(111,)
        sql="delete from amd01 where name=%s or age=%s"
        data=("Manisha",23)
        cur.execute(sql,data)



        conn.commit()
        time.sleep(4)
        print("========rows deleted==================")

        time.sleep(1)
        sql="select * from amd01"
        cur.execute(sql)
        print("====Rows After delete==================")
        for row in enumerate(cur):
            print(f"{row[0]+1}. ",row[1])
            
        conn.close()    
    except Exception as e:
        print(e.__class__.__name__,"Error Solved!",e)