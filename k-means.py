def predict_classification(data,v,vv,k):
    centroides = data[:k]
    distance =[]
    for centroid in centroides:
        ecudis = ((v-centroid[0])**2 + (vv-centroid[1])**2)**0.5
        distance.append(ecudis)
    min_dis = float('inf')
    for dis in distance:
        if min_dis>dis:
            min_dis=dis
    return data[distance.index(min_dis)][2]
data = [
    (1.713, 1.586, 0),
    (0.180, 1.786, 1),
    (0.353, 1.240, 1),
    (0.940, 1.566, 0),
    (1.486, 0.759, 1),
    (1.266, 1.106, 0),
    (1.540, 0.419, 1),
    (0.459, 1.799, 1),
    (0.773, 0.186, 1)
]

var1 = 0.906
var2 = 0.606
k=3
predicted_classification = predict_classification(data, var1, var2,k)
print(predicted_classification)


# output:
#   The predicted classification for VAR1=0.906 and VAR2=0.606 is: 1