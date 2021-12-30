# script-money

1. *微信名或昵称：* deng0_0xuan
2. *discord的ID：* EmmaXuannnn#5186
3. *擅长的建设领域、语言或工具、熟练度：* Applied statistics phd new grad，精通Python，R, 统计建模，机器学习
4. *每周能花在业余项目的时间：* 15小时左右 (最近时间较多)
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 未曾
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```python
def compute(N):
  sum = 0
  for n in range(1,N+1):
    sum += pow(n,3)+pow(n,1/3)
  return sum

print(compute(100))
```
