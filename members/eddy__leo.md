# eddy__leo

1. *微信名或昵称：* cumtsjh
2. *discord的ID：* eddy#3092
3. *擅长的建设领域、语言或工具、熟练度：* 后端开发，熟练使用Golang、PHP。
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 开发过区块链资讯网站。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```golang
package main

import (
    "fmt"
    "math"
)

func main() {
    sum := 0.0
    for i := 1; i <= 100; i++ {
        sum += math.Pow(float64(i),3) - math.Cbrt(float64(i))
    }
    fmt.Println(sum)
}
```