name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on dirt road, it has come to an end and you can go left or right. Which way would you to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim across: ") 

    if answer == "swim":
        print("You swam acrross and were eaten by ab alligator.")
    elif answer == "walk":
        print("You walked for many miles, run out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to bridge,it looks wobbly, do you want to cross ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger, Do you talk to them (yes/no)?")
        if answer == "yes":
            print("You talk to the stranger and they give youa god you win! ")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")


print("Thank you for trying ", name )