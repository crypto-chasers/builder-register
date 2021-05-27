# jurowin9

1. *微信名或昵称：* jurowin
2. *discord的ID：* jurowin9
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发web和后端，精通GoLang、PHP、Python，2年+经验；熟练使用TypeScript开发web，1年经验。
4. *每周能花在业余项目的时间：* 40小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 暂时较少。
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
	for i := float64(1); i <= 100; i++ {
		sum += math.Pow(i,3) - math.Cbrt(i)
	}
	fmt.Printf("%f",sum)
}
```
