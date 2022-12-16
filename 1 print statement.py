###################################### Description ############################################################################################ 
# print(object(s), sep=separator, end=end, file=file, flush=flush)

#           Parameter	Description:
#           object(s)                 	Any object, and as many as you like. Will be converted to string before printed
#           sep='separator'	            Optional. Specify how to separate the objects, if there is more than one. Default is ' '
#           end='end'                  	Optional. Specify what to print at the end. Default is '\n' (line feed)
#           file	                      Optional. An object with a write method. Default is sys.stdout
#           flush	                      Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False
####################################### Description ############################################################################################ 





print("hello world")   # prints or displays "hello world"
print('hello world')  # does the same as above
print(5)  # output >> 5
x = 'byye'
print(x) # >> byye
print(3*2) # output >> 6

print("Hello", "how are u?",, sep="-")  # output >> Hello-how are u?

print("hello","ji",'kaise',"ho?", end ='END\n')   # output >> hello ji kaise ho?END
# if in end argument , u dont use \n then the cursor wont move into the next line

print('hello, it's Divyam here') # this throws error
print('hello, it\'s Divyam here') # this doesnt throw error (\ is used to escape special characters)


