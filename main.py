from weibo import fetch_weibo
from hot_36kr import fetch_36kr

def test_main():
    print('test_main')

def main():
    fetch_weibo()
    fetch_36kr()

if __name__ == '__main__':
    main()
