# StreamingQualityElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**label** | **str** | label of the quality element | [optional] 
**width** | **int** | video width in pixels | [optional] 
**height** | **int** | video height in pixels | [optional] 
**bitrate** | **int** | bit rate of the video | [optional] 
**mime_type** | **str** | media type of the video | [optional] 
**fps** | **int** | frame rate of the video | [optional] 

## Example

```python
from dataforseo_client.models.streaming_quality_element import StreamingQualityElement

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingQualityElement from a JSON string
streaming_quality_element_instance = StreamingQualityElement.from_json(json)
# print the JSON string representation of the object
print StreamingQualityElement.to_json()

# convert the object into a dict
streaming_quality_element_dict = streaming_quality_element_instance.to_dict()
# create an instance of StreamingQualityElement from a dict
streaming_quality_element_form_dict = streaming_quality_element.from_dict(streaming_quality_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


