# littlenine

1. *微信名或昵称：* 永怀
2. *discord的ID：* littlenine#9594
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发web服务(全栈)、wallet connect、交易所钱包，熟练go/js/java，8年+经验。
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 个人负责开发过交易所钱包，开发过基于Selenium的网页自动化工具。
6. *用任意编程语言计算以下公式*
   ![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	var sum, i float64

	for ; i <= 100; i++ {
		sum += math.Pow(i, 3) - math.Cbrt(i)
	}

	fmt.Printf("%f", sum)
}
```
