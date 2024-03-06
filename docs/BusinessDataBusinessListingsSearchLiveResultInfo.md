[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BusinessDataBusinessListingsSearchLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | total number of results in our database relevant to your request | [optional]
**count** | **int** | item types the number of items in the items array | [optional]
**offset** | **int** | offset in the results array of returned businesses | [optional]
**offset_token** | **str** | token for subsequent requests by specifying the unique offset_token when setting a new task, you will get the subsequent results of the initial task; offset_token values are unique for each subsequent task | [optional]
**items** | [**List[BusinessDataBusinessListingsSearchLiveItem]**](BusinessDataBusinessListingsSearchLiveItem.md) | encountered item types types of search engine results encountered in the items array; possible item types: business_listing | [optional]

## Example

```python
from dataforseo_client.models.business_data_business_listings_search_live_result_info import BusinessDataBusinessListingsSearchLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataBusinessListingsSearchLiveResultInfo from a JSON string
business_data_business_listings_search_live_result_info_instance = BusinessDataBusinessListingsSearchLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataBusinessListingsSearchLiveResultInfo.to_json()

# convert the object into a dict
business_data_business_listings_search_live_result_info_dict = business_data_business_listings_search_live_result_info_instance.to_dict()
# create an instance of BusinessDataBusinessListingsSearchLiveResultInfo from a dict
business_data_business_listings_search_live_result_info_form_dict = business_data_business_listings_search_live_result_info.from_dict(business_data_business_listings_search_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")