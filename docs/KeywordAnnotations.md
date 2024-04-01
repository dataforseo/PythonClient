# KeywordAnnotations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concepts** | [**List[ConceptInfo]**](ConceptInfo.md) | the list of concepts for the keyword | [optional] 

## Example

```python
from dataforseo_client.models.keyword_annotations import KeywordAnnotations

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordAnnotations from a JSON string
keyword_annotations_instance = KeywordAnnotations.from_json(json)
# print the JSON string representation of the object
print(KeywordAnnotations.to_json())

# convert the object into a dict
keyword_annotations_dict = keyword_annotations_instance.to_dict()
# create an instance of KeywordAnnotations from a dict
keyword_annotations_form_dict = keyword_annotations.from_dict(keyword_annotations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


