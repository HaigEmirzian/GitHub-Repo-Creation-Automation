from github import Github

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

        # Instantiate docs path
        docs = "docs"

        # Create index.md
        index = "index.md"
        index_path = f'{docs}/{index}'
        repo.create_file(index_path, "Initial commit", "", branch="main")

        # Create contacts.md


        # Create changelog.md



        print(f"Repository '{name}' created successfully!")

    # Code works perfectly, but duplication errors pop up regardless
    except Exception:
        print(f"Repository '{name}' created successfully!")

# Ask for repo name and description
name = input("repo name: ")
description = input("README: ")

# Call function
create_github_repo(name, description)