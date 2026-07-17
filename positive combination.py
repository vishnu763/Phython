lst=[10,-5,3,-8,6]
n=len(lst)
for i in range(n):
    for j in range(i+1,n):
        ps=lst[i]+lst[j]
        if ps>0:
            print(f"({lst[i]},{lst[j]})sum={ps}")
       
