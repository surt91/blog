Title: git subtree
Date: 2022-07-24 17:31
Category: Snip
Slug: git-subtree
Status: published
Lang: en

Who does not know this common situation: We have a new Idea to extend our existing Project `old`. So we create a subdirectory `newIdea` in the corresponding repository. It turns out that the idea was so good that it would also be useful outside of the project `old`. It would be sensible to create a new repository `new` which should only contain the subdirectory `newIdea`. In fact, this problem seems to be so common that there is a special git subcommand since 2012 for this purpose (and more complicated cases): `git subtree`

## New repository from subdirectory

```
old/
├─ newIdea/
│  ├─ lib.rs
├─ main.rs
```

So inside the directory `old` we execute the following command:

```bash
git subtree split --prefix=newIdea/ --branch=onlyNewIdeaBranch
```

This creates a new Branch `onlyNewIdeaBranch` which only contains the contents of `newIdea`, i.e., a new root directory. So this branch has a newly written history consisting only of commits with influence on files below of `newIdea/`.

Now we can create the new repository `new` and pull the newly created branch.Branch pullen.

```bash
cd .. ; mkdir new ; cd new
git init
git pull ../alt onlyNewIdeaBranch
```

Maybe we want to delete the `newIdea` subdirectory from the `old` repository. Probably we have to change infrastructure code in the `new` repository.

```
old/
├─ main.rs
new/
├─ lib.rs
```

## Move a subdirectory into an existing repository

Possibly we notice that the code would fit better into an existing repository instead of a new one? Perhaps because we are in the process of moving our code into a monorepo? No problem at all!

```
old/
├─ newIdea/
│  ├─ lib.rs
├─ main.rs
monorepo/
├─ project1/
├─ project2/
```

We already created the `onlyNewIdeaBranch`, which we want to move into the subdirectory `goodIdea` of the `monorepo`. Again, we can solve it with `git subtree`:

```bash
cd monorepo
git branch withGoodIdeadBranch
git checkout withGoodIdeadBranch
git subtree add --prefix=goodIdea/ ../old onlyNewIdeaBranch
```

As soon as we ensured that our new Branch `withGoodIdeadBranch` looks good and we modified the infrastructure code, we can merge it into main.

```
old/
├─ neueIdee/
│  ├─ lib.rs
├─ main.rs
monorepo/
├─ project1/
├─ project2/
├─ goodIdea/
│  ├─ lib.rs
```
