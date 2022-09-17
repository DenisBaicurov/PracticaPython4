#2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
#[1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]
import os
import random 
os.system("cls")
def Get_Unique_Sequence():
   # Создадим список целых чисел от 0 до 10 . Количество элементов в списке будет от 5 до 10
   get_length_list=random.randint(5,10)
   get_list=[]
   for i in range(0,get_length_list +1):
      get_list.append(random.randint(0,10))
  # получаем уникальный список из первоначального

   unique_list=[]
   for i in get_list:
     if i not in unique_list:
        unique_list.append(i) 
   print(f'Первоначальный список был {get_list}')      
   print(f'Получившийся список будет{unique_list} ')      
Get_Unique_Sequence()