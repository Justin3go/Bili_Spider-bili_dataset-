# Bili_Spider-bili_dataset-
**爬取了B站文章的数据，每条数据包括标题、内容、分类、阅读量、点赞、收藏、分享、回复数等**
## Crawler1:
这个爬虫项目是爬取的**B站文章加标题**的数据：
#### 格式为：
![image](https://user-images.githubusercontent.com/63507251/110720200-23379200-8249-11eb-994e-22cde607d857.png)

每三行一条数据，id下面一行为空的代表已经被用户删除的数据，是无效数据；

你可以在[**这里**](https://pan.baidu.com/s/1M1RFHNUBPRa_aTUboBPmGw)获取我已经爬好了的10万条未经过任何处理的数据（提取码：p4of）；
## Clawler2:
这个爬虫项目是发现前面那点**数据有点不够**就单独再爬的一次

其中包含了每篇文章的观看数目(view)、收藏数(favorite)、点赞数(like)、回复数(reply)、分享数(share)、投币数(coin)、不喜欢数(dislike)这些数据

#### 格式为：
![image](https://user-images.githubusercontent.com/63507251/110720688-fcc62680-8249-11eb-89e5-d4dd8801d54c.png)

每一行就是一条数据，从左到右一次是**ID、view、favor、like、reply、share、coin、dislike**，中间以空格分隔。

###### 注：我并没有爬取完B站的数据，大概到2021/3/11，B站的文章有1亿条左右（包括空的被删除的数据）需要的可以自己爬取，Crawler1不需要延时也不需要买代理，Crawler2在不延时的情况下会被检测，需要买代理，但在延时1秒的时候是可以一直爬取的，我这里是用的后面的一种方法，毕竟只是来试试手；

## 使用
如果你需要使用代码去爬取数据，可以参考以下流程：
***step1:*** pip install scrapy

***step2:*** cd /爬虫项目的路径/ e:cd C:\??\??\??\Crawler1\bili

***step3:*** 选择你需要爬取的数据的区间，在Crawler2\bili1\bili1\spiders\other_data.py或Crawler1\bili\bili\spiders\bili_data.py中

**修改**：![image](https://user-images.githubusercontent.com/63507251/110721709-ff298000-824b-11eb-9b6a-f7a19b44cd43.png)
里面的标记数字为你的开始位置（建议从1000 000开始）

**修改**：![image](https://user-images.githubusercontent.com/63507251/110721807-326c0f00-824c-11eb-8f2e-4bec6d81f929.png)
里面的数字为你的结束位置（目前的的大约是在 101 000 000左右）
相当于在这1亿条数据里面选择一个区间进行爬取；

***step4:*** 输入scrapy crawl other_data 或 scrapy crawl bili_data 开始爬取

***step5：***（可选）在setting.py文件里面设置延时，预定义crawler1的延时为0，crawler2的延时为1秒，如果你需要大量数据，建议买代理池；
