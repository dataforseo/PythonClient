# DomainInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | domain name | [optional] 
**cms** | **str** | content management system content management system identified on a website the content of the generator meta tag the data is taken from the first random page that returns the 200 response code if our crawler was unable to identify the cms, the value would be null | [optional] 
**ip** | **str** | domain ip address | [optional] 
**server** | **str** | website server the version of the server detected on a website the content of the server header the information is taken from the first page which response code is 200 | [optional] 
**crawl_start** | **str** | time when the crawling start date and time when the website was sent for crawling in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**crawl_end** | **str** | time when the crawling ended date and time when the crawling was finished in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00note: informative only if \&quot;crawl_progress\&quot; is \&quot;finished\&quot; if \&quot;crawl_progress\&quot; is in_progress, the value will be null | [optional] 
**extended_crawl_status** | **str** | crawl status and errors indicates the reason why a website was not crawled; can take the following values: no_errors – no crawling errors were detected; site_unreachable – our crawler could not reach a website and thus was not able to obtain a status code; invalid_page_status_code – status code of the first crawled page &gt;&#x3D; 400; forbidden_meta_tag – the first crawled page contains the &lt;meta robots&#x3D;”noindex”&gt; tag; forbidden_robots – robots.txt forbids crawling the page; forbidden_http_header – HTTP header of the page contains “X-Robots-Tag: noindex” ; too_many_redirects – the first crawled page has more than 10 redirects; unknown – the reason is unknown | [optional] 
**ssl_info** | [**SslInfo**](SslInfo.md) |  | [optional] 
**checks** | **Dict[str, Optional[bool]]** | website checks other on-page check-ups related to the website | [optional] 
**total_pages** | **int** | total crawled pages the total number of crawled pages | [optional] 
**page_not_found_status_code** | **int** | status code returned by a non-existent page in most cases, it is recommended a server returns a 404 response code | [optional] 
**canonicalization_status_code** | **int** | status code returned by a canonicalized page the checkup of the server behavior when our crawler tries to access the website via IP; in most cases, it is recommended that canonicalized pages respond with a 301 or 302 status code | [optional] 
**directory_browsing_status_code** | **int** | status code returned by a directory the status code returned by a directory page on a target website in most cases, it is recommended that directories respond with a 403 or 401 status code | [optional] 
**www_redirect_status_code** | **int** | redirect status code the status code of the www to non-www redirect in most cases, it is recommended that redirect returns a 301 status code | [optional] 
**main_domain** | **str** | root domain name | [optional] 

## Example

```python
from dataforseo_client.models.domain_info import DomainInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainInfo from a JSON string
domain_info_instance = DomainInfo.from_json(json)
# print the JSON string representation of the object
print DomainInfo.to_json()

# convert the object into a dict
domain_info_dict = domain_info_instance.to_dict()
# create an instance of DomainInfo from a dict
domain_info_form_dict = domain_info.from_dict(domain_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


