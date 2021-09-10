'''
Casino Royal 2.0

Тренировка ООП
Модуль рандом
Словари
Взаимодействие с пользователем
Конвертирование данных и перезапись в словарь
Мини - проверка на валидность, вводимых данных пользователем
Реализована игра "Угадайка" с выбором ставок на победу (Имеется 3 вида ставок, на каждую отдельное условие)
Реализованы операции конкантенации между "Кошельками" пользователя и программы
Тренировка циклов While, For
break, continue
Операции сравнения
Вложенные условия

'''
import random

print('''Правила игры!\n\nВводите корректные данные в начале игры.\nВыберайте ставку, каждая ставка имеет отдельное условие.\n
2x - Угадать число от 1 до 5, имеется одна попытка.\n4х - Угадать число от 1 до 100, имеется 7 попыток,\nпрограмма подсказывает близость к правильному ответу.
6х - Угадать число от 1 до 10, имеется одна попытка.''')

dict_info_purse = {}
dict_casino_purse = {}

class Game:

    def bat_push(self):

        print('Выберите ставку')
        choose_bat = int(input('x2 - 2, x4 - 4, x6 - 6: '))
        print('На какую сумму хотите сыграть?')
        game_sum = float(input('Введите сумму: '))
        
        while game_sum >= dict_info_purse['Balance']:
            print('Ваш баланс:', round(dict_info_purse['Balance'], 2))
            game_sum = float(input('Введите сумму: '))

        dict_info_purse['Balance'] -= game_sum
        return choose_bat, game_sum
    
    def rolling(self, bat_push, game_sum):
        
        if bat_push == 2:
            
            if dict_casino_purse['CountWin'] % 2 == 0:

                num = random.randint(1,5)
                print('Я загадал число от 1 до 5')
                print('Угадайте его с первой попытки!')
                player_choose = int(input('Ваш выбор: '))
                
                if num != player_choose:
                    print('Ставка не сыграла!')
                    return False
                else:
                    print('Ставка сыграла!')
                    return True
            else:
                print('Я загадал число от 1 до 5')
                print('Угадайте его с первой попытки!')
                player_choose = int(input('Ваш выбор: '))
                print('Ставка не сыграла!')
                return False
            
        elif bat_push == 4:
            
            if dict_casino_purse['CountWin'] % 2 == 0:
                num = random.randint(1, 100)
                print('Я загадал число от 1 до 100')
                print('Угадайте его. У вас есть 7 попыток')
                num1 = 0
                for i in range(7):
                    num1 = int(input('Ваш выбор: '))
                    if num > num1:
                        print('Число больше')
                        continue
                    elif num < num1:
                        print('Число меньше')
                        continue
                    elif num == num1:
                        print('Вы угадали число!')
                        break
                if num1 == num:
                    print('Ставка сыграла!')
                    return True
                else:
                    print('Ставка не сыграла!')
                    return False
            else:
                num = random.randint(1, 100)
                print('Я загадал число от 1 до 100')
                print('Угадайте его. У вас есть 7 попыток')
                num1 = 0
                for i in range(7):
                    num1 = int(input('Ваш выбор: '))
                    if num > num1:
                        print('Число больше')
                        continue
                    elif num < num1:
                        print('Число меньше')
                        continue
                    elif num == num1:
                        print('Вы угадали число')
                        break
                if num == num1:
                    print('Но так как вы в казино ставка не сыграла! :-)')
                    return False
                else:
                    print('Ставка не сыграла!')
                    return False
                    
        if bat_push == 6:
            
            if dict_casino_purse['CountWin'] % 2 == 0:
                num = num = random.randint(1, 10)
                print('Я загадал число от 1 до 10')
                print('Угадайте его с первой попытки!')
                player_choose = int(input('Ваш выбор: '))
                if num != player_choose:
                    print('Ставка не сыграла!')
                    return False
                else:
                    print('Ставка сыграла!')
                    return True

            else:
                print('Я загадал число от 1 до 5')
                print('Угадайте его с первой попытки!')
                player_choose = int(input('Ваш выбор: '))
                print('Ставка не сыграла!')
                return False   
        

class MyPurse:
 
    USD = 73.21
    EUR = 81.74
    
    def info(self):

        dict_info_purse['Name'] = input('Ваше имя: ')
        dict_info_purse['email'] = input('Ваш e-mail: ')
        dict_info_purse['Phone'] = input('Ваш телефон: ')
        dict_info_purse['Valuta'] = int(input('Денежная валюта: RUB - 1, USD - 2, EUR - 3: '))
        dict_info_purse['Balance'] = int(input('Сколько денег хотите внести? '))

    def convert_val(self, summa, val):
        
        if val == 1:
            money = summa
            return round(money, 2)
        elif val == 2:
            money = MyPurse.USD * summa
            dict_info_purse['Balance'] = money
            return round(money, 2)
        elif val == 3:
            money = MyPurse.EUR * summa
            dict_info_purse['Balance'] = money
            return round(money, 2)

    def add_money_purse(self, add_money):
        if add_money == 1:

            print('Валюта пополнения. RUB - 1, USD - 2, EUR - 3')
            val_add = int(input('Ваш ответ: '))
            money_sum = float(input('Сумма пополнения: '))

            if val_add == 1:
                dict_info_purse['Balance'] += money_sum
            elif val_add == 2:
                dict_info_purse['Balance'] += MyPurse.USD * money_sum
            elif val_add == 3:
                dict_info_purse['Balance'] += MyPurse.EUR * money_sum
            
            print('Теперь ваш баланс равен: ', round(dict_info_purse['Balance'], 2))

        elif add_money == 2:
            print(':-)')
        
        
