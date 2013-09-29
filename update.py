"""
	Python CGI script
"""
import sqlite3

error = "<center><h1>We couldn't get your info into database, Sorry!</h1></center>"

form = cgi.FieldStorage()

if "email" not in form or "keyword" not in form:
    print "Please fill in the email and keyword fields."
    return

email = form["email"]
keywords = form.getlist("keyword")

try:
    conn = sqlite3.connect('miuDB.db')
    c = conn.cursor()
except Error:
    print(error)
    return

'''
put email + keywords into database
'''

for k in keywords:
    try:
        c.execute("INSERT INTO Users VALUES ( ? , ?)", (email, k))
    except Error:
        print(error)
        return

Status: 303
See
other
Location: #must be mainpage@localhost (bootstrap)
