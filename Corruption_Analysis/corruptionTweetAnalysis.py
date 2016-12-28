import json
import pandas as pd
import matplotlib.pyplot as plt
import re

def word_in_text(word, text):
	word = word.lower()
	text = text.lower()
	match = re.search(word, text)
	if match:
		return True
	else:
		return False

tweets_data_path = 'warAgainstCorruption.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		print "something"
		continue

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

tweets_by_lang = tweets['lang'].value_counts()
print(tweets_by_lang)

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:10].plot(ax=ax, kind='bar', color='red')
fig.savefig('result/byLanguage.png')


tweets_by_country = tweets['country'].value_counts()
print(tweets_by_country)

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
fig.savefig('result/byCountry.png')


