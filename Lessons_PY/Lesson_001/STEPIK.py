# # # # # ПРИВЕТСТВИЕ
# # # # # # # # # # x = input('Enter your name:')
# # # # # # # # # # print ("Hello", x)

# # # # # ВОЗВЕДЕНИЕ В КВАДРАТ
# # # # # # # # # a = int(input('Enter number:'))
# # # # # # # # # print(a * 2)

# # # # # ПЕРЕВОД ЧАСОВ В МИНУТЫ
# # # # # # # # # a = int(input('Enter hours:'))
# # # # # # # # # b = int(input('Enter minutes:'))
# # # # # # # # # print(a*60 + b)


# # # # # # # # # x = int(input())
# # # # # # # # # h = int(input())
# # # # # # # # # m = int(input())
# # # # # # # # # sum = x+h*60+m
# # # # # # # # # print(sum//60)
# # # # # # # # # print (sum%60)
# # # # # # # # # a = int(input())
# # # # # # # # # print(a>=10 and a<100)
# # # # # # # # a = True
# # # # # # # # b = False
# # # # # # # # print (a and b or not a and not b)
# # # # # # # # x = int(input('Введите первоечисло:'))
# # # # # # # # y = int(input('Введите второе число:'))
# # # # # # # # if y !=0:
# # # # # # # #     print(x/y)
# # # # # # # # else:
# # # # # # # #     print("Деление не возможно")
# # # # # # # #     y = int(input('Введите чиcло не равное нулю:'))
# # # # # # # #     if y ==0:
# # # # # # # #         print("Вы обосрались")
# # # # # # # #     else:
# # # # # # # #         print(x/y)
# # # # # # # A = int(input('Минимальное время сна в часах:'))
# # # # # # # B = int(input('Максимальное время сна в часах:'))
# # # # # # # H = int(input('Сколько спите в данный момент в часах:'))
# # # # # # # if H < A:
# # # # # # #     print('Недосып')
# # # # # # # elif H > B:
# # # # # # #     print('Пересып')
# # # # # # # elif H >= A or H <=B: 
# # # # # # #     print('Это нормально')
# # # # # # # i = int(input())
# # # # # # # if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
# # # # # # #     print("Високосный")
# # # # # # # else:
# # # # # # #     print('Обычный')
# # # # # # print('aboba\n\n\naboba')
# # # # # ##работа со строками##
# # # # # # a = 'lol balabol'
# # # # # # b = 'kek cheburek'
# # # # # # print(a,"\n" +b) 
# # # # # a = int(input())
# # # # # b = int(input())
# # # # # c = int(input())
# # # # # p = (a+b+c)/2
# # # # # S =(p*(p-a)*(p-b)*(p-c))**0.5
# # # # # print(S)
# # # # # x = int(input())
# # # # # A = -15<x<=12 or 14<x<17 or x >=19
# # # # # print(A)
# # # # # # # x = float(input())
# # # # # # # y = float(input())
# # # # # # # s = input()
# # # # # # # if s == ('*'):
# # # # # # #     print(x*y)
# # # # # # # if s == ('+'):
# # # # # # #     print(x+y)
# # # # # # # if s == ('-'):
# # # # # # #     print(x-y)
# # # # # # # elif s == '/':
# # # # # # #     if y!=0:
# # # # # # #         print(x/y)
# # # # # # #     else:
# # # # # # #         print('Деление на 0!')
# # # # # # # elif s == ('mod'):
# # # # # # #     if y!=0:
# # # # # # #         print(x%y)
# # # # # # #     else:
# # # # # # #         print('Деление на 0!')
# # # # # # # elif s == ('div'):
# # # # # # #     if y!=0:
# # # # # # #         print(x//y)
# # # # # # #     else:
# # # # # # #         print('Деление на 0!')
# # # # # # # if s == ('pow'):
# # # # # # #     print(x**y)
# # # # # # P = input()
# # # # # # if P == 'прямоугольник':
# # # # # #     a = float(input())
# # # # # #     b = float(input())
# # # # # #     print(a*b)
# # # # # # if P == 'треугольник':
# # # # # #     c = float(input())
# # # # # #     d = float(input())
# # # # # #     e = float(input())
# # # # # #     p = (c+d+e)/2
# # # # # #     s = (p*(p-c)*(p-d)*(p-e))**0.5
# # # # # #     print(s)
# # # # # # if P == 'круг':
# # # # # #     a = float(input())
# # # # # #     t = 3.14
# # # # # #     S = t*a**2
# # # # # #     print(S)

#Cортировка максимальное-минимальное-оставшееся(неверный вариант)
# # # # # a = int(input())
# # # # # b = int(input())
# # # # # c = int(input())
# # # # # max = a
# # # # # min = a
# # # # # if b > max:
# # # # #     max = b
# # # # # if b <= min:
# # # # #     min = b
# # # # # if c > max:
# # # # #     max = c
# # # # # if c <= min:
# # # # #     min = c
# # # # # non = max - min
# # # # # print(max, min, non,sep='\n')

# # #МИНИМАЛЬНОЕ,МАКСИМАЛЬНОЕ и ТРЕТЕЕ ЧИСЛО
# # # a, b, c = int(input()),int(input()),int(input())
# # # max = a
# # # min = a
# # # smax = a+b+c
# # # if b > max:
# # #     max = b
# # # if b <= min:
# # #     min = b
# # # if c > max:
# # #     max = c
# # # if c <= min:
# # #     min = c
# # # non =smax -(max + min)
# # # print(max, min, non,sep='\n')

# # # #СЧИТАЕМ ПРОГРАММИСТОВ
# # # # n = int(input())
# # # # b = n%10 #ПОСЛЕДНЯЯ ЦИФРА
# # # # c = (n%100)//10 #ВТОРАЯ ЦИФРА С КОНЦА
# # # # if n == 0 or c==1 or b == 0 or 5<= b<=9:
# # # #     print(n,'программистов')
# # # # elif 2<=b<=4:
# # # #     print(n,'программиста')
# # # # elif n == 1 or b == 1:
# # # #     print(n,'программист')

# #Рассчет счастливого билета
# a,b,c,d,e,f = str (input())
# if int(a)+int(b)+int(c) == int(d)+int(e)+int(f):
#     print("Счастливый")
# else:
#     print("Обычный")
