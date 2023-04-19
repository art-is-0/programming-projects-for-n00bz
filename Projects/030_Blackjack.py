import random

st = "     "
n = 2
numbers = [' 2',' 3', ' 4',' 5', ' 6', ' 7', ' 8', ' 9', '10', ' J', ' Q', ' K', ' A']
symbols = ['♡','♣','♢','♠']
for r in range(2):
    st = "     "

    for col in range(n):
        st = st + "______ "
    print(st)

    st = "     "
    for col in range(n):
        st += "|    | "
    print(st)

    st = "     "
    for col in range(n):
        st += "|{}  | ".format(numbers[random.randint(0,len(numbers)-1)])
    print(st)

    st = "     "
    for col in range(n):
        st += "|  {} | ".format(symbols[random.randint(0,len(symbols)-1)])
    print(st)

    st = "     "
    for col in range(n):
        st += "|____| "
    print(st)
    print()
