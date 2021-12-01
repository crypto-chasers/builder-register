# script-money

1. *微信名或昵称：* RekiCool
2. *discord的ID：* Mocer#2612
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发WEB后端，主攻Java，有电商系统开发经验，4年+经验；略会一些Python；
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 基于Selenium写过一些爬虫；未曾专门任职区块链岗位，但有这个想法，以后会考虑。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```java
import java.util.stream.IntStream;

public class Application {
    public static void main(String[] args) {
        double result = IntStream.rangeClosed(1, 100).mapToDouble(e -> Math.pow(e, 3) - Math.cbrt(e)).reduce(Double::sum).getAsDouble();
        System.out.println(result);
    }
}
```
