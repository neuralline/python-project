import json

person = {"name": "john", "age": 30, "city": " new york"}
personJSON = json.dump(person, indent=4, sort_keys=True)
print(personJSON)
