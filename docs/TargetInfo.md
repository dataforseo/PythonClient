# TargetInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** | server | [optional] 
**cms** | **str** | content management system | [optional] 
**platform_type** | **List[Optional[str]]** | platform type | [optional] 
**ip_address** | **str** | IP address of the target | [optional] 
**country** | **str** | country code that the target domain is determined to belong to | [optional] 
**is_ip** | **bool** | indicates if the target is IP if true, the domain, subdomain or webpage functions as an IP address and does not have a domain name | [optional] 
**target_spam_score** | **int** | spam score of the target if the target is a domain/subdomain, this fields indicates the average spam score of all pages of that domain/subdomain; learn more about how the metric is calculated on this help center page | [optional] 

## Example

```python
from dataforseo_client.models.target_info import TargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TargetInfo from a JSON string
target_info_instance = TargetInfo.from_json(json)
# print the JSON string representation of the object
print(TargetInfo.to_json())

# convert the object into a dict
target_info_dict = target_info_instance.to_dict()
# create an instance of TargetInfo from a dict
target_info_form_dict = target_info.from_dict(target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


