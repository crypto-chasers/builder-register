
1. 微信名或昵称：guoyibaha
2. discord的ID：gcon#1567
3. 擅长的建设领域、语言或工具、熟练度：后端开发，4年 nodejs 开发，2年 golang 开发，对分布式内容分发，边缘节点计算等技术比较熟悉，对出海领域社交产品业务比较熟悉，入门级 dapp 开发，正在学习合约开发，区块链技术
4. 每周能花在业余项目的时间： 20小时左右
5. 区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：做过nft mint相关业务
6. 用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```golang
package main

import (
	"fmt"
	"math"
)

func main() {
	var sum float64
	var i float64
	for i = 0; i < 101; i++ {
		sum += (math.Pow(i, 3) - math.Cbrt(i))
	}

	fmt.Printf("%f", sum)
}

```
