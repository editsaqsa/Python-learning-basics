import random
def check(comp , user):
    if comp == user:
        return 0
    #snack vs water (1 vs -1) snake drinks water (snake wins)
    #water vs gun (-1 vs 0) snake drown gun (water wins)
    # gun vs snake (0 vs 1) gun kill snake (gun win)
    
    if comp == 1 and user == -1:
        return -1
    elif comp == -1 and user == 1:
        return 1

    if comp == -1 and user == 0:
        return -1
    elif comp == 0 and user ==-1:
        return 1

    if comp == 0 and user == 1:
        return -1
    elif comp == 1 and user == 0:
        return 1


    # computer ki random choice (0: gun, 1: snake, -1: water)
    comp = random.choice([-1,0,1])
    user_str = input("enter your choice (s for snake, w for  water, g for gun):").lower()

    dictionary = {"s": 1, "w": -1, "g": 0}
    reverse_dict = {1: "snake",-1: "water", 0: "gun"}

    if user_str not in dictionary:
        print("invalide input please enter 's' , 'w', or 'g'.")
    else:
        user = dictionary[user_str]

    print(f"\nComputer chose:{reverse_dict[comp]}")
    print(f"you chose: {reverse_dict[user]}")

          score = check(comp,user)

          if score == 0:
             print("\nMatch Draw")
          elif score == -1:
             print("\nYou lose")
          else:
             print("\nYou win")
