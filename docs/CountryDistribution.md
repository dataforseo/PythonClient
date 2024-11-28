# CountryDistribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_iso_code** | **str** | country ISO code | [optional] 
**search_volume** | **int** | search volume in a given country | [optional] 
**percentage** | **float** | percentage of global search volume | [optional] 

## Example

```python
from dataforseo_client.models.country_distribution import CountryDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of CountryDistribution from a JSON string
country_distribution_instance = CountryDistribution.from_json(json)
# print the JSON string representation of the object
print(CountryDistribution.to_json())

# convert the object into a dict
country_distribution_dict = country_distribution_instance.to_dict()
# create an instance of CountryDistribution from a dict
country_distribution_from_dict = CountryDistribution.from_dict(country_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


