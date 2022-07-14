import ibm_db
conn_str = 'database=bludb;hostname=HOST;port=PORT;protocol=tcpip;uid=UID;pwd=PASSWORD;SECURITY=SSL;'
print("=> Creating the connection")
try:
    connection = ibm_db.connect(conn_str, "", "")
    print("=> Connected to Server ... SUCCESSFULL")
except:
    print("=> Connection to server .... FAILED")
    print("Error Description = " + ibm_db.conn_errormsg())
    print("SQLSTATE = " + ibm_db.conn_error())
    exit(0)
