import sys
import json

import requests

# Use Like python githubber.py HarounTaHa
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    response = requests.get("https://api.github.com/users/{}/events".format(username))
    events = json.loads(response.content)
    result = events[0]['created_at']
    print(result)
