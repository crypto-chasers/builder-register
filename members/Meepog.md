# script-money

1. *微信名或昵称：* Meepog
2. *discord的ID：* Meepo#5179
3. *擅长的建设领域、语言或工具、熟练度：* 擅长java，2年+经验。python熟练。熟悉前端框架React、angular，无dapp经验。
4. *每周能花在业余项目的时间：* 12小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 无
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```typescript
import * as _ from 'lodash';

_.sum(_.reduce(_.range(1, 101), (sum, n) => (sum + Math.pow(n, 3) - Math.cbrt(n)),0));
```
