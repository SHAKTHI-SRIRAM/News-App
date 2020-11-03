from django.shortcuts import render

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='2693b9bec9904c7a8d9ab88faab7c4f8')

def home(request):

    world = newsapi.get_top_headlines(sources='bbc-news, fox-news, google-news', page_size=30)
    india = newsapi.get_top_headlines(sources='the-hindu, the-times-of-india, google-news-in', page_size=30)
    sports = newsapi.get_top_headlines(sources='bbc-sport, espn, espn-cric-info')
    entertainment = newsapi.get_top_headlines(sources='ign, mtv-news, polygon, the-lad-bible, buzzfeed')
    tech = newsapi.get_top_headlines(sources='ars-technica, engadget, hacker-news, new-scientist, recode, the-verge')
    buisness = newsapi.get_top_headlines(sources='bloomberg, business-insider, fortune, the-wall-street-journal')
    health = newsapi.get_top_headlines(sources='medical-news-today')

    main_world = world['articles'][0:3]

    main = {
        "world": world['articles'][0:3],
        "india": india['articles'][0:3],
        "sports": sports['articles'][0:3],
        "entertainment": entertainment['articles'][0:3],
        "tech": tech['articles'][0:3],
        "buisness": buisness['articles'][0:3],
        "health": health['articles'][0:3],
    }


    data = {
        "world": world,
        "india": india,
        "sports": sports,
        "entertainment": entertainment,
        "tech": tech,
        "buisness": buisness,
        "health": health,
        "main": main,
    }
    print(main)
    return render(request, 'home.html', data)
