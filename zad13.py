ocena = int(input('podaj ocenę\n'))

test = int(input('podaj wynik testu kompetencji\n'))

if ocena >= 1 and ocena <= 6 and test >= 0 and test <= 100:
    if ocena >= 5 or test > 90:
        print('zaawansowana')
    else:
        print('podstawa')
else:
    print('błędne dane')