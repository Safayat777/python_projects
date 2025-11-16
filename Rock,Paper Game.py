import random
choices = ('r','p','s')
while True:
 user_choice=input("Enter your choice(r,p,s): ")
 if user_choice not in choices:
    print("Please choose between r, p and s ")
 pc_choice = random.choice(choices)
 if user_choice == pc_choice:
    print('Try again')
 elif user_choice == 'r' and pc_choice == 's':
    print('You win')
 elif user_choice == 'r' and pc_choice == 'p':
    print('You lose')
 elif user_choice == 's' and pc_choice == 'r':
    print('You lose')
 elif user_choice == 'p' and pc_choice == 'r':
    print('You win')
 elif user_choice == 'p' and pc_choice == 's':
    print('You lose')
 elif user_choice == 's' and pc_choice == 'p':
    print('You win')
 print(f'pc chose {pc_choice}')
 print(f'user chose {user_choice}')
