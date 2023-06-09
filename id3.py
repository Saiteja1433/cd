data = [
["I love this car", "positive"],
["This view is amazing", "positive"],
["I feel great", "positive"],
["I'm not happy with the product", "negative"],
["This is a terrible place", "negative"],
["I don't like this movie", "negative"]
]

classes = {}
for line in data :
    if line[1] in classes :
        classes[line[1]] += 1
    else :
        classes[line[1]] = 1
print(classes)
n = len(data)
for lab in classes :
    print(classes[lab]/n)
    classes[lab] = classes[lab]/n
print(classes)
    
wordCount = {}
for line in data :
    words = line[0].split()
    print(words)
    if line[1] not in wordCount :
        wordCount[line[1]] = {}
    for word in words :
        if word in wordCount[line[1]] :
            wordCount[line[1]][word] +=1
        else :
            wordCount[line[1]][word] = 1          
print(wordCount)
for lab in classes :
    n = sum(wordCount[lab].values())
    for word in wordCount[lab] :
       wordCount[lab][word] = wordCount[lab][word]/n
#print(wordCount)
def f(text) :
    words = text.split()
    classScore = {}
    for lab in classes :
        score = classes[lab]
        for word in words :
            if word in wordCount[lab] :
                score *= wordCount[lab][word]
        classScore[lab] = score
    print(max(classScore))
    

text = "I like this place"
f(text)