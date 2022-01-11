# script-money

1. *微信名或昵称：* richme-figo
2. *discord的ID：* Richme#4557
3. *擅长的建设领域、语言或工具、熟练度：* 擅长JavaScript、Nodejs、Puppeteer、React/Vue、Flutter等大前端技术和自动化工具（从业8年，北京多家大厂工作，带团队），了解区块链、以太坊、web3。
4. *每周能花在业余项目的时间：* 20小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 开发过一些抢购脚本，并通过脚本获得10倍以上收益
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Javascript#
Array.from(Array(100), (_, k) => k + 1).reduce(
  (prev, cur) => prev + (Math.pow(cur, 3) - Math.pow(cur, 1 / 3)),
  0
);
```