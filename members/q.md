# q

1. *微信名或昵称：* longhorn_chen
2. *discord的ID：* CeranaK#3469
3. *擅长的建设领域、语言或工具、熟练度：* 擅长互联网产品开发，客户端+后端，精通java，golang，5年经验。了解javascript和typescript，1年经验。
4. *每周能花在业余项目的时间：* 15-20小时
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 做过2个小型dapp；玩过一些defi项目，读过合约。
6. *用任意编程语言计算以下公式*
   ![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```golang
package main
import (
	"fmt"
	"math"
)
func main() {
	result := float64(0)
	for i := 1; i <= 100; i++ {
		result += math.Pow(float64(i), 3) - math.Cbrt(float64(i))
	}
	fmt.Printf("%v", result) //25502149.836097
}
```
