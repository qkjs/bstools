# bstools 使用说明
## 概要
本程序包是在作者开发的过程中发现一些经常用到的功能没有被很好的封装起来而利用业余时间分装的一套工具集合，所包含内容比较杂乱。在多机部署的情况下为了避免重复的拷贝文件，所以我将这套工具的集合发布出来。首先，这些代码并不高深，也没有什么晦涩难懂的地方。希望大家能用得上。谢谢
## 基本信息
作者：Bernie Suen
电子邮件：bernie.suen@outlook.com
授权协议：MIT
## 使用方法介绍
本模块包目前包含三部分，分别为与时间有关系的stTime, 与远程连接有关系的sshCmd 和 与打印输出有关系的formatPrint。
### stTime - 子模块
此模块包含1个装饰器和1个方法
#### performCacl - 装饰器方法
此方法用于模块的耗时计算，没有参数
#### tsToLocalTime - 方法
此方法用于时间戳转换为标准时间展示。
需要两个参数，timestamp, timeType
timestamp: 时间戳，不可省略。没有默认值。float格式。
timeType：事件类型，可接受值（"s", "ms"）,有默认值（"ms"）

-------
示例
```
import time
localTime = toToLocalTIimt(time.time()，"m")
```
### formatPrint - 子模块
此模块包含三个枚举类型和一个方法
#### LftColor
对应liunx 前景色
#### LbgColor
对应liunx 背景色
#### LsType
对应liunx 显示类型
#### cprint - 方法
此方法用于在liunx环境下显示有颜色的内容。
需要四个参数，info, f, a, t
info: 需要输入的内容，不可省略。没有默认值。字符串格式。
f: 前景色，传入LftColor的子类，默认空
a: 前景色，传入LbgColor的子类，默认空
t: 显示类型，传入LsType的子类，默认空

-------
示例
```
import time
localTime = toToLocalTIimt(time.time()，"m")
```

### sshCmd - 子模块
提供linux 远程操作, 此模块依赖 paramiko 模块。必须配置免密登录方可使用。
LiunxCmd(主机名)rCmd（命令）

