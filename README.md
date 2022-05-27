# searched-tweets-analysis

This project search tweets with Twitter Search API and analyze its sentimentals with NLTKs libs

### Install

#### Dependencies

```
python3 -m venv env

source ./env/bin/activate

pip3 install -U pip

pip3 install -r requirements.txt
```

#### NLTK Data

```
python3

import nltk
nltk.download('stopwords')
nltk.download('punkt')
```