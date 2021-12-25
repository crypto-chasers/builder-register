# BlackHare

1. *微信名或昵称：* EtherHare
2. *discord的ID：* BlackHareKnight#7953
3. *擅长的建设领域、语言或工具、熟练度：* 熟悉Python,Solidty,C#,Rust开发语言，熟悉Unity、Cocos游戏制作工具，熟悉Sai绘图工具
4. *每周能花在业余项目的时间：* 10-14小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：*使用Solidty开发过Eth链智能合约，使用Rust开发过Near链智能合约，使用Sai制作过游戏素材，使用Unity制作过PC，安卓2d游戏
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```rust
//使用Rust实现
fn main() {
    let mut sum:f64=0.0;
    for i in 1..101{
        let n:f64=i as f64;
        sum+=n.powf(3.0)-n.cbrt();
    }
    println!("{0}",sum);//结果25502149.836096782
}
