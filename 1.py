with open("BOok1.csv", "r") as file:
    lines = file.readlines()
    # Extract the data from the lines 
    data = []
    for line in lines:
        values = line.strip().split(",")
        data.append(values)
for row in data[:5]:
    print(row)
