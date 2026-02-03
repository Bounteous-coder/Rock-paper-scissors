import random

paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' 
'''

scissors = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  |  `(.-')
   > ._>-'
  // //

'''

rock = '''
    _.---~~~~~~~-.     ____
   ( _.-~   _     `.__,-|
    (_ _.-~^ )        | |
   `( _.-~ )       | |
    `( _.-~ )   ___| |
     `-..-~--~'   `-| O
                    `---
'''
game_images = [rock, paper, scissors]

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Scissors, 2 for Paper: "))
computers_choice = random.randint(0, 2)

if users_choice < 0 or users_choice > 2:
    print("You chose the wrong number, try again")
    exit()

print("You chose:")
print(game_images[users_choice])

print("Computer chose:")
print(game_images[computers_choice])

if users_choice == computers_choice:
    print("It's a Draw!")

elif (
    (users_choice == 0 and computers_choice == 1)
    or (users_choice == 1 and computers_choice == 2)
    or (users_choice == 2 and computers_choice == 0)
):
    print("You win!")


else:
    print("Computer wins!")