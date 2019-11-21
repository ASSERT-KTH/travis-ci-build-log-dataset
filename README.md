# travis-ci-build-log-dataset

This original list of this dataset is based on projects on github that :
  - use travis-ci
  - were active at the time of the gathering (nov. 2018)
  - have a checkstyle.xml ruleset.

You can list all repos with `find . -maxdepth 2 -mindepth 2`

## Collect more repos

Install the virtual env :
```bash
virtualenv --python=python3 venv
source ./venv/bin/activate
pip install -r ./requirements.txt
```

Then you can add your travis ci token to the config :

```bash
cp ./config.example.ini ./cofig.ini
nano ./cofig.ini
```

Then you can run one of the following command :

```bash
python ./collect.py get owner/repo
python ./collect.py get-pool [n-threads] [owner1/repo1] [owner2/repo2] ....
```
