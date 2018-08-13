import json

data_json = """
{
"people":[
{
"Name" : "Vignesh",
"Country" : "France",
"Age" : "25"
},
{
"Name" : "John",
"Country" : "France",
"Age" :  "24"
}
]}
"""

print(data_json)

data=json.loads(data_json)
print(data)