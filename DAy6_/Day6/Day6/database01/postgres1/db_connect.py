def connect():
    try:
        import psycopg2 as pg 
        conn=pg.connect(user="nishant",password='1234',port='5432',
                        database="learning",host='127.0.0.1')
        cur=conn.cursor()
        return conn,cur 
    except Exception as e:
        print('Error :-',e.__class__.__name__)
        print("Msg:-",e)
        conn=None
        cur=None
        return conn,cur
    
if __name__=="__main__":
    conn,cur=connect()
    if conn != None:
        conn.close()