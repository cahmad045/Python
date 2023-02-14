# collections.Counter()
#---------------------------------------------------

from collections import Counter
number_of_shoes = int(input())
sizes = list(map(int,input().split()))
sizes_Container = Counter(sizes)
prices_list = []
number_of_customer = int(input())
sum = 0

counter = 0
while counter<number_of_customer:
    prices = list(map(int, input().split()))
    if len(prices) == 2:
        if prices[0] in sizes_Container:
            if sizes_Container[prices[0]] > 0:
               prices_list.append(prices[1])
               sizes_Container[prices[0]] = sizes_Container[prices[0]]-1
            else:
                counter+= 1
                continue
        else:
            counter+= 1
            continue
    else:
        counter+= 1
        continue

    counter+= 1

for i in prices_list:
    sum+=i
print(sum)
