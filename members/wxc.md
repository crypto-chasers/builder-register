# Layman

1. *微信名或昵称：* layman
2. *discord的ID：* owen123#9377
3. *擅长的建设领域、语言或工具、熟练度：* 精通Java，擅长web脚本
4. *每周能花在业余项目的时间：* 20小时
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 写过写文章和自动化脚本
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```java
public class Test {
    public static void main(String[] args) {
        int n = 1;
        double sum = 0;
        while (n <= 100) {
            sum += Math.pow(n, 3) - Math.cbrt(n);
            n++;
        }
        //2.5502149836096782E7
        System.out.println(sum);
    }
}
```

