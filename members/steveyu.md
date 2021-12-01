# Steve Yu 

METAMASK地址：`steveyu.eth`

1. 微信：`OWOsteveyu`
2. discord ID：`steve yu #5007`

3. 擅长的领域：`前端开发`
4. 每周业余项目时间：`15小时+`
5. 区块链建设经验：
   1. 为 TOKAU.io 做过 NFT 开发（形式，外包赏金）
   2. NEAR nearvember，今日 12.1 日 的排行为第三名（还有3天比赛结束）。（使用rust语言编写合约，使用react写前端）
6. 计算以下公式

![img](https://camo.githubusercontent.com/efe9a158b547540d2d2a9af433231733e98e13edb77eb8685e1ad9c2ebc1eec7/68747470733a2f2f6c617465782e636f6465636f67732e636f6d2f7376672e696d6167653f25354373756d5f2537426e3d312537442535452537423130302537442535436c6566742673706163653b286e253545253742332537442d25354373717274253542332535442537426e2537442673706163653b25354372696768742673706163653b29)

```c++
#include <iostream>
#include <cmath>
double accumulation(double n) {
  double sum = 0;
  for(int i = 0; i <= 100; i++) 
    sum += (n * n * n - pow(n, 1.0/3));
  return sum;
}
int main() {
  double n = 0;
  std::cin >> n;
  std::cout << accumulation(n) << std::endl;
}
```

