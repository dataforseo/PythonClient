[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# SerpBaiduLocationsResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | location code | [optional]
**location_name** | **str** | full name of the location | [optional]
**location_code_parent** | **int** | the code of the superordinate location only City location_type is supported for all countries except China (where Country is also supported); don’t match locations by location_code_parent because the results for Region and Country-level results for most countries are not supported by Baidu SERP API | [optional]
**country_iso_code** | **str** | ISO country code of the location | [optional]
**location_type** | **str** | location type only City is supported for all countries except China (where Country is also supported) | [optional]

## Example

```python
from dataforseo_client.models.serp_baidu_locations_result_info import SerpBaiduLocationsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpBaiduLocationsResultInfo from a JSON string
serp_baidu_locations_result_info_instance = SerpBaiduLocationsResultInfo.from_json(json)
# print the JSON string representation of the object
print SerpBaiduLocationsResultInfo.to_json()

# convert the object into a dict
serp_baidu_locations_result_info_dict = serp_baidu_locations_result_info_instance.to_dict()
# create an instance of SerpBaiduLocationsResultInfo from a dict
serp_baidu_locations_result_info_form_dict = serp_baidu_locations_result_info.from_dict(serp_baidu_locations_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")