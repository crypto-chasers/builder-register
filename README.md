# builder登记说明

fork 当前 repository，在 members 文件夹下创建一个md文件，填入以下信息，提交 pull request（提pr的时候留下自己的metamask钱包地址，有惊喜），格式参考 `./members/script-money.md`。

1. zyz19961022
2. olive888#6825
3. 擅长java，golang，shell开发，熟悉linux操作系统，熟悉idc机房自有节点建设（有相关资源和实际架构经验），filecoin节点封装维护。掌握web.js,合约开发
4. 每周能花在业余项目的时间：allTime (只要能赚)
5. 区块链建设经验：
6. 用任意编程语言计算以下公式：

#!/bin/bash
result=0
for i in $(seq 1 100)
do
        result=$(echo $i 3 $result|awk '{printf ("%.10f\n",$3+$1**$2-$1^(1/$2))}')
done

echo $result
