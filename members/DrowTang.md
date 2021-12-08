# script-money

1. *微信名或昵称：* script-money
2. *discord的ID：* script-money#7183
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发自动化和数据分析的小工具，精通Python，4年+经验；熟练使用Unity3D开发AR类应用，会各种2D、3D设计软件创造素材，5年+经验；熟练使用TypeScript全栈开发dapp，1年经验。
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 写过一些技术文章，开发过基于Selenium+ZMQ的网页自动化工具。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```C#
using System;
using System.Linq;

var sum = Enumerable.Range(1, 100).Select(i => Math.Pow((double)i, 3) - Math.Cbrt(i)).Sum();
Console.WriteLine(sum); // 25502149.836096782
```

# DrowTang

1、wechat：
17702724443
2、discord：
DrowTx#9164
3、擅长领域：
本职工作是嵌入式开发工程师，从事通信交换机数据中心类设备的固件开发工作，包括linux、单片机等底层的固件开发，对通信协议相关比较了解，精通C，用过verilog写FPGA，都是硬件相关的底层固件开发，四年工作经验。
因为没有从事过上层应用开发，以前只用python写过简单的设备自动化测试脚本，现在从新开始使用python开始运维自动化爬虫相关学习。
4、时间不定，可以挤出20小时以上。（开发项目不忙的话）（只要能赚麻，时间可以挤，目前已经想办法远程自家电脑自家服务器。）
5、最近刚误入币圈，合约亏麻，被盗若干。在弄自动跟单的bot，在调，不稳定（易爆仓），暂无稳定盈利方式。（量化套利在研究。想学习点高端的链上科学家姿势，例如mev bot。或者链游自动化脚本，或者薅羊毛之类的，任何能套利的都可以学。）

6：
#!/usr/bin/python3

import math

'''
For a simple calc test.
'''

i = 1
j = 0

while i <= 100:
    j = j + i**3 + pow(i, 1/3)
    #print ('%f %f'%(i,j))
    i = i +1

print('Result is %f' %j)