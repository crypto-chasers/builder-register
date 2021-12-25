# script-money

1. *微信名或昵称：* wildman999
2. *discord的ID：* iyonger
3. *擅长的建设领域、语言或工具、熟练度：* java开发，sql数据分析，熟悉大数据计算和存储框架。
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 暂无。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```java
 public static double f1(){
        double total=0;
        for(int i=1;i<=100;i++){
            total+=(Math.pow(i,3)-Math.pow(i,1/3));
        }
        return total;
 }
