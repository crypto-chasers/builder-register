# script-money

1. *微信名或昵称：* henter
2. *discord的ID：* henter#3640
3. *擅长的建设领域、语言或工具、熟练度：* 10+年后端开发，Golang、PHP，前端开发2年+，熟悉web3 dapp开发。
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 做过defi项目开发，熟悉智能合约。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Golang
package main

import (
	"math"
)

func main() {
	var i, sum float64;
	for i = 0; i <= 100; i++ {
		sum += math.Pow(i, 3) - math.Cbrt(i)
	}
	println(sum)
}

```
