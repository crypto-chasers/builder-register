# script-money

1. *微信名或昵称：* idolzhao622
2. *discord的ID：* idolzhao.eth l Zombinomy#6486
3. *擅长的建设领域、语言或工具、熟练度：* 擅长JAVA、GO、分布式系统、大型系统架构
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 目前在了解阶段、刚开始学习合约
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```GO
import (
	"fmt"
	"math"
)

func main(){
	sum:=0.0
	for i:=1.0;i<=100;i++{
		fmt.Println(i)
		sum+= math.Pow(i,3) - math.Cbrt(i)
	}
	fmt.Printf("%.10f",sum)
}
```
