from pymongo import MongoClient
client = MongoClient('localhost', 27017)
mydatabase = client.college
collection = mydatabase.stud_list


result = collection.find({"course":"MCA", "gender":"female"}, {"name.fname":1, "name.lname":1,"mark":1, "_id":0 })
for x in result:
    print(x)


print(collection.find_one({"course":"MCA"},{"name.fname":1},sort=[("mark", -1)]))



result = collection.find({"gender":"male", "grade":"A+"},{"name.lname": 1,"name.fname": 1})
for x in result:
   print(x["name"]["fname"]+ "  "+x["name"]["lname"])


results = collection.find({"course":"Mechanical"},{"name.fname":1},sort=[("mark", -1)],limit=3)
for x in results:
    print(x)


results = collection.find({"gender":"female","mark":{"$gt":90}},{"name.fname":1,"name.lname":1,"grade":1,"mark":1,"phone.no":1})
for x in results:
   print(x)


results = collection.find({"mark":{"$lt":90, "$gt":80}},{"name.fname":1,"name.lname":1,"grade":1,"mark":1,"phone.no":1})
for x in results:
    print(x)


results = collection.find({"name.fname":{"$regex":"^V"}},{"name":1})
for x in results:
   print(x)


results = collection.find({"address.city":"Kollam"},{"name":1})
for x in results:
   print(x)


results = collection.find({"$nor":[{"address.city": "Kollam"}]},{"name":1, "address.city":1})
for x in results:
   print(x)

10
results = collection.find({"address.city" :{"$in":["Kollam","Thiruvananthapuram"]}},{"name":1, "address.city":1})
for x in results:
   print(x["name"]["fname"] + " " + x["name"]["lname"])
