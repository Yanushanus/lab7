#б) Задача. Визначити наймолодшого працівника і надрукувати відомості про нього.
#Поля структури: Прізвище, Рік народження, Посада, Зарплатня, Освіта.
k={
    'О.В.':
    {'Surname':'Petrov','Year':1990,'Job':'Builder','Payment':6000,'Education':'PTU'},
    'С.Л.':
    {'Surname':'Garbuz','Year':1979,'Job':'Engineer','Payment':15000,'Education':'Politeh'},
    'К.Г.':
    {'Surname': 'Fedotov', 'Year': 2000, 'Job': 'Web codding', 'Payment':14000 ,'Education':'Donnu'},
    'Д.К.':
    {'Surname': 'Salomon', 'Year': 1989, 'Job': 'Sculptor', 'Payment':30000 ,'Education':'Art university'},
    'Л.А.':
    {'Surname': 'Parapa', 'Year': 1996, 'Job': 'Art director ', 'Payment': 20000,'Education':'Home'},
    'M.A.':
    {'Surname': 'Begemot', 'Year':1998 , 'Job': 'Singer', 'Payment': 1,'Education':'Street'},
    'K.B.':
    {'Surname': 'Kaban', 'Year': 1979, 'Job': 'Cooker', 'Payment': 16000,'Education':'Kitchen'}
}
year=0
for i in k.keys():
    if k[i]['Year']>year:
        year=k[i]['Year']
        print(f'{i}:{k[i]}')
