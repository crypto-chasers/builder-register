# zjhmale

1. *微信名或昵称：* flea954348
2. *discord的ID：* zjhmale#4846
3. *擅长的建设领域、语言或工具、熟练度：* 精通`Python`, `Rust`, `Clojure`, `C++`, `Solidity`开发 擅长编辑器插件开发(`VsCode`, `Vim`) 6年软件开发经验
4. *每周能花在业余项目的时间：* 18小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 参与过`FlaminCome`机枪池项目开发, 为`Nervos/ckb`提交过代码
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Rust
let sum = (1u8..=100u8)
            .map(f32::from)
            .collect::<Vec<f32>>()
            .iter()
            .fold(0.0, |acc, x| acc + (x.powf(3.0) - x.powf(1.0/3.0)));

println!("{:?}", sum); // 25502156.0
```
