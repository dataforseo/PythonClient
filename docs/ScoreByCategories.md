[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ScoreByCategories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall** | **float** | overall score of the hotel location indicates the overall score of the hotel’s location in the range from 1 to 5; calculated based on data from the hotel’s proximity to nearby things to do and restaurants, transportation, and airports; note that the criteria are not weighted equally in the overall score | [optional]
**things_to_do** | **float** | score relative to nearby things to do indicates the score of the hotel’s location in the range from 1 to 5; calculated based on data from the hotel’s proximity to nearby things to do | [optional]
**restaurants** | **float** | score relative to nearby restaurants indicates the score of the hotel’s location in the range from 1 to 5; calculated based on data from the hotel’s proximity to nearby restaurants | [optional]
**transit** | **float** | score relative to nearby transit options indicates the score of the hotel’s location in the range from 1 to 5; calculated based on data from the hotel’s proximity to nearby transit options | [optional]
**airport_access** | **float** | score relative to nearby airports indicates the score of the hotel’s location in the range from 1 to 5; calculated based on data from the hotel’s proximity to nearby airports | [optional]

## Example

```python
from dataforseo_client.models.score_by_categories import ScoreByCategories

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreByCategories from a JSON string
score_by_categories_instance = ScoreByCategories.from_json(json)
# print the JSON string representation of the object
print ScoreByCategories.to_json()

# convert the object into a dict
score_by_categories_dict = score_by_categories_instance.to_dict()
# create an instance of ScoreByCategories from a dict
score_by_categories_form_dict = score_by_categories.from_dict(score_by_categories_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")