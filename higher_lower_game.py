from random import randint 
import random
from art import higher_logo
from higher_game_data import data


def get_random_number():
    return random.choice(data)
    
def data_name(account):
    name=account['name']
    description=account['description']
    country=account['country']
    
    return f"{name}, a {description}, from {country}"
    
def check_answer(guess, a_followers,b_followers):
    if a_followers>b_followers:
        return guess=='a'
    else:
        return guess=='b'

def game():
    print(higher_logo)
    score=0
    should_continue=True
    account_a=get_random_number()
    account_b=get_random_number()
    
    while should_continue:
        account_a = account_b
        account_b=get_random_number()
        
        while account_a==account_b:
            account_b=get_random_number()        
            print(f"Compare A: {data_name(account_a)}")
            print(F"Compare B: {data_name(account_b)}")
            guess=input(f"Who have more followers? choose one 'a' or 'b'").lower()
            a_follower_count=account_a["follower_count"]
            b_follower_count=account_b["follower_count"]
            is_correct=check_answer(guess, a_follower_count,b_follower_count)
    
            if is_correct:
                score+=1
                print(F"You are right! Current score: {score}.")
            else:
                should_continue=False
                print(f"Sorry, that's wrong. Final score:{score}")

game()
    
    
