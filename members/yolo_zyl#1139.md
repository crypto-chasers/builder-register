# script-money

1. *微信名或昵称：* yl369340677
2. *discord的ID：* yolo_zyl#1139
3. *擅长的建设领域、语言或工具、熟练度：* C#/.NET开发，5年经验，主要做C端，少量后端。
4. *每周能花在业余项目的时间：* 8小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 曾加入过某国产公链项目技术团队（主要使用C#），不过很快离职，尚未窥其门径。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```C#
using System;
using System.Linq;
// 我就是用的c#，照搬示例，不过示例有一处错误。
var sum = Enumerable
        .Range(1, 100)
        .Select(i => Math.Pow((double)i, 3) - MathF.Cbrt(i)) // 这里应该是MathF，不是Math
        .Sum();
Console.WriteLine(sum); // 25502149.836095214
```
