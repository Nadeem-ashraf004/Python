d={1:"nadeem",2:"ashraf", 3:"ali"}
print(d)
x=dict(a="nadeem",b="ashraf", c="ali")
del x["c"]
print(x)
val=x.pop('b')
print(val)
key ,val = x.popitem()
print(f"key :{key},value:{val}")
print(x.get("a"))
x.clear()
print(x)
##############################################################
d1={
    "product":{"name":"laptop","price":45000,"stock":40},
    "product2":{"name":"mobilephones","price":4000,"stock":20},
    "product3":{"name":"tablet","price ":499,"stock":10}
}
cnt=0
for key ,val in d1.items():
    if isinstance(val,dict):
        for i in val:
            cnt+=1
    else:
        cnt+=1
print(cnt) 
lenght1=len(d1.keys())
print(lenght1)
lenght2=len(d1.values())
print(lenght2)
lenght3=len(d1.items())
print(lenght3) 
################################### to marge the two or more dictionaries
   
def merge_dict():
    A = {"a": "nadeem", "b": "ashraf", "c": "hussain"}
    B = {"f": "Ali", "r": "arif"}
    D = A | B  
    return D
print(merge_dict())