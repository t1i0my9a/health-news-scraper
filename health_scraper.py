import feedparser
import time

#user input
keyword = input("Enter a keyword for health news:")
print(f"Searching for news about {keyword}")

#google news health category
#origin "https://news.google.com/rss/search?q=health&hl=en-US&gl=US&ceid=US:en"
RSS_URL = f"https://news.google.com/rss/search?q={keyword}&hl=en-US&gl=US&ceid=US:en"#add keyword function

#analysis RSS feed
feed = feedparser.parse(RSS_URL)

#display news title and link
if feed.entries:
   #sort by published data
   sorted_entries = sorted(feed.entries, key = lambda x: x.published_parsed, reverse = True)
   
   for entry in feed.entries[:10]:#latest 10 topic
       print(f"Title:{entry.title}")
       print(f"Link:{entry.link}")

       if hasattr(entry, 'published_parsed'):#if there are website with published date, display
          print(f"Published Date:{time.strftime('%Y-%m-%d %H:%M:%S', entry.published_parsed)}")#sorted YYYY-MM-DD HH:MM:SS
       else:
          print("Published Date: Nothing")
          
       print("-" * 40)
else:
    print("there isn't news include this keyword")
