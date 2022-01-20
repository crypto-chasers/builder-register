# Ginharu#6694

1. *微信名或昵称：* Yuanjl_Vi
2. *discord的ID：* Ginharu#6694
3. *擅长的建设领域、语言或工具、熟练度：* 擅长后端各类服务，合约调用链监控等 精通Golang 4年经验；熟练使用python, js搞各类脚本 2年经验；从事区块链4年时间，基本都在做钱包相关，了解各类主链原理挖矿等，主要使用语言go, python, js, solidity。
4. *每周能花在业余项目的时间：* 20小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 暂无
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```go
package main

import (
	"fmt"
	"math"
)

func main()  {
	var sum float64
	for i:= 0; i <=100;i++ {
		sum += math.Pow(float64(i),3) - math.Cbrt(float64(i))
	}
	fmt.Println(sum) //2.5502149836096782e+07
}
```