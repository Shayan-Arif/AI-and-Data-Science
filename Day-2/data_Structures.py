
# List
# List is a collection which is ordered and changeable. Allows duplicate members.

my_list = [1,20.5,"Shayan", False, 1]
print(my_list)
print(my_list[2])
my_list[2] = 111.66665
print(my_list)

# Tuple
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

my_tuple = ("x","y")
print(my_tuple)
print(my_tuple[1])
#my_tuple[1] = "z"

#dictionary
#Dictionaries are unordered collections of key-value pairs.

my_dict = {"name":"Shayan", "age": 20, "city":"Jamshoro"}
print(my_dict)
print(my_dict["name"])
my_dict["name"] = "Shayan Ali"
print(my_dict)


# Set
# Sets are unordered collections of unique elements.    
my_set = {1,2,3,4,5,6,7,8,9,10}
print(my_set)
my_set.add(11)
print(my_set)

