from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_milk = deque(int(x) for x in input().split(', '))
milkshakes_made = 0
enough_milkshakes = False

while chocolates and cups_milk:
    current_chocolate = chocolates.pop()
    current_milk = cups_milk.popleft()
    if current_chocolate <= 0:
        if current_milk > 0:
            cups_milk.appendleft(current_milk)
            continue
        else:
            continue
    if current_milk <= 0:
        if current_chocolate > 0:
            chocolates.append(current_chocolate)
            continue
        else:
            continue
    if current_chocolate == current_milk:
        milkshakes_made += 1
        if milkshakes_made == 5:
            enough_milkshakes = True
            print("Great! You made all the chocolate milkshakes needed!")
            break
    else:
        current_chocolate -= 5
        if current_chocolate > 0:
            chocolates.append(current_chocolate)
        cups_milk.append(current_milk)
else:
    print("Not enough milkshakes.")

if chocolates:
    news_str = ', '.join(str(x) for x in chocolates)
    print(f"Chocolate: {news_str}")
else:
    print("Chocolate: empty")
if cups_milk:
    news_str = ', '.join(str(x) for x in cups_milk)
    print(f"Milk: {news_str}")
else:
    print("Milk: empty")