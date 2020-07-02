temps = [221, 234, 340, 230]

#basic comprehension
new_temps = [temp/10 for temp in temps]

print(new_temps)

#with conditionals threshold being 240
new_temps = [temp/10 for temp in temps if temp > 240 and isinstance(temp, (int, float))]

print(new_temps)

#Define a function that takes a parameter a list that contains
#both numbers and strings and returns the same list but with zeroes
#instead of strings

def foo(lst):
    return [i if isinstance(i, (int, float)) else 0 for i in lst]

#quick test
temperatures = foo([99, 'no data', 95, 94, 'no data'])
print(temperatures)

#force a list of str to float 
def sum_foo(lst):
    return sum([float(i) for i in lst])

#quick test
temper = sum_foo(['1.2', '1.3', '5.55'])
print(temper)