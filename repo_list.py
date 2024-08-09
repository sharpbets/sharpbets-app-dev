import requests

# list my private repos

ghtoken_prefix = "ghp_"
ghtoken_suffix = "<redacted>"
headers = {"Authorization": f"token {ghtoken_prefix}{ghtoken_suffix}"}
url = "https://api.github.com/user/repos"
params = {"visibility": "private", "per_page": 100}
repos = []

while url:
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        break
    repos.extend(response.json())
    url = response.links.get("next", {}).get("url")

for repo in repos:
    print(f"Name: {repo['name']}, Full Name: {repo['full_name']}, Private: {repo['private']}")
