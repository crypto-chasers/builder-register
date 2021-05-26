# onemedicine

1. *微信名或昵称：* Un
2. *discord的ID：* mirror#1277
3. *擅长的建设领域、语言或工具、熟练度：* 
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	var sum float64

	for n := range []int{100:0}{
		sum = sum + (math.Pow(float64(n), 3) - math.Cbrt(float64(n)))
	}
	fmt.Println(sum)	// 	// 2.5502149836096782e+07
}

```
