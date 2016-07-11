import MySQLdb

def connection():
	conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=9000, db='FlaskApp', unix_socket='/opt/lampp/var/mysql/mysql.sock')
	curs = conn.cursor()
	return conn, cur