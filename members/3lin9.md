# 3lin9

1. *微信名或昵称：* ep_ling0
2. *discord的ID：* 3lin9#2592
3. *擅长的建设领域、语言或工具、熟练度：* 擅长开发web开发,H5开发、混合APP开发、小程序开发，精通javascript，5年+经验；熟悉前端框架：APICloud/NodeJs/Vue/Webpack。
4. *每周能花在业余项目的时间：* 20小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 写过一些自动化脚本。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

```javascript
		function accAdd(arg1,arg2){
			var r1,r2,m; 
			try{r1=arg1.toString().split(".")[1].length}catch(e){r1=0} 
			try{r2=arg2.toString().split(".")[1].length}catch(e){r2=0} 
			m=Math.pow(10,Math.max(r1,r2)) 
			return (arg1*m+arg2*m)/m 
		}
		function accSub(arg1,arg2){
			return accAdd(arg1,-arg2)
		}
		var sum = 0
		for(var i=1; i<=100; i++) {
			// console.log(accSub(Math.pow(i,3),Math.cbrt(i)))
			sum = accAdd(sum, accSub(Math.pow(i,3),Math.cbrt(i)))
		}
		console.log(sum) // 25502149.836096782
```
