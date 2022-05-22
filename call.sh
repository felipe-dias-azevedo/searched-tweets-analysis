#!/bin/bash

curl "https://api.twitter.com/2/tweets/search/all?query=%22PROUNI%22%20-is%3Aretweet%20-is%3Areply%20lang%3Apt&max_results=11&sort_order=relevancy&expansions=author_id&tweet.fields=id,created_at,text,public_metrics&user.fields=id,created_at,verified,public_metrics" -H "Authorization: Bearer $BEARER_TOKEN"