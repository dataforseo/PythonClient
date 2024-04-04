# DataforseoLabsBingSubdomainsLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**target** | **str** | domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**total_count** | **int** | total amount of results in our database relevant to your request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[DataforseoLabsSubdomainsLiveItem]**](DataforseoLabsSubdomainsLiveItem.md) | contains subdomains and related data | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_bing_subdomains_live_result_info import DataforseoLabsBingSubdomainsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBingSubdomainsLiveResultInfo from a JSON string
dataforseo_labs_bing_subdomains_live_result_info_instance = DataforseoLabsBingSubdomainsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsBingSubdomainsLiveResultInfo.to_json()

# convert the object into a dict
dataforseo_labs_bing_subdomains_live_result_info_dict = dataforseo_labs_bing_subdomains_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsBingSubdomainsLiveResultInfo from a dict
dataforseo_labs_bing_subdomains_live_result_info_form_dict = dataforseo_labs_bing_subdomains_live_result_info.from_dict(dataforseo_labs_bing_subdomains_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


