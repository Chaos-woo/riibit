from weibo import fetch_weibo
from hot_36kr import fetch_36kr
from zhihu import fetch_zhihu
from zhihu_daily import fetch_zhihu_daily
from acfun import fetch_acfun
from baidu import fetch_baidu
from bilibili import fetch_bilibili
from douyin import fetch_douyin
from jianshu import fetch_jianshu
from juejin import fetch_juejin
from sspai import fetch_sspai
from tieba import fetch_tieba
from m_51cto import fetch_51cto
from douban_group import fetch_douban_group
from douban_movie import fetch_douban_movie
from hello_github import fetch_hello_github
from it_home import fetch_it_home
from netease_news import fetch_netease_news
from qq_news import fetch_qq_news
from the_paper import fetch_the_paper
from toutiao import fetch_toutiao
from v2ex import fetch_v2ex
from github_trending import fetch_github_trending
from anquanke import fetch_anquanke
from csdn import fetch_csdn
from dongqiudi import fetch_dongqiudi
from history_today import fetch_history_today

def test_main():
    print('test_main')


def main():
    fetch_weibo()
    fetch_36kr()
    fetch_zhihu()
    fetch_zhihu_daily()
    fetch_acfun()
    fetch_baidu()
    fetch_bilibili()
    fetch_douyin()
    fetch_juejin()
    fetch_jianshu()
    fetch_sspai()
    fetch_tieba()
    fetch_51cto()
    fetch_douban_group()
    fetch_douban_movie()
    fetch_hello_github()
    fetch_it_home()
    fetch_qq_news()
    fetch_the_paper()
    fetch_toutiao()
    fetch_v2ex()
    fetch_github_trending()
    fetch_anquanke()
    fetch_csdn()
    fetch_dongqiudi()
    fetch_history_today()


if __name__ == '__main__':
    main()
