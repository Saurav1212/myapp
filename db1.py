import mysql.connector as mq
mycon=mq.connect(host='localhost',user="root",password="",database="hotel")
if mycon.is_connected():
    print("connected")
c1=mycon.cursor()
sql_1="select * from boarding"
c1.execute(sql_1)

data=c1.fetchall()

for x in data:
    for i in x:
        print(i,"\t",sep=" ",end=" ")
    print()
m=input()


