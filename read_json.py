import json
from analysis import analyze, find_verified

def read(file_name):

    with open(file=file_name) as f:
        data = json.load(f)
    
    users = data["includes"]["users"]

    for d in data['data']:
        isverified = find_verified(d["author_id"], users)
        analyzed = analyze(d['text'].replace('\n', ' '), isverified, d["created_at"])
        print('analysis:', analyzed)

if __name__ == "__main__":
    read('tweets-2022-05-21_00-36-53.json')