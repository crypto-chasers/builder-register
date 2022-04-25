# wskit

1. *微信名或昵称：* mlz522
2. *discord的ID：* rolling#6385
3. *擅长的建设领域、语言或工具、熟练度：* 擅长Golang，会爬虫和chromedp自动化，目前从事Web3存储项目开发，主要使用IPFS。
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* Web3存储项目网关，Name Server，IPFS相关业务。
6. *用任意编程语言计算以下公式*
    ![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```golang
package main

import (
	"fmt"
	"math"
)

func main() {
	var sum, x float64
	for n := 1; n <= 100; n++ {
		x = float64(n)
		sum += math.Pow(x, 3) - math.Cbrt(x)
	}
	fmt.Printf("%f\n", sum) //25502149.836097
}
```