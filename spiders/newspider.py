#this spider extracts info from fandom.com rather than honeyhunter because...
#WELL, honeyhunter doesn't even connect to my scrapy shell anymore
import scrapy
class fandomspi(scrapy.Spider):
    name = "fandomspi"
    start_urls = ['https://genshin-impact.fandom.com/wiki/Raiden_Shogun/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Kamisato_Ayaka/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Jean/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Lisa/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Barbara/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Kaeya/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Diluc/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Razor/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Amber/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Venti/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Xiangling/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Beidou/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Xingqiu/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Xiao/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Ningguang/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Klee/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Zhongli/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Fischl/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Bennett/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Noelle/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Qiqi/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Chongyun/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Ganyu/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Albedo/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Diona/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Mona/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Keqing/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Sucrose/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Xinyan/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Rosaria/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/HuTao/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Kaedehara_Kazuha/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Yanfei/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Yoimiya/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Thoma/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Eula/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Sayu/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Sangonomiya_Kokomi/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Gorou/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/KujouSara/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Arataki_Itto/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/YaeMiko/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Shikanoin_Heizou/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Yelan/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Aloy/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Shenhe/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Yun_Jin/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Kuki_Shinobu/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Kamisato_Ayato/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Collei/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Dori/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Tighnari/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Nilou/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Cyno/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Candace/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Nahida/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Layla/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Alhaitham/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Dehya/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Paimon/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Yaoyao/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Baizhu/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Faruzan/Voice-Overs',
 'https://genshin-impact.fandom.com/wiki/Mika/Voice-Overs']
    def parse(self, response):
        everything = response.css('table.wikitable')
        alltext = everything.css("span::text").getall()
        namefind = response.css("div.page-header__title-wrapper")
        name = namefind.css("h1.page-header__title::text")
        yield{
            "name": name,
            "lines": alltext
        }
   #def parse(self, response):
    #    chars = response.css("div.char_sea_cont a")
    #    for char in [a.attrib["href"] for a in chars]:
    #       char_url = response.urljoin(char)
     #       yield scrapy.Request(char_url, callback = self.parse_characters)
