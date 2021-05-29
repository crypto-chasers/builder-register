# gracecampo666@gmail.com

1. *微信名或昵称：* always smile
2. *discord的ID：* jinpeng#5768
3. *擅长的建设领域、语言或工具、熟练度：* 擅长java开发，精通msyql，4年+经验；熟练使用IDEA开发JAVAEE应用，熟悉solidity 合约语言，熟悉Flow Playground Cadence 语言开发flow应用。
4. *每周能花在业余项目的时间：* 15小时左右
5. *区块链建设经验（产品、项目、黑客松、技术文章、代码贡献、艺术创作等）：* 写过一些技术文章，参与许多的公链项目节点测试活动。
6. *用任意编程语言计算以下公式* [![img](https://camo.githubusercontent.com/efe9a158b547540d2d2a9af433231733e98e13edb77eb8685e1ad9c2ebc1eec7/68747470733a2f2f6c617465782e636f6465636f67732e636f6d2f7376672e696d6167653f25354373756d5f2537426e3d312537442535452537423130302537442535436c6566742673706163653b286e253545253742332537442d25354373717274253542332535442537426e2537442673706163653b25354372696768742673706163653b29)](https://camo.githubusercontent.com/efe9a158b547540d2d2a9af433231733e98e13edb77eb8685e1ad9c2ebc1eec7/68747470733a2f2f6c617465782e636f6465636f67732e636f6d2f7376672e696d6167653f25354373756d5f2537426e3d312537442535452537423130302537442535436c6566742673706163653b286e253545253742332537442d25354373717274253542332535442537426e2537442673706163653b25354372696768742673706163653b29)

```
    public static void main(String[] args) {
        BigDecimal result = BigDecimal.ZERO;

        for (int n = 1; n <=100 ; n++) {
            double pow = Math.pow(Double.valueOf(n), (double) 1 / 3);
            result = result.add(new BigDecimal(n).pow(3).subtract(new BigDecimal(pow)));
        }
        System.out.println(result);
    } //25502149.8360967822313822850333053793292492628097534179687500
```