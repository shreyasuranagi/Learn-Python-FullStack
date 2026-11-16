import csv
'''
f=open('exam.csv','w',newline='')

ob=csv.writer(f)
ob.writerow(['name','class','marks'])
ob.writerows([['anya',10,100],['tanya',9,90],['sanya',8,89]])

f.close()
'''


'''

f=open('exam.csv','r')
obj=csv.reader(f)

#print(list(obj)) - ?? ehy
 
print(obj)

for l in (obj):
    print(l)
    
'''


#context manager
with open('exam.csv','a') as f:
    ob=csv.writer(f)
    ob.writerow(['panya',10,98])
    
