compis=["raul","sebas","juan","albert","junior"]
print(compis)
for i in range (len(compis)):
    for j in range(len(compis)-i-1):
        if compis[j]>compis[j+1]:
            aux=compis[j+1]
            compis[j+1]=compis[j]
            compis[j]=aux
print(compis)

