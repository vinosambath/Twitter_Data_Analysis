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

tweets_data_path = 'tweetDataset.txt'

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

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 10 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:10].plot(ax=ax, kind='bar', color='red')
fig.savefig('result/byLanguage.png')


tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 10 countries', fontsize=15, fontweight='bold')
tweets_by_country[:10].plot(ax=ax, kind='bar', color='blue')
fig.savefig('result/byCountry.png')



tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
tweets['java'] = tweets['text'].apply(lambda tweet: word_in_text('java', tweet))
tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))
tweets['perl'] = tweets['text'].apply(lambda tweet: word_in_text('perl', tweet))

print tweets['python'].value_counts()
print tweets['python'].value_counts()[True]

print tweets['java'].value_counts()
print tweets['java'].value_counts()[True]

print tweets['ruby'].value_counts()
print tweets['ruby'].value_counts()[True]

print tweets['perl'].value_counts()
print tweets['perl'].value_counts()[True]

prg_langs = ['python', 'java', 'ruby', 'perl']

tweets_by_prg_languages = [tweets['python'].value_counts()[True], tweets['java'].value_counts()[True], tweets['ruby'].value_counts()[True], tweets['perl'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))

print x_pos

width = 0.8
fig, ax = plt.subplots()

plt.bar(x_pos, tweets_by_prg_languages, width, alpha=1, color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: python vs. java vs. ruby vs Perl (Raw Data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()
fig.savefig('result/raw_lang_diff.png')

tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet) or word_in_text('coding', tweet))
print tweets[tweets['relevant'] == True]['python'].value_counts()[True]
print tweets[tweets['relevant'] == True]['java'].value_counts()[True]
print tweets[tweets['relevant'] == True]['ruby'].value_counts()[True]
print tweets[tweets['relevant'] == True]['perl'].value_counts()[True]

tweets_by_prg_languages = [tweets[tweets['relevant'] == True]['python'].value_counts()[True], tweets[tweets['relevant'] == True]['java'].value_counts()[True], tweets[tweets['relevant'] == True]['ruby'].value_counts()[True], tweets[tweets['relevant'] == True]['perl'].value_counts()[True]]
x_pos = list(range(len(tweets_by_prg_languages)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_languages, width,alpha=1,color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: python vs. java vs. ruby vs Perl(Relevant data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(tweets_by_prg_languages)
plt.grid()
fig.savefig('result/lang_diff_by_relevance.png')