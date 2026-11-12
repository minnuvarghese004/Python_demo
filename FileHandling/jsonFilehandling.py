import json
#Python provides a built-in module called json to work with json data
with open("file.json","r") as f:
    data=json.load(f)
    print(data)
    print(data["name"])

#json.dump() - write python data into json file
#json.dumps() - converts a python data into a json string
#json.loads() - convert json string into python data

student={"Mark":80,"Location":"EKM"}
with open("file.json","w") as f:
    json.dump(student,f)

    

