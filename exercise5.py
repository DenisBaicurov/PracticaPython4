#5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
#файл первый:
#AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
#файл второй:
#сжатый текст.

from itertools import count


data_file='AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
file1=open("file1.txt","w")
file2=open("file2.txt","w")

def compression(data):
    enicoding=''
    prev_char=''
    count=''
    if not data:
        return ''
    for i in data:
        if i!=prev_char:
            enicoding+=str(count)+prev_char 
            count=1
            prev_char=i
        else:
            count+=1
    else:
        enicoding+=str(count)+prev_char
        return enicoding

def recovery(data):
    decode=''
    count=''
    for  i in data:
       if i.isdigit():
            count+=i
       else:
        decode+=i*int(count)
        count=''
    return decode

file1.write(recovery(compression(data_file)))
file2.write(compression(data_file)) 
file1.close()
file2.close()       




