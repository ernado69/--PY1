money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

rost = 0
month = 0

delta = salary - spend
while money_capital + delta >= spend:
    money_capital += delta
    rost = increase * spend
    spend += rost

    month += 1
 # количество месяцев, которое можно прожить
print(month)
