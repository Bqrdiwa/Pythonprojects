import mysql.connector



conector = mysql.connector.connect(host='136.243.153.26' , username='stikiir_Bardia', password='4nJ2ZuXbJjS0',
                                       database='stikiir_Paradox')
user = conector.cursor()
commend = "insert into * from Users where username = %s"