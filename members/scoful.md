# script-money

1. *微信名或昵称：* scoful
2. *discord的ID：* scoful#4017
3. *擅长的建设领域、语言或工具、熟练度：* 主要语言java，偏后端，有chrome浏览器插件开发经验，作品：https://github.com/scoful/cloudSkyMonster，用Go写过自动化工具，图片识别，鼠标控制等
4. *每周能花在业余项目的时间：* 下班后等空余时间
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 开发过基于Go的自动化工具，图片识别，鼠标控制等。
6. *用任意编程语言计算以下公式*
  ![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```go
import (
	"math"
)
func main() {
	result := 0.0
	for i := 1; i <= 100; i++ {
		result += math.Pow(float64(i), 3) - math.Cbrt(float64(i))
	}
	println(result)
}
```

7. 地址：0x3FB5f8170B7Af422d4D9dE87D94fd4e4e2af179C