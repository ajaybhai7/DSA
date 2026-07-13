marks = {
    "rohan" : 24,
    "Vijay" : 76,
    "Ajay"  : 87 
}

print(marks.items())
'''
This Function prints all items in the marks dictonary
in the form of tuples that output is 
output: dict_items([('rohan', 24), ('Vijay', 76), ('Ajay', 87)])
'''
print(marks.keys())
'''
This function prints all keys means the left side items in 
the dictonary which we have in the dict
output: dict_keys(['rohan', 'Vijay', 'Ajay'])
'''
print(marks.values())
'''
This function prints all values in the the marks dictonary
that is written in right side in the dict
output: dict_values([24, 76, 87])
'''

marks.update({"Ajay": 55, "Renuka": 76})
'''
This functiona will update item in the dictonary but dictnory never supports
duplicates keys so if the first value and keys exists then it will be updated
if the value is different, and the second is the new key value pair doesn't exist
so it will be add in the marks dictonary it will be a new item in it'''
print(marks)

print(marks.get("Ajay"))
'''
This Function same as the second one but there are some differences if i prints
with the wrong key it will return a none value without getting error'''
print(marks["Ajay"])
'''
This function is returns keys of value if exist in the dictonary if 
the value doesn't exist it will return an error '''

# The conclution is : .get method return a none if the keys are wrong
# print(marks["Ajay"]) this method return an error if the keys are wrong
