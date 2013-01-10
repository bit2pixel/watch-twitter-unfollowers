# Watch Twitter Unfollowers

A small project I made to see who unfollowed me on Twitter.

- `twitter_stats.py` checks if there are any unfollowers every 60 seconds.
- `web.py` serves the results from `localhost:5000`

## Cloning the repository

1. Clone the repo `clone https://github.com/rcakirerk/watch-twitter-unfollowers.git`
2. Go to the directory `cd watch-twitter-unfollowers`

## Setting Up

1. Go to [https://dev.twitter.com/apps](https://dev.twitter.com/apps) and sign in
2. Create an app (if you already have one skip to step 3)
3. Open your apps page
4. Create an access token (if you already have an access token skip to step 5)
5. Go to wherever you've cloned the repo from your console
6. Open settings.py.example and fill the keys and tokens you've just got from Twitter
7. Rename settings.py.example to settings.py

## Running

1. Run twitter_stats.py in the background `python twitter_stats.py &`
2. Run the web server `python web.py`
3. Open your web browser and go to `localhost:5000`
