# script-money

1. *微信名或昵称：* zigzag0128
2. *discord的ID：* billy#1881
3. *擅长的建设领域、语言或工具、熟练度：* 擅长 Web 前端相关工具和框架，熟练 TypeScript/ES 全栈开发 Web 项目，6年+经验。
4. *每周能花在业余项目的时间：* 20小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 暂无相关经验。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

``` typescript
const result = [...Array(100).keys()].map(i => i+=1).reduce((acc, val) => (acc + Math.pow(val, 3) - Math.cbrt(val)), 0);

console.log(result); // 25502149.836096782
```
