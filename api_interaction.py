import requests
from pprint import pprint

url = "https://api.github.com/users/MawuliB/following"
url2 = "https://api.github.com/users/MawuliB/followers"

response = requests.get(url)
response2 = requests.get(url2)

count = 0
count2 = 0
following_list = []
followers_list = []

for following in response.json():
    following_list.append(following['login'])
    pprint(following['login'])
    count += 1

print(f'\nTotal following: {count}\n')

for follower in response2.json():
    followers_list.append(follower['login'])
    pprint(follower['login'])
    count2 += 1

print(f'\nTotal followers: {count2}\n')

print(f'\n\nFollowing But Not Followers: {set(following_list) - set(followers_list)}\n')