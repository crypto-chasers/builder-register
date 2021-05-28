# script-money
### 钱包接着
**0x132191dAc46A625BF15a2E908cE33a31f4f56efc**

1. *微信名或昵称：* 姿势就是力量
2. *discord的ID：* longago#1673
3. *擅长的建设领域、语言或工具、熟练度：* 啥都会一点，啥都不精通
4. *每周能花在业余项目的时间：* all in
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 读过些书，记过些笔记算么。。。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```js
function* run(n) {
  let [a, b, i] = [0, 0, 1]
  do {
    a = Math.pow(i, 3) - Math.pow(i, 1 / 3)
    a = a + b
    b = a
    i++
    yield a
  } while (i <= n)
  return
}

for (i of run(100)) {
    console.log(i)  // 25502149.836096782
    } 
```
