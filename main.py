import datetime

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
from hupu import fetch_hupu
from m_3dm_game import fetch_3dm_game
from youshewang import fetch_youshewang
from woshipm import fetch_woshipm

def test_main():
    print('test_main')
    # fetch_woshipm()

def main():
    try_do(fetch_weibo)
    try_do(fetch_36kr)
    try_do(fetch_zhihu)
    try_do(fetch_zhihu_daily)
    try_do(fetch_acfun)
    try_do(fetch_baidu)
    try_do(fetch_bilibili)
    try_do(fetch_douyin)
    try_do(fetch_juejin)
    try_do(fetch_jianshu)
    try_do(fetch_sspai)
    try_do(fetch_tieba)
    try_do(fetch_51cto)
    try_do(fetch_douban_group)
    try_do(fetch_douban_movie)
    try_do(fetch_hello_github)
    try_do(fetch_it_home)
    try_do(fetch_qq_news)
    try_do(fetch_the_paper)
    try_do(fetch_toutiao)
    try_do(fetch_v2ex)
    try_do(fetch_github_trending)
    try_do(fetch_anquanke)
    try_do(fetch_csdn)
    try_do(fetch_dongqiudi)
    try_do(fetch_history_today)
    try_do(fetch_hupu)
    try_do(fetch_3dm_game)
    try_do(fetch_youshewang)

def try_do(f):
    try:
        print(f'try do {f.__name__} start {datetime.datetime.now(tz=datetime.timezone.utc)}')
        # 尝试执行传入的函数
        f()
    except Exception as e:
        # 处理异常，这里只是打印异常信息，可以根据需要进行其他操作
        print(f"捕获到异常：{e}")
    finally:
        print(f'try do {f.__name__} end')

if __name__ == '__main__':
    main()
