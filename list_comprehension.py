temps = [221, 234, 340, 230]

#basic comprehension
new_temps = [temp/10 for temp in temps]

print(new_temps)

#with conditionals threshold being 240
new_temps = [temp/10 for temp in temps if temp > 240 and isinstance(temp, (int, float))]

print(new_temps)