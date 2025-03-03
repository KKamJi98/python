import modules.logo as logo
from modules.clear import clear

print(logo.logo)

other_bidders = True
bidders = {}
max_bid_price = 0
final_bidder_name = str()

while other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bidders[name] = bid
    if bid > max_bid_price:
        max_bid_price = bid
        final_bidder_name = name

    has_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if has_other_bidders == "no":
        other_bidders = False
    else:
        clear()

print(f"Final Bidder: {final_bidder_name}\t Bid Price: {bidders[final_bidder_name]}")
