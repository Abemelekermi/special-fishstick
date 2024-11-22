import subprocess
import concurrent.futures
import threading

# Collect input before spawning processes
commitLen = int(input("How many times do you want to commit? \n"))
autoPush = input("Auto git push? (y/n) \n")

# Function to perform a single commit
def perform_commit(i, commitLen):
    command = ['git', 'commit', '--allow-empty', '-m', f'Commit {i} of {commitLen}']
    try:
        subprocess.run(command, check=True)
        print(f"Committed {i} of {commitLen}")
    except subprocess.CalledProcessError as e:
        print(f"Error committing {i} of {commitLen}: {e}")

# Use ThreadPoolExecutor for parallel execution with a limited number of threads
max_workers = 10  # Adjust this number based on your system's capabilities
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = [executor.submit(perform_commit, i, commitLen) for i in range(commitLen)]
    concurrent.futures.wait(futures)

print("Committed " + str(commitLen) + " times")

if autoPush == "y":
    try:
        subprocess.run(['git', 'push'], check=True)
        print("Pushed to remote repository")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing to remote repository: {e}")
