# script-money

1. *微信名或昵称：* 这届选东莞仔
2. *discord的ID：* coffiasd#3295
3. *擅长的建设领域、语言或工具、熟练度：* 10年web开发项目，熟悉vue,css,精通php,golang
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 只有学习过区块链相关内容，没有实际项目开发经验.
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```golang
package main

import (
	"fmt"
	"math"
)

func main() {
	var sum float64
	for i := 1.0; i < 101.0; i++ {
		sum = sum + math.Pow(i, 3) + math.Cbrt(i)
	}
	fmt.Println(sum)
}

```
