# specterofnet

1. *微信名或昵称：* 同学
2. *discord的ID：* jialei12138#7936
3. *擅长的建设领域、语言或工具、熟练度：* 底层系统开发，C/C++, 5年+经验。Android Framework/Android Application开发，Java, 1年+经验。以太坊合约开发，solidity, 0.5年+经验.
4. *每周能花在业余项目的时间：* Workday->2hours/day  weekends->3hours/day Total: 16 hours
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 目前还没有开发过完整的区块链项目，都是做些小工具。参加过Ethglobal黑客松，在SKALE Network上面部署一款永恒笔记本应用，包括合约和前端代码。博客：https://blog.csdn.net/ljlinjiu?type=blog(很久不更新了)。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```C++
#include <iostream>
#include <math.h>

using namespace std;

int main() {
    double sum = 0;

    for( int i = 0; i <= 100; ++i )
    {
        sum += ( pow( i, 3.0 ) - pow( i, 1 / 3.0 ) );
    }
    cout<< sum;

    return 0;
}
```
