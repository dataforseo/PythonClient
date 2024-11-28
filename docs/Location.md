# Location


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neighborhood** | **str** | name of the neighborhood where the hotel is located | [optional] 
**neighborhood_description** | **str** | description of the neighborhood where the hotel is located | [optional] 
**maps_url** | **str** | url to the location of the hotel in google maps | [optional] 
**overall_score** | **float** | overall score of the hotel location indicates the overall score of the hotel’s location in the range from 1 to 5; calculated based on data from the hotel’s proximity to nearby things to do and restaurants, transportation, and airports; note that the criteria are not weighted equally in the overall score | [optional] 
**score_by_categories** | [**ScoreByCategories**](ScoreByCategories.md) |  | [optional] 
**latitude** | **float** | hotel latitude latitude coordinates of the hotel’s location example: 39.4806397 | [optional] 
**longitude** | **float** | hotel longitude latitude coordinates of the hotel’s location example: -106.0512973 | [optional] 
**location_chain** | [**List[LocationChain]**](LocationChain.md) | elements of the location chain additional parameters of each element of the location chain | [optional] 

## Example

```python
from dataforseo_client.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


