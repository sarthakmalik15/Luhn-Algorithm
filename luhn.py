
#LuhnAlgorithm
card = str(input('enter your credit card number: '))

cc = list(card)
even = []
odd = []


for j in range(1, len(card), 2):
    odd.append(int(cc[j]))

for k in range(0, len(card), 2):
    even.append(int(cc[k]))

for z in range(len(even)):
    even[z] = even[z]*2

for q in range(len(even)):
    if even[q]//10 != 0:
        y = even[q] % 10
        x = even[q] // 10
        even.append(y)
        even.append(x)
        even.pop(q)

sum = 0
mega = odd+even

for m in range(0, len(mega)):
    sum = sum + mega[m]

print(odd)
print(even)

if sum % 10 == 0:
    print('valid card number')
    if cc[0] == 3:
        print('American Express')
    elif cc[0] == 5:
        print('Mastercard')
    else:
        print('Visa')
else:
    print('invalid card number')

