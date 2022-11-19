from flask import Flask, render_template, request, redirect, url_for, session import ibm_db
import re
app = Flask( name ) app.secret_key = 'a'
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32- 21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY
=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=tbl66129;PWD=LPzyHjRGcm XprQoN",'','')
@app.route('/', methods =['GET', 'POST']) def register():
	msg = ''
	if request.method == 'POST' :
		username = request.form['username'] 
		email = request.form['email']
		password = request.form['password']
		sql = "SELECT * FROM users WHERE username =?"
		stmt = ibm_db.prepare(conn, sql) 
		ibm_db.bind_param(stmt,1,username) 
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'name must contain only characters and numbers !'
		else:
			insert_sql = "INSERT INTO users VALUES (?, ?, ?)" 
			prep_stmt = ibm_db.prepare(conn, insert_sql) 
			ibm_db.bind_param(prep_stmt, 1, username)
			ibm_db.bind_param(prep_stmt, 2, email)
			ibm_db.bind_param(prep_stmt, 3, password) 
			ibm_db.execute(prep_stmt)
			msg = 'You have successfully registered !' 
		elif request.method == 'POST':
			msg = 'Please fill out the form !'
		return render_template('register.html', msg = msg) 
	if__name__== '_ main_':
		app.run(debug = True)
