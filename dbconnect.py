import MySQLdb

def getDBinfo():
	fileName = "/Users/Ns/Documents/mysqldb.txt"
	dbFile = open(fileName, 'r')
	dbInfo = dbFile.readlines()

	for i in xrange(len(dbInfo)):
		dbInfo[i] = dbInfo[i].strip('\n')
		if (i == 2):
			print(dbInfo[i])

	return dbInfo



def connection():
		
	dbInfo = getDBinfo()
	conn = MySQLdb.connect(db=dbInfo[0], 
		user=dbInfo[1], 
		passwd=dbInfo[3], 
		host=dbInfo[2])

	c = conn.cursor()

	return c, conn