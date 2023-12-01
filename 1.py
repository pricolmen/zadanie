a = list(map(int, input().split()))
b = 9999999999
for i in a:
    if i < b:
        b = i
print(b)
        
