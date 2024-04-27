size = int(input("Enter the size of the list: "))
my_list = []
for i in range(size):
    element = int(input("Enter element " + str(i+1) + ": "))
    my_list.append(element)

print("List before sorting:", my_list)
my_list.sort()
print("List after sorting:", my_list)
