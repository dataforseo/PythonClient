# RedditReviews


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subreddit** | **str** | the name of the subreddit | [optional] 
**author_name** | **str** | nickname of the author nicknname of the user who published the post in the subreddit and shared the URL | [optional] 
**title** | **str** | title of the subreddit post | [optional] 
**permalink** | **str** | URL to the subreddit post | [optional] 
**subreddit_members** | **int** | number of subreddit members | [optional] 

## Example

```python
from dataforseo_client.models.reddit_reviews import RedditReviews

# TODO update the JSON string below
json = "{}"
# create an instance of RedditReviews from a JSON string
reddit_reviews_instance = RedditReviews.from_json(json)
# print the JSON string representation of the object
print(RedditReviews.to_json())

# convert the object into a dict
reddit_reviews_dict = reddit_reviews_instance.to_dict()
# create an instance of RedditReviews from a dict
reddit_reviews_from_dict = RedditReviews.from_dict(reddit_reviews_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


