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

if __name__ == '__main__':
    main()
