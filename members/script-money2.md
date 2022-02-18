# script-money

1. *微信名或昵称：* CNF10B280728
2. *discord的ID：* 
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发自动化、爬虫、图像识别脚本，精通Python，0.5年经验；
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 使用selenium开发过推特全功能自动更新（格式化发推，点赞，基于情绪的自动评论，关注）脚本，多账号水军刷评论脚本，监控推特币圈大V更新并实时自动评论的脚本，批量提取内容并@大v发推脚本；gate.io的抢新币开盘脚本+官网公告爬取；简单网页/站的制作/改动/部署；使用币安交易数据的双指标（CCI+KDJ）量化脚本；starrynift链游的图像二值化的自动抢土地脚本；能看懂智能合约；等值空投智能合约；爱西欧自动兑换合约；多种类型的发币智能合约；网站部署；熟悉linux系统；多个土狗工具；..
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Python

import math
import sympy

total = float()
for i in range(1, 100):
    # total_each = i ** 3 - pow(i, sympy.S(1)/3)
    total_each = i ** 3 - math.pow(i, 1.0 / 3)
    print(total_each)
    total += total_each
print(total)

```
