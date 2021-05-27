# script-money

1. *微信名或昵称：* lhp6636
2. *discord的ID：* atur#2952
3. *擅长的建设领域、语言或工具、熟练度：* 擅长服务端开发，熟练使用Java、Python 等编程语言，3年开发经验；精通测试、数据处理方案，智能合约审计；
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 录制过Solidity 视频教程、参与多次黑客松获奖、负责某NFT项目合约开发及审计
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Golang
package main

import (
	"fmt"
	"math"
)

func sum(i float64) float64 {
	if i == 1 {
		return 0
	}
	temp := math.Pow(i, 3) - math.Cbrt(i)
	return temp + sum(i-1)
}

func main() {
	result := sum(100)
	fmt.Printf("%.8f\n", result)   // 25502149.83609678
}
```
