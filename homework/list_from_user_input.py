num_names = int(input("How many names do you want to enter? "))

names = []

for i in range(num_names):
        name = input("Enter a name, please: ")
        names.append(name)
        i+=1

for name in names:
    print(name)


