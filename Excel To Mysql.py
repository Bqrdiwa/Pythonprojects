import mysql.connector
import xlrd
excel_reader = xlrd.open_workbook(r'C:\Users\BrGaMeRxD\PycharmProjects\pythonProject\texts\excel.xls')
sheet = excel_reader.sheet_by_index(0)
row = 1
list = []
cnx = mysql.connector.connect(user='root', password='3243173337', host='localhost')
cursor = cnx.cursor()
cursor.execute('show databases')
x=cursor.fetchall()
len1 = len(x)
for i in range(len1):
    print(str(x[i]).replace(',','').replace(')','').replace('(','|-').replace("'",''))
cnx.close()
q10 = input('Select your database: ')
cnx = mysql.connector.connect(user='root', password='3243173337', host='localhost', database=q10)
cursor = cnx.cursor()
q1 = input('You want me to create a table for you or not? ')
if q1 != 'yes':
    q1 = input('Enter your table name: ')
def writer(list,row,q1):
    for i in range(sheet.ncols):
        if sheet.cell_type(row,i) == 3:
            date=xlrd.xldate_as_datetime(sheet.cell_value(row,i),excel_reader.datemode)
            date = str(date)
            date = date.replace('00:00:00','')
            date = date.strip()
            list.append(date)
        else:
            list.append(sheet.cell_value(row, i))
        if len(list) == sheet.ncols:
            if q1 == 'yes':
                u = []
                h=('(')
                q2= input('what should i name the table? ')
                print('Creating...')
                for i in range(0,sheet.ncols-1):
                    u.append(str((sheet.cell_value(0,i))+' VARCHAR(245),'))
                    print('Col %i/%i'%(i,sheet.ncols))
                u.append(str(sheet.cell_value(0,sheet.ncols-1)+' VARCHAR(245)'))
                print('Col %i/%i'%(sheet.ncols,sheet.ncols))
                for i in range(len(u)):
                    h = h+ str(u[i])
                cursor.execute('CREATE TABLE '+q2+h+')')
                q1 = q2

            print('We are sending the information to the database----We are at-->'+str(row)+'/'+str(sheet.nrows-1))
            cursor.execute('INSERT INTO '+q1+' VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' %(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7]))
            cnx.commit()
            if row+1 == sheet.nrows:
                break
            list= []
            row = row +1
            writer(list,row,q1)
writer(list,row,q1)
print('We have send %s culomn and %s row to the database!'%(sheet.ncols,sheet.nrows-1))
print('We have done the transmission successfully!')
cnx.close()