CREATE  table  if  not EXISTS ipinfo(
id  int  auto_increment PRIMARY KEY,
ip_address  VARCHAR(15) ,
country VARCHAR(10)  ,
countryid VARCHAR(4) ,
area VARCHAR(4)  ,
region VARCHAR(10)     ,
region_id VARCHAR(10)     ,
city  VARCHAR(10)    ,
city_id  VARCHAR(10)  ,
isp  VARCHAR(10)   ,
isp_id  VARCHAR(10)


);