print("Número Invertido")
print("--"*17)

num = (input("Digite o número: "))
numstr = str(num)
tm = len(numstr)
strfim = ''

for i in range(0, tm):
	tm -= 1
	strfim += numstr[tm]
print("--"*17)

print("O número invertido de {} é {}".format(num, strfim))