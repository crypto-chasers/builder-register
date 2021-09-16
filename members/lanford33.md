# lanford33

1. *微信名或昵称：* accoropitor
2. *discord的ID：* lanford#2178
3. *擅长的建设领域、语言或工具、熟练度：* 擅长区块链钱包中间件开发，Elixir 3 年开发经验。较为熟练使用 web3.js/ethers.js。熟悉 Swift 和 iOS 开发。
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 写过一些技术文章，开发过一些小 Solidity 合约和工具脚本。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```elixir
1..100
|> Enum.reduce(0, &(:math.pow(&1, 3) - :math.pow(&1, 1/3) + &2)) 
|> IO.inspect(label: "Result is") # Result is: 25502149.836096782
```
