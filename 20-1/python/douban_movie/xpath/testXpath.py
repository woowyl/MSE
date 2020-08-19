# coding: utf-8
import requests 
import json
from lxml import etree
import csv
import time 
import random
from bs4 import BeautifulSoup
import bs4
import os.path
from fake_useragent import UserAgent  
from requests.adapters import HTTPAdapter
import re
import emoji

def tetXpath():
        html = '''<!DOCTYPE html>
<html lang="zh-CN" class="ua-windows ua-webkit">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <title>
        海王 (豆瓣)
</title>
    
    <meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
    <link rel="apple-touch-icon" href="https://img9.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
    <link href="https://img9.doubanio.com/f/shire/b8383160c4478308dcfd49d1363ebfffbb93a017/css/douban.css" rel="stylesheet" type="text/css">
    <link href="https://img9.doubanio.com/f/shire/f1cf2b03de9dd8c9c233229c819fc1f993ba9b0d/css/separation/_all.css" rel="stylesheet" type="text/css">
    <link href="https://img9.doubanio.com/f/movie/8864d3756094f5272d3c93e30ee2e324665855b0/css/movie/base/init.css" rel="stylesheet">
    <script type="text/javascript">var _head_start = new Date();</script>
    <script type="text/javascript" src="https://img9.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
    <script type="text/javascript" src="https://img9.doubanio.com/f/shire/5ecaf46d6954d5a30bc7d99be86ae34031646e00/js/douban.js"></script>
    <script type="text/javascript" src="https://img9.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js"></script>
    
    <meta name="keywords" content="海王,Aquaman,海王影评,剧情介绍,电影图片,预告片,影讯,在线购票,论坛">
    <meta name="description" content="海王电影简介和剧情介绍,海王影评、图片、预告片、影讯、论坛、在线购票">
    <meta name="mobile-agent" content="format=html5; url=https://m.douban.com/movie/subject/3878007/"/>
    <link rel="alternate" href="android-app://com.douban.movie/doubanmovie/subject/3878007/" />
    <link rel="stylesheet" href="https://img9.doubanio.com/dae/cdnlib/libs/LikeButton/1.0.5/style.min.css">
    <script type="text/javascript" src="https://img9.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
    <style type="text/css">img { max-width: 100%; }</style>
    <script type="text/javascript"></script>
    <link rel="stylesheet" href="https://img9.doubanio.com/misc/mixed_static/1fc65bc9b908d65e.css">

    <link rel="shortcut icon" href="https://img9.doubanio.com/favicon.ico" type="image/x-icon">
</head>

<body>
  
    
<div id="db-global-nav" class="global-nav">
    <div class="bd">
        
    <div class="top-nav-info">
    <a href="https://accounts.douban.com/passport/login?source=movie" class="nav-login" rel="nofollow">登录/注册</a>
    </div>


    <div class="top-nav-doubanapp">
        <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
        <div id="doubanapp-tip">
            <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
            <a href="javascript: void 0;" class="tip-close">×</a>
        </div>
        <div id="top-nav-appintro" class="more-items">
                <p class="appintro-title">豆瓣</p>
                <p class="qrcode">扫码直接下载</p>
                <div class="download">
                    <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
                    <span>·</span>
                    <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
                </div>
        </div>
    </div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="">
      <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="on">
      <a href="https://movie.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">豆品</a>
    </li>
  </ul>
</div>

  </div>
</div>



<div id="db-nav-movie" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;movie.douban.com">豆瓣电影</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;search.douban.com&#47;movie/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="搜索电影、电视剧、综艺、影人" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1002" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li    ><a href="https://movie.douban.com/cinema/nowplaying/"
     >影讯&购票</a>
    </li>
    <li    ><a href="https://movie.douban.com/explore"
     >选电影</a>
    </li>
    <li    ><a href="https://movie.douban.com/tv/"
     >电视剧</a>
    </li>
    <li    ><a href="https://movie.douban.com/chart"
     >排行榜</a>
    </li>
    <li    ><a href="https://movie.douban.com/tag/"
     >分类</a>
    </li>
    <li    ><a href="https://movie.douban.com/review/best/"
     >影评</a>
    </li>
    <li    ><a href="https://movie.douban.com/annual/2019?source=navigation"
     >2019年度榜单</a>
    </li>
    <li    ><a href="https://m.douban.com/standbyme/annual2019?source=navigation"
            target="_blank"
     >2019书影音报告</a>
    </li>
  </ul>
</div>

    <a href="https://movie.douban.com/annual/2019?source=movie_navigation" class="movieannual"></a>
  </div>
</div>

    <div id="wrapper">
        

        
    <div id="content">
        

    <div id="dale_movie_subject_top_icon"></div>
    <h1>
        <span property="v:itemreviewed">海王 Aquaman</span>
            <span class="year">(2018)</span>
    </h1>

        <div class="grid-16-8 clearfix">
            

            
            <div class="article">

        <div class="indent clearfix">
            <div class="subjectwrap clearfix">
                <div class="subject clearfix">

<div id="info">
        <span ><span class='pl'>导演</span>: <span class='attrs'><a href="/celebrity/1032122/" rel="v:directedBy">温子仁</a></span></span><br/>
        <span ><span class='pl'>编剧</span>: <span class='attrs'><a href="/celebrity/1351120/">大卫·莱斯利·约翰逊-麦戈德里克</a> / <a href="/celebrity/1326235/">威尔·比尔</a> / <a href="/celebrity/1005296/">乔夫·琼斯</a> / <a href="/celebrity/1032122/">温子仁</a> / <a href="/celebrity/1047241/">莫尔特·魏辛格</a> / <a href="/celebrity/1397492/">保罗·诺里斯</a></span></span><br/>
        <span class="actor"><span class='pl'>主演</span>: <span class='attrs'><a href="/celebrity/1022614/" rel="v:starring">杰森·莫玛</a> / <a href="/celebrity/1044702/" rel="v:starring">艾梅柏·希尔德</a> / <a href="/celebrity/1010539/" rel="v:starring">威廉·达福</a> / <a href="/celebrity/1006919/" rel="v:starring">帕特里克·威尔森</a> / <a href="/celebrity/1054442/" rel="v:starring">妮可·基德曼</a> / <a href="/celebrity/1040508/" rel="v:starring">杜夫·龙格尔</a> / <a href="/celebrity/1374708/" rel="v:starring">叶海亚·阿卜杜勒-迈丁</a> / <a href="/celebrity/1013898/" rel="v:starring">特穆拉·莫里森</a> / <a href="/celebrity/1351645/" rel="v:starring">林路迪</a> / <a href="/celebrity/1041218/" rel="v:starring">迈克尔·比奇</a> / <a href="/celebrity/1345622/" rel="v:starring">兰道尔·朴</a> / <a href="/celebrity/1323191/" rel="v:starring">格拉汉姆·麦克泰维什</a> / <a href="/celebrity/1014029/" rel="v:starring">雷·沃纳尔</a> / <a href="/celebrity/1406310/" rel="v:starring">泰努伊·柯克伍德</a> / <a href="/celebrity/1406311/" rel="v:starring">塔穆尔·柯克伍德</a> / <a href="/celebrity/1406390/" rel="v:starring">丹泽尔·夸克</a> / <a href="/celebrity/1385540/" rel="v:starring">卡恩·古尔杜尔</a> / <a href="/celebrity/1405972/" rel="v:starring">奥蒂斯·丹吉</a> / <a href="/celebrity/1406391/" rel="v:starring">克考亚·克库毛诺</a> / <a href="/celebrity/1041081/" rel="v:starring">朱莉·安德鲁斯</a> / <a href="/celebrity/1147054/" rel="v:starring">约翰·瑞斯-戴维斯</a> / <a href="/celebrity/1044880/" rel="v:starring">杰曼·翰苏</a> / <a href="/celebrity/1406293/" rel="v:starring">索菲亚·福雷斯特</a> / <a href="/celebrity/1336790/" rel="v:starring">娜塔莉·萨福兰</a> / <a href="/celebrity/1406307/" rel="v:starring">杰克·安德鲁</a> / <a href="/celebrity/1277175/" rel="v:starring">汉克·阿莫斯</a> / <a href="/celebrity/1406295/" rel="v:starring">帕特里克·考克斯</a> / <a href="/celebrity/1390002/" rel="v:starring">罗伯特·朗斯特里特</a> / <a href="/celebrity/1133501/" rel="v:starring">德维卡·帕利赫</a> / <a href="/celebrity/1406306/" rel="v:starring">梅布尔·塔莫内</a> / <a href="/celebrity/1256160/" rel="v:starring">文森特·B·拉戈斯</a> / <a href="/celebrity/1406296/" rel="v:starring">加布里埃拉·佩特科娃</a> / <a href="/celebrity/1406294/" rel="v:starring">爱丽丝·兰斯伯里</a> / <a href="/celebrity/1406299/" rel="v:starring">帕特里克·艾奇逊</a> / <a href="/celebrity/1392772/" rel="v:starring">约翰·盖蒂尔</a> / <a href="/celebrity/1406292/" rel="v:starring">塔丽亚·杰德·霍尔特</a> / <a href="/celebrity/1406300/" rel="v:starring">罗斯·克纳汉</a> / <a href="/celebrity/1406309/" rel="v:starring">布拉登·刘易斯</a> / <a href="/celebrity/1406308/" rel="v:starring">萨尔瓦多·梅伦达</a> / <a href="/celebrity/1406305/" rel="v:starring">山姆·莫纳汉</a> / <a href="/celebrity/1406301/" rel="v:starring">温妮·穆赞贝</a> / <a href="/celebrity/1254341/" rel="v:starring">凯·潘塔诺</a> / <a href="/celebrity/1406297/" rel="v:starring">安娜·帕奇</a> / <a href="/celebrity/1406303/" rel="v:starring">乔恩·奎斯蒂德</a> / <a href="/celebrity/1406302/" rel="v:starring">迪伦·斯图默</a> / <a href="/celebrity/1406298/" rel="v:starring">米奇·武尔夫</a></span></span><br/>
        <span class="pl">类型:</span> <span property="v:genre">动作</span> / <span property="v:genre">奇幻</span> / <span property="v:genre">冒险</span><br/>
        <span class="pl">官方网站:</span> <a href="http://www.aquamanmovie.com" rel="nofollow" target="_blank">www.aquamanmovie.com</a><br/>
        <span class="pl">制片国家/地区:</span> 美国 / 澳大利亚<br/>
        <span class="pl">语言:</span> 英语 / 毛利语 / 意大利语 / 俄语<br/>
        <span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="2018-12-07(中国大陆)">2018-12-07(中国大陆)</span> / <span property="v:initialReleaseDate" content="2018-12-21(美国)">2018-12-21(美国)</span><br/>
        <span class="pl">片长:</span> <span property="v:runtime" content="143">143分钟</span><br/>
        <span class="pl">又名:</span> 水行侠(港/台) / 潜水侠 / 水人 / 人鱼哥(豆友译名)<br/>
        <span class="pl">IMDb链接:</span> <a href="https://www.imdb.com/title/tt1477834" target="_blank" rel="nofollow">tt1477834</a><br>

</div>




                </div>
                    


<div id="interest_sectl">
    <div class="rating_wrap clearbox" rel="v:rating">
        <div class="clearfix">
          <div class="rating_logo ll">豆瓣评分</div>
          <div class="output-btn-wrap rr" style="display:none">
            <img src="https://img9.doubanio.com/f/movie/692e86756648f29457847c5cc5e161d6f6b8aaac/pics/movie/reference.png" />
            <a class="download-output-image" href="#">引用</a>
          </div>
          
          
        </div>
        



<div class="rating_self clearfix" typeof="v:Rating">
    <strong class="ll rating_num" property="v:average">7.6</strong>
    <span property="v:best" content="10.0"></span>
    <div class="rating_right ">
        <div class="ll bigstar bigstar40"></div>
        <div class="rating_sum">
                <a href="collections" class="rating_people">
                    <span property="v:votes">743569</span>人评价
                </a>
        </div>
    </div>
</div>
<div class="ratings-on-weight">
    
        <div class="item">
        
        <span class="stars5 starstop" title="力荐">
            5星
        </span>
        <div class="power" style="width:31px"></div>
        <span class="rating_per">21.3%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars4 starstop" title="推荐">
            4星
        </span>
        <div class="power" style="width:64px"></div>
        <span class="rating_per">43.1%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars3 starstop" title="还行">
            3星
        </span>
        <div class="power" style="width:44px"></div>
        <span class="rating_per">30.3%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars2 starstop" title="较差">
            2星
        </span>
        <div class="power" style="width:6px"></div>
        <span class="rating_per">4.5%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars1 starstop" title="很差">
            1星
        </span>
        <div class="power" style="width:1px"></div>
        <span class="rating_per">0.9%</span>
        <br />
        </div>
</div>

    </div>
        <div class="rating_betterthan">
            好于 <a href="/typerank?type_name=奇幻&type=16&interval_id=75:65&action=">72% 奇幻片</a><br/>
            好于 <a href="/typerank?type_name=动作&type=5&interval_id=85:75&action=">82% 动作片</a><br/>
        </div>
</div>


                
            </div>
                




<div id="interest_sect_level" class="clearfix">
        
            <a href="https://www.douban.com/reason=collectwish&amp;ck=" rel="nofollow" class="j a_show_login colbutt ll" name="pbtn-3878007-wish">
                <span>想看</span>
            </a>
            <a href="https://www.douban.com/reason=collectcollect&amp;ck=" rel="nofollow" class="j a_show_login colbutt ll" name="pbtn-3878007-collect">
                <span>看过</span>
            </a>
        <div class="ll j a_stars">
            
    
    评价:
    <span id="rating"> <span id="stars" data-solid="https://img9.doubanio.com/f/shire/5a2327c04c0c231bced131ddf3f4467eb80c1c86/pics/rating_icons/star_onmouseover.png" data-hollow="https://img9.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" data-solid-2x="https://img9.doubanio.com/f/shire/7258904022439076d57303c3b06ad195bf1dc41a/pics/rating_icons/star_onmouseover@2x.png" data-hollow-2x="https://img9.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png">

            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-3878007-1">
        <img src="https://img9.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star1" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-3878007-2">
        <img src="https://img9.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star2" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-3878007-3">
        <img src="https://img9.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star3" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-3878007-4">
        <img src="https://img9.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star4" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-3878007-5">
        <img src="https://img9.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star5" width="16" height="16"/></a>
    </span><span id="rateword" class="pl"></span>
    <input id="n_rating" type="hidden" value=""  />
    </span>

        </div>
    

</div>


            

















<div class="gtleft">
    <ul class="ul_subject_menu bicelink color_gray pt6 clearfix">
        
    
        
                <li> 
    <img src="https://img9.doubanio.com/f/shire/cc03d0fcf32b7ce3af7b160a0b85e5e66b47cc42/pics/short-comment.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_cmnt_login'})" class="j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">写短评</a>
 </li>
                    <li> 
    
    <img src="https://img9.doubanio.com/f/shire/5bbf02b7b5ec12b23e214a580b6f9e481108488c/pics/add-review.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_rv_login'})" class="j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">写影评</a>
 </li>
                <li> 
    



 </li>
                <li> 
   

   
    
    <span class="rec" id="电影-3878007">
    <a href= "#"
        data-type="电影"
        data-url="https://movie.douban.com/subject/3878007/"
        data-desc="电影《海王 Aquaman》 (来自豆瓣) "
        data-title="电影《海王 Aquaman》 (来自豆瓣) "
        data-pic="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2541280047.jpeg"
        class="bn-sharing ">
        分享到
    </a> &nbsp;&nbsp;
    </span>

    <script>
        if (!window.DoubanShareMenuList) {
            window.DoubanShareMenuList = [];
        }
        var __cache_url = __cache_url || {};

        (function(u){
            if(__cache_url[u]) return;
            __cache_url[u] = true;
            window.DoubanShareIcons = 'https://img9.doubanio.com/f/shire/d15ffd71f3f10a7210448fec5a68eaec66e7f7d0/pics/ic_shares.png';

            var initShareButton = function() {
                $.ajax({url:u,dataType:'script',cache:true});
            };

            if (typeof Do == 'function' && 'ready' in Do) {
                Do(
                    'https://img9.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img9.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js',
                    'https://img9.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js',
                    initShareButton
                );
            } else if(typeof Douban == 'object' && 'loader' in Douban) {
                Douban.loader.batch(
                    'https://img9.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img9.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js',
                    'https://img9.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js'
                ).done(initShareButton);
            }

        })('https://img9.doubanio.com/f/movie/32be6727ed3ad8f6c4a417d8a086355c3e7d1d27/js/movie/lib/sharebutton.js');
    </script>


  </li>
            

    </ul>

    <script type="text/javascript">
        $(function(){
            $(".ul_subject_menu li.rec .bn-sharing").bind("click", function(){
                $.get("/blank?sbj_page_click=bn_sharing");
            });
            $(".ul_subject_menu .create_from_menu").bind("click", function(e){
                e.preventDefault();
                var $el = $(this);
                var glRoot = document.getElementById('gallery-topics-selection');
                if (window.has_gallery_topics && glRoot) {
                    // 判断是否有话题
                    glRoot.style.display = 'block';
                } else {
                    location.href = $el.attr('href');
                }
            });
        });
    </script>
</div>




                




<div class="rec-sec">
<span class="rec">
    <script id="movie-share" type="text/x-html-snippet">
        
    <form class="movie-share" action="/j/share" method="POST">
        <div class="clearfix form-bd">
            <div class="input-area">
                <textarea name="text" class="share-text" cols="72" data-mention-api="https://api.douban.com/shuo/in/complete?alt=xd&amp;callback=?"></textarea>
                <input type="hidden" name="target-id" value="3878007">
                <input type="hidden" name="target-type" value="0">
                <input type="hidden" name="title" value="海王 Aquaman‎ (2018)">
                <input type="hidden" name="desc" value="导演 温子仁 主演 杰森·莫玛 / 艾梅柏·希尔德 / 美国 / 澳大利亚 / 7.6分(743569评价)">
                <input type="hidden" name="redir" value=""/>
                <div class="mentioned-highlighter"></div>
            </div>

            <div class="info-area">
                    <img class="media" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2541280047.jpg" />
                <strong>海王 Aquaman‎ (2018)</strong>
                <p>导演 温子仁 主演 杰森·莫玛 / 艾梅柏·希尔德 / 美国 / 澳大利亚 / 7.6分(743569评价)</p>
                <p class="error server-error">&nbsp;</p>
            </div>
        </div>
        <div class="form-ft">
            <div class="form-ft-inner">
                



                <span class="avail-num-indicator">140</span>
                <span class="bn-flat">
                    <input type="submit" value="推荐" />
                </span>
            </div>
        </div>
    </form>
    
    <div id="suggest-mention-tmpl" style="display:none;">
        <ul>
            {{#users}}
            <li id="{{uid}}">
              <img src="{{avatar}}">{{{username}}}&nbsp;<span>({{{uid}}})</span>
            </li>
            {{/users}}
        </ul>
    </div>


    </script>

        
        <a href="/accounts/register?reason=recommend"  class="j a_show_login lnk-sharing" 
            share-id="3878007" 
            data-mode="plain" data-name="海王 Aquaman‎ (2018)" 
            data-type="movie" data-desc="导演 温子仁 主演 杰森·莫玛 / 艾梅柏·希尔德 / 美国 / 澳大利亚 / 7.6分(743569评价)" 
            data-href="https://movie.douban.com/subject/3878007/" data-image="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2541280047.jpg" 
            data-properties="{}" 
            data-redir="" data-text="" 
            data-apikey="" data-curl="" 
            data-count="10" data-object_kind="1002" 
            data-object_id="3878007" data-target_type="rec" 
            data-target_action="0" 
            data-action_props="{&#34;subject_url&#34;:&#34;https:\/\/movie.douban.com\/subject\/3878007\/&#34;,&#34;subject_title&#34;:&#34;海王 Aquaman‎ (2018)&#34;}">推荐</a>
</span>


</div>






            <script type="text/javascript">
                $(function() {
                    $('.collect_btn', '#interest_sect_level').each(function() {
                        Douban.init_collect_btn(this);
                    });
                    $('html').delegate(".indent .rec-sec .lnk-sharing", "click", function() {
                        moreurl(this, {
                            from : 'mv_sbj_db_share'
                        });
                    });
                });
            </script>
        </div>
            


    <div id="collect_form_3878007"></div>


        





    <div id="dale_movie_subject_banner_after_intro"></div>

    <div id="comments-section">
        <div class="mod-hd">
            
            
        <a class="comment_btn j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">
            <span>我要写短评</span>
        </a>

            
    <h2>
        <i class="">海王的短评</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/3878007/comments?status=P">全部 224101 条</a>
            )
            </span>
    </h2>

            
        </div>
        <div class="mod-bd">
                

            <div class="tab-hd">
                <a id="hot-comments-tab" href="comments" data-id="hot" class="on">热门</a>&nbsp;/&nbsp;
                    <a id="new-comments-tab" href="comments?sort=time" data-id="new">最新</a>&nbsp;/&nbsp;
                <a id="following-comments-tab" href="follows_comments" data-id="following"  class="j a_show_login">好友</a>
            </div>

            <div class="tab-bd">
                <div id="hot-comments" class="tab">
                    <div class="comment-item" data-cid="1541999923">               
                        <div class="comment">
                            <h3>
                                <span class="comment-vote">
                                    <span class="votes">6629</span>
                                    <input value="1541999923" type="hidden"/>
                                    <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
                                </span>
                                <span class="comment-info">
                                    <a href="https://www.douban.com/people/luzhiyu/" class="">陆支羽</a>
                                        <span>看过</span>
                                        <span class="allstar40 rating" title="推荐"></span>
                                    <span class="comment-time " title="2018-12-04 23:58:18">
                                        2018-12-04
                                    </span>
                                </span>
                            </h3>
                            <p class="">
                                
                                    <span class="short">4.5。1.从造梦层面而言，温子仁真的远超我的预期；如果你觉得这也算失手，那我无话可说，只能闭嘴。2.这场梦始于失落的亚特兰蒂斯，继而又按图索骥，如探索迷宫般牵引出整座深海帝国的神秘版图，看似不过闯关游戏式的老套路，其实还是以西方古典神话为模本的，类似亚瑟王寻找圣杯。3.固然温子仁并没有全然秉承DC的暗黑风格，但那场海王亚瑟与守护三叉戟的海怪之间的对话，着实是以DC的方式丰满了角色。4.要说不足，...</span>
                                    <span class="hide-item full">4.5。1.从造梦层面而言，温子仁真的远超我的预期；如果你觉得这也算失手，那我无话可说，只能闭嘴。2.这场梦始于失落的亚特兰蒂斯，继而又按图索骥，如探索迷宫般牵引出整座深海帝国的神秘版图，看似不过闯关游戏式的老套路，其实还是以西方古典神话为模本的，类似亚瑟王寻找圣杯。3.固然温子仁并没有全然秉承DC的暗黑风格，但那场海王亚瑟与守护三叉戟的海怪之间的对话，着实是以DC的方式丰满了角色。4.要说不足，西西里跑酷略显脱节，而海底决战时刻有点场面失控。</span>
                                    <span class="expand">(<a href="javascript:;">展开</a>)</span>
                            </p>
                        </div>
                    </div>
                    
                    <div class="comment-item" data-cid="1498198779">
                        <div class="comment">
                            <h3>
                                <span class="comment-vote">
                                    <span class="votes">2797</span>
                                    <input value="1498198779" type="hidden"/>
                                    <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
                                </span>
                                <span class="comment-info">
                                    <a href="https://www.douban.com/people/60307113/" class="">AZWayne</a>
                                        <span>看过</span>
                                        <span class="allstar50 rating" title="力荐"></span>
                                    <span class="comment-time " title="2018-12-07 01:49:14">
                                        2018-12-07
                                    </span>
                                </span>
                            </h3>
                            <p class="">
                                
                                    <span class="short">马王没能统一的七国终于在变身海王后统一七海了。</span>
                            </p>
                        </div>
                    </div>
        
                    <div class="comment-item" data-cid="1558439746">
                            <div class="comment">
                                <h3>
                                    <span class="comment-vote">
                                        <span class="votes">2151</span>
                                        <input value="1558439746" type="hidden"/>
                                        <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
                                    </span>
                                    <span class="comment-info">
                                        <a href="https://www.douban.com/people/MovieL/" class="">木卫二</a>
                                            <span>看过</span>
                                            <span class="allstar30 rating" title="还行"></span>
                                        <span class="comment-time " title="2018-12-07 10:16:01">
                                            2018-12-07
                                        </span>
                                    </span>
                                </h3>
                                <p class="">
                                    
                                        <span class="short">一出爽片，告诉D家还是别玩深沉，适当鸡汤、疯狂爆米花，这不就挺好。放几个微博号，拔高至电影史，完全不必——太像一堆水炮。电影算好看啦，问题有超级英雄的自身软肋，像除了不想当海王，就没有性格毛病了。温子仁花大气力构筑的不同场景，确实花哨诡奇，但始终难以统一，比如那段跑酷的必要性，比如两次大场面，全部靠鱼海对决，看多了还是一个样。角色参与感太弱，尽管虾兵蟹将死那么多，who cares。一致叫好的海沟...</span>
                                        <span class="hide-item full">一出爽片，告诉D家还是别玩深沉，适当鸡汤、疯狂爆米花，这不就挺好。放几个微博号，拔高至电影史，完全不必——太像一堆水炮。电影算好看啦，问题有超级英雄的自身软肋，像除了不想当海王，就没有性格毛病了。温子仁花大气力构筑的不同场景，确实花哨诡奇，但始终难以统一，比如那段跑酷的必要性，比如两次大场面，全部靠鱼海对决，看多了还是一个样。角色参与感太弱，尽管虾兵蟹将死那么多，who cares。一致叫好的海沟族，是照恐怖片的惊骇拍法，私货刺激，构思清奇（却还是解决不了我的困惑：主人公在海里像鱼雷速度，坐人类小船飘啊摇的干嘛）。至于夺王位的故事，全部是抡叉撸铁的蛮力角斗，打不死不说，挂个彩都好难。最后，那位苍蝇头反派，真的不是用来搞笑吗</span>
                                        <span class="expand">(<a href="javascript:;">展开</a>)</span>
                                </p>
                            </div>
                    </div>
        
                    <div class="comment-item" data-cid="1018262359">
                        <div class="comment">
                            <h3>
                                <span class="comment-vote">
                                    <span class="votes">2442</span>
                                    <input value="1018262359" type="hidden"/>
                                    <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
                                </span>
                                <span class="comment-info">
                                    <a href="https://www.douban.com/people/adakenndy/" class="">Ada🧣Wong💋💍</a>
                                        <span>看过</span>
                                        <span class="allstar50 rating" title="力荐"></span>
                                    <span class="comment-time " title="2018-12-07 00:52:02">
                                        2018-12-07
                                    </span>
                                </span>
                            </h3>
                            <p class="">
                                
                                    <span class="short">建议JL电影所有负责人全体跪着看完海王自我反省写1000字检讨！ 👍温导亲自示范教如何拿1.6亿拍出3亿的史诗效果。如果女侠拯救了DC，那温导海王就是惊艳了DCEU！谨代表所有漫改粉公车上书强烈要求华纳令温子仁掌舵DC宇宙！和以往所有的超级英雄电影都不同，仰拍俯拍长镜头用到炉火纯青，总结就是气势恢宏，格局庞大。华纳DC定律：动画电影拍的一般的，真人电影都不错。视觉效果星球大战+阿凡达+哥斯拉，无需...</span>
                                    <span class="hide-item full">建议JL电影所有负责人全体跪着看完海王自我反省写1000字检讨！ 👍温导亲自示范教如何拿1.6亿拍出3亿的史诗效果。如果女侠拯救了DC，那温导海王就是惊艳了DCEU！谨代表所有漫改粉公车上书强烈要求华纳令温子仁掌舵DC宇宙！和以往所有的超级英雄电影都不同，仰拍俯拍长镜头用到炉火纯青，总结就是气势恢宏，格局庞大。华纳DC定律：动画电影拍的一般的，真人电影都不错。视觉效果星球大战+阿凡达+哥斯拉，无需再多赘述赞美之语，海王亚瑟举起波赛冬三叉戟那一刻正式象征着DC继诺兰蝙蝠侠三部曲之后再次崛起势不可挡！再拍第二个BVS和对路人不友好DCEU就是死路一条！DC宇宙需要多元化发展而不是抱残守缺死守一角！黑深残从来不等于DC，我觉得是时候要扎斯林这块毒瘤划清界限了，祸害DCEU还不够吗？</span>
                                    <span class="expand">(<a href="javascript:;">展开</a>)</span>
                            </p>
                        </div>
                    </div>
        
                    <div class="comment-item" data-cid="1558007792">
                                <div class="comment">
                                    <h3>
                                        <span class="comment-vote">
                                            <span class="votes">1413</span>
                                            <input value="1558007792" type="hidden"/>
                                            <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
                                        </span>
                                        <span class="comment-info">
                                            <a href="https://www.douban.com/people/48369193/" class="">二十二岛主</a>
                                                <span>看过</span>
                                                <span class="allstar40 rating" title="推荐"></span>
                                            <span class="comment-time " title="2018-12-07 00:04:52">
                                                2018-12-07
                                            </span>
                                        </span>
                                    </h3>
                                    <p class="">
                                        
                                            <span class="short">没有一些人吹的那么高，但足够精彩。温子仁没疯，他只是太会讲故事，太会知道如何调动观众的肾上腺素，无论是以前拍恐怖片、动作片，还是这次拍超级英雄片，什么时候该打斗，什么时候该落寞，什么时候该摆pose，什么时候该接吻，什么时候该逗比，他在这些已经程式化的东西中加入了自己的天马行空，于是我们跟随着海王和湄拉的脚步上天入地下海，从一个夺位权谋片生生变成了热血冒险片。不得不说这部的特效确实是目前能想到的最...</span>
                                            <span class="hide-item full">没有一些人吹的那么高，但足够精彩。温子仁没疯，他只是太会讲故事，太会知道如何调动观众的肾上腺素，无论是以前拍恐怖片、动作片，还是这次拍超级英雄片，什么时候该打斗，什么时候该落寞，什么时候该摆pose，什么时候该接吻，什么时候该逗比，他在这些已经程式化的东西中加入了自己的天马行空，于是我们跟随着海王和湄拉的脚步上天入地下海，从一个夺位权谋片生生变成了热血冒险片。不得不说这部的特效确实是目前能想到的最顶级的展现，各种奇观应有尽有。而海王的成长，也是战胜自卑接受使命的过程，甚至有几分东方武侠的风韵。只可惜故事本身太过套路，确实乏善可陈，只能以特效和热血来弥补了。</span>
                                            <span class="expand">(<a href="javascript:;">展开</a>)</span>
                                    </p>
                                </div>
                    </div>
                    &gt; <a href="comments?sort=new_score&status=P" >
                        更多短评
                            224101条
                    </a>
                </div>
                <div id="new-comments" class="tab">
                    <div id="normal">
                    </div>
                    <div class="fold-hd hide">
                        <a class="qa" href="/help/opinion#t2-q0" target="_blank">为什么被折叠？</a>
                        <a class="btn-unfold" href="#">有一些短评被折叠了</a>
                        <div class="qa-tip">
                            评论被折叠，是因为发布这条评论的帐号行为异常。评论仍可以被展开阅读，对发布人的账号不造成其他影响。如果认为有问题，可以<a href="https://help.douban.com/help/ask?category=movie">联系</a>豆瓣电影。
                        </div>
                    </div>
                    <div class="fold-bd">
                    </div>
                    <span id="total-num"></span>
                </div>
                <div id="following-comments" class="tab">
                    <div class="comment-item">
                        你关注的人还没写过短评
                    </div>
                </div>
            </div>


            
            
        </div>
    </div>




        
    
        
                





<div id="askmatrix">



</div>



            </div>

        </div>
    </div>

        
    </div>

</body>

</html>
    '''
        film = {}
        html2 = '''<!DOCTYPE html><html>
            <body>
                 <div id="wrapper">test</div>
            </body></html>'''
        html_elem = etree.HTML(give_emoji_free_text(html))
        print(str(html_elem))
        film['title'] = '/'.join(html_elem.xpath('//span[@property="v:itemreviewed"]/text()'))
        film['year'] = '/'.join(html_elem.xpath('//span[@class="year"]/text()')).replace('(','').replace(')', '')
        film['director'] = '/'.join(html_elem.xpath('//a[@rel="v:directedBy"]/text()'))
        film['screenwriter'] = '/'.join(html_elem.xpath('//div[@id="info"]/span[2]/span[@class="attrs"]/a/text()'))
        film['actors'] = '/'.join(html_elem.xpath('//div[@id="info"]/span[@class="actor"]/span[@class="attrs"]/a[@rel="v:starring"]/text()'))
        film['type'] = '/'.join(html_elem.xpath('//div[@id="info"]/span[@property="v:genre"]/text()'))
        film['runtime'] = '/'.join(html_elem.xpath('//div[@id="info"]/span[@property="v:runtime"]/text()'))
        film['pubtime'] = '/'.join(html_elem.xpath('//div[@id="info"]/span[@property="v:initialReleaseDate"]/text()'))
        film['country'] = getFistEleFromList(html_elem.xpath('//*[@id="info"]/text()[preceding-sibling::span[contains(text(), "制片国家/地区:")] and following-sibling::br]'))
        # film['alias'] = getFistEleFromList(html_elem.xpath('//*[@id="info"]/text()[preceding-sibling::span[contains(text(), "制片国家/地区:")] and following-sibling::br]'))
        film['language'] = getFistEleFromList(html_elem.xpath('//*[@id="info"]/text()[preceding-sibling::span[contains(text(), "语言:")] and following-sibling::br]'))
        film['scoreNum'] = getFistEleFromList(html_elem.xpath('//span[@property="v:votes"]/text()'))
        film['score'] = getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()'))
        film['star5'] =getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[1]/span[2]/text()'))
        film['star4'] =getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[2]/span[2]/text()'))
        film['star3'] =getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[3]/span[2]/text()'))
        film['star2'] =getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[4]/span[2]/text()'))
        film['star1'] =getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[5]/span[2]/text()'))
        film['smallCommentNum'] = getDigit('/'.join(html_elem.xpath('//*[@id="comments-section"]/div[1]/h2/span/a/text()')))
        film['longCommentNum'] = getDigit('/'.join(html_elem.xpath('//*[@id="reviews-wrapper"]/header/h2/span/a/text()')))
        film['posterurl'] = getFistEleFromList(html_elem.xpath('//img[@rel="v:image"]/@src'))
        film['summary'] = '/'.join(getFistEleFromList(html_elem.xpath('//*[@id="link-report"]/span/text()'))).strip().replace('\n', '').replace('\r', '')
        #return data
        print("film data ==",film)
        return film
def give_emoji_free_text(text):
    allchars = [str for str in text.encode().decode('utf-8')]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.encode().decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text
    
def getDigit(str):
    return ''.join([x for x in str if x.isdigit()])

def getFistEleFromList(list): 
    if len(list) > 0 : 
        return list[0]
    else :
        return ''

# 爬取详情页
if __name__ == '__main__':
    tetXpath()
    