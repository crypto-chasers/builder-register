# majiangjiang

1. *微信名或昵称：* majiangjiang001
2. *discord的ID：* Jack Ma#9573
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发自动化和数据分析的小工具，精通Python、Js，4年+经验；熟练使用solidity开发以太坊智能合约，2年经验；现就职于区块链公司，研究开发套利程序。
4. *每周能花在业余项目的时间：* 20小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 做过借贷项目、nft项目、现维护两条公司私有链。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Python
import math
from functools import reduce

s = 0
for i in range(101):
    s += math.pow(i, 3) - math.pow(i, 1/3)
print(s)

def sum(x, y):
    return x + math.pow(y, 3) - math.pow(y, 1/3)

print(reduce(sum, range(1,101)))
```
