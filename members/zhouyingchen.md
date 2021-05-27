/*
微信名：cjj0530_0801
discord的ID： zyc#5347
擅长的建设领域、语言或工具、熟练度： 高级驱动工程师，擅长C、C++、java，在工作中负责GPS、BT底层驱动开发 
每周能花在业余项目的时间： 12小时左右
区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）： 暂无，目前学习中。
用任意编程语言计算以下公式 
*/

//C

#include <stdio.h>
#include <math.h>
void main()
{
    int n;
    double sum;
    for(sum=0,n=1;n<=100;n++)
    {
        sum=sum+pow(n,3) - pow(n,1/3);
    }
    printf("%.0f\n",sum);
}