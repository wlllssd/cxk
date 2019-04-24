# 仅供个人娱乐研究使用

## 使用方法

`python cxk.py`



## 制作方法

### 制作工具

1. PotPlayer 
2. Ascgen2
3. python

### 过程

1. 使用PotPlayer（或者KMPlayer等）逐帧截取视频画面，得到N张图片
2. 使用Ascgen将每张图片转化为字符串txt
3. 用python读取txt并输出

### 难点

输出时，若使用清屏函数，cmd会闪烁，无法正常观看，因此采用了print到cmd中固定一行的方法

具体实现方法见：

​	知乎：python 能否print到console固定一行？

​	<https://www.zhihu.com/question/21100416>

### 可能导致无法正常运行的问题

1. 画面显示扭曲

   这可能是因为每个字大小不同，使得每一行长度不同，导致看起来歪曲

   解决方法是设置cmd的字体为：新宋体

   顶部右键-->属性-->字体

2. 画面中存在乱码

   尝试先输入cls后再运行

3. 画面跳动

   全屏cmd，同时在字体中将字体大小缩小

