
emp = {'sandeep': 1, 'pavan': 2,
        'ajay': 6, 'yash': 3, 'rahul': 4}
 
keys = list(emp.keys())
keys.sort()
sort = {i: emp[i] for i in keys}
 
print(sort)