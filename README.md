# Git Essentials / Git For Everybody
Visit [gitforeverybody.com](https://gitforeverybody.com/) for free tutorials and the full course.

> This is a course to teach you how to use everyday git.


## Contributing
Welcome to my example Git Essentials repo! If you're here from the course, you have a few options:

1. Clone this repo to download all the code you see here (but you can't make changes and overwrite my code)
2. Fork this repo to add all this code to your GitHub profile _and then_ clone this repository from your account. Then you can make file changes and `git push` them to your forked version of this repo.
3. Open a GitHub issue! Feel free to open an issue and explore.
4. Once you've forked this repo and made some changes, you can open a pull request to merge your code into my repo here. Feel free to experiment with that until you feel confident opening a pull request.

If you decide to open a pull request and add some work to this repo, I ask that you keep it simple. You can add a new file or update this README.md file with your name in the contributors list at the bottom, but please don't make changes to the original files from the course.

## Where to get this course:
- [x] [Git for Everybody.com](https://gitforeverybody.com/git-essentials/)
- [x] [Git Essentials on Skillshare.com](https://skl.sh/2viPzB9)
- [x] [Git Essentials on Udemy.com](https://www.udemy.com/course/git-and-github-tutorial/?referralCode=91132F334DCD0CCAA250)

## Docker (advanced devs only)
If you want a completely new and clean environment to start learning git form scratch, you can use a Docker container. That's what I did for this course. Below are the steps to reproduce the same setup I used in the Git Essentials course:

```bash
git clone git@github.com:KalobTaulien/git-essentials.git
cd git-esentials
docker build -t git .
docker run -itd --hostname "gitforeverybody.com" --name "gitforeverybody.com" git
docker container ls -a
docker exec -it <container_id> bash

# Once inside your Docker container, run these commands:
apt update
apt install vim nano git
export PS1="\[$(tput setaf 6)\]kalob\[$(tput setaf 2)\]@\[$(tput setaf 3)\]gitforeverybody.com: \[$(tput sgr0)\]"
export TERM=xterm-256color

# Now you can run git commands as if you were on a brand new computer. You'll need to generate an SSH key and add it to GitHub.
```

## Contibutors
If you're opening a pull request against this repo, you should put your name (and website, optional) in the list below!

* Kalob Taulien [(website)](https://gitforeverybody.com/)
* Magni Inter Pix [(website)](https://magniip.com/)

___

Course created by Kalob Taulien.
