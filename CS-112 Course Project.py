#Hailey Incorvaia 

import statistics
dataset= []
i = 1

while i <= 10:
    x = float(input("Enter a temperature values between 68 and 80: "))
    dataset.append(x)
    i = i + 1
print(dataset)

std = statistics.stdev(dataset)

if std <= 1:
    print("Comfy")
else:
    print("Not Comfy")
