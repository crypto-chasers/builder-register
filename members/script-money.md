# script-money

1. *微信名或昵称：* 吹个球，吹个大气球
2. *discord的ID：* 吹个球，吹个大气球#1430
3. *擅长的建设领域、语言或工具、熟练度：*
    擅长iOS平台开发Swift、Objecte-c, 8年经验。能用Python、nodejs 、ruby做些小工具，刚工作时做过.Net C# web应用程序开发2年经验。
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 无，渴望学习区块链开发经验
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```swift
import UIKit
import Numerics

var greeting = "Hello, playground"

typealias ComplexDouble = Complex<Double>

let result = (1...100).enumerated().map {
     ComplexDouble.pow(Complex<Double>($0.element), 3).real - ComplexDouble.root(Complex<Double>($0.element), 3).real
}.reduce(0, +)

print(result) // 25502149.836096775
```
