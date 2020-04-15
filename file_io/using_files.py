my_file = open("grocery_list.txt","w+")
my_file.write("veggies\n")
my_file.write("fruits \n")
my_file.writelines([
    "oil\n",
    "wine\n",
    "cheese\n",
    "milk\n",
    "snacks\n",
])

my_file.seek(0)
my_file.write("egg")
my_file.seek(0)
print(my_file.read())

my_file.close()

# my_file = open("grocery_list.txt","r")
# print(my_file.read())

#as bytes
with open("grocery_list.txt","rb") as file:
   print(file.read) # return byte object

