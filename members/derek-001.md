# script-money

1. *微信名或昵称：* 王大飞

2. *discord的ID：* Derek hu#2629

3. *擅长的建设领域、语言或工具、熟练度：* 

   擅长信息检索和消息处理。C/C++/Java。读书的时候用C/C++较多，数据库内核开发。21年毕业开始Java开发，大数据领域。

4. *每周能花在业余项目的时间：* 10小时左右

5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 做过一些near的撸空投教程，不过就是依葫芦画瓢，没有深入理解过原理。

6. *用任意编程语言计算以下公式*
    ![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```c++
#include <iostream>
#include <math.h>

using namespace std;

int main() {
    double sum;
    for (int i = 1; i <= 100; i++) {
        sum += pow(i, 3) - pow(i, 1.0 / 3);
    }
    printf("%.9f\n", sum); // 25502149.836096782
    return 0;
}
```
