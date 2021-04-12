import mysql.connector as mq
mycon=mq.connect(host='localhost',user="root",password="",database="hotel")
if mycon.is_connected():
    print("connected")
c1=mycon.cursor()
c1.execute("select * from boarding")
data=c1.fetchall()
print(data)
for x in data:
    print(x)

for i in data:
    for j in i:
        print(j,end=" ")
    print()

