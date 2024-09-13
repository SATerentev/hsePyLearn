spb_price = 50000 # 50k
msc_price = 80000 # 80k
ekb_price = 40000 # 40k
total = 0
result = ''

city = input('Введите город:')
count = int(input('Введите количество туристов: '))

if city == 'spb':
    total = spb_price * count
elif city == 'msc':
    total = msc_price * count
elif city == 'ekb':
    total = ekb_price * count
else:
    print('Некорректный ввод города')
    exit()


    
print('Сумма поездки - ' + result + ', приятного отдыха.')