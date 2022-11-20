#this spider extracts info from fandom.com rather than honeyhunter because...
#WELL, honeyhunter doesn't even connect to my scrapy shell anymore

import scrapy
class fandomspi(scrapy.Spider):
    name = "fandomspi"
    start_urls = ['https://genshin-impact.fandom.com/wiki/Raiden_Shogun',
 'https://genshin-impact.fandom.com/wiki/Kamisato_Ayaka',
 'https://genshin-impact.fandom.com/wiki/Jean',
 'https://genshin-impact.fandom.com/wiki/Lisa',
 'https://genshin-impact.fandom.com/wiki/Barbara',
 'https://genshin-impact.fandom.com/wiki/Kaeya',
 'https://genshin-impact.fandom.com/wiki/Diluc',
 'https://genshin-impact.fandom.com/wiki/Razor',
 'https://genshin-impact.fandom.com/wiki/Amber',
 'https://genshin-impact.fandom.com/wiki/Venti',
 'https://genshin-impact.fandom.com/wiki/Xiangling',
 'https://genshin-impact.fandom.com/wiki/Beidou',
 'https://genshin-impact.fandom.com/wiki/Xingqiu',
 'https://genshin-impact.fandom.com/wiki/Xiao',
 'https://genshin-impact.fandom.com/wiki/Ningguang',
 'https://genshin-impact.fandom.com/wiki/Klee',
 'https://genshin-impact.fandom.com/wiki/Zhongli',
 'https://genshin-impact.fandom.com/wiki/Fischl',
 'https://genshin-impact.fandom.com/wiki/Bennett',
 'https://genshin-impact.fandom.com/wiki/Noelle',
 'https://genshin-impact.fandom.com/wiki/Qiqi',
 'https://genshin-impact.fandom.com/wiki/Chongyun',
 'https://genshin-impact.fandom.com/wiki/Ganyu',
 'https://genshin-impact.fandom.com/wiki/Albedo',
 'https://genshin-impact.fandom.com/wiki/Diona',
 'https://genshin-impact.fandom.com/wiki/Mona',
 'https://genshin-impact.fandom.com/wiki/Keqing',
 'https://genshin-impact.fandom.com/wiki/Sucrose',
 'https://genshin-impact.fandom.com/wiki/Xinyan',
 'https://genshin-impact.fandom.com/wiki/Rosaria',
 'https://genshin-impact.fandom.com/wiki/HuTao',
 'https://genshin-impact.fandom.com/wiki/Kaedehara_Kazuha',
 'https://genshin-impact.fandom.com/wiki/Yanfei',
 'https://genshin-impact.fandom.com/wiki/Yoimiya',
 'https://genshin-impact.fandom.com/wiki/Thoma',
 'https://genshin-impact.fandom.com/wiki/Eula',
 'https://genshin-impact.fandom.com/wiki/Sayu',
 'https://genshin-impact.fandom.com/wiki/Sangonomiya_Kokomi',
 'https://genshin-impact.fandom.com/wiki/Gorou',
 'https://genshin-impact.fandom.com/wiki/KujouSara',
 'https://genshin-impact.fandom.com/wiki/Arataki_Itto',
 'https://genshin-impact.fandom.com/wiki/YaeMiko',
 'https://genshin-impact.fandom.com/wiki/Shikanoin_Heizou',
 'https://genshin-impact.fandom.com/wiki/Yelan',
 'https://genshin-impact.fandom.com/wiki/Aloy',
 'https://genshin-impact.fandom.com/wiki/Shenhe',
 'https://genshin-impact.fandom.com/wiki/Yun_Jin',
 'https://genshin-impact.fandom.com/wiki/Kuki_Shinobu',
 'https://genshin-impact.fandom.com/wiki/Kamisato_Ayato',
 'https://genshin-impact.fandom.com/wiki/Collei',
 'https://genshin-impact.fandom.com/wiki/Dori',
 'https://genshin-impact.fandom.com/wiki/Tighnari',
 'https://genshin-impact.fandom.com/wiki/Nilou',
 'https://genshin-impact.fandom.com/wiki/Cyno',
 'https://genshin-impact.fandom.com/wiki/Candace',
 'https://genshin-impact.fandom.com/wiki/Nahida',
 'https://genshin-impact.fandom.com/wiki/Layla',
 'https://genshin-impact.fandom.com/wiki/Alhaitham',
 'https://genshin-impact.fandom.com/wiki/Dehya',
 'https://genshin-impact.fandom.com/wiki/Paimon',
 'https://genshin-impact.fandom.com/wiki/Yaoyao',
 'https://genshin-impact.fandom.com/wiki/Baizhu',
 'https://genshin-impact.fandom.com/wiki/Faruzan',
 'https://genshin-impact.fandom.com/wiki/Mika']
    #def parse(self, response):
    #    chars = response.css("div.char_sea_cont a")
    #    for char in [a.attrib["href"] for a in chars]:
    #       char_url = response.urljoin(char)
     #       yield scrapy.Request(char_url, callback = self.parse_characters)
    def parse_characters(self, response):
        everything = response.css('table.wikitable')
        alltext = everything.css("span::text").get()
        namefind = response.css("div.page-header__title-wrapper")
        name = namefind.css("h1.page-header__title::text")
        yield{
            "name": name,
            "lines": alltext
        }