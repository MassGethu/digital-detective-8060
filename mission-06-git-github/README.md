# Mission 6 — Git and GitHub

## 1. Task / objective

Use Git to stage and commit a change, create a branch, and open a pull request into main.

## 2. Work completed

### Task 6.1 — Basic Git workflow

| Operation | What it does |
| --- | --- |
| Check repository status | `git status --short` summarises changes and shows which are staged. |
| Stage selected changes | `git add mission-06-git-github/README.md` copies the selected file’s current content into the proposed snapshot. |
| Create a commit | `git commit -m "message"` records a snapshot of the staged content and includes the message in history. |
| View commit history | `git log --oneline -3` shows the latest three commits with short IDs and subjects. |

Staging selects content for the next snapshot. Committing saves that selected snapshot in the local repository history.

### Tasks 6.2 and 6.3 — Branch and pull request

The `update-about` branch added a **My Learning** section to the root README. The pull request proposes that change from `update-about` into `main`. Its Files changed view contains the root `README.md` only. The pull request remains open for review.

A branch is a named line of work that can advance independently. A pull request collects the proposed changes in one place so collaborators can review, discuss and eventually integrate them.

### Task 6.4 — Git glossary

| Command | Purpose |
| --- | --- |
| `git init -b main` | Starts a repository and sets its initial branch name. |
| `git status` | Shows the current branch and working or staged changes. |
| `git add <path>` | Stages the selected content. |
| `git commit -m "message"` | Saves staged content as a named checkpoint. |
| `git log --oneline` | Lists commits with abbreviated IDs and messages. |
| `git branch` | Lists local branches. |
| `git switch -c <branch>` | Creates and switches to a branch. |
| `git switch main` | Switches the working files back to `main`. |
| `git push` | Sends local commits to the remote and updates a remote branch. |
| `git fetch` | Retrieves remote commits and branch information for inspection. |
| `git pull` | Fetches changes and integrates them into the current branch. |

## 3. Commands / tools used

`git status`, `git add`, `git commit`, `git log`, `git switch`, `git diff`, and `git push` were used to record and check the change. The GitHub API opened the pull request and verified its changed file.

## 4. My understanding

A local commit captures the staged changes. Pushing publishes the commit to a remote branch. A separate branch and pull request let a change receive review while main can keep moving.

## 5. Difficulties faced

The browser opened to a GitHub sign-in prompt.

## 6. How I resolved them

The existing Git credential authenticated Git pushes and GitHub API actions for the assignment repository.

## 7. Evidence / files

[`update-about` branch](https://github.com/MassGethu/digital-detective-8060/tree/update-about) and [open pull request](https://github.com/MassGethu/digital-detective-8060/pull/1).

## 8. Commit details

Commit message: `Complete Git and GitHub collaboration mission`. The [public main-branch history](https://github.com/MassGethu/digital-detective-8060/commits/main/) shows the mission commits.
