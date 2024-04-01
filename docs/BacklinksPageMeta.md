# BacklinksPageMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | page title | [optional] 
**canonical** | **str** | canonical page | [optional] 
**internal_links_count** | **int** | number of internal links on the page | [optional] 
**external_links_count** | **int** | number of external links on the page | [optional] 
**images_count** | **int** | number of images on the page | [optional] 
**words_count** | **int** | number of words on the page | [optional] 
**page_spam_score** | **int** | spam score of the page learn more about how the metric is calculated on this help center page | [optional] 
**social_media_tags** | **Dict[str, Optional[str]]** | array of social media tags found on the page contains social media tags and their content supported tags include but are not limited to Open Graph and Twitter card | [optional] 
**h1** | **List[Optional[str]]** | h1 tag content of h1 tags | [optional] 
**h2** | **List[Optional[str]]** | h2 tag content of h2 tags | [optional] 
**h3** | **List[Optional[str]]** | h3 tag content of h3 tags | [optional] 
**images_alt** | **List[Optional[str]]** | content of alt tags | [optional] 
**powered_by** | **List[Optional[str]]** | CMS details | [optional] 
**language** | **str** | page content language example: en | [optional] 
**charset** | **str** | character encoding examples: utf-8 | [optional] 
**platform_type** | **List[Optional[str]]** | type of a platform | [optional] 
**technologies** | **Dict[str, Optional[str]]** | website technologies | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_page_meta import BacklinksPageMeta

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksPageMeta from a JSON string
backlinks_page_meta_instance = BacklinksPageMeta.from_json(json)
# print the JSON string representation of the object
print(BacklinksPageMeta.to_json())

# convert the object into a dict
backlinks_page_meta_dict = backlinks_page_meta_instance.to_dict()
# create an instance of BacklinksPageMeta from a dict
backlinks_page_meta_form_dict = backlinks_page_meta.from_dict(backlinks_page_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


