# Lambda Functions:
# A lambda function is a small anonymous function created using the lambda keyword.

# 1 Addition of two numbers
# add=lambda x,y,z=10:x+y+z
# print(add(3,4,))


# 2 Square of number
# sq=lambda x:x*x
# print(f"Square :{sq(5)}")



# 3 Even or Odd
# eo=lambda x:"Even" if x %2 ==0 else "Odd"
# print(eo(9))


# 4 map():map() applies a function to every element.
# number=[2,3,4,5,6,7,8]
# result=list(map(lambda x:"even" if x % 2 ==0 else "odd",number))
# print(result)


# 5 filter() selects elements that satisfy a condition.
# number=[2,3,4,5,6,7,8]
# result=list(filter(lambda x: x % 2 ==0,number))
# print(result)

# 6 The reduce() function applies a function repeatedly
#  to elements and reduces the entire iterable to a single result.
# from functools import reduce
# number=[1,2,3,4]
# result=reduce(lambda x,y:x+y,number)
# print(result)