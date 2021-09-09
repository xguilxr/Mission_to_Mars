#!/usr/bin/env python
# coding: utf-8

# In[30]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[31]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[9]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[10]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[11]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[12]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # Visit URL
# url = 'https://spaceimages-mars.com'
# browser.visit(url)

# ### Featured Images
# 

# In[13]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[14]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[15]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[16]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[17]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[18]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[19]:


url = 'https://galaxyfacts-mars.com/'
browser.visit(url)


# In[20]:


from pandas import pandas as pd


# In[21]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[22]:


df.to_html()


# In[32]:


#D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

## Hemispheres

### 1. Use browser to visit the URL 

url = 'https://marshemispheres.com/'

browser.visit(url)


# In[33]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[34]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.

for i in range(4):
    #create empty dictionary
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.links.find_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()
    


# In[35]:


# 4. Print the list that holds the dictionary of each image url and title.

hemisphere_image_urls


# In[36]:


# 5. Quit the browser
browser.quit()


# In[ ]:




