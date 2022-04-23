import json

# myDict = {
#     'admin': 'admin',
#     'huỳnh khả phi': '3301'
# }

# with open('userData.json', 'w', encoding='utf-8') as userData:
#     json.dump(
#         myDict, 
#         userData, 
#         ensure_ascii=False,
#         indent=4
#     )

with open('userData.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    print(data)