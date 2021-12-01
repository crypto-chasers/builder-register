'''
Author: isanwenyu@163.com
Date: 2021-12-01 23:29:40
LastEditors: isanwenyu
LastEditTime: 2021-12-02 00:09:39
Description: 
'''
sum=0
for i in range(1,101):
    sum += (i**3-pow(i,1.0/3.0))
print(sum)  #25502149.836096782