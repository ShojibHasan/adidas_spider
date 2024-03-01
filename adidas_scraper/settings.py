BOT_NAME = "adidas_scraper"

SPIDER_MODULES = ["adidas_scraper.spiders"]
NEWSPIDER_MODULE = "adidas_scraper.spiders"

ROBOTSTXT_OBEY = True


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
