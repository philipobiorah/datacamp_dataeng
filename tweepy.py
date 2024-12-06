#import package
import json

# String of path to file: tweets_data_path

tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())
#output: dict_keys(['in_reply_to_user_id_str', 'geo', 'in_reply_to_status_id_str', 'created_at', 'filter_level', 'in_reply_to_user_id', 'truncated', 'possibly_sensitive', 'timestamp_ms', 'extended_entities', 'in_reply_to_screen_name', 'id', 'favorite_count', 'text', 'entities', 'retweeted', 'is_quote_status', 'id_str', 'in_reply_to_status_id', 'source', 'favorited', 'lang', 'contributors', 'coordinates', 'place', 'retweet_count', 'user', 'quoted_status_id_str', 'quoted_status_id
#_str


#initialize list to store tweet counts
[cliton, trump, sanders, cruz] = [0, 0, 0, 0]

#iterate through df, counting the number of tweets in which each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

# Import package
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']



# Create a bar plot with cv on x-axis and cd on y-axis
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()


    