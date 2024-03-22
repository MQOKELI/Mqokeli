## Normal VS Comprehension List bullet number 1

##This is a normal list
List=[14,15,16,17,18,19,20]

my_list=[]

for n in List:
    my_list.append(n)
    print(n)


    ##Comprehension List

List=[14,15,16,17,18,19,20]

my_list=[n for n in List]
print(my_list)