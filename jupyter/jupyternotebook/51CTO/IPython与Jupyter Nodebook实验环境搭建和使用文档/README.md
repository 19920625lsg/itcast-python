# Python交互环境简介与IPython安装
> https://edu.51cto.com/course/13107.html

## REPL

## 开发Python程序的选择：
+ 1.	普通的文本编辑器：vi，sublime text
+ 2.	集成的IDE（eclipse、PyCharm）
+ 3.	IPython和Jupyter Notebook

## IPython安装

> IPython是一个交互式计算系统，可以认为是增强版的Python Shell。提供了强大的REPL功能。

### Python2
`pip2 install ipython = 5.1`

### Python3
`pip install ipython`

# IPython的自动补全、查看文档与快捷键

> 自动补全：按Tab键会出来成员列表

+ 查看文档时，如果内容比较多，一页显示不下，可以按空格翻页，按q键退出

+ Ctrl+P或上箭头：重新输入上一条命令
+ Ctrl+C：清空当前正在输入的代码
+ Ctrl+A：跳转到行头
+ Ctrl+E：跳转到行尾

# IPython的魔术方法

> 以%开头的命令称为IPython的魔术方法

+ `%hist`：查看输入历史
+ `%timeit`：检测某条语句的执行时间    %timeit math.cos(20)
+ `%paste`：粘贴并执行剪贴板上的命令
+ `%cat` ：用于查看文本文件的内容
+ `%run`：用于执行python脚本 –i表示在当前命名空间执行
+ `%who`：显示当前命名空间中的变量
+ `%xdel`：删除变量，同时删除在IPython上的一切引用，del命令只删除变量，并不删除引用
+ `%env`：用于查看系统环境变量
+ `%quickref`：用于显示魔术方法的文档
+ `%magic`：显示详细文档

# Jupyter Notebook简介与安装

> Jupyter Notebook是一个交互式笔记本，用于编辑和运行各种编程语言，前身是IPython Notebook

# 为什么要使用Jupyter Notebook？
- 更美观的界面
- 更好的可视化（在web里可视化，并与web深度结合）
- 方便远程访问，放在服务器上，任何时候都可以访问

# 安装Jupter Notebook

+ `pip install jupyter`

# 运行

+ `jupyter notebook`

# 让Jupyter Notebook支持其他编程语言

> 汇总地址：https://github.com/jupyter/jupyter/wiki/Jupyter-kernels

+ C:[C](https://github.com/brendan-rius/jupyter-c-kernel)
+ Java:[IJava](https://github.com/SpencerPark/IJava)以及[scijava-jupyter-kernel](scijava-jupyter-kernel)
+ Scala:
+ Kotlin
+ JavaScript:[IJavascript](https://github.com/n-riesco/ijavascript)
+ C++
+ Perl

## [BerkerX](http://beakerx.com/documentation)可以支持多种语言，安装一个就够了！！！


# 调整Jupyter Notebook的主题（字体、字号等）

+ 工具地址：[jupyter-themes](https://github.com/dunovank/jupyter-themes)

+ 安装： `pip install – upgrade jupyterthemes`

+ `jt –l`   查看当前可用的主题

+ 更多的主题设置等命令可以见项目的README.md
