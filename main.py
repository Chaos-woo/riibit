from weibo import fetch_weibo
from hot_36kr import fetch_36kr
from zhihu import fetch_zhihu
from zhihu_daily import fetch_zhihu_daily

def test_main():
    print('test_main')


def main():
    fetch_weibo()
    fetch_36kr()
    fetch_zhihu()
    fetch_zhihu_daily()

if __name__ == '__main__':
    main()
