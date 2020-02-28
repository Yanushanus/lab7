#Дана непорожня послідовність слів з малих українських літер; між сусідніми
#словами - кома, за останнім словом - крапка. Вивести на екран в алфавітному порядку всі
#глухі приголосні букви, що входять в кожне непарне слово і не входять хоча б в одне
#парне слово.
while True:
    while True:
        try:
            a = input('Введіть ваш текст').split(',')
            s = ['п', 'х', 'к', 'т', 'ц', 'ч', 'ш', 'щ']
            j = []
            count = 0
            break
        except ValueError:
            if a in range(0,100):
                print('Тільки текст')

    for i in a:
        if count % 2 == 0:
            for k in i:
                for g in s:
                    if g in k:
                        j.append(g)
        else:
            continue
    count += 1
    q = set(j)
    print(sorted(q))
    answer = input("Ще раз?Якщо так,натисніть 1,якщо ні-щось інше")
    if answer == '1':
        continue
    else:
        break
