# script-money

1. *微信名或昵称：* peerlesspyy
2. *discord的ID：* Sk#0739
8. *擅长的建设领域、语言或工具、熟练度：* 刚毕业一年，擅长开发goweb应用，移动端自动化脚本程序，熟练golang，java，c#，工具熟练vscode和eclipse
9. *每周能花在业余项目的时间：* 每天12小时 每周就是12*7
10. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 做过电信的项目，电子签章这种
11. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

import java.text.NumberFormat;
import java.util.stream.IntStream;

public class Test {

    public static void main(String[] args) {
        double[] sum = {0d};
        IntStream.range(1,101).forEach(x->{
            sum[0] = sum[0] + (Math.pow(x,3d) - Math.cbrt(x));
        });
        NumberFormat nf = NumberFormat.getInstance();
        nf.setMaximumFractionDigits(10);
        nf.setGroupingUsed(false);
        System.out.println(nf.format(sum[0]));
    }

}
