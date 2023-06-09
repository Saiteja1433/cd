table = [
['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'],
['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'],
['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no'],
['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes']
]
hypothesis=['null', 'null', 'null', 'null', 'null', 'null']
h1=['null', 'null', 'null', 'null', 'null', 'null']
for i in range(len(table)):
    if table[i][6]=="yes":
        h1 = table[i][:6]
        if hypothesis == ['null', 'null', 'null', 'null', 'null', 'null']:
            hypothesis=h1
        else:
            for j in range(len(h1)):
                if(hypothesis[j]!=h1[j]):
                    hypothesis[j]='?'
print(hypothesis)



# with open("./d.csv", "r") as file:
#     lines = file.readlines()
#     table = []
#     for line in lines:
#         values = line.strip().split(",")
#         table.append(values)
# hypothesis=['null', 'null', 'null', 'null', 'null', 'null']
# h1=['null', 'null', 'null', 'null', 'null', 'null']
# for i in range(len(table)):
#     if table[i][6]=='yes':
#         h1 = table[i][:6]
#         if hypothesis == ['null', 'null', 'null', 'null', 'null', 'null']:
#             hypothesis=h1
#         else:
#             for j in range(len(h1)):
#                 if(hypothesis[j]!=h1[j]):
#                     hypothesis[j]='?'
# print(hypothesis)