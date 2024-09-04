# SerpGoogleDatasetInfoAdvancedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**dataset_id** | **str** | ID of the dataset | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional] 
**scholarly_citations_count** | **int** | count of articles that refer to the dataset | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | sitelinks the links shown below some of Google Dataset’s search results if there are none, equals null | [optional] 
**dataset_providers** | [**List[LicensesElement]**](LicensesElement.md) | the list of institutions that provided the dataset | [optional] 
**formats** | [**List[FormatsElement]**](FormatsElement.md) | the list of file formats of the dataset | [optional] 
**authors** | **object** | the list of authors of the dataset | [optional] 
**licenses** | [**List[LicensesElement]**](LicensesElement.md) | the list of licenses issued to the dataset | [optional] 
**updated_date** | **str** | date and time when the result was last updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2022-11-27 02:00:00 +00:00 | [optional] 
**area_covered** | **object** | the list of areas covered in the dataset for example: Africa, Global | [optional] 
**period_covered** | [**PeriodCovered**](PeriodCovered.md) |  | [optional] 
**dataset_description** | [**DatasetDescription**](DatasetDescription.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_dataset_info_advanced_item import SerpGoogleDatasetInfoAdvancedItem

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleDatasetInfoAdvancedItem from a JSON string
serp_google_dataset_info_advanced_item_instance = SerpGoogleDatasetInfoAdvancedItem.from_json(json)
# print the JSON string representation of the object
print SerpGoogleDatasetInfoAdvancedItem.to_json()

# convert the object into a dict
serp_google_dataset_info_advanced_item_dict = serp_google_dataset_info_advanced_item_instance.to_dict()
# create an instance of SerpGoogleDatasetInfoAdvancedItem from a dict
serp_google_dataset_info_advanced_item_form_dict = serp_google_dataset_info_advanced_item.from_dict(serp_google_dataset_info_advanced_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


