number_usernames = int(input())

username = []

for _ in range(number_usernames):
    name = input()
    if name in username:
        continue
    else:
        username.append(name)

for user in username:
    print(user)