# Learning how to use git NOTES

# Examples
Git init is used for creating a new repo or reinitializing an existing repo.
```
git init 
```

branch will be used for checking the current branch your working in and creating new branches. Always create a test branch!!
```
git branch new_branch_here
```

switch & checkout, can both be used for switching to a diff branch.
```
git checkout test-branch 
git switch test-branch
```

Add will added files to be tracked and logged. 
```
git add file.py file.py
```

Status will display any updates to any files.
```
git status
```

Commit will record changes to the repo. 
```
git commit -a -m 'message here about changes'
```

pull updates the repo from the remote server.
```
git pull
```

Push will push whatever updates you have done to the files to the remote server. 
```
git push 
git push origin master
```



