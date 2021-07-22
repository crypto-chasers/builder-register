# script-money

1. *微信名或昵称：* 成全
2. *discord的ID：* chengquan#9676
3. *擅长的建设领域、语言或工具、熟练度：* 熟悉react, node前端开发，2年+经验。了解python。
4. *每周能花在业余项目的时间：* 20小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 刚入门学习中。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```javascript
var sum = new Array(100).fill('').map((item, i) => ++i).reduce(
    (total, item) => total +  Math.pow(item, 3) - Math.cbrt(item), 0);
console.log(sum);
```