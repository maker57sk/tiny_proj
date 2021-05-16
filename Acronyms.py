text = str(input('Enter Your Text: ')).split()

a = " "

for i in text:
    a = a + str(i[0].upper())
print(a)