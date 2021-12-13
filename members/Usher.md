# Usher

1. *微信名或昵称：* Usher
2. *discord的ID：* Usher#6299
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发java后端和爬虫的小工具，精通java，2年+经验；熟练使用python开发；
4. *每周能花在业余项目的时间：* 14小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 了解一些区块链知识、正在学习。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```Java
        Flux.range(1, 100)
                .subscribeOn(Schedulers.parallel())
                .map(i -> Math.pow(i, 3) - Math.pow(i, 1.0 / 3))
                .reduce(Double::sum)
                .subscribe(System.out::println);
                
                2.5502149836096782E7
```
