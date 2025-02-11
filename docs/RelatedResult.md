# RelatedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**domain** | **str** | domain where a link points | [optional] 
**title** | **str** | title of a given link element | [optional] 
**url** | **str** | reference page URL | [optional] 
**cache_url** | **str** | cached version of the page | [optional] 
**related_search_url** | **str** | URL to a similar search URL to a new search for the same keyword(s) on related sites | [optional] 
**breadcrumb** | **str** | breadcrumb in SERP | [optional] 
**website_name** | **str** | name of the website in the ad element | [optional] 
**is_image** | **bool** | indicates whether the element contains an image | [optional] 
**is_video** | **bool** | indicates whether the element contains a video | [optional] 
**description** | **str** | description of the hotel booking element | [optional] 
**pre_snippet** | **str** | includes additional information appended before the result description in SERP | [optional] 
**extended_snippet** | **str** | includes additional information appended after the result description in SERP | [optional] 
**images** | [**List[ImagesElement]**](ImagesElement.md) | images of the element | [optional] 
**amp_version** | **bool** | Accelerated Mobile Pages indicates whether an item has the Accelerated Mobile Page (AMP) version | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional] 
**highlighted** | **List[Optional[str]]** | words highlighted in bold within the results description | [optional] 
**about_this_result** | [**AboutThisResultElement**](AboutThisResultElement.md) |  | [optional] 
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.related_result import RelatedResult

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedResult from a JSON string
related_result_instance = RelatedResult.from_json(json)
# print the JSON string representation of the object
print(RelatedResult.to_json())

# convert the object into a dict
related_result_dict = related_result_instance.to_dict()
# create an instance of RelatedResult from a dict
related_result_from_dict = RelatedResult.from_dict(related_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


