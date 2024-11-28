# DataforseoLabsStatusInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_update** | **str** | update date of the Google endpoints indicates the last date when the Google endpoints of DataForSEO Labs API were updated; example: 2022-05-16 | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_status_info import DataforseoLabsStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsStatusInfo from a JSON string
dataforseo_labs_status_info_instance = DataforseoLabsStatusInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsStatusInfo.to_json())

# convert the object into a dict
dataforseo_labs_status_info_dict = dataforseo_labs_status_info_instance.to_dict()
# create an instance of DataforseoLabsStatusInfo from a dict
dataforseo_labs_status_info_from_dict = DataforseoLabsStatusInfo.from_dict(dataforseo_labs_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


