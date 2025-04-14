import json  # JSON - JavaScript Object Notation


'''
dump - з Python в JSON-файл
load - з JSON-файлу в Python

dumps - з Python в JSON-строку
loads - з JSON-строки в Python 
'''


python_data = {
    'key1': True,
    'key2': [
        1,
        2,
        3]
    ,
    'key3': 54.654,
    'key4': None
}

# # -----ЗАПИС
# with open('files\\data.json', 'w') as json_file:
#     json.dump(python_data, json_file, indent=4)

# # -----ЧИТАННЯ
# with open('files\\data.json', 'r') as json_file:
#     data = json.load(json_file)
#
# print(data)


json_data = json.dumps(python_data, indent=4)
print(json_data)
