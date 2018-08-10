import feedparser

feed = feedparser.parse("https://www.secnews24.com/feed/")
feed_title = feed['feed']