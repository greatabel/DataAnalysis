import json

class SourceDataDemo:

    def __init__(self):
        self.title = '二手车大数据可视化展板'
        self.counter = {'name': '美国二手车获取数据', 'value': 310000}
        self.counter2 = {'name': '国内二手车获取数据', 'value': 30}
        self.echart1_data = {
            'title': '种类分布',
            'data': [
                {"name": "柴油车", "value": 20},
                {"name": "汽油车", "value": 40},
                {"name": "电动车", "value": 30},


            ]
        }
        self.echart2_data = {
            'title': '汽车制造商',
            'data': [
                {"name": "rissian", "value": 10},
                {"name": "dryster", "value": 4},
                {"name": "jeep", "value": 3},
                {"name": "ford福特", "value": 3},
                {"name": "audi奥迪", "value": 2},
       
            ]
        }
        self.echarts3_1_data = {
            'title': '车龄分布',
            'data': [
                {"name": "2012", "value": 20},
                {"name": "2013", "value": 30},
                {"name": "2014", "value": 20},
                {"name": "2015", "value": 15},
                {"name": "2018", "value": 15},
            ]
        }
        self.echarts3_2_data = {
            'title': '车主职业分布',
            'data': [
                {"name": "电子商务", "value": 10},
                {"name": "教育", "value": 20},
                {"name": "IT/互联网", "value": 20},
                {"name": "金融", "value": 30},
                {"name": "freelancer", "value": 40},
                {"name": "其他", "value": 50},
            ]
        }
        self.echarts3_3_data = {
            'title': '销售方式分布',
            'data': [
                {"name": "经销商", "value": 4},
                {"name": "直营", "value": 5},
                {"name": "网上", "value": 9},
                {"name": "其他", "value": 8},
            ]
        }
        self.echart4_data = {
            'title': '时间趋势',
            'data': [
                {"name": "电动车", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 4]},
                {"name": "汽油车", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3, 5, 6, 1, 5, 3, 7, 2, 5, 8]},
            ],
            'xAxis': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17',
                      '18', '19', '20', '21', '22', '23', '24'],
        }
        self.echart5_data = {
            'title': '汽车地域分布',
            'data': [

                {"name": "美国", "value": 300000},
                {"name": "中国", "value": 20},
                {"name": "其他", "value": 9},
            ]
        }
        self.echart6_data = {
            'title': '汽车地域分布比例',
            'data': [
                {"name": "中国", "value": 64, "value2": 36, "color": "01", "radius": ['59%', '70%']},
                {"name": "美国", "value": 1176, "value2": 214, "color": "02", "radius": ['49%', '60%']},
                {"name": "欧洲", "value": 80, "value2": 20, "color": "03", "radius": ['39%', '50%']},
                {"name": "其他", "value": 82, "value2": 18, "color": "04", "radius": ['29%', '40%']},
               
            ]
        }
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '天津', 'value': 239},
                {'name': '北京', 'value': 121},
                {'name': '其他', 'value': 203},
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = '二手车大数据可视化展板'

