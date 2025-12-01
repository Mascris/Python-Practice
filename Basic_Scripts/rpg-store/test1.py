def buy_items():
    cart = input("enter the name of the items you want to buy: \n")
    amount = int(input("enter how many piece you wish to buy: \n"))

    for item, details in store.items():
        if item == cart:
            total_price = store[cart]["price"] * amount
            if details["stock"] >= amount:
                if details["price"]<= player["coins"]:
                    player["coins"] -= total_price
                    print(f"Nice! You just bought {amount} {cart}(s)! 🛒")
                    print(f"Pleasure doing business! You’ve got {player['coins']} coins left in your pouch. 💼")
                    with open(player_path, "w") as f:
                        json.dump(player, f, indent=4)
                    break
                else:
                    print("you dont have enought Money")
                    break
            else:
                print("the amount you want is impossible")
                break
    else:
        print("the item is inValid")

    return

