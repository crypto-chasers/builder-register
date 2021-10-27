# script-money

1. *微信名或昵称：* YANG
2. *discord的ID：* JerryYang#5303
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发自动化和数据分析的小工具，精通Python，4年+经验；
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 写过一些技术文章，开发过基于Selenium+ZMQ的网页自动化工具。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Python
import math


def cal_sum():
    _sum = 0
    for i in range(1, 101):
        x = math.pow(i, 3) - math.pow(float(i), 1/3)
        _sum += x
    return _sum 
# 25502149.836096782
```
