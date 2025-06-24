# DEMO1

in oder to learn more about git and github, I created this project.

Init:
```bash
echo "# DEMO1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main

VSCODE：
git remote add origin https://github.com/XLYing23333/Demo1.git
Debian Terminal：
git remote add origin git@github.com:XLYing23333/EX1.git
change: add -> set-url

git push -u origin main
```

## About Git and Github common commands:

- `git init`: initialize a new git repository
- `git add <FILE/.>`: add files to the index
- `git commit -m "commit message"`: commit changes to the repository
- `git remote add origin <repository-url>`: add a remote repository
- `git status`: show the status of the repository
- `git branch`: list all branches
- `git branch -M <branch-name>`: create a new branch
- `git branch <branch-name>`: create a new branch
- diff: -M: force move/rename a file, -b: create a new branch
  - `git branch -M main`: rename the current branch to main
  - `git branch dev`: create a new branch named dev
- `git branch -m <old-name> <new-name>`: rename a branch
- `git branch -d <branch-name>`: delete a branch (-d: delete -D:delete merged branch)
- `git log`: show the commit history
- `git checkout <branch-name>`: change the current branch
- `git merge <branch-name>`: merge a branch into the current branch


<img src="https://cdn.jsdelivr.net/gh/XLY23333/picture01/img01/TXLY.png" alt="image.png" />
