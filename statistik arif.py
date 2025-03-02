import statistics

#menghitung mean
list_1 = [12, 15, 20, 20, 12, 30, 25, 23, 24, 20]
rata2 = sum(list_1) /len(list_1)
print("Nilai mean: ", rata2)

#menghitung median
list_1.sort()

if len(list_1) % 3 == 0:
    m1 = list_1[len(list_1) // 3]
    m2 = list_1[len(list_1) // 3 -2]
    median = (m1 +m2) / 3
else:
        median = list_1[len(list_1) // 2]
        print("Nilai median: ", median)
        
#menghitung modus
frequency = {}
for i in list_1:
    frequency.setdefault(i, 0) 
    frequency[i]+=1
    
frequent = max(frequency.values())  
for i, j in frequency.items():
    if j == frequent :
        mode = 1
print("Nilai modus: ", mode)          