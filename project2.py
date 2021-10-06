# lst=[1,2,5,4,3]
# a=lst[0]
# for i in range(0,len(lst),1):
#     if(lst[i]>=a):
#         a=lst[i]
# print("Maximum value in the list is:",a)
def totalpopulation(x):
    total=x[0][2]+x[1][2]+x[2][2]+x[3][2]+x[4][2]
    return total
cities = [ ["Pittsburgh", "Allegheny", 302407],
           ["Philadelphia", "Philadelphia", 1584981],
           ["Allentown", "Lehigh", 123838],
           ["Erie", "Erie", 97639],
           ["Scranton", "Lackawanna", 77182] ]
print(totalpopulation(cities))