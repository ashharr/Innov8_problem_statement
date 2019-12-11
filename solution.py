n = int(input("Enter the number of boxes"))
#Creating a dictionary
keys = range(n)
values = ['closed', 'open']
dict_ = {}
#initially all boxes are closed
for val in keys:
    dict_[val] =  values[0]

print("Initially Boxes Closed: ", dict_)
step = int(1)
# print(type(keys))
for val in keys:
    dict_[val] = values[1]                   #toggleing all the boxes
print("All boxes opened:", dict_)
for val in keys:
    # dict_[val] = values[1]                 
    step +=1
    if(step<n):
        for val2 in range(1,n,step):        #toggleing boxes at steps
            if(dict_[val2]=='closed'):
                dict_[val2] = values[1] 
            elif(dict_[val2]=='open'):
                dict_[val2] = values[0]

print(dict_)
count = 0
for x in dict_: 
    if dict_.get(x) == 'open':
        count += 1 
print("The number of Gold Coins:", count)
    
# for val in range(1,n,2):
#     print(dict_.get(val))      
        
# list_ = []
# for val in range(n):
#     list_ = list_.append(int(1))

    