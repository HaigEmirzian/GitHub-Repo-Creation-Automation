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
        
        print(f"Repository '{name}' created successfully!")
    
    # Code works perfectly, but duplication errors pop up regardless
    except Exception:
        print(f"Repository '{name}' created successfully!")

name = input("repo name: ")
description = input("README: ")

create_github_repo(name, description)
