import psycopg
from psycopg.rows import dict_row
 
URL = "postgresql://postgres:postgres1@localhost/taskdb"
 
def get_conn():
    return psycopg.connect(URL, row_factory=dict_row)
 
# create table 
with get_conn() as conn:
    conn.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL UNIQUE,
        done BOOLEAN NOT NULL DEFAULT FALSE)""")
print("table ready")

'''
# insert rows
sql = "INSERT INTO tasks (title, done) VALUES (%s, %s)"
with get_conn() as conn:
    conn.execute(sql, ("Bwuy milk1000", False))
    conn.execute(sql, ("Stwudy SQL1000", True))
print("saved")



# select * 
with get_conn() as conn:
    cur = conn.execute("SELECT * FROM tasks ORDER BY id")
    rows = cur.fetchall()
    print(rows)

# select * with where
with get_conn() as conn:
    sql = "SELECT * FROM tasks WHERE id = %s"
    one = conn.execute(sql, (2,)).fetchone()
    nobody = conn.execute(sql, (99,)).fetchone()
 
print(one)
print(nobody)


'''