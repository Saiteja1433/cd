train_data = [
    ['medium', 'skiing', 'design', 'single', 'twenties', 'no', 'highRisk'],
    ['high', 'golf', 'trading', 'married', 'forties', 'yes', 'lowRisk'],
    ['low', 'speedway', 'transport', 'married', 'thirties', 'yes', 'medRisk'],
    ['medium', 'football', 'banking', 'single', 'thirties', 'yes', 'lowRisk'],
    ['high', 'flying', 'media', 'married', 'fifties', 'yes', 'highRisk'],
    ['low', 'football', 'security', 'single', 'twenties', 'no', 'medRisk'],
    ['medium', 'golf', 'media', 'single', 'thirties', 'yes', 'medRisk'],
    ['medium', 'golf', 'transport', 'married', 'forties', 'yes', 'lowRisk'],
    ['high', 'skiing', 'banking', 'single', 'thirties', 'yes', 'highRisk'],
    ['low', 'golf', 'unemployed', 'married', 'forties', 'yes', 'highRisk']
]
golf = 0
for d in train_data:
    if d[1]=='golf':
        golf+=1
golf = golf / len(train_data)
single_medrisk=0
medrisk=0
for d in train_data:
    if d[3]=='single' and d[6]=='medRisk':
        single_medrisk+=1
    if d[6] == 'medRisk':
        medrisk +=1
print("Unconditional probability of 'golf",golf)
print("Conditional probability of 'single' given 'medRisk'",single_medrisk / medrisk)

