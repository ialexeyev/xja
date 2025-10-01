import sqlite3

conn = sqlite3.connect('instance/prismdb.db')
prism_cursor = conn.cursor()

#conn = sqlite3.connect('instance/users.db')
#prism_cursor = conn.cursor()

#prism_cursor.execute("SELECT * FROM user;")

#prism_cursor.execute("DROP TABLE user;")

prism_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

#prism_cursor.execute("DELETE FROM user WHERE id = 1;")
#prism_cursor.execute("INSERT INTO services (spagename, sname, sdata) VALUES (?, ?, ?)", ('mainpage', 'pageTitle', 'SKILL UP: Home page'))
#prism_cursor.execute("DROP TABLE dyn_attendance;")
#prism_cursor.execute("DELETE FROM dyn_attendance;")
#prism_cursor.execute("ALTER TABLE dyn_attendance ADD COLUMN ahostname TEXT;")
#prism_cursor.execute("DELETE FROM dyn_attendance WHERE id = 2;")
#prism_cursor.execute("PRAGMA table_info('user');")
#prism_cursor.execute("SELECT * FROM dyn_attendance")
prism_cursor.execute('SELECT * FROM services')
#prism_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#prism_cursor.execute("""CREATE TABLE dyn_attendance (
#   id INTEGER PRIMARY KEY,
#   aid TEXT,
#   afname TEXT,
#   alname TEXT,
#   aip TEXT,
#   acurrentpage TEXT,
#   ahostdata TEXT
#)""")
#prism_cursor.execute("INSERT INTO services (spagename, sname, sdata) VALUES (?, ?, ?)", ('home', 'positionFieldPlaceholder', 'Position'))
#prism_cursor.execute("INSERT INTO users (uid, ufname, ulname, umail, udepartment, usupervisor,  uposition, uaccess, upassword) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", ('a.saudabayev', 'Azamat', 'Saudabayev', 'a.saudabayev@hyundai.kz', 'Manufacturing development department', 'Igor Alexeyev', 'Setup technician', 'user', 'azamatst30'))

#conn.commit()

data = prism_cursor.fetchall()

#prism_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#data = prism_cursor.fetchall()
conn.close()

print(data)
