# script-money

1. *微信名或昵称：* itliusir
2. *discord的ID：* A股最牛李大霄#2641
3. *擅长的建设领域、语言或工具、熟练度：* 
	1. 本职微服务、基础平台(监控、调度、私有云)开发
	2. 语言：熟悉java golang
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 
  暂时刚入区块链，还没经验
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```go
	func main() {
		var sum float64
		for i := 1; i <= 100; i++ {
			sum += math.Pow(float64(i), 3) - math.Pow(float64(i), 1/3)
		}

		fmt.Printf("sum: %f", sum)
	}
```
