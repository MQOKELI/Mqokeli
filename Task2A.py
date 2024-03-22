##Normal VS Comprehension List Bullet Number 3

#Normal List

List=[14,15,16,17,18,19,20]

for n in List:
    if n%2!=0:
      print(n)


#Comprehension List
List=[14,15,16,17,18,19,20]

odds=[n for n in List if n%2!=0]
print(odds)