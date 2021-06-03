# script-money

1. *微信名或昵称：a1083617435
2. *discord的ID：yushuiey#2328
3. *擅长的建设领域、语言或工具、熟练度：* 擅长各种WEB应用和自动化脚本，精通PHP，5年+经验；熟练使用python3,C,GO,shell等服务器语言
4. *每周能花在业余项目的时间：* 24小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：了解Lotus,chia-blockchain等开源项目,并开发出服务于该项目用户层应用
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

``` php 

bcscale(6);
$sum = '0';
for ($i=1; $i <= 100; $i++) { 
    $pow = bcpow((string)$i,'3');
    $cbr = pow((string)$i,'0.33333333');
    $sum = bcadd(bcsub($pow,$cbr),$sum);
}
echo $sum;
```
