# azy

1. *微信名或昵称：* daoc4p
2. *discord的ID：* 剁刀师甲#2681
3. *擅长的建设领域、语言或工具、熟练度：* 擅长网络安全、代码逆向、漏洞挖掘，精通Golang、IDA Pro。
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 几乎没有写过技术文章，但是目前正在学习智能合约相关知识。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Golang
package main
import (
	"fmt"
	"math"
)
func main() {
	fmt.Println(calculate(100)) // 2.5502149836096782e+07
}
func calculate(n int) float64 {
	sum := float64(0)
	for i := 1; i <= n; i++ {
		sum += math.Pow(float64(i), 3) - math.Cbrt(float64(i))
	}
	return sum
}
```
