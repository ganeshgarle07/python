records = [
    {"name": "suvajit", "gender": "Male"},
    {"name": "sandip", "gender": "Male"},
    {"name": "sudeshna", "gender": "FeMale"},
]
# def is_same_gender(records):
#     s = set()
#     for i in records:
#         s.add(i['gender'])
#     return len(s) == 1

# print(is_same_gender(records))

# input: {"apple": 1, "ant": 1, "bat": 2, "cat": 3, "dog": 4, "cow": 3}
# output: {1: ["apple", "ant"], 2: ["bat"], 3: ["cat", "cow"], 4: ["dog"]}
# exercise newoutput : {1: ['apple', 'ant'], 2: 'bat', 3: ['cat', 'cow'], 4: 'dog'}

# input = {"apple": 1, "ant": 1, "bat": 2, "cat": 3, "dog": 4, "cow": 3}
# output = {}
# for k,v in input.items():
#     if(v not in output):
#         output[v] = []
#     output[v].append(k)
# for k,v in output.items():
#     if(len(v) == 1):
#         output[k] = v[0]
# print(output)

# my_list = [2, 3, 5, 7, 11]
# # construct a dictionary from the list where index should be a key and items should be the value. like
# # {0: 2, 1: 3, 2: 5, 3: 7, 4: 11}
# output = {}
# for i in range(len(my_list)):
#     output[i] = my_list[i]
# print(output)

# for i, j in enumerate(my_list):
#     output[i] = j
# print(output)

l = ["Toyota_2015_03", "Toyota_2015_04", "Kia_2016_01", "Kia_2016_04", "Kia_2016_05", "Tata_2016_06"]
d = {"2016_05": 665, "2016_04": 462, "2015_03": 568, "2015_08": 895}
# output: {'Toyota': 568, 'Kia': 1127}
output = {}
for i in l:
    name, year_month = i.split('_', 1)
    print( output.get(name, 0),'--------', d.get(year_month,0))
    output[name] = output.get(name, 0) + d.get(year_month,0)

print(output)


# dictionary = [
#     {"Flow": 100, "Location": "USA", "Name": "A1"},
#     {"Flow": 90, "Location": "Europe", "Name": "B1"},
#     {"Flow": 20, "Location": "USA", "Name": "A1"},
#     {"Flow": 70, "Location": "Europe", "Name": "B1"},
# ]

# new_dictionary = [
#     {"Flow": 120, "Location": "USA", "Name": "A1"},
#     {"Flow": 160, "Location": "Europe", "Name": "B1"},
# ]

# output = {}

# for i in dictionary:
#     key = (i['Location'], i['Name'])
#     output[key] = output.get(key,0) + i['Flow']
# l = []
# for k,v in output.items():
#     d1 = {'Name': k[0],'Location':k[1], 'Flow': v}
#     l.append(d1)

# print(output)
# print(l)
# input_list = [
#     {"Flow": 100, "Location": "USA", "Name": "A1"},
#     {"Flow": 90, "Location": "Europe", "Name": "B1"},
#     {"Flow": 20, "Location": "USA", "Name": "A1"},
#     {"Flow": 70, "Location": "Europe", "Name": "B1"},
# ]

# output_dict = {}

# for entry in input_list:
#     key = (entry["Location"], entry["Name"])
#     if key in output_dict:
#         output_dict[key]["Flow"] += entry["Flow"]
#     else:
#         output_dict[key] = entry

# print('--------',output_dict)
# output_list = list(output_dict.values())

# print(output_list)
