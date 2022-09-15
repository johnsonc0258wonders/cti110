budget = "2500"
gas = "295"
food = "350"
accomodation = "240"
location = "Tokyo"
remaining = "1615"
print('This program calculates and displays travel expenses on how much money will be spent.')
print()
print('Enter Budget:', budget)
print()
print('Location:', location)
print()
print('How much do you think you will spend on gas?:', gas)
print()
print('How much do you need for food?:', food)
print()
print('How much will you need for an accomodation?:', accomodation)
print()
print('----------Travel Expenses----------')
print('Location:', "{0:^30}".format(location))
print('Initial Budget:', "{0:^20}".format("$" + (budget) + ".0"))
print('Fuel:', "{0:^39}".format("$" + (gas) + ".0"))
print('Food:', "{0:^39}".format("$" + (food) + ".0"))
print('Accomodation:', "{0:^22}".format("$" + (accomodation) + ".0"))
print('-----------------------------------')
print()
print('Remaining Balance:', "{0:^13}".format("$" + (remaining) + ".0"))
