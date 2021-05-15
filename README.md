# bug_free_game
Collaborative game-dev-arino project

This project will be free of bugs


### Setup
This project requires [pre-commit](https://pre-commit.com/) to be installed for the git installation you're using for this project.

### Running Locally
Getting this project set up and running locally should be easy to accomplish with a few simple steps:
1. Install Python 3.9: https://www.python.org/downloads/release/python-394/
2. Pull down the project locally with `git clone https://github.com/spg1502/bug-free-game.git`
3. Use pip to install the project's requirements: `pip install -r REQUIREMENTS.txt`
4. Run the game with `python -m bugFreeGame.py`

### Contributing
Our dev team currently uses PyCharm as our IDE, so the following instructions will assume you're using the same.
1. Install PyCharm: https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html
2. Import the project into PyCharm
3. Make your changes
4. Run the game to view your changes by using the `.run` run configuration
5. Test your changes with `python -m unittest tests/test_game.py`
6. If you're happy with your changes, make a pull request with `git push origin HEAD:<branch name here>`