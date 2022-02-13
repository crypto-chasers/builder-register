# Amagi

1. *微信名或昵称：* AmagiDDmxh
2. *discord的ID：* AmagiDDmxh#3853
3. *擅长的建设领域、语言或工具、熟练度：* 主职为 Front End，熟练使用 TypeScript 全栈开发 dapp，4年+的开发经验；
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：*
   1. 参与过 Polka 第一届 和 eth-global nft-hack 黑客松
   2. 参与过 DeFi、Dex、Dapp、Wallet 等项目的前端开发
   3. 参与 Rebase 贡献分享、GitCoin Moonshot Collective 周会
   4. 给各种开源项目包括 [Uniswap](https://github.com/Uniswap/interface/pull/1379)、[Cheers](https://github.com/NaturalSelectionLabs/Cheers/pull/135) 贡献过代码并被 Merged
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```TypeScript
// result of cumulative `n**3 - cbrt(n)` from 1 to 100
// 25_502_149.836_096_782
Array.from({ length: 100 })
  .map((_, i) => (n = i + 1)**3 - Math.cbrt(n))
  .reduce((acc, cur) => acc + cur)
```
