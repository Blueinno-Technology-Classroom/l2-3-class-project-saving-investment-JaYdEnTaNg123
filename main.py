curent_balance = 0
intrest_rate = 0.065
intrest = 0
deposit = 100
new_balance = 1000

for i in range(25):
    curent_balance = new_balance
    intrest = intrest_rate * curent_balance
    new_balance += intrest
    print(f'{i+1:02}: current_balance: {curent_balance:.2f}, interest: {intrest:.2f}, deposit: {deposit}, new balance: {new_balance:.2f}')
    if i > 0:
        new_balance += deposit