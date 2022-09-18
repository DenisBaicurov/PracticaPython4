#3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Пример:
#Волков Андрей 5
#Наталья Тарасова 5
#Фредди Меркури 3
#Денис Байцуров 4

#Программа выдаст:
#ВОЛКОВ АНДРЕЙ 5
#НАТАЛЬЯ ТАРАСОВА 5
#Фредди Меркури 3
#Денис Байцуров 4

import os 
os.system("cls")



def File_Change():
    file=open("file.txt","r+",encoding="UTF-8")
    list_num=[]
    lines=file.readlines()
    for line in lines:
        list_num.append(line.strip())
    file.close()    
    return list_num    

def Student_mark(list_number:list):
  file=open("file.txt","r+",encoding="UTF-8")  
  file.seek(0)
  print (list_number)
  for i in range(len(list_number)):

    if int(str(list_number[i])[len(list_number[i])-1])>4:
        list_number[i]=str(list_number[i]).upper()
    file.write(str(list_number[i]+'\n'))
  file.close()
Student_mark(File_Change())       
