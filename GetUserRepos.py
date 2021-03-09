import requests


def get_repo_commits(gid):

    url = f"https://api.github.com/users/{gid}/repos"
    url_reponse = requests.get(url)
    response =url_reponse.json()
    #
    if isinstance(response, dict):
        print("Message not found")
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


        #return [{'Repo': 'CasinoSlotMachine', 'Number of commits': 3}, {'Repo': 'CS570-DataStructures', 'Number of commits': 5}, {'Repo': 'GEDCOM-Parser-Project---CS-555', 'Number of commits': 30}, {'Repo': 'German-English-Laguage-Translator', 'Number of commits': 2}, {'Repo': 'helloworld', 'Number of commits': 2}, {'Repo': 'kg_nicole894_2021', 'Number of commits': 3}, {'Repo': 'Multiplayer-tic-tac-toe', 'Number of commits': 4}, {'Repo': 'NicoleAnnikaGonsalves_Projects_Python', 'Number of commits': 2}, {'Repo': 'PythonHackerRankChallenges', 'Number of commits': 3}, {'Repo': 'SSW-567-HW02a', 'Number of commits': 13}, {'Repo': 'SSW567-HW01', 'Number of commits': 2}, {'Repo': 'SSW567-HW04GitApi', 'Number of commits': 3}]


if __name__ == "__main__":
    print("Welcome to Assignment 4!")
    print("Enter a GitHub userID ")
    uid = input()
    result = get_repo_commits(uid)
    print(result)
