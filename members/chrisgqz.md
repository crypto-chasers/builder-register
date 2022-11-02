# chrisgqz

1. *微信名或昵称：* gqzgavin
2. *discord的ID：* 啊点#6452
3. *擅长的建设领域、语言或工具、熟练度：* golang开发3年，擅长处理数据量大和并发高项目。Python能编写小工具。有前端基础
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 无
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```C#
package main

import (
	"fmt"
	"math"
)

func main() {
	sum := 0.0
	for i := 1.0; i <= 100.0; i++ {
		sum += math.Pow(i, 3) - math.Cbrt(i)
	}
	fmt.Printf("%.9f", sum)
	//25502149.836096782
}
```
