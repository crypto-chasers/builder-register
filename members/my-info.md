# script-money

1. *微信名或昵称：* q8334416351
2. *discord的ID：* Eeenifg#4679
3. *擅长的建设领域、语言或工具、熟练度：* 擅长JAVA、GoLang、Python、能够流畅切换多种语言工作。
4. *每周能花在业余项目的时间：* 1天左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 经常编写自动化工具。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	var res float64
	for i := 1; i <= 100; i++ {
		res += math.Pow(float64(i), 3) - math.Cbrt(float64(i))
	}

	fmt.Println(res) // 2.5502149836096782e+07
}

```
