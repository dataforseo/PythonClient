[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BusinessDataBusinessListingsSearchLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the element in SERP the name of the business entity for which the results are collected | [optional]
**description** | **str** | description of the element in SERP the description of the business entity for which the results are collected | [optional]
**category** | **str** | business category Google My Business general category that best describes the services provided by the business entity | [optional]
**category_ids** | **List[Optional[str]]** | global category IDs universal category IDs that do not change based on the selected country | [optional]
**additional_categories** | **List[Optional[str]]** | additional business categories additional Google My Business categories that describe the services provided by the business entity in more detail | [optional]
**cid** | **str** | google-defined client id unique id of a local establishment learn more about the identifier in this help center article | [optional]
**feature_id** | **str** | the unique identifier of the element in SERP learn more about the identifier in this help center article | [optional]
**address** | **str** | address of the business entity | [optional]
**address_info** | [**AddressInfo**](AddressInfo.md) |  | [optional]
**place_id** | **str** | unique place identifier place id of the local establishment featured in the element learn more about the identifier in this help center article | [optional]
**phone** | **str** | phone number of the business entity | [optional]
**url** | **str** | absolute url of the business entity | [optional]
**domain** | **str** | domain of the business entity | [optional]
**logo** | **str** | URL of the logo featured in Google My Business profile | [optional]
**main_image** | **str** | URL of the main image featured in Google My Business profile | [optional]
**total_photos** | **int** | total count of images featured in Google My Business profile | [optional]
**snippet** | **str** | additional information on the business entity | [optional]
**latitude** | **float** | latitude coordinate of the local establishments in google maps example: \&quot;latitude\&quot;: 51.584091 | [optional]
**longitude** | **float** | longitude coordinate of the local establishment in google maps example: \&quot;longitude\&quot;: -0.31365919999999997 | [optional]
**is_claimed** | **bool** | shows whether the entity is verified by its owner on Google Maps | [optional]
**attributes** | [**BusinessDataAttributesInfo**](BusinessDataAttributesInfo.md) |  | [optional]
**place_topics** | **Dict[str, Optional[int]]** | keywords mentioned in customer reviews contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword example:  \&quot;place_topics\&quot;: { \&quot;egg roll\&quot;: 48, \&quot;birthday\&quot;: 33 } | [optional]
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional]
**rating_distribution** | **Dict[str, Optional[int]]** | the distribution of ratings of the business entity the object displays the number of 1-star to 5-star ratings, as reviewed by users | [optional]
**people_also_search** | [**List[PeopleAlsoSearch]**](PeopleAlsoSearch.md) | related business entities | [optional]
**work_time** | [**WorkInfo**](WorkInfo.md) |  | [optional]
**popular_times** | [**PopularTimes**](PopularTimes.md) |  | [optional]
**local_business_links** | [**List[BaseLocalBusinessLink]**](BaseLocalBusinessLink.md) | available interactions with the business list of options to interact with the business directly from search results | [optional]
**contact_info** | [**List[BusinessDataContactInfo]**](BusinessDataContactInfo.md) | available contacts of the business list of contacts to interact with the business | [optional]
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional]
**last_updated_time** | **str** | date and time when the data was last updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2023-01-26 09:03:15 +00:00 | [optional]

## Example

```python
from dataforseo_client.models.business_data_business_listings_search_live_item import BusinessDataBusinessListingsSearchLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataBusinessListingsSearchLiveItem from a JSON string
business_data_business_listings_search_live_item_instance = BusinessDataBusinessListingsSearchLiveItem.from_json(json)
# print the JSON string representation of the object
print BusinessDataBusinessListingsSearchLiveItem.to_json()

# convert the object into a dict
business_data_business_listings_search_live_item_dict = business_data_business_listings_search_live_item_instance.to_dict()
# create an instance of BusinessDataBusinessListingsSearchLiveItem from a dict
business_data_business_listings_search_live_item_form_dict = business_data_business_listings_search_live_item.from_dict(business_data_business_listings_search_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")