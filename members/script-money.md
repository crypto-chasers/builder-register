# script-money

1. *微信名或昵称：* ying031213
2. *discord的ID：* joey111#1151
3. *擅长的建设领域、语言或工具、熟练度：* 熟练使用java 及C，5年开发经验
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 写过一些技术文章。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```C
double calculation(double n) {
    return pow(n, 3) - cbrt(n);
}

void solution() {
    double num = 1;
    double result = 0;
    while (num <= 100) {
        result += calculation(num);
        num += 1;
    }
    NSLog(@"result is:%f", result);
} // 25502149.836096782
```
