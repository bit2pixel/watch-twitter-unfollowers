import yaml
import time
import shelve
import datetime

import settings
from twython import Twython

from contextlib import contextmanager

@contextmanager
def closing(this):
    try:
        yield this
    finally:
        this.close()

class TwitterStats():
    def __init__(self):
        # connect to twitter api
        self.twitter = Twython(
                        app_key=settings.consumer_key,
                        app_secret=settings.consumer_secret,
                        oauth_token=settings.oauth_token,
                        oauth_token_secret=settings.oauth_token_secret
                        )

    def init_storage(self):
        storage = shelve.open('twitter_stats', writeback=True)

        if not storage:
            storage['followers'] = set()
            storage['unfollowers'] = []
            storage['unfollowers_since_last_check'] = None
            storage['last_update'] = None

        return storage

    def get_followers(self):
        follower_ids = self.twitter.getFollowersIDs()['ids']

        return set(follower_ids)

    def show_screen_name(self, user_id):
        user = self.twitter.showUser(user_id=user_id)
        screen_name = user['screen_name']

        return screen_name

    def update_unfollower_stats(self):
        with closing(self.init_storage()) as storage:
            previous_followers = storage['followers']
            current_followers = self.get_followers()

            new_unfollower_ids = previous_followers - current_followers
            
            unfollowers_since_last_check = []

            for follower_id in new_unfollower_ids:
                unfollower = {
                    'id': follower_id,
                    'screen_name': self.show_screen_name(follower_id),
                    'timestamp': datetime.datetime.now().strftime('%b %d %Y %H:%M:%S')
                }

                storage['unfollowers'].append(unfollower)
                unfollowers_since_last_check.append(unfollower)

            storage['followers'] = current_followers
            storage['unfollowers_since_last_check'] = unfollowers_since_last_check
            storage['last_update'] = datetime.datetime.now().strftime('%b %d %Y %H:%M:%S')

def main():
    twitter_stats = TwitterStats()

    while True:
        twitter_stats.update_unfollower_stats()
        time.sleep(10)

if __name__ == '__main__':
    main()
