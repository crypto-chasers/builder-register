# meteor
1. *微信名或昵称：* 星坠
2. *discord的ID：* 星坠#7644
3. *擅长的建设领域、语言或工具、熟练度：* 精通Python，2年+经验；数据行业相关，2年+经验；。
4. *每周能花在业余项目的时间：* 5小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* bsc链初试 pancake ifo。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```python
import math


def calculate(rangeN,xN,cN):
    sumN = 0 
    for i in range(1,rangeN+1):
        sumN += (math.pow(i,xN)+math.pow(i,1/cN))
        print(i)
        print(math.pow(i,xN))
        print(math.pow(i,1/cN))


if __name__=='__main__':
    print('calculate')
    calculate(100,3,3)

```
