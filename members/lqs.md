# script-money

1. *微信名或昵称：* wxid_flu7j8psv8u621
2. *discord的ID：* lqs#9128
3. *擅长的建设领域、语言或工具、熟练度：* 擅长web后端开发，PHP四年经验；Golang两年经验；
4. *每周能花在业余项目的时间：* 7 ~ 10 小时
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 区块链入门阶段，有去了解相关概念。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```go
import (
	"fmt"
	"math"
)

func main() {
	var sum float64

	for n := 1; n <= 100; n++ {
		sum += math.Pow(float64(n), 3) - math.Cbrt(float64(n))
	}

	fmt.Printf("%f", sum) // 25502149.836097
}
```
