import os

commitLen = int(input("How many times do you want to commit? \n"))
autoPush = input("Auto git push? (y/n) \n")

for i in range(commitLen):
	os.system(f'git commit --allow-empty -m "Commit {i} of {commitLen}"')	

print("Commited " + str(commitLen) + " times")

if autoPush == "y":
	os.system('git push')