# DataAmazonAmazonReviewItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank among all the listed reviews absolute position among all reviews on the list | [optional] 
**position** | **str** | the alignment of the review in SERP can take the following values: right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**verified** | **bool** | indicates whether the review has the “Verified Purchase” mark | [optional] 
**subtitle** | **str** | subtitle of the review | [optional] 
**helpful_votes** | **int** | helpful votes count number of users who clicked on the ‘Helpful” button under the review text | [optional] 
**images** | [**List[ImagesElement]**](ImagesElement.md) | images of the product submitted by the reviewer | [optional] 
**videos** | [**List[VideoElement]**](VideoElement.md) | videos of the product submitted by the reviewer | [optional] 
**user_profile** | [**UserProfileInfo**](UserProfileInfo.md) |  | [optional] 
**title** | **str** | title of the review | [optional] 
**url** | **str** | URL to the review | [optional] 
**review_text** | **str** | content of the review | [optional] 
**publication_date** | **str** | date and time when the review was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15 12:57:46 +00:00 | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.data_amazon_amazon_review_item_serp_element_item import DataAmazonAmazonReviewItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAmazonAmazonReviewItemSerpElementItem from a JSON string
data_amazon_amazon_review_item_serp_element_item_instance = DataAmazonAmazonReviewItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(DataAmazonAmazonReviewItemSerpElementItem.to_json())

# convert the object into a dict
data_amazon_amazon_review_item_serp_element_item_dict = data_amazon_amazon_review_item_serp_element_item_instance.to_dict()
# create an instance of DataAmazonAmazonReviewItemSerpElementItem from a dict
data_amazon_amazon_review_item_serp_element_item_form_dict = data_amazon_amazon_review_item_serp_element_item.from_dict(data_amazon_amazon_review_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


