[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# Graph

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GraphElement]**](GraphElement.md) | additional items present in the element if there are none, equals null | [optional]
**previous_items** | [**List[GraphElement]**](GraphElement.md) | previous close data contains stock price data based on the preceding time period | [optional]

## Example

```python
from dataforseo_client.models.graph import Graph

# TODO update the JSON string below
json = "{}"
# create an instance of Graph from a JSON string
graph_instance = Graph.from_json(json)
# print the JSON string representation of the object
print Graph.to_json()

# convert the object into a dict
graph_dict = graph_instance.to_dict()
# create an instance of Graph from a dict
graph_form_dict = graph.from_dict(graph_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")