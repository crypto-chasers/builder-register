# owen

1. *微信号：* wen535358136
2. *discord的ID：* owen123#9377
3. *擅长的建设领域、语言或工具、熟练度：* 擅长Java、爬虫、JS、自动化脚本、数据库；熟悉Rust 安卓。 
4. *每周能花在业余项目的时间：* 30小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 经常开发爬虫软甲和自动化脚本软件。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```java
import java.util.stream.IntStream;

public class Demo {
    public static void main(String[] args) {
        double sum = IntStream.range(1, 101).asDoubleStream().map(o -> Math.pow(o, 3) - Math.cbrt(3)).sum();
        System.out.println(sum);
    }
}
```
