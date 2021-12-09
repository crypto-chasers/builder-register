1. *微信名或昵称：* 很洋气的一个名字
2. *discord的ID：* brianfellii#7610
3. *擅长的建设领域、语言或工具、熟练度：* 擅长前端开发，有去哪儿网、滴滴2年+互联网公司前端开发工程师工作经验，熟悉 React、TypeScript等前端开发技术栈。
4. *每周能花在业余项目的时间：* 10小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 暂无，希望能深入探索。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```JavaScript
/**
 * 运行方式, terminal切换到对应目录执行： node sigma.js
 */

/**
 * sigma 函数
 * @param {*} start 起始位置
 * @param {*} end 终止位置
 * @param {*} func 函数
 * @returns sigma求和
 */
const sigma = (start, end, func) => {
  const length = end - start + 1;
  const mapFn = (v, k) => func ? func(k + start) : k + start;
  const sumFn = (a, b) => a + b;

  return Array.from({ length }, mapFn).reduce(sumFn);
}

/**
 * js 中内置的 Math 函数计算幂运算和立方根
 * @param {*} n 算数
 * @returns 3次幂减立方根的差
 */
const calcFun = n => {
  return Math.pow(n, 3) - Math.cbrt(n);
}

const res = sigma(1, 100, calcFun);

console.log('sigma求和后的结果是', res); // 25502149.836096782
```
