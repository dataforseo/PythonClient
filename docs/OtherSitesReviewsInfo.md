# OtherSitesReviewsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | review title contains a name of the third-party site where review initially appeared | [optional] 
**url** | **str** | review url URL to the a third-party site where review initially appeared | [optional] 
**review_text** | **str** | review text text of the review | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.other_sites_reviews_info import OtherSitesReviewsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OtherSitesReviewsInfo from a JSON string
other_sites_reviews_info_instance = OtherSitesReviewsInfo.from_json(json)
# print the JSON string representation of the object
print(OtherSitesReviewsInfo.to_json())

# convert the object into a dict
other_sites_reviews_info_dict = other_sites_reviews_info_instance.to_dict()
# create an instance of OtherSitesReviewsInfo from a dict
other_sites_reviews_info_form_dict = other_sites_reviews_info.from_dict(other_sites_reviews_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


