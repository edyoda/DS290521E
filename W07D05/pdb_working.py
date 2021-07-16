# pdb is builtin python debugger

a = input('type a ')
b = input('type b ')

breakpoint()

def sum_the_values(a,b):
	breakpoint()
	print('We are inside this function!!')
	print(a+b)

sum_the_values(a,b)




# pdb console appears whenever it sees a breakpoint().
# c(continue) => continue all the leftover code after breakpoint,
# untill the end of file or the next breakpoint appears.
# n (next) => runs the very next piece of code.
# s (step inside) => to step inside a function.
# we can use print to know the value of the variables at a stage,
# in pdb
# we can know the data type by using "whatis"