class Validator:

    email = ['@', '.ru', '.com']

    def email_validator(self, valid):
        cnt = 0
        for i in Validator.email:
            if i in valid:
                cnt += 1
        if cnt == 2:
            return True
        elif cnt < 2 or cnt > 2:
            return False

    def phone_validator(self, valid):
        if valid[0] == '+' and valid[1] == '7' and len(valid) == 12:
            cnt = 0
            for i in valid:
                if i.isdigit():
                    cnt += 1
            if cnt == 11:
                return True
            else:
                return False
        elif valid[0] == '8' and len(valid) == 11:
            for i in valid:
                if i.isdigit():
                    return True
                else:
                    return False
        else:
            return False

    def valuta_validator(self, valid):
        if valid == 1 or valid == 2 or valid == 3:
            return True
        else:
            return False

    def balance_validator(self, valid):
        if valid > 0:
            return True
        else:
            return False
    
class CasinoPurse:

    dict_casino_purse['Balance'] = 5143242
    dict_casino_purse['CountWin'] = 0

    def oper_minus(self, choose_bat, game_sum):
        dict_casino_purse['CountWin'] += 1
        cash = game_sum * choose_bat
        dict_info_purse['Balance'] = dict_info_purse['Balance'] + cash
        dict_casino_purse['Balance'] = dict_casino_purse['Balance'] - game_sum

    def oper_plus(self, game_sum):
        dict_casino_purse['CountWin'] += 1
        cash = game_sum
        dict_casino_purse['Balance'] = dict_casino_purse['Balance'] + cash


print('Ну чтож приступим!\n')

id_1 = MyPurse()
valid = Validator()

id_1.info()

valid_flag_email = valid.email_validator(dict_info_purse['email'])
while valid_flag_email != True:
    print('Вы ввели некорректный e-mail')
    print('Пожалуста повторите попытку')
    dict_info_purse['email'] = input('Введите корректный e-mail: ')
    valid_flag_email = valid.email_validator(dict_info_purse['email'])
    
valid_flag_phone = valid.phone_validator(dict_info_purse['Phone'])
while valid_flag_phone != True:
    print('Вы ввели некорректный телефонный номер')
    print('Пожалуста повторите попытку')
    dict_info_purse['Phone'] = input('Введите корректный телефон: ')
    valid_flag_phone = valid.phone_validator(dict_info_purse['Phone'])
    
valid_flag_valuta = valid.valuta_validator(dict_info_purse['Valuta'])
while valid_flag_valuta != True:
    print('Вы неверно указали значение валюты')
    print('Введите корректное значение валюты')
    dict_info_purse['Valuta'] = int(input('Денежная валюта: RUB - 1, USD - 2, EUR - 3: '))
    valid_flag_valuta = valid.valuta_validator(dict_info_purse['Valuta'])
    
valid_flag_balance = valid.balance_validator(dict_info_purse['Balance'])
while valid_flag_balance != True:
    print('Вы ввели некорректный баланс')
    print('Значение не может быть равно нулю или меньше нуля')
    print('Введите корректное значение')
    dict_info_purse['Balance'] = int(input('Введите корректный баланс: '))
    valid_flag_balance = valid.balance_validator(dict_info_purse['Balance'])
                                     
convert_RUB = id_1.convert_val(dict_info_purse['Balance'], dict_info_purse['Valuta'])

print('Ваши деньги переведены в RUB.')
print('Ваш баланс: ', convert_RUB, 'RUB')

quest = int(input('Хотите начать игру? Да - 1, Нет - 2: '))
while quest != 2:
    
    game = Game()

    choose_bat, game_sum = game.bat_push()
    flag = game.rolling(choose_bat, game_sum)

    bo = CasinoPurse()

    if flag == True:
        bo.oper_minus(choose_bat, game_sum)
    else:
        bo.oper_plus(game_sum)

    print('Ваш баланс:', round(dict_info_purse['Balance'], 2))
    print('Баланс казино: ', round(dict_casino_purse['Balance'], 2))
    print('Хотите сыграть еще раз? Да - 1, Нет - 2')
    
    quest = int(input('Ваш ответ: '))

    if quest == 2:
        continue
    elif quest == 1:
        print('Хотите пополнить баланс? Да - 1, Нет - 2')
        add_money = int(input('Ваш ответ: '))   
        id_1.add_money_purse(add_money)
        
    
print('Всего хорошего!')




    

