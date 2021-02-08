
''' 
Variables Assignment 
'''

# name = "Adriana"
# print(name)

# =======================

# assign same value to multiple variables on the same line
# a = b = c = 'cat'
# print(b)
# print(a)
# print(c)

# =======================

# reuse variable names, the last assingment is printed 
# colour = ' Red'
# colour = 'Blue'

# print(colour)

# =======================
''' 
Reserved keywords 
'''
# help('keywords')

# =======================

# variable types
# var = "Hello world"
# print(type(var))

# var1 = 23
# print(type(var1))
'''
Object Identity 
'''
# score = 400
# print(id(score))

# score = 400
# indentity = id(score)
# print(indentity)

# =======================

# score variables is saved into the pb by reference

# score = 400
# pb = score
# print(id(score))
# print(id(pb))
'''
Object reference 
'''
# both score and pb point to the same into object
# score ---------> int 100  <----------- pb

# score = 100
# pb = score

# print(type(score))
# print(type(pb))
# print(score)
# print(pb)

# =======================

# pb   ----------> int 20
#score ----------> int 100
# pb = 20
# score = 100

# print(type(score))
# print(type(pb))
# print(score)
# print(pb)

# =======================
# garbage collection

# pb    ---------> int 20
# score ---------> str 'Completed'
#       ----------> int 100

# pb = 20
# score = 100
# score = 'Completed'

# print(type(score))
# print(type(pb))
# print(score)
# print(pb)