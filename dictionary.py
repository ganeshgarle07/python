# # dictionary is mutable you can change the property
d = {"name": "max", "age": 28, "city": "New York"}
d["email"] = "ganeshgarle@gmail.com"
print(d)
del d["age"]
print(d)
d.pop("city")
print(d)
d.popitem()
print(d)
print("age" in d)

# try:
#     print(d['ages'])
# except:
#     print('No')

# d = {"name":"max", "age": 28, "city":"New York"}
# for key in d:
#     print(key,'-------->', d[key])
# for key in d.keys():
#     print(key,'-------->', d[key])
# for value in d.values():
#     print(value)
# for key, value in d.items():
#     print(key,'------------',value)

# d_copy = d
# d['email'] = 'g@gmail.com'
# print(d_copy)
# print(d)

# d_copy = d.copy() # option 1
# d_copy = dict(d) # option 2
# d['email'] = 'g1@gmail.com'
# print(d_copy)
# print(d)


d = {"name": "max", "age": 28, "city": "New York"}
d1 = dict(name="Mary", age=4, email="ggarle@gmail.com")
d.update(d1)
print(d)
print(d1)
