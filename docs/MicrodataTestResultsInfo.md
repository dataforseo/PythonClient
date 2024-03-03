# MicrodataTestResultsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | level of microdata error can take the following values: fatal, error, warning, info | [optional] 
**message** | **str** | message associated with an error message providing the details of the detected error | [optional] 

## Example

```python
from dataforseo_client.models.microdata_test_results_info import MicrodataTestResultsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodataTestResultsInfo from a JSON string
microdata_test_results_info_instance = MicrodataTestResultsInfo.from_json(json)
# print the JSON string representation of the object
print MicrodataTestResultsInfo.to_json()

# convert the object into a dict
microdata_test_results_info_dict = microdata_test_results_info_instance.to_dict()
# create an instance of MicrodataTestResultsInfo from a dict
microdata_test_results_info_form_dict = microdata_test_results_info.from_dict(microdata_test_results_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


