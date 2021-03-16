import requests
from unittest import mock
from unittest.mock import Mock


def get_repo_commits(gid):

    url = f"https://api.github.com/users/{gid}/repos"
    url_reponse = requests.get(url)
    response = url_reponse._headers

    if isinstance(response, dict):
        print("Invalid UserId")
        #result = "Not a Valid UserID"
        return response['message']
    elif len(response) == 0:
        print(f"No Repositories found for user {gid}")
        return None
    else:
         list_repos = []
         for entry in response:
             list_repos.append(entry)

    return list_repos




if __name__ == "__main__":
    print("Welcome to Assignment 5!")
    print("Enter a GitHub userID ")
    uid = input()
    result = get_repo_commits(uid)
    print(result)
