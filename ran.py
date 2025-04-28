import random



rock='''
            ______
      ______|  ____)
              (_____)
            (________)
             (_______)
      ______ (______)
'''

paper='''
        _______
 _______|  _____)___      
         ___________)_
         _____________)
          __________)
--------|________)
'''
scissor='''
       ________
_______|  _____)_____
          ___________)_
          _____________)
        (_______)
----|____(_____)
'''
game=[rock,paper,scissor]
com=random.randint(0,2)

user= int(input("What do you choose ? type 0 for rock,1 for paper ,2 for scissors\n"))
 
if user >= 3 or user < 0:
    print("yowzz! you typed invalid number")
 
if user >= 0 and user <= 2 :
    print(f'you choose {user}')
    print(game[user])



    
    print(f"computer choose {com}")
    print(game[com])



if user == 0 and com == 2:
    print("you win")
elif user == 0 and com ==1:
    print("you lose")
elif user == 1 and com == 2: 
    print("you lose")
elif user ==1 and com == 0:
    print("you win")
elif user == com:
    print("it's draw")
elif user == 2 and com == 1:
    print("you win")
elif user ==2 and com ==0:
    print("you lose")