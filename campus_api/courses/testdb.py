
import psycopg
from psycopg.rows import dict_row
 
URL = "postgresql://postgres:postgres@localhost/testdb1"
 
def get_conn():
    return psycopg.connect(URL, row_factory=dict_row)
 
 
with get_conn() as conn:
    conn.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL UNIQUE,
        done BOOLEAN NOT NULL DEFAULT FALSE)""")
print("table ready")
