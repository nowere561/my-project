from git import Repo
import os

# Path to your local repository
local_repo_path = r"C:\\Users\Vedant\Desktop\my-project"
file_to_upload = "test.txt"  # Name of the file you want to upload
commit_message = "Initial commit"

try:
    # Initialize repository object
    repo = Repo(local_repo_path)
    
    # Create a test file
    file_path = os.path.join(local_repo_path, file_to_upload)
    with open(file_path, 'w') as f:
        f.write("This is a test file\nCreated by Python script")
    
    # Add file to staging area
    repo.index.add([file_to_upload])
    
    # Commit changes
    repo.index.commit(commit_message)
    
    # Push changes to remote (using 'main' branch)
    origin = repo.remote('origin')
    
    # Create and checkout main branch if it doesn't exist
    if 'main' not in repo.heads:
        repo.create_head('main')
    repo.heads.main.checkout()
    
    # Push to main branch
    origin.push('main')
    
    print("Successfully pushed changes to GitHub")
    
except Exception as e:
    print(f"Error: {e}")