from bs4 import BeautifulSoup
import requests

# https://blog.51cto.com/u_1145004/1099592
# 自行查找
def get_whether(city):
    citycode = {
    '北京': '101010100',
    '海淀': '101010200',
    '朝阳': '101010300',
    '顺义': '101010400',
    '怀柔': '101010500',
    '武汉': '101200101',
    '上海': '101020100'
}
    try:
        url = 'http://www.weather.com.cn/weather/'+str(citycode[city])+'.shtml'
        res = requests.get(url)
        # print(res.text)
        res.encoding='utf-8'
        soup = BeautifulSoup(res.text,'lxml')
        day = soup.select('li.on > h1')[0].string

        weather = soup.select('p.wea')[0].string

        tem = soup.select(' p.tem > i')[0].string

        wind= soup.select(' p.win > i')[0].string

        content = day+weather+tem+wind
        print('#',content)
    except:
        content = "error"
    return content


# city = input('cityname=')
# get_whether(city)

 

