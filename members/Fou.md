# Fou

1. *微信名或昵称：* Chainges
2. *discord的ID：* Fou | SoulMade#2216
3. *擅长的建设领域、语言或工具、熟练度：* 5年大数据从业经验，包括数据库开发维护，云端架构设计，ETL工作流等，AWS认证架构师，约1年Flow/Cadence开发经验，也从事过联盟链开发； Java, Scala, Python, Cadence, JavaScript, DAML 等等都会一点。
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 在任Flow中国技术大使，有在Flow上做一个可组合NFT项目，预计4月上线。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```python

# 方法一
import math

i = 1
sum = 0
while i <= 100:
    sum = sum + math.pow(i, 3) - math.pow(i, 1 / 3)
    i = i + 1

print(sum)

# 方法二
from functools import reduce

sum2 = reduce((lambda x, y: x + y), list(map(lambda x: (math.pow(x, 3) - math.pow(x, 1 / 3)), range(1, 101))))
print(sum2)

```
