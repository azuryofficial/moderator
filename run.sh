case $OSTYPE in
  msys*)
    pipenv install
    python3 moderator.py
  ;;
  linux*)
    pipenv install
    python moderator.py
  ;;
esac