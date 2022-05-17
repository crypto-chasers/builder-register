# script-money

1. *微信名或昵称：* chenshaworyc
2. *discord的ID：* cccc#1902
3. *擅长的建设领域、语言或工具、熟练度：* unity客户端3年经验、熟练lua、c#
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 无
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```C#
using System;
using System.Linq;
using UnityEngine;

public class TTT
{
    public static void TTTt()
    {
        var sum = Enumerable.Range(1, 100).Select(i => Math.Pow((double) i, 3) - Cbrt(i)).Sum();
        Debug.LogError(sum);//25502149.8360833

        double Cbrt(double x)
        {
            var y = Math.Pow(Math.Abs(x), 1f / 3f);
            return x < 0 ? -y : y;
        }
    }
}
```
