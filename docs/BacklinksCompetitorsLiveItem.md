[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksCompetitorsLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**target** | **str** | competitor domain | [optional]
**rank** | **int** | domain rank domain rank across all domains in the database rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional]
**intersections** | **int** | indicates the number of backlink intersections with the target specified in the POST array | [optional]

## Example

```python
from dataforseo_client.models.backlinks_competitors_live_item import BacklinksCompetitorsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksCompetitorsLiveItem from a JSON string
backlinks_competitors_live_item_instance = BacklinksCompetitorsLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksCompetitorsLiveItem.to_json()

# convert the object into a dict
backlinks_competitors_live_item_dict = backlinks_competitors_live_item_instance.to_dict()
# create an instance of BacklinksCompetitorsLiveItem from a dict
backlinks_competitors_live_item_form_dict = backlinks_competitors_live_item.from_dict(backlinks_competitors_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")