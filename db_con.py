#Needed for postgres
#import psycopg2 

#Use sqllite
import sqlite3


def get_db():
    #Postgres
    #return psycopg2.connect(host="localhost", dbname="authme" , user="loki", password="4prez")
    return sqlite3.connect("database.db")

def create_db_table():
    try:
        conn = get_db()
        conn.execute('''
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                phone TEXT NOT NULL,
                gender TEXT NOT NULL,
                birth DATA NOT NULL, 
                introduce TEXT NOT NULL 
            );
        ''')
        conn.commit()
        print("User table is created successfully!")
    except:
        print("Failed to create table")
    finally:
        conn.close()


def get_db_instance():  
    db  = get_db()
    cur  = db.cursor( )

    return db, cur 



if __name__ == "__main__":
    db, cur = get_db_instance()

    cur.execute("select * from users")
    for r in cur.fetchall():
        print(r)

    cur.execute("create table music ( song_name varchar(255), rating int);")
    db.commit()




