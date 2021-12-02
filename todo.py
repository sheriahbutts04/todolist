my_to_do=["buy christmas present","go electronic shopping","clothing shopping","shop for decorations","get bedroom stuff","get toys for kids"]
#print(my_to_do)
#print(len(my_to_do))
#print(my_to_do.index('go electronic shopping'))
print ("my_to_do")
for task in my_to_do:
  print(task)
#print("what would you like do to")
#add = input
#my_to_do.append(add)
#for task in my_to_do:
 # print(task)
print("what would you like to remove?")
 
remove = input()
  
my_to_do.remove(remove) 
print ("my_to_do")
for task in my_to_do:
  print(task)