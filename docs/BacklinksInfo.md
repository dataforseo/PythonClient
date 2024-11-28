# BacklinksInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referring_domains** | **int** | number of referring domains | [optional] 
**referring_main_domains** | **int** | number of referring main domains | [optional] 
**referring_pages** | **int** | number of referring pages | [optional] 
**dofollow** | **int** | number of dofollow links | [optional] 
**backlinks** | **int** | total number of backlinks the total number of backlinks, including dofollow and nofollow links | [optional] 
**time_update** | **str** | date and time when backlink data was updated in the UTC format: \&quot;yyyy-mm-dd hh-mm-ss +00:00\&quot; example: 2019-11-15 12:57:46 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_info import BacklinksInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksInfo from a JSON string
backlinks_info_instance = BacklinksInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksInfo.to_json())

# convert the object into a dict
backlinks_info_dict = backlinks_info_instance.to_dict()
# create an instance of BacklinksInfo from a dict
backlinks_info_from_dict = BacklinksInfo.from_dict(backlinks_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


