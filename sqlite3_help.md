---------------------------------------------------
# 金鑫哥的工作

功能：
支持：
查询：
计算：
显示：

--------------------------------------------------
## Data source: 数据来源

中国足彩网 -> 比分直播 ->  北京单场 -> 分析: 平均欧赔 赔率3种： 胜平负

--------------------------------------------------
## Data structure: 数据结构

例子
巴萨罗那 - 马德里竞技 北京单场 ([http://live.zgzcw.com/bd/](http://example.com/))

<font color=red>这里的所有比赛数据你都要保存吗？</font>

赔率网页 ([http://fenxi.zgzcw.com/2004315/bjop](http://fenxi.zgzcw.com/2004315/bjop))

![image](file:///Users/zhengjiankang/Desktop/course/jin_xin/images/1.png)

球队 - 日期 - 比分 - 赔率：最开始赔率（初始赔率）- 开场前赔率（比赛开始前10分钟）- 开场后赔率（比赛结束后?）
	
巴萨, 马竞, 日期(1/30/2016), 主队得分(2), 客队得分(1), 

1.52, 4.03, 6.12, (<font color=red>初始赔率</font>)

1.50, 4.13, 6.68, (<font color=red>最新赔率，开场前10分钟，还是距离比赛开始前最近的赔率?</font>)

1.51, 4.12, 6.66 (<font color=red>最新赔率，开场结束后还是比赛结束后?</font>)

<font color=red>需要其他信息? 联赛？(英超西甲) 其他? 轮次</font>


## Front-end developer: 查询命令

* 查询输入
输入赔率？ 1.52, 4.03, 6.12 
-------------------------------------------------------

database design 

team table 
-----------------------
id  name  country level
----------------------- 
01   巴萨罗那     西班牙  甲级
02   皇家马德里   西班牙  甲级
03   马德里竞技   西班牙  甲级
04   瓦伦西亚     西班牙  甲级
05   曼联        英格兰   超级
06   曼城        英格兰   超级
07   拜仁慕尼黑   德国    甲级
08   多特蒙德     德国    甲级

...
-------------

match table
------------------------------------------------------------
id match_name  home_id  guest_id  home_score  guest_score  date  
------------------------------------------------------------
0001 01  06  1  2  2016/06/20 欧冠
0002 01  02  1  3  2016/04/20 西甲
...
-------------------------------------------------------------

odds table initial
----------------------------------------------------
id match_id win tie lost

---------------------------------------------------- 

odds table before
----------------------------------------------------
id home_id  guest_id date win tie lost

---------------------------------------------------- 


odds table after
----------------------------------------------------
id home_id  guest_id date win tie lost

---------------------------------------------------- 


<!--  Code structure

* Front end
前端功能：  支持查询
输入赔率    查询   


* Query data 
  能够自动查询搜集 数据库保存结果

  去重问题(time stamp?)

* Date structure


-----------------------------------
BackEnd: database

- table match 
球队 - 日期 - 比分 - 赔率：最开始赔率（初始赔率）- 开场前赔率（比赛开始前10分钟）- 开场后赔率（比赛结束后）
match_id (pk) | date | home_team | visit_team | home_score | visit_score






----------------------------------------
阶段2：
模串匹配查询
手动输入
x-1xx   {0301, 0302, 102....};

----------------------
其他：
横向 纵向  
英超比赛 对称结构
实时更新比赛 -->




