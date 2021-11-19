# script-money

1. _微信名或昵称: surestfeng
2. _discord 的 ID：surestfeng
3. _擅长的建设领域、语言或工具、熟练度：擅长Web开发，全栈开发工程师；熟练使用 JavaScript、PHP、Golang, 了解以及可以熟练开发WEB端的各种解决方案，3年工作经验
4. _每周能花在业余项目的时间：_ 20 - 25 小时左右
5. _区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：_ 首次接触区块链开发经验，了解过合约相关【未参与过】
6. _用任意编程语言计算以下公式_
   ![](<https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;)>)

```Javascript

// 获取 1 - 100 单位值
const cRange = () => Array.from(Array(100), (v, k) => k + 1);
// 条件计算
const cSelect = v => v.map(n => Math.pow(n, 3) - Math.cbrt(n));
// 求和
const sum = cSelect(cRange()).reduce((a, b) => a + b);
console.log(sum); // 25502149.836096782

```

```PHP

function cRange($length) {
    $arr = [];
    for ($i = 1;  $i <= $length; $i ++) {
        $arr[] = $i;
    }
    return $arr;
}

function cSelect($arr) {
    return array_map(function ($n) {
        return pow($n, 3) - pow($n, 1/3);
    }, $arr);
}

function cSum($arr) {
    return array_reduce($arr, function ($a, $b) {
        return $a + $b;
    });
}

$sum = cSum(cSelect(cRange(100)));
var_dump($sum); # 25502149.836097

```

```Golang

import (
	"fmt"
	"math"
)

func main()  {
	var arr []float64
	var sum float64
	for i := 1; i <= 100; i++ {
		var n float64
		n = math.Pow(float64(i), 3) - math.Cbrt(float64(i))
		arr = append(arr, n)
	}

	for _, v := range arr{
		sum += v
	}
	s := fmt.Sprintf("sum: %f", sum)
	fmt.Printf(s) // sum: 25502149.836097
}

```
