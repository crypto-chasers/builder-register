# muzik

1. *微信名或昵称：* muzik
2. *discord的ID：* hirsh#5973
3. *擅长的建设领域、语言或工具、熟练度：* 基于Ruby的Web开发,多年经验。
4. *每周能花在业余项目的时间：* 5小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 暂无。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Ruby#
Range.new(1,100).collect{|n| n.pow(3) - Math.cbrt(n)}.inject(0,:+)
#=> 25502149.836096782
```