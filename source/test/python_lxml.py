#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-11 17:12:02
# @Author  : Linsir (root@linsir.org)
# @Link    : http://linsir.org
# @Version :

data = '''

<html>
　　<head>
　　　　<meta name="content-type" content="text/html; charset=utf-8" />
　　　　<title>友情链接查询 - 站长工具</title>
　　　　<!-- uRj0Ak8VLEPhjWhg3m9z4EjXJwc -->
　　　　<meta name="Keywords" content="友情链接查询" />
　　　　<meta name="Description" content="友情链接查询" />

　　</head>
　　<body>
　　　　<h1 class="heading">Top News</h1>
　　　　<p style="font-size: 200%">World News only on this page</p>
　　　　Ah, and here's some more text, by the way.
　　　　<p>... and this is a parsed fragment ...</p>

　　　　<a href="http://www.cydf.org.cn/" rel="nofollow" target="_blank">青少年发展基金会</a>
　　　　<a href="http://www.4399.com/flash/32979.htm" target="_blank">洛克王国</a>
　　　　<a href="http://www.4399.com/flash/35538.htm" target="_blank">奥拉星</a>
　　　　<a href="http://game.3533.com/game/" target="_blank">手机游戏</a>
　　　　<a href="http://game.3533.com/tupian/" target="_blank">手机壁纸</a>
　　　　<a href="http://www.4399.com/" target="_blank">4399小游戏</a>
　　　　<a href="http://www.91wan.com/" target="_blank">91wan游戏</a>
    <form class="navbar-form" action="/search" method="get">
    <div class="form-group">
    <input type="text" placeholder="Search" class="form-control" name="key">
    </div>
    </form>

    <form id="lzform" name="lzform" method="post" onsubmit="return validateForm(this);" action="https://accounts.douban.com/login"><div style="display:none;"><input type="hidden" name="ck" value="V-sc"/></div>
      <div style="display:none;">
        <img src="https://www.douban.com/pics/blank.gif" onerror="document.lzform.action='https://accounts.douban.com/login'"/>
      </div>
      <input name="source" type="hidden" value="group"/>
        <input name="redir" type="hidden" value="https://www.douban.com"/>
      <div class="item-right">
        <a href="?redir=http://www.douban.com&amp;source=group&amp;login_type=sms">手机验证码登录</a>
      </div>
      <div class="item">
        <label>帐号</label>
        <input id="email" name="form_email" type="text" class="basic-input"
               maxlength="60" value="邮箱/手机号/用户名" tabindex="1"/>
      </div>
      <div class="item">
        <label>密码</label>
        <input id="password" name="form_password" type="password" class="basic-input" maxlength="20" tabindex="2"/>
      </div>
      <!-- d2sJX7XNueo | 118.113.41.16 -->
      
      <div class="item">
        <label>&nbsp;</label>
        <p class="remember">
          <input type="checkbox" id="remember" name="remember" tabindex="4"/>
          <label for="remember" class="remember">下次自动登录</label>
          | <a href="https://accounts.douban.com/resetpassword">忘记密码了</a>
        </p>
      </div>
      <div class="item">
        <label>&nbsp;</label>
        <input type="submit" value="登录" name="login" class="btn-submit" tabindex="5"/>
      </div>
      



    <div class="item item-3rd">
      <label>
      第三方登录：
      </label>
     <script>
        function before_qq_login(){
            if (!confirm("已不支持新用户QQ帐号登录，如果已经用过QQ帐号登录的请点击确定")){
                return false
            }
            return true
        }
    </script>
      <a target="_top" href="https://www.douban.com/accounts/connect/wechat/?from=douban-web&amp;redir=http%3A//www.douban.com" class="item-wechat"><img src="https://img3.doubanio.com/f/accounts/1b6cc3ca91f78cf47f41eafa91fbcd4918ae239c/pics/connect_wechat.png" title="微信"></a>
      <a target="_top" href="https://www.douban.com/accounts/connect/sina_weibo/?from=douban-web&amp;redir=http%3A//www.douban.com&amp;fallback=" class="item-weibo"><img src="https://img3.doubanio.com/f/accounts/e2f1d8c0ede93408b46cbbab4e613fb29ba94e35/pics/connect_sina_weibo.png" title="新浪微博"></a>
        <a target="_top" href="https://www.douban.com/accounts/connect/qq/?from=group&amp;redir=http%3A//www.douban.com" onclick="javascript:return before_qq_login()" class="item-qq"><img src="https://img3.doubanio.com/f/accounts/be10f8fb4a3fd87f2f0d2fa18ed83b7d6b880697/pics/connect_qq.png" title="QQ"></a>
    </div>

    </form>
　　</body>
</html>

'''

from lxml.html import fromstring, tostring
page = fromstring(data.lower().decode('utf-8'))

for i in page.forms:
#    print i.attrib
    for element in i.iter():
        if  element.tag == 'input':
            print element.attrib
    print '\n'
