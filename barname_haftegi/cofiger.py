import mysql.connector


conector = mysql.connector.connect(host = '136.243.153.26', username = 'stikiir_Bardia',password ='4nJ2ZuXbJjS0',database ='stikiir_BData')
mcurs = conector.cursor()
x = 'insert into users(username,password,id) values (%s,%s,%s);'%('bardia','3243173337','0000')
x.s
print('insert into users(username,password,id) values (%s,%s,%s);'%('bardia','3243173337','0000'))
mcurs.execute('insert into users(username,password,id) values (\'%s\',\'%s\',\'%s\');'%('bardia','3243173337','0000'))
conector.commit()
for i in mcurs:
    print(type(i))
