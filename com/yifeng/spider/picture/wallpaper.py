from urllib import request
import math
import re

'''
爬取小鸟壁纸高清美女大图
'''

base_url = 'http://wallpaper.apc.360.cn/index.php?c=WallPaper&a=getAppsByCategory&cid=6&count=10&start='

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
#保存到本地的路径地址
base_filepath = 'E:/wallpaper/'

total = 6705
count = 10
totalPage = math.ceil(total / count)

for i in range(0, totalPage):
    try:
        print("======开始下载第"+str(i+1)+"页的图片======")
        url = base_url + str(i * 10)
        req = request.Request(url, headers=header)
        resp = request.urlopen(req).read().decode('utf-8')
        pat = 'url_mobile":"(.*?)",'
        pat1 = '"url":"(.*?)",'
        pat2 = 'utag":"(.*?)",'
        url_mobile_list = re.compile(pat).findall(resp)
        url__list = re.compile(pat1).findall(resp)
        #utag_list = re.compile(pat2).findall(resp)

        for j in range(0, len(url_mobile_list)):
            download_url = url_mobile_list[j]
            #当url_mobile_list的地址为""时，采用url的地址
            if (download_url == ""):
                download_url = url__list[j]
            #将\/转换成/
            reurl = download_url.replace('\/', '/')

            #将Unicode中文编码转换成中文汉字，并利用这个ustag作为文件的名字
            #utag = utag_list[j].encode('utf-8').decode('unicode_escape')
            #request.urlretrieve(reurl, base_filepath + utag + '.jpg')

            # 使用数字作为图片名字
            request.urlretrieve(reurl, base_filepath + str(i+1) + str(j) + '.jpg')
        print("======第" + str(i + 1) + "页的图片下载完成======")
    except Exception as err:
        print(err)