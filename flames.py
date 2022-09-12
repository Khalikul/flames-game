name1 = input("Enter 1st name: ").lower()
name2 = input("Enter 2nd name: ").lower()

list1=list(name1)
list2=list(name2)

for i in list1[:]:
    if i in list2:
        list1.remove(i)
        list2.remove(i)

count=len(list1)+len(list2)

num=count%6
if num==1:
    print("Friends")
elif num==2:
    print("love")
elif num==3:
    print("Affection")
elif num==4:
    print("Marriage")
elif num==5:
    print("Enemy")
elif num==0:
    print("Siblings")

print(count,num)
