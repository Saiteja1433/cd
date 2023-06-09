data=[]
with open("./../data.csv","r") as file:
    rows = file.readlines()
    for row in rows:
        data.append(row.strip().split(","))
for row in data:
    print(row)