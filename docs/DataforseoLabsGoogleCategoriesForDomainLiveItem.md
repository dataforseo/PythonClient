[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsGoogleCategoriesForDomainLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**categories** | **List[int]** | product and service categories you can download the full list of possible categories | [optional]
**metrics** | [**Dict[str, MetricsInfo]**](MetricsInfo.md) | ranking data relevant to the specified domain or subdomain | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_categories_for_domain_live_item import DataforseoLabsGoogleCategoriesForDomainLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleCategoriesForDomainLiveItem from a JSON string
dataforseo_labs_google_categories_for_domain_live_item_instance = DataforseoLabsGoogleCategoriesForDomainLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleCategoriesForDomainLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_google_categories_for_domain_live_item_dict = dataforseo_labs_google_categories_for_domain_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleCategoriesForDomainLiveItem from a dict
dataforseo_labs_google_categories_for_domain_live_item_form_dict = dataforseo_labs_google_categories_for_domain_live_item.from_dict(dataforseo_labs_google_categories_for_domain_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")