# PositiveConnotationDistribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positive** | [**ContentAnalysisSummaryInfo**](ContentAnalysisSummaryInfo.md) |  | [optional] 
**negative** | [**ContentAnalysisSummaryInfo**](ContentAnalysisSummaryInfo.md) |  | [optional] 
**neutral** | [**ContentAnalysisSummaryInfo**](ContentAnalysisSummaryInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.positive_connotation_distribution import PositiveConnotationDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of PositiveConnotationDistribution from a JSON string
positive_connotation_distribution_instance = PositiveConnotationDistribution.from_json(json)
# print the JSON string representation of the object
print(PositiveConnotationDistribution.to_json())

# convert the object into a dict
positive_connotation_distribution_dict = positive_connotation_distribution_instance.to_dict()
# create an instance of PositiveConnotationDistribution from a dict
positive_connotation_distribution_from_dict = PositiveConnotationDistribution.from_dict(positive_connotation_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


