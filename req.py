from datetime import datetime
from dotenv import load_dotenv
from os import getenv
from requests import get
import json

def main():

    load_dotenv()

    token = getenv('TWEETER_TOKEN')
    max_count = 10

    val = get(f"https://api.twitter.com/2/tweets/search/recent?query=%22PROUNI%22%20-is%3Aretweet%20-is%3Areply%20lang%3Apt&max_results={max_count}&sort_order=relevancy&expansions=author_id&tweet.fields=id,created_at,text,public_metrics&user.fields=id,created_at,verified,public_metrics", headers={'Authorization': f"Bearer {token}"})

    if val.ok:
        print("REQUEST OK!")
        result = json.loads(val.content)
        dt = str(datetime.utcnow()).replace(':','-').replace(' ','_')[:-7]
        with open(f'tweets-{dt}.json', 'w') as fp:
            json.dump(result, fp, indent=4)
        print("JSON CREATED!")
    else:
        print("SOMETHING WENT WRONG...")
        print(val.status_code)
        print(val.text)


if __name__ == "__main__":
    main()
