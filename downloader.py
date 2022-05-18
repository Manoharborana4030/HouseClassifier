from icrawler.builtin import GoogleImageCrawler
google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'dataset/living_room'})
google_Crawler.crawl(keyword = 'House living room images', max_num = 1000)

