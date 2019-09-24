import scrapy
from bs4 import BeautifulSoup
from apple.items import AppleItem

class NasaCrawler(scrapy.Spider):
    name = 'apple'
    start_urls = ['https://spacecoastlaunches.com/launch-schedule/']

    def parse(self, response):
        counter = 0
        list_month = []
        list_year = []
        list_day = []
        list_time = []
        list_mission = []
        list_where = []
        list_TBD = []
        res = BeautifulSoup(response.body, features="lxml")
        appleitem = AppleItem()


        for news in res.select('.sc-launch__month'):
            print(news.text)
            list_month.append(news.text)
            #appleitem['month'] = news.text
        for news in res.select('.sc-launch__year'):
            print(news.text)
            list_year.append(news.text)
            #appleitem['year'] = news.text
        for news in res.select('.sc-launch__day'):
            print(news.text)
            if(news.text == 'TBD'):
                list_TBD.append(news.text)
            else:
                list_day.append(news.text)
                #appleitem['day'] = news.text

        for item in list_TBD:
            list_day.append(item)
            
        for news in res.select('.sc-launch__time'):
            length = len(str(news.text)) - 1

            while(length):
                if((str(news.text)[length] != ' ') & (str(news.text)[length] != '\n')):
                    end = length
                    have_content = True
                if(have_content & (str(news.text)[length] == ' ')):
                    #start = length
                    have_content = False
                    #print("start = ", start, "end = ", end)
                    break
                length = length - 1;

            if(length != 0):
                print(str(news.text)[end-6:end+7])
                list_time.append(str(news.text)[end-6:end+7])
                #appleitem['time'] = "none"
            elif (length == 0):
                print("none")
                list_time.append("none")
            
                
        for news in res.select('.sc-launch__content'):
            length = len(str(news.text)) - 1

            for i in range(0, length):
                if(str(news.text)[i].isalpha()):
                    start2 = i
                    break
            
            while(length):
                if((str(news.text)[length] != ' ') & (str(news.text)[length] != '\n')):
                    end2 = length
                    break
                else:
                    length = length - 1;

            counter = counter + 1;
            if(counter%2 == 1): #mission
                print( news.text[start2:end2] )
                list_mission.append(news.text[start2:end2])
                #appleitem['mission'] = news.text[start2:end2]
            else:#where
                print( news.text[start2:end2] )
                list_where.append(news.text[start2:end2])
                #appleitem['where'] = news.text[start2:end2]

        size_of_continuous_none = len(list_TBD)
        
        
        del list_time[0:size_of_continuous_none]
        for i in range(0,size_of_continuous_none):
            list_time.append("none")

        appleitem['month'] = list_month
        appleitem['year'] = list_year
        appleitem['day'] = list_day
        appleitem['time'] = list_time
        appleitem['mission'] = list_mission
        appleitem['where'] = list_where
            
        return appleitem