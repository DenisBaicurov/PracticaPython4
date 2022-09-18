#4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
#Сдвиг часто называют ключом шифрования.
#Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает 
import os 
os.system("cls")

eng_alph='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
rus_alph='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def Encryption():
    get_message=input('Введите сообщение,которое вы хотите зашифровать').upper()
    while True:
     direction=input('Введите 0,если хотите направление сдвига вправо и 1, если хотите направление сдвига влево '+'\n')
     if not (direction=='0' or direction=='1'):
         print('Вы не ввели направление сдвига, повторите ввод')
     else:
        break    
    while True:
     get_number = input("Введите шаг сдвига: ")
     if not get_number.isnumeric():
        print("Вы неправильно ввели число. Попробуйте снова: ")
     else:
        break
    number=int(get_number)
    if direction=='0':
        k=1
    elif direction=='1':
        k=-1    
    string_shifr=''
    for s in get_message:
      if s.isalpha() and s in rus_alph:
        get_index=rus_alph.find(s)+k*number   
        if get_index>63:
            get_index-=64
            string_shifr+=rus_alph[get_index]
        else:
            string_shifr+=rus_alph[get_index]
      elif  s.isalpha() and s in eng_alph:
        get_index=eng_alph.find(s)+k*number 
        if get_index>51:
            get_index-=52
            string_shifr+=eng_alph[get_index] 
        else:
            string_shifr+=eng_alph[get_index]
      else:
        string_shifr+=s

    print(string_shifr)
    return string_shifr                     

Encryption()