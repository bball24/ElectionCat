import psycopg2 as pg2
conn = pg2.connect(database = 'ID', user = 'postgres', password = 'slasher56')
cur = conn.cursor();

query1 = 'SELECT * from listofIDS'
cur.execute(query1);
data = cur.fetchall();
print(data);


conn2 = pg2.connect(database = 'Candidates', user = 'postgres', password = 'slasher56')
cur2 = conn2.cursor();

query2 = 'SELECT * from Candidates'
cur2.execute(query2);
data2 = cur2.fetchall();
print(data2);



#def returnDictionaries():
 #   return

#def checkID():
 #   return

#def addVotes();
#	return

#def returnTotal();
	#return