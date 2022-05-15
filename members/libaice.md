## BAICE- 李百策

1. *微信名或昵称：* lbc14678   李百策

2. *discord的ID：* baice#6847

3. *擅长的建设领域、语言或工具、熟练度：*

   > * 在一家区块链公司做后端与合约开发，熟悉Java,GoLang, Js, 
   > * 使用Solidity 写了部分的合约，对于内联汇编与Opcode还在学习研究。
   > * 在学Rust与Wasm编译器,在Solana的DevNet 开发NFT。

   

4. *每周能花在业余项目的时间：* 15小时左右

5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：*

   >  最近居家隔离，做了一些关于Defi产品的应用与研究的文章，过段时间会更新到自己的GitHub之上。

   

6. *用任意编程语言计算以下公式*
  ![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```go
func main() {
	var total float64 = 0
	for i := 1; i <= 100; i++ {
		total = total + math.Pow(float64(i), 3) - math.Pow(float64(i), float64(1)/float64(3))
	}
	fmt.Println("total is ", fmt.Sprintf(strconv.FormatFloat(total, 'f', 9, 64)))
}
```

> 结果输出   `total is  25502149.836096782`
