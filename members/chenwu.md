# chenwu

1. *微信名或昵称：* Eason__-__Chan
2. *discord的ID：* 陈武#3666
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发web系统前后端，精通Java，熟练使用javaScript，2年经验。
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 暂无
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Java
import java.lang.Math;
import java.math.BigDecimal;
import java.util.stream.IntStream;

public class Test {
    public static void main(String[] args) {
        IntStream evenNumbers = IntStream.rangeClosed(1, 100);
        double sum = evenNumbers.asDoubleStream().map(i -> Math.pow(i, 3) - Math.pow(i, 1.0 / 3)).sum();
        System.out.println(new BigDecimal(sum));//25502149.8360967822372913360595703125
    }
}
```