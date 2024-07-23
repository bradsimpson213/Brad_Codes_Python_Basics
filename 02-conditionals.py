# CONDITIONALS IF/ELIF/ELSE 

def breakfast(food):
    """function that accepts a string breakfast food and judges your choices"""

    if food == "waffles":
        print(f"{food} are the best breakfast, you win!")

    elif food == "pancakes":
        print(f"{food} is a really good choice too!")

    elif food == "bacon":
        print(f"{food} is an amazing choice, you also win!")    
        
    else: 
        print(f"{food} is okay, no real judgement")


breakfast("waffles")
breakfast("pancakes")
breakfast("bacon")
breakfast("cereal")