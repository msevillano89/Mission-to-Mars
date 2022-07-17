#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


# Set up executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# 1. we're searching for elements with a specific combination of tag (div) and attribute (list_text)
# 2.  we're also telling our browser to wait one second before searching for components


# ## 10.3.3 Scrape Mars Data: The News

# In[3]:


# we'll set up the HTML parser:
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text') #This is our parent element. This means that this element holds all of the other elements within it, 
# and we'll reference it when we want to filter search results even further


# In[4]:


# Scrape article's title
slide_elem.find('div', class_='content_title') # The output should be the HTML containing 
# the content title and anything else nested inside of that


# In[5]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

#.get_text(). When this new method is chained onto .find(), only the text of the element is returned


# In[6]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ## 10.3.4 Scrape Mars Data: Featured Image

# In[7]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[8]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[9]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[10]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[11]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## 10.3.5 Scrape Mars Data: Mars Facts

# In[12]:


# read_html() specifically searches for and returns a list of tables found in the HTML
# By specifying an index of 0, we're telling Pandas to pull only the first table it encounters,
df = pd.read_html('https://galaxyfacts-mars.com')[0]
# we assign columns to the new DataFrame for additional clarity.
df.columns=['description', 'Mars', 'Earth']
#we're turning the Description column into the DataFrame's index. 
# inplace=True means that the updated index will remain in place
df.set_index('description', inplace=True)
df


# In[13]:


# convert our DataFrame back into HTML-ready code using the .to_html() 
df.to_html()


# In[14]:


# end session
browser.quit()


# # Mission to Mars Challenge

# In[15]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[16]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[17]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[18]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[19]:


slide_elem.find('div', class_='content_title')


# In[20]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[21]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[23]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[24]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[25]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[26]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[27]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[28]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[29]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

#Iterate through each of the four hemisphere links:
for i in range(4):
    hemispehere = {}
    #Navigate to each image thumbnail and click
    thumb_image_elem = browser.find_by_css("h3")[i]
    thumb_image_elem.click()
    # Parse the new page
    html= browser.html
    img_soup = soup(html, 'html.parser')
    # Retrieve the full size image
    hemi_img_url_rel = img_soup.find('img', class_="wide-image").get('src')
    hemi_img_url = f'https://marshemispheres.com/{hemi_img_url_rel}'
    #Retrieve title
    hemi_title = img_soup.find("h2", class_="title").get_text()
    # Define and append to the dictionary
    hemisphere = {'title': hemi_title, 'img_url': hemi_img_url,}
    hemisphere_image_urls.append(hemi_dict)
    #Go back to main page
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()
