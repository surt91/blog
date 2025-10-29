# :black_nib: This is the repository of my personal blog

[![CI](https://github.com/surt91/blog/actions/workflows/main.yml/badge.svg)](https://github.com/surt91/blog/actions/workflows/main.yml)

Visit it at [blog.schawe.me](https://blog.schawe.me).

## :hammer_and_wrench: Setup

Ensure that `python3` is installed and `uv` is available.

1. `git clone https://github.com/surt91/blog.git`
2. `cd blog`
3. `git submodule update --init --recursive`
4. `uv sync`
5. `uv run make publish`
6. upload the static files in the `output` directory to some web server or use a cloud service
    * [GitHub pages](https://pages.github.com/) using GitHub Actions
    * [Netlify](https://www.netlify.com/) using [`netlify.toml`](netlify.toml)
