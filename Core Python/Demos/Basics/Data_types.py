#1.numerical

#complex
var=10+5j
print(type(var))

#int
var=10
print(type(var))

#float
var=3.14
print(type(var))


##2.text

#string
str='abhishek'   ## here can't use under single cote another cotes as as to their multiple cotes
print(type(str))

str="firstbit solutins"
print(type(str))

str='''multiple lines of string
can use in this '''
print(type(str))

str="""here also multiple lins 
can write here """
print(type(str))
 

##3.sequencial

#list
var=[10,20,30,40,50]
print(type(var))

#tuple
var=(10,20,30,40,50)
print(type(var))

#range
var=range(1, 100)
print(type(var))


##4.Set type

#set
var={10,20,30}
print(type(var))

#frozenset
var=frozenset({10,20,30})
print(type(var))


##5.mapping

#dict
var={'id':101,'name':'Abhishek'}
print(type(var))


##6.others

#Boolean
var=True
print(type(var))
