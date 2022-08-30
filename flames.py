list1 = (input("Enter 1st name: ").lower())
list2 = input("Enter 2nd name: ").lower()

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            c = list1[i]

            print(c)
