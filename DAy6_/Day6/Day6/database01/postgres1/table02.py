from db_connect import connect 
conn,cur=connect()
if conn!=None:
    sql="""create table if not exists AMD02(
    id serial primary key not null,
    name text not null,
    age int not null ,
    address varchar(20),
    salary real  )
    """
    cur.execute(sql)
    conn.commit()
    conn.close()
else:
    print("Conn. Failed")