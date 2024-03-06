[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# GoogleReviewsSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional]
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | the XPath of the element | [optional]
**reviews_count** | **int** | the number of reviews | [optional]
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional]
**place_id** | **str** | the identifier of a place | [optional]
**feature** | **str** | the additional feature of the review | [optional]
**cid** | **str** | google-defined client id | [optional]
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional]

## Example

```python
from dataforseo_client.models.google_reviews_serp_element_item import GoogleReviewsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleReviewsSerpElementItem from a JSON string
google_reviews_serp_element_item_instance = GoogleReviewsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print GoogleReviewsSerpElementItem.to_json()

# convert the object into a dict
google_reviews_serp_element_item_dict = google_reviews_serp_element_item_instance.to_dict()
# create an instance of GoogleReviewsSerpElementItem from a dict
google_reviews_serp_element_item_form_dict = google_reviews_serp_element_item.from_dict(google_reviews_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")