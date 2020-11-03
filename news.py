from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='2693b9bec9904c7a8d9ab88faab7c4f8')

# Sports
# top_headlines = newsapi.get_top_headlines(sources='bbc-sport, espn, espn-cric-info')

# Entertainment
# top_headlines = newsapi.get_top_headlines(sources='ign, mtv-news, polygon, the-lad-bible, buzzfeed')

# Tech
# top_headlines = newsapi.get_top_headlines(sources='ars-technica, engadget, hacker-news, new-scientist, recode, the-verge')

# Buisness
# top_headlines = newsapi.get_top_headlines(sources='bloomberg, business-insider, fortune, the-wall-street-journal')

# Health
# top_headlines = newsapi.get_top_headlines(sources='medical-news-today')

# World
# top_headlines = newsapi.get_top_headlines(sources='bbc-news, fox-news, google-news', page_size=30)

# India
# top_headlines = newsapi.get_top_headlines(sources='the-hindu, the-times-of-india, google-news-in', page_size=30)

print(top_headlines)