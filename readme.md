# Adidas Spider

To crawling adidas mens page here I used Scrapy-Splash. 

### Requirements

- Python3.10
### Process
- clone the repository using ``` git clone git@github.com:ShojibHasan/adidas_spider.git ```
- Make a virtualenv 
  - to make vitualenv open terminal and install virtualenv python package: ``` pip3 install virtualenv ```
  - for macos and linux now type: ``` python3 -m virtualenv venv ```
  - install requirements.txt : ``` pip3 install -r requirements.txt ```

### Run Adidas Spider
active the virtualenv ``` source venv/bin/activate  ``` 
To start crawling and  save data in a Spreadsheet we need to enter this command
``` scrapy crawl adidas -o adidas_products.csv  ```

Throw this command crawling will start and a Spreadsheet will create in the project directory. Open the csv file, you'll get adidas mens product data
