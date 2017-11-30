#!/usr/bin/env python
#-*-coding:utf-8-*-
with   open("new_date","r",encoding="utf-8") as file:
    Str=file.read()
    #print(type(Str))
    NEW=Str.replace("上海云信留客信息科技","外滩海纳互联网金融服务（上海）有限公司")
    ne3=NEW.replace("杭州同盾科技","博盾习言")
    new2=ne3.replace("外滩海纳互联网金融服务（上海）有限公司", "阿里巴巴")
    #print(new2.count("杭州同盾科技"))


    with open("1+new.doc","w",encoding="utf-8") as newfile:
        for eachline  in new2:
            newfile.writelines(eachline)
