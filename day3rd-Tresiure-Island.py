'''links 1- https://ascii.co.uk/art 2- 
https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVf>
'''
print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/____/__
*******************************************************************************''')
print("Wellcome to Tresure Island.")
print("Your mission is to find the tresure.")
choice1 = input('you\'re at a crossroad, where do  you want to go? type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an  island in the middle of the lake. Type "wait" to wait  for  a bot. Type  "swin" to swim across.\n').lower()
    if choice2 == "wait":
       choice3 = input("you arrive at the island unharmed. There is a house with 3 door. One red, one yellow amd and one bule. Which color do you choose?\n").lower()
       if choice3 == "red":
             print("It's a room full of fire. Game Over.")
       elif choice3  == "yellow":
              print("You found the tresure! You Win!")
       elif choice3 == "blue":
              print("You enter a room of beasts. Game Over.")
       else:
              print("You chose a door that doesn't exit. Game Over.")
    else:
         print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")
