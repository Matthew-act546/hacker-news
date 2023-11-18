from operator import itemgetter

import requests

# Make an API call and store the responses
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

news = int(input("Enter a desired amount of Hacker News:"))
submission_req = input("\nDo you want to see how it progress by seeing the submission id and status code(Y/N):\n->")

# Process information about each submission. 
submission_ids = r.json()
submission_dicts = [] 
for submission_id in submission_ids[:news]:
    # Make a seperate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    if submission_req.lower() in 'y':
        print(f"ID: {submission_id}\tStatus: {r.status_code}")
    else:
        print("Then wait.....")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://hacker-news.firebaseio.com/v0/item?id={submission_id}.json",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")