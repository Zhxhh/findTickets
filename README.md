# findTickets
Use python crawlers(scrapy framework) to capture ticket/train/bus ticket price information on major travel sites

<ul>
  <li>目前已实现去哪儿网站火车票抓取</li>
</ul>

<img src="https://github.com/Zhxhh/findTickets/blob/master/images/result.png" width="60%"/>
<img src="https://github.com/Zhxhh/findTickets/blob/master/images/running%20screenshot.png" width="60%"/>
<p>TODO：</p>
<ul>
  <li>实现机票/汽车票；携程/飞猪信息抓取</li>
</ul>


<h2>运行程序</h2>
<pre><code>
cd findTickets/findTickets/spiders
<br/>
python main.py -n
</code></pre>

<h2>运行并导出信息到result.csv</h2>
<pre><code>
python main.py -o  
</code></pre>

<p>可以更改出发地/目的地/出发日期；获取在制定出发日期后的制定时间段内车票信息</p>
<pre><code>
cd findTickets/findTickets/spiders/findTickets_spider.py
#例子
dptDate = '2019-02-06'
dptPlace = '广州'
arrPlace = '香港'
count = 3   #获取dptDate开始，三天内的车票信息
</code></pre>

