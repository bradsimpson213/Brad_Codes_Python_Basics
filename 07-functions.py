# FUNCTIONS

def is_even(num) -> bool:
    """function that takes in an integer as an arguement 
    and returns if that integer is even or not"""

    if num % 2 == 0:
        print("its event!")
        return True
    else:
        print("its odd!")
        return False
    

print(is_even(4))
print(is_even(5))
help(is_even)