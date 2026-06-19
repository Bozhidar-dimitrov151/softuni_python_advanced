from collections import deque

money = list(map(int, input().split()))
prices = deque(map(int, input().split()))

count = 0

while money and prices:
    current_money = money[-1]
    current_price = prices[0]

    if current_money == current_price:
        money.pop()
        prices.popleft()
        count += 1
    elif current_money > current_price:
        change = current_money - current_price
        money.pop()
        if money:
            money[-1] += change
        prices.popleft()
        count += 1
    else:
        money.pop()
        prices.popleft()


if count >= 4:
    print(f"Gluttony of the day! Henry ate {count} foods.")
elif count == 0:
    print("Henry remained hungry. He will try next weekend again.")
else:
    print(f"Henry ate: {count} food{'s' if count != 1 else ''}.")