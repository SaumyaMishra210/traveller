my_dict = {'banana': 3, 'apple': 4,'as':10, 'pear': 1, 'orange': 2, 'ghg':4}

# print(sorted(my_dict.items(),reverse=True))
# d ={}
#
# while my_dict:
#         minkey = min(my_dict,key=my_dict.get)
#         d[minkey] = my_dict.pop(minkey)
#
# print("dict:",d)

d = {}
m = {}
curr = iter(my_dict.values())

for i in range(len(my_dict)):
    vv = next(curr)
    for k, v in my_dict.items():
        # print(f"Cur-val : {vv} , v : {v}")
        if v < vv:
            d[k] = v
        else :
            m[k]= v
d.update(m)
print(d)
