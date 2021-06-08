# delato


1. *微信名或昵称：* bingshan2911
2. *discord的ID：* delato#0063
3. *擅长的建设领域、语言或工具、熟练度：* 熟练使用go语言开发服务器长链接服务端，2年+经验；熟悉solidity语言开发，1年自由经验。
4. *每周能花在业余项目的时间：* 18小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 写过一些技术文章博客bsblog123.com，开发过一款NFT类Dapp游戏，可以质押挖矿、喂养、合成等玩法。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	var a int
	for i := 1; i <= 100; i++ {
		a = i*i*i + a
	}
	var b float64
	for i := 1; i <= 100; i++ {
		b = math.Cbrt(float64(i)) + b
	}
	answer := float64(a) - b
	fmt.Println(answer) //2.5502149836096782e+07
}
```