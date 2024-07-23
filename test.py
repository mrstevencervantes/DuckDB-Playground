import duckdb

conn = duckdb.connect()

try:
    conn.execute("CREATE TABLE test (a INTEGER, b VARCHAR);")
    conn.execute("INSERT INTO test VALUES (1, 'one'), (2, 'two'), (3, 'three');")
    result = conn.execute("SELECT * FROM test;").fetchall()
    print(result)
except Exception as e:
    print(e)
finally:
    conn.close()