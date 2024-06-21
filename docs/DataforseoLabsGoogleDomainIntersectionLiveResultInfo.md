# DataforseoLabsGoogleDomainIntersectionLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**target1** | **str** | the first target domain in a POST array | [optional] 
**target2** | **str** | the second target domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**total_count** | **int** | total amount of results in our database relevant to your request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[DataforseoLabsDomainIntersectionLiveItem]**](DataforseoLabsDomainIntersectionLiveItem.md) | contains keywords, relevant SERP elements and related data | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_domain_intersection_live_result_info import DataforseoLabsGoogleDomainIntersectionLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleDomainIntersectionLiveResultInfo from a JSON string
dataforseo_labs_google_domain_intersection_live_result_info_instance = DataforseoLabsGoogleDomainIntersectionLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleDomainIntersectionLiveResultInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_domain_intersection_live_result_info_dict = dataforseo_labs_google_domain_intersection_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleDomainIntersectionLiveResultInfo from a dict
dataforseo_labs_google_domain_intersection_live_result_info_form_dict = dataforseo_labs_google_domain_intersection_live_result_info.from_dict(dataforseo_labs_google_domain_intersection_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


