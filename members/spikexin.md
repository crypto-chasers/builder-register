# spikexin

1. *微信名或昵称：* spikexin
2. *discord的ID：* spikexin#7123
3. *擅长的建设领域、语言或工具、熟练度：* 自身专业是芯片设计，会C++/python，对Scala比较熟悉，有使用scala编写电路编译器的经验，目前正在学习solidity
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 暂时没有区块链建设经验，自身懂一些密码学，非常希望能在crypto领域从事开发。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Scala
import scala.math._

object Main {
  def main(args:Array[String])
  {
    val result = (1 to 100).map(x => pow(x, 3) - cbrt(x.toDouble)).reduce(_+_)
    println(result)
  }
}
```
