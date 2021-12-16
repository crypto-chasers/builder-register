# Younger

* 微信名或昵称：
> oYo

* discord的ID：
> Younger#6132

* 擅长的建设领域、语言或工具、熟练度：
> Java 7年
> JS (node、vue、web3)  5年
> Solidity合约开发 自己写过一些套利合约

* 每周能花在业余项目的时间：
> 5小时左右

* 区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：
> [Newland](https://newland.finance) （挖矿）主要开发者

6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```javascript
    const Bignumber = require('bignumber.js');
    const result = Bignumber.sum(...Array.from({length:100}, (v,k) => k + 1).map(n => n**3 - Math.cbrt(n)))
    console.log(result.toString())  //  25502149.83609678249539
```
