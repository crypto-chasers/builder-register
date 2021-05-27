# suzumiya2014

1. *微信名或昵称：* 大喵星人
2. *discord的ID：* 咕噜#6443
3. *擅长的建设领域、语言或工具、熟练度：* 什么都会一点，什么都不精通。主业是一些大型行业web项目，侧重后端，基本都是重架构SSH/SpringMVC/SpringCloud/SpringBoot，各种数据库、中间件、消息队列等，主要使用语言java。C/C++/汇编/python等也能写一些。事实上最近2年代码写的比较少。
4. *每周能花在业余项目的时间：* 4-20小时不等
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 接触不长，比较懒，只写过一些简单教程，参与过一些节点测试项目，cosmos系居多。
6. *用任意编程语言计算以下公式*
![](https://latex.codecogs.com/svg.image?\sum_{n=1}^{100}\left&space;(n^{3}-\sqrt[3]{n}&space;\right&space;))

一个循环就能搞定的事情，不过还是考虑用forkjoin，毕竟这样百亿也很快。未对开根号的精度进行额外处理，要处理的话可以单独写一个类来控制计算精度。

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
            for(long i = start ;i<=end ;i++)
            {
                sum+=Math.pow(i,3)-Math.pow(i,1/3);
            }
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

结果输出：

```
100次累加执行时间：6毫秒  执行结果：25502400
100亿次累加执行时间：42毫秒  执行结果：6028400663710535392
```
