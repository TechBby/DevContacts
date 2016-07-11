#import flask
from flask import Flask,session
#import render_template so we can now start rendering templates
from flask import render_template, redirect, url_for
#import request from flask to read posted values
from flask import request
#import json so that we can use it to return data to the ui
from flask import jsonify, json
#import abort to call for display of 404
from flask import abort
#import make_response to handle error 404
from flask import make_response
# import session to track user session via cookies
from flask import session
#import for fetching time
import time
#import mysqldb
import MySQLdb
# garbage collection, collect any garbage from uncleared cache
import gc
# necessary to abstract the interaction with database
from dbconnect import connection
#import for debugging pursposes
import pprint
#better import necessary for password hashing
from passlib.hash import sha256_crypt
#create app using flask
app = Flask(__name__)

#definition of basic route and corresponding request handler
@app.route("/")
def main():
	return render_template('index.html')
#definition of show all students link
@app.route("/showAll/")
def showAll():
	try:
		conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=9000, db='FlaskApp', unix_socket='/opt/lampp/var/mysql/mysql.sock')
		cur = conn.cursor()
		cur.execute('select * from Developers')
		data = cur.fetchall()
		rows = len(data)
		return render_template('show_all.html', data=data, rows=rows)
	except Exception, e:
		return (str(e))

@app.route("/showAddNew/")
def showAddNew():
	try:
		return render_template('new.html')
	except Exception, e:
		raise (str(e))

#definition of add new students link
@app.route('/new', methods=['GET', 'POST'])
def new():
	try:
		_devName = request.args.get('name')
		_devMatricule = request.args.get('matricule')
		_devTechnology = request.args.get('technology')
		if _devName and _devMatricule and _devTechnology:
			# The logged in user has provided information for developer
			conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=9000, db='FlaskApp', unix_socket='/opt/lampp/var/mysql/mysql.sock')
			cur = conn.cursor()
			#use the provided information to fill up developer table, 2nd id corresponds to logged in user, the one that modifies developer
			cur.execute('insert into Developers values (%s, %s, %s, %s, %s)', (0, 0,_devName, _devMatricule, _devTechnology))
			pprint.pprint('I can still fill you')
			conn.commit()
			conn.close()
			cur.close()
			gc.collect()	
			# redirect to showall page with all available users in the table
			return jsonify(result=200)
		else:
			# logged In user has not provided enough information about developer
			pprint.pprint('All fields are required')
			return jsonify(result='I am staying on the same page')
	except Exception, e:
		return (str(e))

#definition orf showsign route and correspond	ing request 
@app.route("/showSignUp/")
def showSignUp():
	try:
		return render_template('signup.html')
	except Exception, e:
		return (str(e))
	
#handle post signup data using flask
@app.route("/signUp", methods=["GET","POST"])
def signUp():
	try:
		_name = request.args.get('inputName')

		_email = request.args.get('inputEmail')

		_password = sha256_crypt.encrypt(request.args.get('inputPassword')) 
		if _name and _email and _password:
			conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=9000, db='FlaskApp', unix_socket='/opt/lampp/var/mysql/mysql.sock')
			cur = conn.cursor()
			# pprint.pprint('connection testing cursor assignment passed')
			rslt = cur.execute('select * from Users where email = (%s) or username = (%s)', (_email,_name))
			if int(rslt) > 0:
				 return jsonify(result='That user email or username is already taken please choose another combination of username and email')
			else:
				cur.execute('insert into Users values (%s, %s, %s, %s, %s)', (0, _name, _email, _password,0))
				conn.commit()
				conn.close()
				cur.close()
				gc.collect()
				# session not working
				# session['logged_in'] = True
				# session['username'] = _name
				# pprint.pprint('now i am about to return some stuff in json format to you')
				return jsonify(result=200)
   		else:
			return jsonify(result='Please fill in all required fields')
	except Exception, e:
		return (str(e))
@app.route("/_logIn", methods=["GET","POST"])
def login():
	try:
		_name = request.args.get('inputName')
		_password = request.args.get('inputPassword')
		if _name and _password:
			#check for the presence of a user in the database
			conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=9000, db='FlaskApp', unix_socket='/opt/lampp/var/mysql/mysql.sock')
			cur = conn.cursor()
			rslt1 = cur.execute('select * from Users where username = (%s) or email = (%s)', (_name, _name))
			if int(rslt1) > 0:
				#it is a valid user name
				pprint.pprint('user name is valid')
				pswd = cur.fetchone()[3]
				# check for validity of password
				if sha256_crypt.verify(_password, pswd):
					pprint.pprint('passwords match')
					# session['logged_In'] = True
					pprint.pprint('Session now working')
					# session['username'] = cur.fetchone()[2]

				#if found redirect to the all users page
					return jsonify(result=200)
				else:
					return jsonify(result='Password Not Correct')
			else:
				# user name not valid
				return jsonify(result="No such user")
		else:
			return jsonify(result="Username or password not Filled")
	except Exception, e:
		return (str(e))
@app.route("/showLogin")
def showLogin():
	try:
		return render_template('login.html')
	except Exception, e:
		return (str(e))
#check if executed file is the main program and run the app
if __name__ == '__main__':
	app.run(debug=True)