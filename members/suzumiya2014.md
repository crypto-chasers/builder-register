# suzumiya2014

1. *微信名或昵称：* 大喵星人
2. *discord的ID：* 咕噜#6443
3. *擅长的建设领域、语言或工具、熟练度：* 什么都会一点，什么都不精通。主业是一些大型行业web项目，侧重后端，基本都是重架构SSH/SpringMVC/SpringCloud/SpringBoot，各种数据库、中间件、消息队列等，主要使用语言java。C/C++/汇编/python等也能写一些。事实上最近2年代码写的比较少。
4. *每周能花在业余项目的时间：* 4-20小时不等
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 接触不长，比较懒，只写过一些简单教程，参与过一些节点测试项目，cosmos系居多。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

一个循环就能搞定的事情，不过还是考虑用forkjoin，毕竟这样百亿也很快。下面的方法讲返回long，不保留小数点，全部使用double可以提高精度。

```java
import java.util.concurrent.RecursiveTask;

public class ForkJoinCalculate extends RecursiveTask<Long> {

    private long start;
    private long end;
    private static  final  long  THRESHOLD= 10000L;

    public ForkJoinCalculate(long start, long end) {
        this.start = start;
        this.end = end;
    }

    @Override
    protected Long compute() {
        long length = end-start;
        if(length<=THRESHOLD)
        {
            long sum = 0;
            double temp = 0;
            for(long i = start ;i<=end ;i++)
            {
                temp += (double)Math.pow(i,3)-(double) Math.pow(i,1.0/3);
            }
            sum = Math.round(temp);
            return sum;
        }else{
            long middle = (start+end)/2;
            ForkJoinCalculate left = new ForkJoinCalculate(start,middle);
            left.fork();//拆分子任务 ，同时压入线程队列
            ForkJoinCalculate right = new ForkJoinCalculate(middle+1,length);
            right.fork();
            return left.join()+right.join();
        }
    }
}
```

测试类

```java

import org.junit.Test;

import java.time.Duration;
import java.time.Instant;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.ForkJoinTask;

import static java.time.Instant.now;

public class ForkJoinTest {
    @Test
    public void test(){
        Instant start = now();
        ForkJoinPool pool = new ForkJoinPool();
        ForkJoinTask<Long> task = new ForkJoinCalculate(1,100L);
        Long sum = pool.invoke(task);
        Instant end = now();
        System.out.println("100次累加执行时间："+ Duration.between(start,end).toMillis()+"毫秒  执行结果："+sum);
    }
    //百亿级
    @Test
    public void test1()
    {
        Instant start = now();
        ForkJoinPool pool = new ForkJoinPool();
        ForkJoinTask<Long> task = new ForkJoinCalculate(1,10000000000L);
        Long sum = pool.invoke(task);
        Instant end = now();
        System.out.println("100亿次累加执行时间："+ Duration.between(start,end).toMillis()+"毫秒  执行结果："+sum);
    }
}
```

long类型的结果输出：

```
100次累加执行时间：9毫秒  执行结果：25502150
100亿次累加执行时间：35毫秒  执行结果：6028400663709265422
```
