a = []
for i in range(int(input())):
  a.append(int(input()))
i=0
while (i<len(a)):
  smallest = min(a[i:])
  index_of_smallest = a.index(smallest)
  a[i],a[index_of_smallest] = a[index_of_smallest], a[i]
  i=i+1
print(a[2])