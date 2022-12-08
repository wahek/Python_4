path_1 = 'equation.txt'
data_1 = open(path_1, 'r')
for line in data_1:
    equation = line[:-2].split('+')
my_equation = []
for item in equation:
    my_equation.append(item.split('*x**'))

path_2 = 'equation_2.txt'
data_2 = open(path_2, 'r')
for line in data_2:
    equation_2 = line[:-2].split('+')
my_equation_2 = []
for item in equation_2:
    my_equation_2.append(item.split('*x**'))


last_el_1 = my_equation.pop()
last_el_2 = my_equation_2.pop()
need_pars_1 = my_equation.pop()
need_pars_2 = my_equation_2.pop()

# print(my_equation)
# print(my_equation_2)
for i in need_pars_1:
    my_equation.append(i.split('*x'))
for i in need_pars_2:
    my_equation_2.append(i.split('*x'))
# second_el_1 = my_equation.pop()
# second_el_2 = my_equation_2.pop()


print(my_equation)
print(my_equation_2)
# dictionary = {}
# for item in my_equation:
#     for i in range(item):
#         if i == 1:
#             dictionary[int(item[i])] = item[i-1]
# print(dictionary)
my_equation.append(last_el_1)
my_equation_2.append(last_el_2)
print(my_equation)
print(my_equation_2)

# for item in my_equation:
#     for i in item:
#         i = int(i)
# for item in my_equation_2:
#     for i in item:
#         i = int(i)
