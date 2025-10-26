import sqlite3

def get_data():
    try:
        db=sqlite3.connect("app.db")
        print("connected to database")
        cr=db.cursor()
        cr.execute("CREATE TABLE if not exists users(name text, salary integer, title text)")
        cr.execute("INSERT INTO users(name,salary,title) values ('hassan',5000,'enginner')")
        cr.execute("INSERT INTO users(name,salary,title) values ('hassan',5000,'enginner')")
        db.commit()
    except sqlite3.DatabaseError as err:
        print(f" data error {err}")
    finally:
        print("database closed")
        db.close()






get_data()