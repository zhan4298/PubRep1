import sys
import requests

def main():
    username = "zhan4298" #My username
    repositoryurl = "https://api.github.com/users/"
    url = repositoryurl + username + "/repos"
    res = requests.get(url)
    repository = res.json()

    print("Public repositories in this account:")
    for rep in repository:
        if rep['private'] == False: #output public repository.
            print (rep['name'])


if __name__ == "__main__":
    main()
    sys.exit()
