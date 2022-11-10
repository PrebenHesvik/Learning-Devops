##### Three areas
- Working area
- Staging area
- Committed files

##### Process
- `git init` ==> initialize repository
- Create file and write some text to it
  - `touch main.py`
  - `echo "this is the main python file" >> main.py`
  - This file is now in the git **working area**
- `git status`
- `git add main.py` ==> add file to the **staging area**
- `git commit -m "added main.py"` ==> main.py is now **comitted**

##### Branches
A branch is a pointer to a certain commit
- `git branch sarah` ==> create new branch called sarah
- `git checkout sarah` ==> switch to existing branch named sarah
- `git checkout -b sarah` ==> create and switch to a new branch "sarah"
- `git branch` ==> get list of branches 
- `git branch -d sarah` ==> delete the branch named sarah

##### Merge branches
- Two types of merges
  - fast-forward merge
    - when the current branch has no extra commits compared to the branch we are merging
  - no-fast-forward merge

- `git checkout master`
- `git merge feature/signup`

##### Remote
- `git remote -v` ==> list all remote repositories
- `git remote add origin <connection-string>` ==> add remote connection string
- `git push origin <branch_name>`
  - `git push origin master`
- `git clone <shh_link>` ==> download a project to the computer
  - `git clone git@github.com:<account>/<remote-repo>.git`


##### Pull requests
- We do this at the GitHub website

##### Fetch
- `git fetch origin master` ==> download latest update of master branch
- `git merge origin/master` ==> update the master branch on our local repo
- `git pull origin master` ==> combines the two commands above

##### Rebasing
- `git rebase master` ==> move our branch on top of the updated master branch
  - When we do this we modify the history of our git commits


##### Interactive rebasing
  - Used when several commits should ideally just have been one commit
    - fix typo 1
    - fix typo 2
    - fix typo 3
      - ==> one commit for fixing all typos
  - `git rebase -i HEAD~4` ==> replace last four commits with one commit
![img](../images/interactive_rebasing.PNG)

##### Cherry picking
- `git cherry-pick <hash>` ==> copy a specific commit of a branch into the master branch

#### Revert
![img](../images/git_revert.PNG)

#### Reset
- `git reset --soft HEAD~1` ==> removes the last commit
  - by using the soft reset we still have access to the changes made
  - this can be seen by writing `git status`
- `git reset --hard HEAD~1` ==> removes the last commit 
  - by using hard reset we also lose the changes we have made 

##### Stashing
- `git stash` ==> stash something
- `git stash pop` ==> retrieve from stash back into the staging area
- `git stash list` ==> list of all stashes

#### Reflog
- `git reflog` ==> list of all changes
- `git reset --hard <hash>` ==> revert a certain change


##### Other commands
- `git log` ==> show a log of commits
- `git log --oneline` ==> git log "barebones"
- `git log --graph --decorate`