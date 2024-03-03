# PageMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links_external** | **int** | number of external links the number of links pointing to other websites | [optional] 
**links_internal** | **int** | number of internal links the number of links pointing to other pages within the target website | [optional] 
**duplicate_title** | **int** | number of pages with duplicate titles | [optional] 
**duplicate_description** | **int** | number of pages with duplicate descriptions | [optional] 
**duplicate_content** | **int** | number of pages with duplicate content | [optional] 
**broken_links** | **int** | number of broken links number of broken links across all crawled pages on a target website | [optional] 
**broken_resources** | **int** | number of broken resources the number of images and other resources with broken links | [optional] 
**links_relation_conflict** | **int** | number of links present on the target website that may have a conflict for example, if \&quot;links_relation_conflict\&quot;: 2, the target website is referring to the same source by at least one internal link with the rel&#x3D;\&quot;nofollow\&quot; attribute and by at least one dofollow link | [optional] 
**redirect_loop** | **int** | number of redirect chains that start and end at the same URL number of redirect chains where the destination URL redirects back to the original URL | [optional] 
**onpage_score** | **float** | shows how website is optimized on a 100-point scale this field shows how website is optimized considering critical on-page issues and warnings detected; 100 is the highest possible score that means website does not have any critical on-page issues and important warnings; note that this value depends on the number of crawled pages; learn more about how the metric is calculated in this help center article | [optional] 
**non_indexable** | **int** | number of non-indexable pages number of pages that are blocked from being indexed by Google and other search engines by robots.txt, HTTP headers, or meta tags settings; you can receive a list of non-indexable URLs using this endpoint | [optional] 
**checks** | **Dict[str, Optional[int]]** | page-specific on-page check-ups | [optional] 

## Example

```python
from dataforseo_client.models.page_metrics import PageMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of PageMetrics from a JSON string
page_metrics_instance = PageMetrics.from_json(json)
# print the JSON string representation of the object
print PageMetrics.to_json()

# convert the object into a dict
page_metrics_dict = page_metrics_instance.to_dict()
# create an instance of PageMetrics from a dict
page_metrics_form_dict = page_metrics.from_dict(page_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


