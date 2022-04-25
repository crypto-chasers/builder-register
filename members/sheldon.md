# script-money

1. *微信名或昵称：* xd_0795
2. *discord的ID：* xd0795#0701
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发Linux后端程序，6年Linux C/C++经验，熟练编写Shell，熟练Linux下的系统性能排查和调优。半年Golang经验，Rust学习中，会编写基本Python程序。
4. *每周能花在业余项目的时间：* 8小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：看过部分比特币代码，阅读过以太坊智能合约书籍*
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```CPP
#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;
 
int main()
{
    double sum = 0.0;
    int n = 100;
    for( int i = 1; i <= n; i++ ){
        sum += pow(i, 3) - pow(i, 1.0/3);
    }   
    cout << sum << endl;    // 2.55021e+07
    // printf( "%f\n", sum );  // 25502149.836097

    return 0;
}
```
