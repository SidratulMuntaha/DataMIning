{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Acquisition of Data from Reddit\n",
    "### Using web crawling method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Libraries\n",
    "# PRAW is a Python wrapper for the Reddit API\n",
    "# Pandas is for creating dataframe\n",
    "# Datetime is for .....\n",
    "\n",
    "import praw          \n",
    "import pandas as pd\n",
    "import datetime as dt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Authentication process from Reddit\n",
    "# Required Client_id, Client_secret and user_agent\n",
    "\n",
    "reddit = praw.Reddit(client_id=\"Eo_DjUw2l7iIog\", \n",
    "                     client_secret=\"7rQQlaoThKY982iPhMAtCfwzg8Y\", \n",
    "                     user_agent=\"DataMining\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Selected trendy subreddits for laptop brands\n",
    "\n",
    "# 1) r/SuggestALaptop\n",
    "# 2) r/mac\n",
    "# 3) r/Dell\n",
    "# 4) r/ASUS\n",
    "# 5) r/thinkpad\n",
    "# 6) r/AcerOfficial"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Scraping from subreddits"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Subreddits under hot tag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts1 = []\n",
    "ml_subreddit = reddit.subreddit('SuggestALaptop')\n",
    "for post in ml_subreddit.hot(limit=2000):\n",
    "    posts1.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts1 = pd.DataFrame(posts1,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts2 = []\n",
    "ml_subreddit = reddit.subreddit('mac')\n",
    "for post in ml_subreddit.hot(limit=2000):\n",
    "    posts2.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts2 = pd.DataFrame(posts2,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts3 = []\n",
    "ml_subreddit = reddit.subreddit('Dell')\n",
    "for post in ml_subreddit.hot(limit=2000):\n",
    "    posts3.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts3 = pd.DataFrame(posts3,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts4 = []\n",
    "ml_subreddit = reddit.subreddit('ASUS')\n",
    "for post in ml_subreddit.hot(limit=2000):\n",
    "    posts4.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts4 = pd.DataFrame(posts4,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts5 = []\n",
    "ml_subreddit = reddit.subreddit('thinkpad')\n",
    "for post in ml_subreddit.hot(limit=2000):\n",
    "    posts5.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts5 = pd.DataFrame(posts5,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts6 = []\n",
    "ml_subreddit = reddit.subreddit('AcerOfficial')\n",
    "for post in ml_subreddit.hot(limit=1000):\n",
    "    posts6.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts6 = pd.DataFrame(posts6,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5980, 8)"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Merging several dataframes\n",
    "\n",
    "df_merged = pd.concat([posts1, posts2, posts3, posts4, posts5, posts6])\n",
    "df_merged.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>score</th>\n",
       "      <th>id</th>\n",
       "      <th>subreddit</th>\n",
       "      <th>url</th>\n",
       "      <th>num_comments</th>\n",
       "      <th>body</th>\n",
       "      <th>created</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>READ THIS BEFORE POSTING OR COMMMENTING. RULES...</td>\n",
       "      <td>44</td>\n",
       "      <td>6dwp6l</td>\n",
       "      <td>SuggestALaptop</td>\n",
       "      <td>https://www.reddit.com/r/suggestalaptop/wiki/r...</td>\n",
       "      <td>0</td>\n",
       "      <td></td>\n",
       "      <td>1.496041e+09</td>\n",
       "      <td>2017-05-29 14:49:20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>/R/SuggestALaptop Stress Test Project! Submit ...</td>\n",
       "      <td>16</td>\n",
       "      <td>ekkvox</td>\n",
       "      <td>SuggestALaptop</td>\n",
       "      <td>https://www.reddit.com/r/SuggestALaptop/commen...</td>\n",
       "      <td>2</td>\n",
       "      <td>Laptops this gen often have thermal or TDP th...</td>\n",
       "      <td>1.578295e+09</td>\n",
       "      <td>2020-01-06 15:23:07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>why is everything so thin?</td>\n",
       "      <td>17</td>\n",
       "      <td>fjx4l7</td>\n",
       "      <td>SuggestALaptop</td>\n",
       "      <td>https://www.reddit.com/r/SuggestALaptop/commen...</td>\n",
       "      <td>7</td>\n",
       "      <td>Hi, I am looking at laptops... specifically th...</td>\n",
       "      <td>1.584440e+09</td>\n",
       "      <td>2020-03-17 18:06:03</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title  score      id  \\\n",
       "0  READ THIS BEFORE POSTING OR COMMMENTING. RULES...     44  6dwp6l   \n",
       "1  /R/SuggestALaptop Stress Test Project! Submit ...     16  ekkvox   \n",
       "2                         why is everything so thin?     17  fjx4l7   \n",
       "\n",
       "        subreddit                                                url  \\\n",
       "0  SuggestALaptop  https://www.reddit.com/r/suggestalaptop/wiki/r...   \n",
       "1  SuggestALaptop  https://www.reddit.com/r/SuggestALaptop/commen...   \n",
       "2  SuggestALaptop  https://www.reddit.com/r/SuggestALaptop/commen...   \n",
       "\n",
       "   num_comments                                               body  \\\n",
       "0             0                                                      \n",
       "1             2   Laptops this gen often have thermal or TDP th...   \n",
       "2             7  Hi, I am looking at laptops... specifically th...   \n",
       "\n",
       "        created           timestamp  \n",
       "0  1.496041e+09 2017-05-29 14:49:20  \n",
       "1  1.578295e+09 2020-01-06 15:23:07  \n",
       "2  1.584440e+09 2020-03-17 18:06:03  "
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Fixing the date column\n",
    "\n",
    "def get_date(created):\n",
    "    return dt.datetime.fromtimestamp(created)\n",
    "\n",
    "_timestamp = df_merged[\"created\"].apply(get_date)\n",
    "\n",
    "df_merged_hottag = df_merged.assign(timestamp = _timestamp)\n",
    "df_merged_hottag.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Saving the dataframe to csv format\n",
    "\n",
    "df_merged_hottag.to_csv(r'C:\\Users\\User\\Desktop\\Milestone 2 - Cleaning & ETL\\reddit_hottag.csv', index = False, header=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Subreddits under new tag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts1 = []\n",
    "ml_subreddit = reddit.subreddit('SuggestALaptop')\n",
    "for post in ml_subreddit.new(limit=2000):\n",
    "    posts1.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts1 = pd.DataFrame(posts1,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts2 = []\n",
    "ml_subreddit = reddit.subreddit('mac')\n",
    "for post in ml_subreddit.new(limit=2000):\n",
    "    posts2.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts2 = pd.DataFrame(posts2,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts3 = []\n",
    "ml_subreddit = reddit.subreddit('Dell')\n",
    "for post in ml_subreddit.new(limit=2000):\n",
    "    posts3.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts3 = pd.DataFrame(posts3,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts4 = []\n",
    "ml_subreddit = reddit.subreddit('ASUS')\n",
    "for post in ml_subreddit.new(limit=2000):\n",
    "    posts4.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts4 = pd.DataFrame(posts4,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts5 = []\n",
    "ml_subreddit = reddit.subreddit('thinkpad')\n",
    "for post in ml_subreddit.new(limit=2000):\n",
    "    posts5.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts5 = pd.DataFrame(posts5,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts6 = []\n",
    "ml_subreddit = reddit.subreddit('AcerOfficial')\n",
    "for post in ml_subreddit.new(limit=1000):\n",
    "    posts6.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts6 = pd.DataFrame(posts6,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5953, 8)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Merging several dataframes\n",
    "\n",
    "df_merged = pd.concat([posts1, posts2, posts3, posts4, posts5, posts6])\n",
    "df_merged.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>score</th>\n",
       "      <th>id</th>\n",
       "      <th>subreddit</th>\n",
       "      <th>url</th>\n",
       "      <th>num_comments</th>\n",
       "      <th>body</th>\n",
       "      <th>created</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Recommendations for audio/image editing and ga...</td>\n",
       "      <td>1</td>\n",
       "      <td>fk25ch</td>\n",
       "      <td>SuggestALaptop</td>\n",
       "      <td>https://www.reddit.com/r/SuggestALaptop/commen...</td>\n",
       "      <td>0</td>\n",
       "      <td>* **Total budget and country of purchase:** \\n...</td>\n",
       "      <td>1.584465e+09</td>\n",
       "      <td>2020-03-18 01:11:50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Help me choose between these 3 options, please?</td>\n",
       "      <td>1</td>\n",
       "      <td>fk24k0</td>\n",
       "      <td>SuggestALaptop</td>\n",
       "      <td>https://www.reddit.com/r/SuggestALaptop/commen...</td>\n",
       "      <td>0</td>\n",
       "      <td>[Option 1](https://www.amazon.ae/Dell-G3-Gamin...</td>\n",
       "      <td>1.584465e+09</td>\n",
       "      <td>2020-03-18 01:09:46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Cheap laptop to learn coding</td>\n",
       "      <td>1</td>\n",
       "      <td>fk0tp9</td>\n",
       "      <td>SuggestALaptop</td>\n",
       "      <td>https://www.reddit.com/r/SuggestALaptop/commen...</td>\n",
       "      <td>0</td>\n",
       "      <td>KB\\n\\n* **Total budget and country of purchas...</td>\n",
       "      <td>1.584457e+09</td>\n",
       "      <td>2020-03-17 23:01:47</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title  score      id  \\\n",
       "0  Recommendations for audio/image editing and ga...      1  fk25ch   \n",
       "1    Help me choose between these 3 options, please?      1  fk24k0   \n",
       "2                       Cheap laptop to learn coding      1  fk0tp9   \n",
       "\n",
       "        subreddit                                                url  \\\n",
       "0  SuggestALaptop  https://www.reddit.com/r/SuggestALaptop/commen...   \n",
       "1  SuggestALaptop  https://www.reddit.com/r/SuggestALaptop/commen...   \n",
       "2  SuggestALaptop  https://www.reddit.com/r/SuggestALaptop/commen...   \n",
       "\n",
       "   num_comments                                               body  \\\n",
       "0             0  * **Total budget and country of purchase:** \\n...   \n",
       "1             0  [Option 1](https://www.amazon.ae/Dell-G3-Gamin...   \n",
       "2             0   KB\\n\\n* **Total budget and country of purchas...   \n",
       "\n",
       "        created           timestamp  \n",
       "0  1.584465e+09 2020-03-18 01:11:50  \n",
       "1  1.584465e+09 2020-03-18 01:09:46  \n",
       "2  1.584457e+09 2020-03-17 23:01:47  "
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Fixing the date column\n",
    "\n",
    "import datetime as dt\n",
    "\n",
    "def get_date(created):\n",
    "    return dt.datetime.fromtimestamp(created)\n",
    "\n",
    "_timestamp = df_merged[\"created\"].apply(get_date)\n",
    "\n",
    "df_merged_newtag = df_merged.assign(timestamp = _timestamp)\n",
    "df_merged_newtag.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Saving the dataframe to csv format\n",
    "\n",
    "df_merged_newtag.to_csv(r'C:\\Users\\User\\Desktop\\Milestone 2 - Cleaning & ETL\\reddit_newtag.csv', index = False, header=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Filtering subreddits of hot tag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       id  num_comments                                              title  \\\n",
      "1  ekkvox             2  /R/SuggestALaptop Stress Test Project! Submit ...   \n",
      "2  fjx4l7             7                         why is everything so thin?   \n",
      "3  fjsvgw             4  Under 1000€ laptop for programming and some ga...   \n",
      "5  fjy7ix             1                                         Under 1000   \n",
      "9  fjsdd9             3                                   Developer Laptop   \n",
      "\n",
      "        subreddit  \n",
      "1  SuggestALaptop  \n",
      "2  SuggestALaptop  \n",
      "3  SuggestALaptop  \n",
      "5  SuggestALaptop  \n",
      "9  SuggestALaptop  \n"
     ]
    }
   ],
   "source": [
    "# Filtering the subreddits with comments\n",
    "\n",
    "df2 = df_merged_hottag[['id','num_comments', 'title','subreddit']]\n",
    "df2 = df2.loc[(df2 != 0).all(axis=1), :]\n",
    "print(df2.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4988, 4)"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(234, 4)"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.drop(df2[df2.num_comments < 4].index, inplace=True)\n",
    "df2.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Filtering subreddits of new tag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        id  num_comments                                              title  \\\n",
      "3   fk0e9e             1  Need laptop with thunderbolt 3, one nvme and o...   \n",
      "5   fjyvu9             1      Recommendations for laptop for medical school   \n",
      "7   fjy7ix             1                                         Under 1000   \n",
      "12  fjxsxl             1                    In need of a laptop for college   \n",
      "14  fjx4l7             7                         why is everything so thin?   \n",
      "\n",
      "         subreddit  \n",
      "3   SuggestALaptop  \n",
      "5   SuggestALaptop  \n",
      "7   SuggestALaptop  \n",
      "12  SuggestALaptop  \n",
      "14  SuggestALaptop  \n"
     ]
    }
   ],
   "source": [
    "# Filtering the subreddits with comments\n",
    "\n",
    "df3 = df_merged_newtag[['id','num_comments', 'title','subreddit']]\n",
    "df3 = df3.loc[(df3 != 0).all(axis=1), :]\n",
    "print(df3.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4967, 4)"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df3.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(275, 4)"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df3.drop(df3[df3.num_comments < 4].index, inplace=True)\n",
    "df3.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Scraping threads under the subreddit topics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Threads under subreddit hot tag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scraping the threads of comments\n",
    "\n",
    "L = []\n",
    "for i in df2['id']:\n",
    "    submission = reddit.submission(id=i)\n",
    "\n",
    "    submission.comments.replace_more(limit=0)\n",
    "    for top_level_comment in submission.comments:\n",
    "        L.append([i, top_level_comment.body])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1131, 2)"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Creating dataframe with attributes id and comments\n",
    "\n",
    "L = pd.DataFrame(L,columns=['id', 'comments'])\n",
    "L.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Saving it to csv format\n",
    "\n",
    "L.to_csv(r'C:\\Users\\User\\Desktop\\Milestone 2 - Cleaning & ETL\\reddit_comments_hottag.csv', index = False, header=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Threads under subreddit new tag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scraping the threads of comments\n",
    "\n",
    "N = []\n",
    "for i in df3['id']:\n",
    "    submission = reddit.submission(id=i)\n",
    "\n",
    "    submission.comments.replace_more(limit=0)\n",
    "    for top_level_comment in submission.comments:\n",
    "        N.append([i, top_level_comment.body])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1050, 2)"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Creating dataframe with attributes id and comments\n",
    "\n",
    "N = pd.DataFrame(N,columns=['id', 'comments'])\n",
    "N.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Saving it to csv format\n",
    "\n",
    "N.to_csv(r'C:\\Users\\User\\Desktop\\Milestone 2 - Cleaning & ETL\\reddit_comments_newtag.csv', index = False, header=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
