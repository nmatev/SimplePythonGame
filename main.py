print("Welcome to my first game!")
userName = input("What is your name? ")
age = int (input("What's your age? "))

health = 100

if age >= 18:
    print("You are old enough to play!")
    
    whants_to_play = input("Do you whant to play (yes/no)? ").lower()
    if whants_to_play == "yes":
        print("You are starting with", health, "health")
        print("Let's play")
        
        left_or_right = input("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ").lower()
        
        if ans == "around":
            print("You went around and reached the other side of the lake")
        elif ans == "across":
            print("You managed to get across, but were bit by a fish and lost 50 health")
            health -= 50
            
            ans = input("You notice a house end a river. Wich do you go to (river/house)? ").lower()
            if ans == "house":
                print("You go to the house and are greted by the owner... He doesn't like you and you lose 50 health...")
                health -= 50
            
                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived... You Win! ")
            
            else:
                print("You fell in the river and lost...")
        
        else:
            print("You fall down and lost..")
        
    else:
        print("Cya...")
        
else:
    print("You are not old enough to play...")