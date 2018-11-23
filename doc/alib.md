# Mylib contains a parser and related files for this parser

## Contributing
From @cpcloud:

My pandas workflow usually goes something like this:

0. Always use [`virtualenvwrapper`](http://virtualenvwrapper.readthedocs.org/en/latest/). Period. Then I do [`workon pandas`](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#workon).
1. Depending on how much time I have I'll try to prioritize based on some combination of which issues are high-priority and those for which I see an easy fix and those that I think would be fun to work on.
2. Once I've selected an issue I'll start hacking on it. I usually *don't* use any local branches unless I'm implementing something new and there's a bunch of things for that feature that can be worked on separately.
3. I use [`git stash`](http://git-scm.com/book/en/Git-Tools-Stashing) **all the time**. In fact so much so that I have aliases for every `git stash` subcommand. Often times I'll get interrupted and I'll need to stash something so I do. I can then come back to it. If you end up accumulating a crap ton of stashes (which I do) then you can inspect them with `git stash list` followed by `git stash -p stash@{0}` or whatever stash number you want to see the diff of. I'll also occasionally prune the stash via visual inspection and/or my own memory of what's been merged recently or by comparison of stashes to `upstream/master`.
4. Two things that I use a lot are the command `git push -u origin $(git rev-parse --abbrev-ref HEAD)` and [`hub`](https://github.com/github/hub). The first command pushes a remote branch with the same name as the one that I made locally to the `origin` remote (my fork). I have `git rev-parse --abbrev-ref HEAD` aliased to `gcb` which I remember as "git current branch". The other command I use is `hub pull-request -b pydata:master` which *automatically* submits a PR. I can essentially push the remote *and* the PR in a single step on the command line without having to use the mouse. Pretty neat.
5. `git reflog` is great for those times when you accidentally type `git reset --hard` and you need to recover something.
6. Finally I'll rebase using `git rebase upstream/master` to pull in the latest from the `upstream` remote (which I have set to `http://github.com/pydata/pandas.git`)
7. Throughout the dev process I'm constantly doing `git fetch && git rebase upstream/master`, although recently I've toned that down a bit and I've started to just do it when I need to.
8. I also use `git log` all the time. Since the standard `git log` is a bit too verbose I use [scm_breeze](https://github.com/ndbroadbent/scm_breeze) and it has a gorgeous standard `git log` (as long as you've set `git config --global color.ui auto`!)

`git merge` and `git rebase`
============================

`git merge`
-----------
`git merge <a-branch-name>` will take the union of the commits of the branch that you're currently on and the branch named `a-branch-name`. `git merge` is nice when you want to create a branch off of another branch and then you want to go back to your original branch and bring the changes from the branch you've just made changes in. 

For example,

```sh
git checkout master
git checkout -b new-branch

# try to not to break all the things!
gvim pandas/core/frame.py

git add .
git commit -m'ENH: made pandas awesomer!'

# make a new branch based off the one you're current on
git checkout -b newer-branch new-branch

# make some more awesome changes to frame.py

git checkout new-branch
git merge newer-branch
```

This can sometimes leave ugly messages like `Merged foo from bar` (but not always).

**NOTE:** It's worth spending a significant amount of time understanding some of the details of what `git` is doing, otherwise you'll always feel a bit lost. This is especially true when making changes to the history via `git rebase` or any other history changing mechanism. A Google search for "Git book" will turn up plenty of useful resources.

`git rebase`
------------
`git rebase` allows you to change the history of a repository. Changing the history is not necessarily a good thing (some people hate it) if you've pushed to a remote that a bunch of people depend on. For pandas pull requests, it's usually okay to rebase since very few people (if any) are going to base code off of your PR. Trolling the pandas repo, you'll see much talk about "I'll squash spam after I zip up the foo bar that does baz". This is just letting the core devs know that you're going to get rid of commits that are very small and/or have commit messages that are not meaningful.

Squashing and reordering commits is done with interactive rebases:

```sh
git rebase -i
```

A editor will pop up which lists all commits line by line. You can reorder them (just move the lines up&down), edit individual commits (prefix the commit with `edit` instead of `pick`), remove commits (simple delete the line) or squash them together (combine that commit with the commit in the line above -> Use `squash` to edit the commit message for the resulting commit or `fixup` to only use the commit message of the above commit). 

For example, if you found a small error in an earlier commit, you can do the small fix, commit with a simple commit message (`git commit -m "fixup for xyz"`) and then use `git rebase -i` to a) move the fixup commit line directly after the commit which had the error and then b) prefix that fixup commit line with `fixup` (or `f`) instead of `pick` to squash that commit into the previous one.

Another thing you probably want to do on occasion is:

```sh
git fetch upstream
git rebase upstream/master
```

**If a core developer asks you to rebase on top of master, this is what we mean.**

Rebasing will speed up the merging of your PR by making *you* deal with merge conflicts. Your changes are going to be most familiar to you and thus will be resolved faster than if someone who doesn't know why you did what you did tries to resolve the conflicts. Note that if you made changes to `pandas/doc/source/release.rst` and changes have occurred upstream then you'll almost always get a merge conflict from that. Those are pretty much unavoidable, so don't be scared when you get one. Just remove the conflict markers keeping your addition to `release.rst` *along with the lines that created the conflict*.

The people around pandas have been very patient and helpful with my (lack of) knowledge about `git` especially @y-p. If you're confused about something, even after reading the wiki and searching around for an answer, don't hesitate to ask. We won't bite :smile:

Also keep in mind that this is the tip of `git`-berg, but this can be a useful jumping off point to clarify a couple of conventions you might see around here.