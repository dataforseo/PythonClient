# GoogleBusinessInfoBusinessDataSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment in SERP | [optional] 
**title** | **str** | title of the element in SERP the name of the business entity for which the results are collected | [optional] 
**original_title** | **str** | original title of the element original title not translated by Google | [optional] 
**description** | **str** | description of the element in SERP the description of the business entity for which the results are collected | [optional] 
**category** | **str** | business category Google My Business general category that best describes the services provided by the business entity | [optional] 
**category_ids** | **List[str]** | global category IDs universal category IDs that do not change based on the selected country | [optional] 
**additional_categories** | **List[str]** | additional business categories additional Google My Business categories that describe the services provided by the business entity in more detail | [optional] 
**cid** | **str** | google-defined client id unique id of a local establishment; can be used with Google Reviews API to get a full list of reviews learn more about the identifier in this help center article | [optional] 
**feature_id** | **str** | the unique identifier of the element in SERP learn more about the identifier in this help center article | [optional] 
**address** | **str** | address of the business entity | [optional] 
**address_info** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**place_id** | **str** | unique place identifier place id of the local establishment featured in the element learn more about the identifier in this help center article | [optional] 
**phone** | **str** | phone number of the business entity | [optional] 
**url** | **str** | absolute url of the business entity | [optional] 
**contact_url** | **str** | URL of the preferred contact page | [optional] 
**contributor_url** | **str** | URL of the user’s or entity’s Local Guides profile, if available | [optional] 
**book_online_url** | **str** | URL in the ‘book online’ button of the element URL directing users to the online booking or order page of the business entity | [optional] 
**domain** | **str** | domain of the business entity | [optional] 
**logo** | **str** | URL of the logo featured in Google My Business profile | [optional] 
**main_image** | **str** | URL of the main image featured in Google My Business profile | [optional] 
**total_photos** | **int** | total count of images featured in Google My Business profile | [optional] 
**snippet** | **str** | additional information on the business entity | [optional] 
**latitude** | **float** | latitude coordinate of the local establishments in google maps example: \&quot;latitude\&quot;: 51.584091 | [optional] 
**longitude** | **float** | longitude coordinate of the local establishment in google maps example: \&quot;longitude\&quot;: -0.31365919999999997 | [optional] 
**is_claimed** | **bool** | shows whether the entity is verified by its owner on Google Maps | [optional] 
**questions_and_answers_count** | **int** |  | [optional] 
**attributes** | [**BusinessDataAttributesInfo**](BusinessDataAttributesInfo.md) |  | [optional] 
**place_topics** | **Dict[str, Optional[int]]** | keywords mentioned in customer reviews contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword example:  \&quot;place_topics\&quot;: { \&quot;egg roll\&quot;: 48, \&quot;birthday\&quot;: 33 } | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**hotel_rating** | **int** | hotel class rating class ratings range between 1-5 stars, learn more if there is no hotel class rating information, the value will be null | [optional] 
**price_level** | **str** | property price level can take values: inexpensive, moderate, expensive, very_expensive if there is no price level information, the value will be null | [optional] 
**rating_distribution** | **Dict[str, Optional[int]]** | the distribution of ratings of the business entity the object displays the number of 1-star to 5-star ratings, as reviewed by users | [optional] 
**people_also_search** | [**List[PeopleAlsoSearch]**](PeopleAlsoSearch.md) | related business entities | [optional] 
**work_time** | [**WorkTime**](WorkTime.md) |  | [optional] 
**popular_times** | [**PopularTimes**](PopularTimes.md) |  | [optional] 
**local_business_links** | [**List[BaseLocalBusinessLink]**](BaseLocalBusinessLink.md) | available interactions with the business list of options to interact with the business directly from search results | [optional] 
**is_directory_item** | **bool** | business establishment is a part of the directory indicates whether the business establishment is a part of the directory; if true, the item is a part of the larger directory of businesses with the same address (e.g., a mall or a business centre); note: if the business establishment is a parent item in the directory, the value will be null | [optional] 
**directory** | [**BusinessDirectoryInfo**](BusinessDirectoryInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.google_business_info_business_data_serp_element_item import GoogleBusinessInfoBusinessDataSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleBusinessInfoBusinessDataSerpElementItem from a JSON string
google_business_info_business_data_serp_element_item_instance = GoogleBusinessInfoBusinessDataSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleBusinessInfoBusinessDataSerpElementItem.to_json())

# convert the object into a dict
google_business_info_business_data_serp_element_item_dict = google_business_info_business_data_serp_element_item_instance.to_dict()
# create an instance of GoogleBusinessInfoBusinessDataSerpElementItem from a dict
google_business_info_business_data_serp_element_item_from_dict = GoogleBusinessInfoBusinessDataSerpElementItem.from_dict(google_business_info_business_data_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


