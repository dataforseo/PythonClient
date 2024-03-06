[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# Redirect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**status_code** | **int** | HTTP status code of the URL | [optional]
**url** | **str** | indirect link URL | [optional]

## Example

```python
from dataforseo_client.models.redirect import Redirect

# TODO update the JSON string below
json = "{}"
# create an instance of Redirect from a JSON string
redirect_instance = Redirect.from_json(json)
# print the JSON string representation of the object
print Redirect.to_json()

# convert the object into a dict
redirect_dict = redirect_instance.to_dict()
# create an instance of Redirect from a dict
redirect_form_dict = redirect.from_dict(redirect_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")