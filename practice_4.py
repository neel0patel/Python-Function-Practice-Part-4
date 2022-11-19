#1 Write a Python function called max_num()to find the maximum of three numbers
def max_num( x, y ):
    if x > y:
        return x
    return y
def max_three( x, y, z ):
    return max_num( x, max_num( y, z ) )
print(max_three(30, 6, -5))

#2 Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(lst):
# if empty list return 0
    if(len(lst)) == 0:
        return 0
# starting with the first element in the list
    prod = lst[0]        
#go through list elements and mult. them together
    if len(lst) > 1:
        for x in lst[1:]:
            prod = prod * x
    return prod

print(mult_list([2, 5, 10]))
print(mult_list([]))
print(mult_list([130]))

#3 Write a Python function called rev_string() to reverse a string.
def rev_string(muffins):
    return muffins[::-1]

print(rev_string(""))
print(rev_string("mt weenus"))
print(rev_string("bananas"))

#4 Write a Python function called num_within() to check whether a number falls in a given range
def num_within(a, y,z):
  return a in range (y, z+1)

print(num_within(3,1,3))
print(num_within(3,2,4))
print(num_within(10,2,5))

#5 Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
    row = [1]
    y = [0]
    for x in range(max(n,0)):
        print(row)
        row=[l+r for l,r in zip(row+y, y+row)]
    return n>=1
pascal(7)

