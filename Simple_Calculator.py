print('Welcome to calculator, type button')
fn = int(input('First number: '))
sn = int(input('Second number: '))
nol = int(input('1+,2-,3*,4/: '))
if nol == 1:
    ress = fn + sn
    print('Sum: ' + str(ress))
elif nol == 2:
    ress = fn - sn
    print('Sub: ' + str(ress))
elif nol == 3:
    ress = fn * sn
    print('Mul: ' + str(ress))
elif nol == 4:
    ress = fn / sn
    print('Div: ' + str(ress))
elif nol != int(nol):
    print('You need to input integer type of symbol')
else:
    print('You need to input number between 1 to 4')

