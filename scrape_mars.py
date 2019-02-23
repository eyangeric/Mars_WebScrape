#scrape different Mars websites
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    Mars_Dict = {}

    #scrape first Mars News Title
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all("div", class_="content_title")

    title_list = []
    for result in results:
        title = result.a.text
        title_list.append(title)
  
    news_title  = title_list[0]
    
    #scrape first Mars Article's Teaser
    results2 = soup.find_all("div", class_="article_teaser_body")

    teaser_list = []
    for result in results2:
        teaser = result.text
        teaser_list.append(teaser)

    news_p = teaser_list[0]

    #scrape Mars Image
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #extracting link to picture of latest Mars image
    results = soup.find_all("a", class_="fancybox")

    Mars_Image_List = []
    for result in results:
        Image_link = result["data-fancybox-href"]
        Mars_Image_List.append(Image_link)

    featured_image_url = "https://www.jpl.nasa.gov/" + Mars_Image_List[1]
    featured_image_url

    Mars_Image_URL = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(Mars_Image_URL)
    Mars_Image_HTML = browser.html
    Mars_Image_soup = BeautifulSoup(Mars_Image_HTML, "html.parser")

    Mars_Image_results = Mars_Image_soup.find_all("a", class_="fancybox")

    Mars_Image_List = []
    for Mars_Image_result in Mars_Image_results:
        Mars_Image_Link = Mars_Image_result["data-fancybox-href"]
        Mars_Image_List.append(Mars_Image_Link)

    featured_image_url = "https://www.jpl.nasa.gov/" + Mars_Image_List[1]

    #scrape latest Mars Weather Tweet
    tweet_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(tweet_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #extract latest Mars Weather tweet
    results = soup.find_all("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")

    Mars_Weather_Tweets = []
    for result in results:
        tweet = result.text
        if "Sol" and "high" and "low" and "hPa" in tweet:
            Mars_Weather_Tweets.append(tweet)
            
    Mars_Weather_Tweets_New = []
    for tweet in Mars_Weather_Tweets:
        tweet_pic_split = tweet.split("pic")
        Mars_Weather_Tweets_New.append(tweet_pic_split)
        
    mars_weather  = Mars_Weather_Tweets_New[0][0]

    ####getting Mars Hemispheres Images

    #Cerberus Hemisphere
    Cerberus_Hem_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(Cerberus_Hem_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #extract image link of Cerberus Hemisphere
    results = soup.find_all("img", class_="wide-image")

    Img_list = []
    for result in results:
        img_link = result['src']
        Img_list.append(img_link)

    Cerberus_Hem_Image_url = "https://astrogeology.usgs.gov" + Img_list[0]

    #extract image link of Schiaparelli Hemisphere
    Schiaparelli_Hem_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(Schiaparelli_Hem_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #extract image link of Schiaparelli Hemisphere
    results = soup.find_all("img", class_="wide-image")

    Img_list = []
    for result in results:
        img_link = result['src']
        Img_list.append(img_link)

    Schiaparelli_Hem_Image_url = "https://astrogeology.usgs.gov" + Img_list[0]

    #extract image link of Syrtis Major Hemisphere
    SyrtisMajor_Hem_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(SyrtisMajor_Hem_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #extract image link of Syrtis Major Hemisphere
    results = soup.find_all("img", class_="wide-image")

    Img_list = []
    for result in results:
        img_link = result['src']
        Img_list.append(img_link)

    SyrtisMajor_Hem_Image_url = "https://astrogeology.usgs.gov" + Img_list[0]

    #extract image link of Valles Marineris Hemisphere
    VallesMarineris_Hem_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(VallesMarineris_Hem_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #extract image link of Valles Marineris Hemisphere
    results = soup.find_all("img", class_="wide-image")

    Img_list = []
    for result in results:
        img_link = result['src']
        Img_list.append(img_link)

    VallesMarineris_Hem_Image_url = "https://astrogeology.usgs.gov" + Img_list[0]

    hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": Cerberus_Hem_Image_url},
    {"title": "Schiaparelli Hemisphere", "img_url": Schiaparelli_Hem_Image_url},
    {"title": "Syrtis Major Hemisphere", "img_url": SyrtisMajor_Hem_Image_url},
    {"title": "Valles Marineris Hemisphere", "img_url": VallesMarineris_Hem_Image_url},
    ]
    
    #scrape Mars Facts
    Mars_Facts_URL = "https://space-facts.com/mars/"
    Mars_Facts_Table = pd.read_html(Mars_Facts_URL)
    Mars_Facts_DF = Mars_Facts_Table[0]
    Mars_Facts_DF.columns = ["Variable", "Value"]
    Mars_Facts_DF = Mars_Facts_DF.set_index('Variable')
    Mars_Facts_Table = Mars_Facts_DF.to_html()
    Mars_Facts_Table = Mars_Facts_Table.replace("\n", "")

    Mars_Dict["news_title"] = news_title
    Mars_Dict["news_p"] = news_p
    Mars_Dict["image"] = featured_image_url
    Mars_Dict["mars_weather"] = mars_weather
    Mars_Dict["hemisphere_image_urls"] = hemisphere_image_urls
    Mars_Dict["facts"] = Mars_Facts_Table
    

    return Mars_Dict