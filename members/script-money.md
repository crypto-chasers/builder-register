# script-money

1. *微信名或昵称：* hnzhangmeiqing
2. *discord的ID：* kingjay#2897
3. *擅长的建设领域、语言或工具、熟练度：* 擅长C#后端开发，winform桌面开发，网站开发,熟悉Python，做过一些爬虫方面的小项目！
4. *每周能花在业余项目的时间：* 16小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 无
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```C#
using System;
using System.Linq;

var sum = Enumerable.Range(1, 100).Select(i => Math.Pow((double)i, 3) - Math.Cbrt(i)).Sum();
Console.WriteLine(sum); // 25502149.836096782
```
