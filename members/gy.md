# gy

1. *微信名或昵称：* lazymanGY
2. *discord的ID：* lazyman#8660
3. *擅长的建设领域、语言或工具、熟练度：* 全栈开发，2年+经验，擅长 swift，golang，js，kotlin，架构领域，5年+经验。
4. *每周能花在业余项目的时间：* 10-20小时
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 只看过一些 contract，会一点 solidity
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```swift
import Foundation

let result: Double = (1...100).reduce(0.0) { $0 + pow(Double($1), 3) - cbrt(Double($1)) }
print(result)
```
