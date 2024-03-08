import oracledb

un = 'system'
cs = 'localhost/free'
pw = 'Ora1234'

connection = oracledb.connect(user=un, password=pw, dsn=cs)
print("Successfully connected to Oracle Database")
