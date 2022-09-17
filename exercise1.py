
#1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#N = 20 -> [2,5]
#N = 30 -> [2, 3, 5]
import os 
os.system("cls")

def GetInput():
    while True:
     input_data = input("Введите число: ")
     if not input_data.isnumeric():
        print("Вы неправильно ввели число. Попробуйте снова: ")
     else:
        break
    return  int(input_data)

    # создаём список множетелей числа
def   Multiplier_List(num):  
    list_num=[]
    for i in range(2,num+1):
        if (num%i==0):list_num.append(i)
    return list_num

def  List_of_Prime_Factors(list_num:list) :

  list_simple=[]
  for i in list_num:
    fact=True
    for j in range(2,i):
        if (i% j==0):
            fact=False
    if fact==True :
        list_simple.append(i)

  print (f'Список простых множеств {list_simple}')    
  return list_simple             

List_of_Prime_Factors(Multiplier_List(GetInput()))
