#ak touple bnya 
my_touple = (1, 2, 3, 4, 5)
#count() aur index() method ka use touple me hota hai
print(my_touple.count(3))
print(my_touple.index(4))
#touple lo change krnaa ka jugarr
temp_list = list(my_touple)
temp_list.append(99)
my_touple = tuple(temp_list)