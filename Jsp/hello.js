/*
var x
var  mycars = new  Array()
mycars[0] = "北京现代"
mycars[1] = "保时捷"
mycars[2] = "法拉利"
function sumnum(a,b)
{
  return(a+b)
}

for (x in  mycars)
{
    document.write("<h1>")

    document.write(mycars[x])

    document.write("</h1>")
}
document.write(sumnum(10,20))

var person = {
    name: 'Bob',
    age: 20,
    tags: ['js', 'web', 'mobile'],
    city: 'Beijing',
    hasCar: true,
    zipcode: null
};
document.write("\t"+person.tags)
var x = 100;
console.log(person)
console.log(`多行
字符串
测试`)
var  new_string=`winnerloo   bundcredit.com baidu.com
sohu.com
sougou.com
tongdun.com`
document.write(new_string.toLowerCase())
document.write(new_string.toLocaleUpperCase())
document.write(new_string.indexOf('bundcredit.com')+"\n")
document.write("\n"+ new_string.length)
var  xiaoming={
   name:"xiaoming",
    age:"20",
    work:"DBA"
}

xiaoming.address="南京东路"
document.write(xiaoming.work)
    */
'use strict';

var height = parseFloat(prompt('请输入身高(m):'));
var weight = parseFloat(prompt('请输入体重(kg):'));
var bm1=weight/(height*height)
if (bm1 < 18.5){
    document.write("过轻")

}else  if (bm1 >= 18.5 && bm1<25)
{
    document.write("正常")
}else  if (bm1 >= 25 && bm1< 28)
{
    document.write("过重")
} else  if (bm1 >= 28 && bm1<32)
{
    document.write("肥胖")
}else
{
   document.write("严重肥胖")
}