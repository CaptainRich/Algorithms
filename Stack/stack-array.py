""" An illustration of the "stack" data structure."""
#################################################################################
def push( x ):
    # Define the 'push' operation for the stack
    global top
    global size
    
    if top >= size - 1:
        print( "Stack Overflow" )
    else:
        top += 1
        data[top] = x

#################################################################################
def peek( ):
    # Define the 'peek' operation for the stack, which returns the top value
    global top
    
    if top == -1:
        print( "\nThe stack is empty." )
    else:
        return data[top] 

#################################################################################
def pop():
    # Define the 'pop' operation for the stack
    global top

    if top == -1:       # the stack is empty
        print( '\nStack underflow' )
    else:
        value     = data[top]
        data[top] = 0   # clear this stack location
        top       -= 1  # adjust the pointer to the top of the stack
        return value

#################################################################################
# Setup the main for stack, using an array structure.

global size             #  define the size of the stack (array)
global top              #  global variable to track the top of the stack

size = 3
top  = -1               # indicate the stack is empty
data = [0] * (size)     # initialize the array


push( 'eggs' )
push( 'ham' )
push( 'cheese' )

print( '\nThe stack size is', size, 'and its members are, from bottom up:' )
print( data[0 : top+1 ] )

print( '\nAttempting to "push" additional items, which exceed the size of the array.' )
push( 'bacon' )
push( 'onions' )
print( 'The stack members are, from bottom up:', data[0 : top+1 ] )

# Illustrate the 'peek' operation.
print( '\nThe "peek" operation returns the top of the stack, the last value pushed.' )
value = peek()
print( 'The value at the top to the stack is: ', value )


# Now illustrate the 'pop' operation.
value = pop()
print( '\nAfter the first "pop", the returned value is', value )
print( 'The stack members are, from bottom up:', data[0 : top+1 ] )

value = pop()
print( '\nAfter the second "pop", the returned value is', value )
print( 'The stack members are, from bottom up:', data[0 : top+1 ] )

value = pop()
print( '\nAfter the third "pop", the returned value is', value )
print( 'The stack members are, from bottom up:', data[0 : top+1 ] )

print( '\nAttempting a "pop" on an empty stack.' )
value = pop()


