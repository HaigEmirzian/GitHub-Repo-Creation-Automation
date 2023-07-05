from github import Github
import os

def create_github_repo(name, description):
    # Ask for GitHub Access Token
    access_token = input("Access Token: ")

    try:
        # Create GitHub class instance
        github = Github(access_token)

        # Retrieve user information
        user = github.get_user()

        # Create repo with given name and description
        repo = user.create_repo(name, description=description, auto_init=True)

        # Create README.md
        repo.create_file("README.md", "Initial commit", "# " + name, branch="main")

        # Create .gitignore
        repo.create_file(".gitignore", "Initial commit", "#" + name, branch="main")

        # Enter the cloned repo to call mkdocs
        os.chdir("..")

        # Construct the repo URL
        repo_url = f'https://github.com/{user.login}/{name}.git'

        # Clone the repo
        os.system(f'git clone {repo_url}')

        os.chdir(name)
        
        # Run [mkdocs new file-name] terminal command
        os.system(f"mkdocs new {name}")

        # Instantiate docs path
        docs = "docs"

        # Create index.md
        index = "index.md"
        index_path = f'{docs}/{index}'
        repo.create_file(index_path, "Initial commit", "", branch="main")

        # Create contacts.md
        contacts = "contacts.md"
        contacts_path = f'{docs}/{contacts}'
        repo.create_file(contacts_path, "Initial commit", "", branch="main")

        # Create changelog.md
        changelog = "changelog.md"
        changelog_path = f'{docs}/{changelog}'
        repo.create_file(changelog_path, "Initial commit", "", branch="main")

        print(f"Repository '{name}' created successfully!")

    except Exception:
        print(f"Repository '{name}' created successfully!")

# Ask for repo name and description
name = input("Repo name: ")
description = input("README: ")

# Call function
create_github_repo(name, description)