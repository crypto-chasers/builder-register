# script-money

1. *微信名或昵称：* dragonv96
2. *discord的ID：* semapher#7332
3. *擅长的建设领域、语言或工具、熟练度：* 
- 擅长开发单体/分布式的服务器/网站后台，Java/MySQL/Shell，4年+实战经验，熟练；
- 缓存/消息队列等中间件，docker容器。4年+实战经验，熟练；
- 擅长通过Java版selenium自动化框架、JavaFX快速开发小工具，熟练；
- Vue.js全栈开发dapp/前端网站，一般。
4. *每周能花在业余项目的时间：* 25小时左右（目前自由职业）
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 写过[基础总结](https://github.com/DragonV96/study-notes/blob/master/%E5%8C%BA%E5%9D%97%E9%93%BE/%E5%8C%BA%E5%9D%97%E9%93%BE%E7%AC%94%E8%AE%B0.md)，开发过基于(Java)Selenium+JavaFX的网页自动化工具客户端+服务器，一线交易所API上新提醒通知，链上监控等。
6. *用任意编程语言计算以下公式*
    ![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```java
public class Test {
    public static void main(String[] args) {
        double sum = 0;
        for (int i = 1; i < 101; i++) {
            sum += Math.pow(i, 3) - Math.pow(i, 1d/3);
        }
        System.out.println(String.format("%.9f", sum)); // 25502149.836096782
    }
 }
```
