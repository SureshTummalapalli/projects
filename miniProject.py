#1.dictionary update
my_dict={'name':'python','age':25}
my_dict['city']='west godavari'
print(my_dict)

#2.dictionary access
product_info={'name':'laptop','brand':'dell','price':'1200'}
print(product_info['price'])

#3.dictionary removal
my_dict={'name':'python','age':'30','city':'bhimavaram'}
my_dict.pop('city')
print(my_dict)

#4.dictionary keys
my_dict={'name':'python','age':'25','city':'rajahmundry'}
print(my_dict.keys())

#5.dictionary values
my_dict={'name':'python','age':'25','city':'tanuku'}
print(my_dict.values())

#exercise1
dict={'name':'sravani','age':'20','address':'kongara kalan'}
dict1={'person':'niharika','gender':'f','city':'hyderabad'}
dict.update(dict1)
print(dict)
#exercise2
print(dict['name'])
#exercise3
dict.pop('address')
print(dict)
#exercise4
print(dict1.keys())
#exercise5
print(dict1.values())