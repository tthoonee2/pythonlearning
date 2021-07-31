from igramscraper.instagram import Instagram # pylint: disable=no-name-in-module
from time import sleep

instagram = Instagram()
# instagram.with_credentials('novos_news', 'Chegaturn2019!', '/cachepath')
# instagram.login(force=False,two_step_verificator=True)

sleep(2) # Delay to mimic user

username = '_gencarelli'
followers = []
account = instagram.get_account(username)
sleep(3)
followers = instagram.get_followers(account.identifier, 150, 100, delayed=True) # Get 150 followers of 'kevin', 100 a time with random delay between requests

for follower in followers['accounts']:
    print(follower)