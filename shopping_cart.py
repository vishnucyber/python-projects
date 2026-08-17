#Shopping cart program
foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you like(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of the item: "))
        foods.append(food)
        prices.append(price)
        
        
print("-----Your Cart-----")

for food in foods:
        print(f"{food}")

for price in prices:
        total += price

print(f"Total = ${total}")