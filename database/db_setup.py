import sqlite3
# sqlite3 is case sensitive
#conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('data.db')

# create a database table
# step1 : create a cursor
cr = conn.cursor()

# step2 : create a table

many_data = [('wes', 'Brown', "wesBrown.com"),
             ('steph', 'kuema', 'steph.com'),
             ('Don', 'Bravo', "don.com")]

#cr.executemany("INSERT INTO project VALUES (?,?,?)", many_data)
print("command executed succesfully !")

# update records
#cr.execute("""UPDATE project SET first_name = 'fool'
#           WHERE last_name LIKE 'Br%'""")

# delete the records
#cr.execute("DELETE from project WHERE rowid = 3")

# ordering the results - query the database
#cr.execute("SELECT rowid,* FROM project ORDER BY last_name DESC")


# query the database
#cr.execute("SELECT * FROM project")
#cr.fetchone()
#cr.fetchmany()
#cr.fetchall()

# And/Or
#cr.execute("SELECT rowid, * FROM project WHERE last_name LIKE 'Br%' OR rowid = 1")

# limiting results
#cr.execute("SELECT rowid, * FROM project ORDER BY rowid DESC LIMIT 3")

# delete the entire table (drop table)
cr.execute("DROP TABLE project")

cr.execute("SELECT rowid, * FROM project")
items = cr.fetchall()
 
for item in items: 
    print(item)

# Datatypes : NULL,INTEGER,REAL,TEXT,BLOB



# step3 : commit our command
conn.commit()

# step4 : close our connection
conn.close()






