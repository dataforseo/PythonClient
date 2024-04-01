# FeaturedSnippetSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements found in SERP note values are returned in the ascending order, with values corresponding to advanced SERP features omitted from the results; to get all items (including SERP features and rich snippets) with their positions, please refer to the Google Organiс Advanced SERP endpoint | [optional] 
**domain** | **str** | domain of the ad element in SERP | [optional] 
**title** | **str** | title of the ad element in SERP | [optional] 
**description** | **str** | description of the ad element in SERP | [optional] 
**url** | **str** | relevant URL of the ad element in SERP | [optional] 
**breadcrumb** | **str** | breadcrumb of the ad element in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**featured_title** | **str** | title | [optional] 
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**images** | [**List[ImagesElement]**](ImagesElement.md) | images of the element | [optional] 
**table** | [**Table**](Table.md) |  | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.featured_snippet_serp_element_item import FeaturedSnippetSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturedSnippetSerpElementItem from a JSON string
featured_snippet_serp_element_item_instance = FeaturedSnippetSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(FeaturedSnippetSerpElementItem.to_json())

# convert the object into a dict
featured_snippet_serp_element_item_dict = featured_snippet_serp_element_item_instance.to_dict()
# create an instance of FeaturedSnippetSerpElementItem from a dict
featured_snippet_serp_element_item_form_dict = featured_snippet_serp_element_item.from_dict(featured_snippet_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


