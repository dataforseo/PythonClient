# GoogleBusinessPostBusinessDataSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank among all the listed updates absolute position among all present elements | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**author** | **str** | author of the post | [optional] 
**snippet** | **str** | additional content of a post | [optional] 
**post_text** | **str** | main content of a post | [optional] 
**url** | **str** | url of a post | [optional] 
**images_url** | **str** | url of an image included in the post | [optional] 
**post_date** | **str** | date when a post was published in the following format: \&quot;mm/dd/yyyy hh:mm:ss\&quot; | [optional] 
**timestamp** | **str** | time when a post was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | links included in the post | [optional] 

## Example

```python
from dataforseo_client.models.google_business_post_business_data_serp_element_item import GoogleBusinessPostBusinessDataSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleBusinessPostBusinessDataSerpElementItem from a JSON string
google_business_post_business_data_serp_element_item_instance = GoogleBusinessPostBusinessDataSerpElementItem.from_json(json)
# print the JSON string representation of the object
print GoogleBusinessPostBusinessDataSerpElementItem.to_json()

# convert the object into a dict
google_business_post_business_data_serp_element_item_dict = google_business_post_business_data_serp_element_item_instance.to_dict()
# create an instance of GoogleBusinessPostBusinessDataSerpElementItem from a dict
google_business_post_business_data_serp_element_item_form_dict = google_business_post_business_data_serp_element_item.from_dict(google_business_post_business_data_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


