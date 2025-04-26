num = [1,2,3,4,5,6,7,8,9,10]

r = []

for i in range(0,len(num)//2):
    r.append(num[i])

print("Original list: ",num)
print("Extracted first five elements: ",r)
print("Reversed extracted elements: ",r[-1::-1])