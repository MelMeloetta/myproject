import requests


class HeFeng():
    def __init__(self):
        self.url = 'https://cdn.heweather.com/china-city-list.txt'

    def get_citys_code(self):
        data1 = self.get_citys()
        citys = data1[6:]
        print(citys)
        for each in citys:
            yield (each[2:13])

    def get_citys(self):
        html = requests.get(self.url)
        html.encoding = 'utf8'
        data = html.text
        data1 = data.split('\n')
        print(len(data1))
        return data1

    def get_weather(self, city_code):
        url = "https://free-api.heweather.net/s6/weather/forecast?location=" + city_code + '&key=c8bf4ff8796244f5b14e0f648683c562'
        info = requests.get(url)
        info.encoding = 'utf8'
        # print("--------------------")
        # print(info.text)
        # print("--------------------")
        dict = info.json()
        print(dict)
        for item in dict["HeWeather6"][0]['daily_forecast']:
            print("max of temperature %s, min of temperature %s " % (item['tmp_max'], item['tmp_min']))


if __name__ == '__main__':
    hefeng = HeFeng()
    hefeng.get_weather("CN101010100")
    codes = hefeng.get_citys_code()
    for i in range(5):
        print(codes.__next__())