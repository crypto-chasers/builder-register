# bright1989

1. *微信名或昵称：* bright-gz
2. *discord的ID：* brightyang#5999
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发数据库处理及API接口调用工具，精通Java，6年+经验；熟练使用各种关系数据库，例如Oracle、MySQL、PostgreSQL等，6年+经验；熟练使用Python，1年经验。
4. *每周能花在业余项目的时间：* 16小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 搭建过ETH测试网客户端，用程序参与交易所交易大赛，机器人刷成交量等。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```JAVA
import org.junit.Test;
import java.util.stream.IntStream;

public class MathTest {
	@Test
	public void testSum() {
        double sum = IntStream.rangeClosed(1, 100).mapToDouble(i ->
                Math.pow(i, 3) - Math.cbrt(i)).sum();
        System.out.printf("%.9f", sum);
	}

}
```