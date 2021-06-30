# script-money

1. *微信名或昵称：* MasamiYaa
2. *discord的ID：* TianKong#8837   
3. *擅长的建设领域、语言或工具、熟练度：* Android两年经验,java,kotlin

5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 没有哎....
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```C#

import kotlin.math.pow
    var sum = 0.0
    for (i in 1..100) 
	{
    sum += ((i.toDouble().pow(3.0)) - Math.cbrt(i.toDouble()))
    }
    toastCenterNoIconK("$sum")