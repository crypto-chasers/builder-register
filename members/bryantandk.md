# script-money

1. *微信名或昵称：* bryant-nz
2. *discord的ID：* thinkslow#6779
3. *擅长的建设领域、语言或工具、熟练度：* 全栈开发者, 擅长效率工具开发, 精通 JavaScript. 6年全栈开发经验, 前端全能, 后端可以熟练写 web 服务. 
4. *每周能花在业余项目的时间：* 20小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 刚开始了解不久, 目前在研究 Defi Kingdoms 这个游戏, 做了抢英雄的 bot 和一些数据分析工具, 暂时不能开源代码, 这里有一个不是实时数据的版本: https://dfk-report.netlify.app
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Javascript#
new Array(100)
    .fill(0)
    .map((_, i) => Math.pow(i+1, 3) - Math.cbrt(i+1))
    .reduce((acc, current) => acc + current, 0)
```
