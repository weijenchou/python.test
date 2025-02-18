"""
pip install pytube
"""
from pytube import YouTube

def yt_d1(url):
    try:
        #實例化物件
        yt= YouTube(url)
        print(f'正在下載{yt.title}')

        #取得高畫質影片
        stream= yt.streams.get_highest_resolution()

        #下載
        stream.download()

        print(f'{yt.title}下載完成')

    except Exception as e:
        print(f'錯誤原因:{e}')

if __name__ =='__main__':
    url= input('輸入你的網址:')
    yt_d1(url)