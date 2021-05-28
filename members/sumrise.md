# sumrise

1. *微信名或昵称：* sumrise
2. *discord的ID：* sumrise#5561
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发各种自动化，偷懒工具。熟悉python、js、java。熟悉合约，喜欢hack，研究黑客
4. *每周能花在业余项目的时间：* 24小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 会搞过产品，没写过文章，只会自己一个人写程序，默默撸毛
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```python
import math
from sympy import *

sum = 0.0
for i in range(1, 101):
    sum += math.pow(float(i), 3.0) - cbrt(float(i))
print(sum)

```
