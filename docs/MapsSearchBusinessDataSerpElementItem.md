# MapsSearchBusinessDataSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from the rank_group | [optional] 
**rank_absolute** | **int** | absolute rank among all the elements | [optional] 
**domain** | **str** | domain of the business entity | [optional] 
**title** | **str** | directory title can take the following values: At this place, Directory | [optional] 
**url** | **str** | URL to view the menu | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**rating_distribution** | **Dict[str, Optional[int]]** | the distribution of ratings of the business entity the object displays the number of 1-star to 5-star ratings, as reviewed by users | [optional] 
**snippet** | **str** | additional information about the business entity | [optional] 
**address** | **str** | address of the business entity | [optional] 
**address_info** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**place_id** | **str** | unique place identifier place id of the local establishment featured in the element learn more about the identifier in this help center article | [optional] 
**phone** | **str** | phone number of the business entity | [optional] 
**main_image** | **str** | URL of the main image featured in Google My Business profile | [optional] 
**total_photos** | **int** | total count of images featured in Google My Business profile | [optional] 
**category** | **str** | business category Google My Business general category that best describes the services provided by the business entity | [optional] 
**additional_categories** | **List[str]** | additional business categories additional Google My Business categories that describe the services provided by the business entity in more detail | [optional] 
**price_level** | **str** | property price level can take values: inexpensive, moderate, expensive, very_expensive if there is no price level information, the value will be null | [optional] 
**hotel_rating** | **int** | hotel class rating class ratings range between 1-5 stars, learn more if there is no hotel class rating information, the value will be null | [optional] 
**category_ids** | **List[str]** | global category IDs universal category IDs that do not change based on the selected country | [optional] 
**work_hours** | [**WorkInfo**](WorkInfo.md) |  | [optional] 
**feature_id** | **str** | the unique identifier of the element in SERP learn more about the identifier in this help center article | [optional] 
**cid** | **str** | google-defined client id unique id of a local establishment; can be used with Google Reviews API to get a full list of reviews learn more about the identifier in this help center article | [optional] 
**latitude** | **float** | latitude coordinate of the local establishments in google maps example: \&quot;latitude\&quot;: 51.584091 | [optional] 
**longitude** | **float** | longitude coordinate of the local establishment in google maps example: \&quot;longitude\&quot;: -0.31365919999999997 | [optional] 
**is_claimed** | **bool** | shows whether the entity is verified by its owner on Google Maps | [optional] 
**local_justifications** | **List[str]** | Google local justifications snippets of text that “justify” why the business is showing up for search query | [optional] 
**is_directory_item** | **bool** | business establishment is a part of the directory indicates whether the business establishment is a part of the directory; if true, the item is a part of the larger directory of businesses with the same address (e.g., a mall or a business centre); note: if the business establishment is a parent item in the directory, the value will be null | [optional] 

## Example

```python
from dataforseo_client.models.maps_search_business_data_serp_element_item import MapsSearchBusinessDataSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of MapsSearchBusinessDataSerpElementItem from a JSON string
maps_search_business_data_serp_element_item_instance = MapsSearchBusinessDataSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(MapsSearchBusinessDataSerpElementItem.to_json())

# convert the object into a dict
maps_search_business_data_serp_element_item_dict = maps_search_business_data_serp_element_item_instance.to_dict()
# create an instance of MapsSearchBusinessDataSerpElementItem from a dict
maps_search_business_data_serp_element_item_form_dict = maps_search_business_data_serp_element_item.from_dict(maps_search_business_data_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


