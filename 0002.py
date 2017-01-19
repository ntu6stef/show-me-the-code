#the idea: use random to judge use which kind random. Just two loops
import random
#import the mysql connect API
import mysql.connector

#connect the mysql server
conn = mysql.connector.connect(user = 'root',password = '',database = 'test')
cursor = conn.cursor()
#create the code table
cursor.execute('create table Cod (id varchar(20) primary key, name varchar(20))')
i = 1
s = set([])
while i<=200 :		#in case of repeat
	string = ""	
	for j in range(10):
		rand = random.randint(1,3)
		if rand ==1:
			x = str(random.randint(0,9))
			string = string + x
		if rand==2:
			y = chr(random.randint(65,90))
			string =string +y
		if rand==3:
			z = chr(random.randint(97,122))
			string =string + z
	s.add(string)
	if len(s) > i:
		cursor.execute('insert into Cod (id, name) values (%s, %s)', [str(i), string])
		conn.commit()
		print(i)
		i = i + 1
print(cursor.rowcount)
cursor.close()
conn.close()