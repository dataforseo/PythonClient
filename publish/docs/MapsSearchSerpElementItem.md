# MapsSearchSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**domain** | **str** | domain in the SERP element | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | relevant URL in SERP | [optional] 
**contact_url** | **str** | URL of the preferred contact page | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**hotel_rating** | **int** | hotel class rating class ratings range between 1-5 stars, learn more if there is no hotel class rating information, the value will be null | [optional] 
**price_level** | **str** | property price level can take values: inexpensive, moderate, expensive, very_expensive if there is no price level information, the value will be null | [optional] 
**rating_distribution** | **Dict[str, Optional[int]]** | the distribution of ratings of the business entity the object displays the number of 1-star to 5-star ratings, as reviewed by users | [optional] 
**snippet** | **str** | element snippet contains the address and other information about the local establishment featured in the element | [optional] 
**address** | **str** | address line address of the local establishment featured in the element | [optional] 
**address_info** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**place_id** | **str** | unique place identifier place id of the local establishment featured in the element | [optional] 
**phone** | **str** | phone number phone number of the local establishment featured in the element | [optional] 
**main_image** | **str** | URL of the main image featured in Google My Business profile | [optional] 
**total_photos** | **int** | total count of images featured in Google My Business profile | [optional] 
**category** | **str** | business category Google My Business general category that best describes the services provided by the business entity | [optional] 
**additional_categories** | **List[Optional[str]]** | additional business categories additional Google My Business categories that describe the services provided by the business entity in more detail | [optional] 
**category_ids** | **List[Optional[str]]** | global category IDs universal category IDs that do not change based on the selected country | [optional] 
**work_hours** | [**WorkHours**](WorkHours.md) |  | [optional] 
**feature_id** | **str** | the unique identifier of the element in SERP | [optional] 
**cid** | **str** | google-defined client id unique id of a local establishment; can be used with Google Reviews API to get a full list of reviews | [optional] 
**latitude** | **float** | latitude coordinate of the local establishments in google maps example: \&quot;latitude\&quot;: 51.584091 | [optional] 
**longitude** | **float** | longitude coordinate of the local establishment in google maps example: \&quot;longitude\&quot;: -0.31365919999999997 | [optional] 
**is_claimed** | **bool** | indicates whether ownership of this local establishment is claimed | [optional] 
**local_justifications** | [**List[LocalJustificationInfo]**](LocalJustificationInfo.md) | Google local justifications snippets of text that “justify” why the business is showing up for search query | [optional] 
**is_directory_item** | **bool** | indicates whether this local establishment is a directory | [optional] 

## Example

```python
from dataforseo_client.models.maps_search_serp_element_item import MapsSearchSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of MapsSearchSerpElementItem from a JSON string
maps_search_serp_element_item_instance = MapsSearchSerpElementItem.from_json(json)
# print the JSON string representation of the object
print MapsSearchSerpElementItem.to_json()

# convert the object into a dict
maps_search_serp_element_item_dict = maps_search_serp_element_item_instance.to_dict()
# create an instance of MapsSearchSerpElementItem from a dict
maps_search_serp_element_item_form_dict = maps_search_serp_element_item.from_dict(maps_search_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


