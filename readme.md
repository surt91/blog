# This is my personal blog. [![Build Status](https://travis-ci.org/surt91/blog.svg?branch=master)](https://travis-ci.org/surt91/blog) [![Scc Count Badge](https://sloc.xyz/github/surt91/blog/)](https://github.com/surt91/blog/)

Visit it at [blog.schawe.me](https://blog.schawe.me)

## Setup

Ensure that `python3` is installed and `pip` is available. Advanced users might prefer to perform
step 4. in a python [virtual environment](https://docs.python.org/3/tutorial/venv.html).

1. `git clone https://github.com/surt91/blog.git`
2. `cd blog`
3. `git submodule update --init --recursive`
4. `pip3 install --user -r requirements.txt`
5. `make publish`
6. upload the static files in the `output` directory to some web server or use a cloud service
    * [GitHub pages](https://pages.github.com/) using [TravisCI](https://travis-ci.org/) and [`.travis.yml`](.travis.yml)
    * [Netlify](https://www.netlify.com/) using [`netlify.toml`](netlify.toml)
