# script-money

1. *微信名或昵称：* #418 小亏怡情
2. *discord的ID：* sun#0393
3. *擅长的建设领域、语言或工具、熟练度：* 大数据开发，go后台开发，大厂6年经验，solidity开发一年经验。
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 交易所羊毛脚本，gamefi合约开发，聚合dex合约开发。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```go
package main

import "fmt"
import "math"

func main() {
   	channel := make(chan float64)
   	for i := 1; i < 101; i++ {
		if6 := float64(i)
		go func(i int) {
			channel <- math.Pow(if6, 3)-math.Cbrt(if6)
		}(i)
   	}
   	sum := 0.0
	for i := 0; i < 100; i++ {
		sum += <- channel
	}
   	fmt.Println(sum) //2.5502149836096782e+07
}
```
