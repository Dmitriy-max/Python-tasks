Crypto Address Management
Crypto Address Management - is an application used to manage crypto addresses.


Quick Start

python3 -m venv .venv
source .venv/bin/activate
pip install --requirement requirements-dev.txt
python3 flask_api.py


Launch

Inside Docker


TBD



From sources

Prerequisites

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt






Developer Notes

Init

Open the project in VS Code

Setup recommended extensions in VS Code such a ms-python.python

Initialize Virtual Environment

python3 -m venv .venv





Re-new requirements.txt

python3 -m pip freeze > requirements.txt





Rebase work branch

At some point you may want to rebase your branch to actual state on dev branch... So lets do it.

Lets said your work branch is 15-my-pretty-cool-task. You have to execute following sequence of commands:

git fetch --all
git checkout 15-my-pretty-cool-task
git rebase origin/dev

###... HERE YOU MAY HAVE A PROBLEM WITH CONFLICTS... YOU HAVE TO MERGE CHANGES LOCALLY ...###

git push --force
