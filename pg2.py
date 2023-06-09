table=[]
data=[]
with open("data1.csv") as file:
  lines=file.readlines()
  for line in lines:
    values=line.strip().split(",")
    data.append(values)
for row in data[1:5]:
  table.append(row)
##print(table) 
specific=['null','null','null','null','null','null']  
general=[
  ['?','?','?','?','?','?'],
  ['?','?','?','?','?','?'],
  ['?','?','?','?','?','?'],
  ['?','?','?','?','?','?'],
  ['?','?','?','?','?','?'],
  ['?','?','?','?','?','?']
  ]
for i in range(4):
  if table[i][6]==' yes' and specific==['null','null','null','null','null','null']:
    specific=table[i][:6]
  elif table[i][6]==' yes':
    temp=table[i][:6]
    for j in range(6):
      if temp[j]!=specific[j]:
        specific[j]='?'
  else:
    for j in range(6):
      if table[i][j]!=specific[j]:
        for k in range(6):
          if general[k]==['?','?','?','?','?','?']:
            general[k][j]=specific[j]
            break

for i in range(6):
  for j in range(6):
    if general[i][j] not in specific and general[i][j]!='?':
      general[i][j]='?'

for i in range(6):
  if general[i]!=['?','?','?','?','?','?']:
    print(general[i])
print(specific)