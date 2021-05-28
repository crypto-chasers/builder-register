# Leek
以太地址：0x6A62a664974939513f165703e76Ab8E16aC8eB17
1. *微信名或昵称：* jc13005458097
2. *discord的ID：* Leek#5812
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发数据分析的小工具，精通Java，4年+经验；熟练使用AndroidStudio开发支付类APP，2年+经验。
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 写过一些技术文章，开发过基于SpringCloud+Mysql的POS机支付系统。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

import java.math.BigDecimal;

public class Accumulator {
    public static void main(String[] args) {
        BigDecimal sum = new BigDecimal(0);
        for (double i = 1; i< 101; i++) {
            sum = sum.add(new BigDecimal(Math.pow(i, 3)).subtract(new BigDecimal(Math.pow(i, 1.0/3))));
        }
        System.out.println("sum = " + sum);
    }
}
