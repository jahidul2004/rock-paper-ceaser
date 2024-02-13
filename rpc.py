#Import random module for randomly choice a value
import random
#Create a list for randomly choice a value from the list
rpc = ['rock','paper','ceaser']
#Define User and Bot Initial Value are 0
user_point = 0
bot_point = 0
#A loop for rereun the code while user point or bot point is not 0
while bot_point or user_point != 5:
    bot = random.choice(rpc)
    user = input("Enter your choice 'rock','paper' or 'ceaser':")
    #Apply all condition for Tie! Output.
    if bot == user:
        print(f"Bot is:{bot},User is:{user}.Thats Tie!")
    #Apply all condition for Bot Win! Output.
    elif bot == 'rock' and user == 'ceaser' or bot == 'paper' and user == 'rock' or bot == 'ceaser' and user == 'paper':
        print(f"Bot is:{bot},User is:{user}.Bot win!")
        bot_point += 1
        print("Bot point is:",bot_point)
        #Apply a condition for break the loop when bot point is 5.
        if bot_point == 5:
            print("Great!Bot is win!")
            break
    #Apply all condition for User Win! Output.
    elif bot == 'ceaser' and user == 'rock' or bot == 'paper' and user == 'ceaser' or bot == 'rock' and user == 'paper':
        print(f"Bot is:{bot},User is:{user}.You win!")
        user_point += 1
        print("User point is:",user_point)
        #Apply a condition for break the loop when user point is 5.
        if user_point == 5:
            print("Great!You are win!")
            break
    #Apply condition for handle unknown input.
    else:
        print("Unknown Input!Try again!")
