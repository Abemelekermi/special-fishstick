import subprocess
import concurrent.futures

commitLen = int(input("How many times do you want to commit? \n"))
autoPush = input("Auto git push? (y/n) \n")

# Function to perform a single commit
def perform_commit(i, commitLen):
    command = ['git', 'commit', '--allow-empty', '-m', f'Commit {i} of {commitLen}']
    subprocess.run(command, check=True)

# Use ThreadPoolExecutor for parallel execution
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(perform_commit, i, commitLen) for i in range(commitLen)]
    concurrent.futures.wait(futures)

print("Committed " + str(commitLen) + " times")

if autoPush == "y":
    subprocess.run(['git', 'push'], check=True)
