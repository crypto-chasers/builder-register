# crrrrrw

1. *微信名或昵称：* MoreFree2021_x
2. *discord的ID：* ChenFree#7473
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发分布式高性能中间件系统，精通Java，5年+经验。
4. *每周能花在业余项目的时间：* 3~10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 暂无，小白，使用过常见的Dapp。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```java#
package calc;

import java.util.stream.IntStream;

public class Demo {

    public static void main(String[] args) {
        double sum = IntStream.range(1, 101).asDoubleStream().map(n -> Math.pow(n, 3) - Math.cbrt(n)).sum();
        System.out.println(sum); // 2.5502149836096782E7
    }

}
```

