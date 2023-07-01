from github import Github, GithubException
from requests.exceptions import ConnectionError, ReadTimeout
import uuid

def create_github_repo(name, description):
    access_token = input("Access Token: ")
    github = Github(access_token)
    user = github.get_user()
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            repo = user.create_repo(name, description=description, auto_init=True)
            unique_filename = str(uuid.uuid4())
            readme = repo.create_file(f"{unique_filename}/README.md", "Initial commit", "# " + name, branch="main")
            print(f"Repository '{name}' created successfully!")
            return  # Exit the function if the repository is created successfully
        except GithubException as error:
            if error.status == 422 and error.data.get('errors', [{}])[0].get('message') == 'name already exists on this account':
                print(f"Repository '{name}' already exists.")
                name = input("Enter a different Repo Name: ")
            else:
                print(f"An error occurred: {error}")
                attempts += 1
                if attempts < max_attempts:
                    print(f"Retrying ({attempts}/{max_attempts})...")
                else:
                    print(f"Maximum number of attempts reached. Exiting.")
        except (ConnectionError, ReadTimeout) as error:
            print(f"A connection error occurred: {error}")
            attempts += 1
            if attempts < max_attempts:
                print(f"Retrying ({attempts}/{max_attempts})...")
            else:
                print(f"Maximum number of attempts reached. Exiting.")

name = input("Repo Name: ")
description = input("Repo Description: ")

create_github_repo(name, description)
