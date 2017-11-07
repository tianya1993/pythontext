#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
number_tuple=(1,3,5,7,9)
string_tuple=("MySQL","Cassandra","Redis","MongoDB")
mixed_tuple=(3,15,"java","database")
seconed_num=number_tuple[1]
third_string=string_tuple[2]
fourth_mix=mixed_tuple[3]
print("seconed_num:{0}\nthird_string:{1}\nfourth_mix:{2}".format(seconed_num,third_string,fourth_mix))
print("number_list before:"+ str(number_tuple))
#number_tuple[1]=30
del  number_tuple
for  i  in  string_tuple:
    print(i)
#print("number_list after:" + str(number_tuple))
"""
"""
phone_book={"李明":"1383099133",
"咨询电话1":"010-63218422",
"咨询电话2":"010-63218423",
"咨询电话3":"010-63256488"
            }
print(phone_book)
for  key,value  in  phone_book.items():
    print(key)
    print("phone_book_key:{0},phone_book_value:{1}".format(key,value))

user_list=["教育学","文学","经济学","法学","历史学","理学","工学","管理学","艺术学"]
user_dict={}
for  index,username  in  enumerate(user_list):
    print("subeject_id:{0},subeject_user:{1}".format(str(index),username))
with open("pythonfile.txt", "r", encoding="utf8") as  filename:
    print(str(filename.readlines())
"""
list=["教育学","文学","经济学","法学","历史学","理学","工学","管理学","艺术学"]
def repeat_str(s,times=1):
    repeat_strs=s * times
    return  repeat_strs
strre=repeat_str(list,2)

print(type(strre))

def print_paras(fpara,*nums,**words):
    print("fpara:"+str(fpara))
    print("numbers:" + str(nums))
    print("words:" + str(words))
print_paras(199,1,3,4,5,6,kword="linux",subect="docker")print random.randrange(1,10)mport

print (random.randrange(1,10))