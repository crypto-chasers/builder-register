1.微信名或昵称： mx970616

2.discord的ID： 小码#9466

3.擅长的建设领域、语言或工具、熟练度： Java开发/一年工作经验

4.每周能花在业余项目的时间： 10小时左右(情况不定

5.区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）： 无

6.用任意编程语言计算以下公式 
$$
\sum_{n=1}^{100}{(n^3-\sqrt[3]{n})}
$$

```java
public class GetSum {

    public static Double getSum(Integer n){
        Double result = Double.valueOf(0);
        for (int i = 1; i <= n; i++) {
            result += Math.pow(i,3) - Math.pow(i,1.0/3);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(getSum(100));
    }
}
```
