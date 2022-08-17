# How to contribute to RecycleIT
## Read and agree to the License
RecycleIT is licencend under GPL-3.0. Make sure that you agree with this
licence before contributing to the project.

## Fork the project
- Fork the project to your GitHub.
- Then clone the forked project to your computer:

```
git clone https://github.com/your-github-username/RecycleIT-A
```

## Sync your fork
Always sync your fork with the origin repository. You can do it on GitHub or
in the command line:

```
# Add a new remote upstream repository
git remote add upstream https://github.com/RecycleAI/RecycleIT-A.git

# Sync your fork on your device
git fetch upstream
git checkout main
git merge upstream/main

# Sync your fork on your GitHub repo
git push
```

## Create a new branch
- The recommended name of the branch contains the name of the feature you are
working on. For example I am writhn a "How to contribute" document and I will
use "howto-contribute" for the name of my branch:

```
git branch howto-contribute
```

Then switch to your branch:

```
git checkout howto-contribute
```

## Do your changes
Do your changes in the repository. For instance add a new code, fix a bug or
modify the README. Then do:

```
git branch --set-upstream-to=origin/main howto-contribute
```

Add the file/code that you created/modified:

```
git add name-of-the-file
```

Then commit the changes with a meaningful comment:

```
git commit -m "A meaningful comment here please"
```

## Push your branch
Push your branch to your GitHub fork:

```
git push origin howto-contribute
```

## Create a pull request
After all this you will see a "Compare and pull request" green button in your
GitHub. Click on it and make a miningful pull request by adding a title, the
reason for your commit and a link to the issue (if you are resolving an issue).

At this stage you are done and you have to wait for the approval of your pull
request.