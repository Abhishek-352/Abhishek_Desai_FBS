
# Default pamameter

# def emp(id,name,sal,dep='backoffice'):    
#     print("ID: ",id)
#     print("NMAE: ",name)
#     print("SALARY: ",sal)
#     print("DEPARTMENT: ",dep)

# emp(101,'abc',50000,'IT')

# print("###############################")

# emp(102,'xyz',10000)


# Keyword paramter

# def emp(id,name,sal,dep='backoffice'):
#     print("ID: ",id)
#     print("NMAE: ",name)
#     print("SALARY: ",sal)
#     print("DEPARTMENT: ",dep)

# emp(sal=50000,name='abc',dep='IT',id=101)

# print("###############################")

# emp(102,'xyz',dep='cse',sal=10000)


# Variable length for Multiple paramter passing

# def add(*data):
#     sum=0
#     for val in tuple(data):
#         sum += val
#     print(sum)

# res=add(10,20,30)
# print(res)



# Keyword Variable with paramter

def emp(**data):
    for key, val in data.items():
        print(key, ':', val)

emp(id=101,age=34,sal=50000,name='abc',dep='IT')


