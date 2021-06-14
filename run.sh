case $OSTYPE in
  msys*)
    pip install --user pipenv
    pipenv install
    pipenv run python3 moderator.py
  ;;
  linux*)
    pip install --user pipenv
    pipenv install
    pipenv run python moderator.py
  ;;
esac