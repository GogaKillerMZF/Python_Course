def my_func(first, second, third):
    if first <= second and first <= third:
        return second + third
    elif second <= first and second <= third:
        return first + third
    else:
        return first + second
    
    
print(my_func(5,2,3))