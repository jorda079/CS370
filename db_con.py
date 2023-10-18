#Needed for postgres
#import psycopg2
# Description

#Use sqllite
import sqlite3


def get_db():
    #Postgres
    #return psycopg2.connect(host="localhost", dbname="authme" , user="loki", password="4prez")
    return sqlite3.connect("database.db")

def create_user_table():
    query = """
            CREATE TABLE IF NOT EXISTS "users" (
            id INTEGER PRIMARY KEY,
            name TEXT,
            password TEXT,
            email TEXT,
            address TEXT,
            phone TEXT,
            gender TEXT,
            birth DATE, 
            introduce TEXT
        );
        """
    return query


def create_questionnaire_table():
    query = """
            CREATE TABLE IF NOT EXISTS "questionnaire" (
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            answer_1 boolean DEFAULT 0,
            answer_2 boolean DEFAULT 0,
            answer_3 boolean DEFAULT 0,
            answer_4 boolean DEFAULT 0,
            answer_5 boolean DEFAULT 0
            )
    """
    return query


def get_db_instance():  
    db  = get_db()
    cur  = db.cursor( )

    return db, cur

"git"
if __name__ == "__main__":
    db, cur = get_db_instance()

    cur.execute("select * from users")
    for r in cur.fetchall():
        print(r)
    cur.execute(create_user_table())
    cur.execute(create_questionnaire_table())
    cur.execute("create table music ( song_name varchar(255), rating int);")
    db.commit()




