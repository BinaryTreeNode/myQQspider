myqqspider
this program is similar to QQ_Zone in github
it can help get the information u want from friends' qqzone and write it into excel

some differences:
1.we can define our list of usrs in wanteduserinfo.ini
2,we can see the time when our friends sent their messages to QQzone
3,we can see who had commented on on our friends' qqzone
4,u can get all friends' QQs and names by calling functions in getallfriends.py

python environment:
python3.6.3
requests
selenium
configparser
xlwt
re<
time

ps:maybe you should affirm whether u have chromedriver in ur environment
if u haven't got it, u should download from http://chromedriver.storage.googleapis.com/index.html first.
</ul>

<h1>operation environment</h1>
<ul>
<li>ubuntu17.10</li>
<li>chromium</li>

</ul>

<h1>project explaniation</h2>
<ul>
<li>open userinfo.ini,fill in ur qq_number,qq_password</li><br>
<li>open wanteduserinfo.ini,fill in ur friends' qq_number,qq_password,seprating by comma</li><br>
<li>enter the directory of project and type into "python qq_spider.py"，after a while, the data that u have got will be saved in the directory of friends,mood_detail</li><br>
  
<li>The final results will be saved in excel directory</li><br>
</ul>

<ul>
<li>reference</li><br>
  <a href="https://my.oschina.net/u/3264690/blog/1498751">抓取60000+QQ空间说说做一次数据分析
</a>

</ul>
