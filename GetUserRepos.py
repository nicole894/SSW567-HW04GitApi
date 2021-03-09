import requests


def get_repo_commits(gid):

    url = f"https://api.github.com/users/{gid}/repos"
    url_reponse = requests.get(url)
    response =url_reponse.json()
    #
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
             for k, v in entry.items():
                 if k == "name":
                     statement = dict()
                     commit_url = f"https://api.github.com/repos/{gid}/{v}/commits"
                     commit_response = requests.get(commit_url)
                     commit_responses = commit_response.json()
                     statement.update({'Repo' : v})
                     statement.update({'Number of commits': len(commit_responses)})
                     list_repos.append(statement)
                     #statements = (f"Repo: {v}  ; Number of commits: {len(commit_responses)}")


    return list_repos




if __name__ == "__main__":
    print("Welcome to Assignment 4!")
    print("Enter a GitHub userID ")
    uid = input()
    result = get_repo_commits(uid)
    print(result)
