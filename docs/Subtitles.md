# Subtitles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | language of subtitles | [optional] 
**is_translatable** | **bool** | defines if subtitles are translatable | [optional] 
**is_auto_generated** | **bool** | defines if subtitles are auto generated | [optional] 

## Example

```python
from dataforseo_client.models.subtitles import Subtitles

# TODO update the JSON string below
json = "{}"
# create an instance of Subtitles from a JSON string
subtitles_instance = Subtitles.from_json(json)
# print the JSON string representation of the object
print(Subtitles.to_json())

# convert the object into a dict
subtitles_dict = subtitles_instance.to_dict()
# create an instance of Subtitles from a dict
subtitles_from_dict = Subtitles.from_dict(subtitles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


