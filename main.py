from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to our Bid party!!!")
is_enough = True
add_name_price = {}

def the_winner(bidder_record):
  highest_bid = 0
  winner = ""
  for bidder in bidder_record:
    bid_amount = bidder_record[bidder]
    if bid_amount> highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"{winner} is winner with amount of {highest_bid}")  
while is_enough:


  name_user= input("What is your name?: ")
  bid_price = int(input("How much will you invite?:  $"))
  add_name_price[name_user] = bid_price


  other_person = input("Anyone who can invite a bid? Yes or No\n ").lower()
  if other_person == "yes":
    is_enough = True
    clear()
    # add_name_price.update(name_user = bid_price)
  # print(add_name_price)
    

  elif other_person == "no":
    is_enough = False
    the_winner(add_name_price)
    
        
    

