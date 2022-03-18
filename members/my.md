微信名或昵称： x1494448024
discord的ID： ^_Crab_^#1098
擅长的建设领域、语言或工具、熟练度： 五年小运维，平时用python/shell比较多，学过golang/java
每周能花在业余项目的时间： 周未双休，可以安排
区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）： 菜鸟，刚入圈

#!/bin/bash
#求和
sigma=0
for i in $(seq 100); do
        n1=$(( i * i * i ))
        n2=$(echo $i 3|awk '{printf("%.9f", $1^(1/$2))}')
        n=$(echo $n1 $n2 | awk '{printf("%.9f", $1 - $2)}' )
        sigma=$(echo $n $sigma | awk '{printf("%.9f", $1 + $2)}' )
done
echo $sigma
