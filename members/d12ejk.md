# d12ejk

1. *微信名或昵称：* xiziv838
2. *discord的ID：* d12ejk#7728
3. *擅长的建设领域、语言或工具、熟练度：* 擅长服务端开发，熟练掌握Java、Spring、MySQL、Linux、计算机网络等，4年+经验
4. *每周能花在业余项目的时间：* 24小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 了解web3j、开发过一些爬虫监控和链上自动交易工具
6. *用任意编程语言计算以下公式*
   ![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Java
public class SolutionTest {

   public static void main(String[] args) {
      BigDecimal result = BigDecimal.ZERO;
      for (int i = 1; i <= 100; i++) {
         Double num = Math.pow(i, 3) - Math.pow(i, 1.0 / 3.0);
         result = result.add(new BigDecimal(num.toString()));
      }
      System.out.println(result.toPlainString()); // 25502149.836096782495390
   }
}
```
