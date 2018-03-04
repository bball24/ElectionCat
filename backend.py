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

conn3 = pg2.connect(database = 'Votes', user = 'postgres', password = 'slasher56')
cur3 = conn3.cursor();

query3 = 'SELECT * from votes'
cur3.execute(query3);
data3 = cur3.fetchall();
print(data3);


#def returnDictionaries():
 #   return

def checkID():
 list = []; # need to obtain list of all voter ids
 for i in list
	if len(list[i]) < 9 and list[0:3] != "861"
 		return false;

 return true;

#def addVotes();

#def returnTotal();
	#return