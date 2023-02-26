# genshincrawler
需要整一个excel用来快速查台词 内鬼网用着太费劲了

## Purpose
Creating 1 Google Doc with every Genshin Impact character's Open World gameplay lines.
It basically makes searching for things easier.
其他的懂得都懂

## How to Use
***Even if you follow all the steps, there's a very high chance you'll encounter bugs because this repository isn't properly cleaned up yet***
Either clone the repository and open it on your computer, or just... download the entire thing.

The actual scraper is located within the file called gnsncrape. For some reason, automatically appending each individual characte's path to the main link didn't work, so we now have a huge chunk of links there. It works just fiine.
(The links are NOT automatically updated, so you have to add the new character(s)'s link to it every time you use it.)

After installing scrapy, open a terminal and type 
`scrapy crawl fandomspi -o namename.csv`
<br>change "namename" to whatever you want to name your file.

There will now be a very ugly csv file inside your repository folder that's gonna look something like this:
![ugly.png](/images/ugly.png)

Now open Jupyter Notebook and upload the file called `gnsn_formatting_0226.ipynb` and the csv you just crawled.
Run all the code in the Jupyter Notebook (don't forget to change the initial csv name according to what you named it) and download the final product (in the code I've written, it's called `output5.csv`.)

Now all you have to do is... well, clean up anything that looks ugly. Extra commas are always gonna pop up somewhere.
It won't take you too long as long as you always stay up to date with the new characters.

## Future Updates
**better functions**<br>
I don't think the str.replace function is working right now (it works if you open a new ipynb project and re-upload the csv, so idk what's going on here)

**fetters lines**<br>
Formatting them also follows the same logic, but I'm not sure how useful they will be.

## Misc
You can also choose to scrape the JP/CN versions by adding /Japanese or /Chinese to the end of the links. I haven't tried that out with this new target website yet, so I'm not 100% if the formatting stuff will work. But I'm pretty sure it at least follows the same logic.
