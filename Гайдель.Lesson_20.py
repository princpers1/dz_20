# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Пользователь ничего не вводит,
# все 4 вызова функции с соответствующим типом данных должны быть прописаны в коде.(функции2)
def kortedg(x):
    if  type(x) == int:
        x = str(x)
        nechet = 0
        for i in x:
            i = int(i)
            if i % 2 != 0:
                nechet += 1
        print('Является числом!В нем нечетных чисел: ', nechet)
    elif type(x)==list:
        chisl,bykv=0,0
        for i in x:
            if type(i) ==str:
                for j in i:
                    if j.isalpha():
                        bykv+=1
                    elif j.isdigit():
                        chisl+=1
            elif type(i)==int:
                chisl+=1
        print('Является списком!В нём букв: ', bykv, 'и чисел: ', chisl)
    elif type(x)==tuple:
        slova=[]
        for i in x:
            if type(i)==str and i.isalpha():
                slova.append(i)
                slova.append(len(i))
        print('Является картежем!В ней слова  с длинной: ', *slova)
    elif type(x) == str:
        bukv=0
        for i in x:
            if i.isalpha():
                bukv+=1
        print('Является строкой!В ней букв: ', bukv)


f = (10,2,'lol')
d =[1,2,5,'prosto','lol']
r = 'Привет меня зовут Влад'
e = 123456

kortedg(f)
kortedg(d)
kortedg(r)
kortedg(e)