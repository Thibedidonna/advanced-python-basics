#Loops control statement

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits :
    if fruit =="cherry":
        break # Exists the loop if cherry is found
    print(fruit)
    
    print()
    
    for fruit in fruits:
        if fruit == "cherry":
            continue # Skips cherry and continues to the iteraction
        print(fruit)
        
    print()
    
    for fruit in fruits:
        if fruit == "cherry":
            pass # Placeholder, no action is needed for cherry        
        print(fruit)   
        
    