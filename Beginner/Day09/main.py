import art
print(art.logo)
bidders = {}         # Stores name: bid
bid_order = []       # Stores (name, bid) in order
bid_number = 1       # Start counting from 1

would_continue = True

while would_continue:
    print(f"\n {bid_number}")
    name = input("What is your name: ").lower()
    bid = int(input("What is your bid price: $"))

    bidders[name] = bid
    bid_order.append((bid_number, name, bid))  # Store order with number

    ask = input("Would you like to enter another bid? (yes/no): ").lower()
    if ask == "no":
        would_continue = False
        print("Goodbye 👋")
    elif ask == "yes":
        print("\n"*30)
    else:
        print(" you have enetered invalid data" )

# Find the highest bidder
highest_bidder = max(bidders, key=bidders.get)
highest_bid = bidders[highest_bidder]

# Find their bid number
for number, name, bid in bid_order:
    if name == highest_bidder and bid == highest_bid:
        highest_bid_number = number
        break

# Final output
print(f"\n The winner is {highest_bidder.title()} with a bid of ${highest_bid} (Bid{highest_bid_number})")
