import os

def create_repo_content(name):
    # Go back one directory
    os.chdir("..")

    # Create a new repo
    os.system(f"git init {name}")

    # Go into repo
    os.chdir(f'{name}')

    # Create a readme file
    os.system("touch README.md")

    # Initialize new mkdocs project
    os.system(f'mkdocs new {name}')

    # Go into test-repo once again
    os.chdir(f'{name}/docs')

    # Create index.md
    os.system("touch index.md")

    # Create contacts.md
    os.system("touch contacts.md")

    # Create changelog.md
    os.system("touch changelog.md")

    # Create controls folder
    os.system("mkdir controls")

    # Go into controls folder
    os.chdir("controls")

    # Create controls from 5.11 to 5.31
    first_control_heading = 5
    first_control_subheading = 11
    
    for i in range(21):
        os.system(f"touch {first_control_heading}.{first_control_subheading}.md")
        first_control_subheading += 1

    # Create controls from 6.11 to 6.14
    second_control_heading = 6
    second_control_subheading = 11

    for j in range(4):
        os.system(f"touch {second_control_heading}.{second_control_subheading}.md")
        second_control_subheading += 1

    # Create controls from 7.11 to 7.14
    third_control_heading = 7
    third_control_subheading = 11

    for k in range(4):
        os.system(f"touch {third_control_heading}.{third_control_subheading}.md")
        third_control_subheading += 1

    return

name = input("Repo Name: ")
create_repo_content(name)