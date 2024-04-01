# SslInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_certificate** | **bool** | ssl certificate validity indicates whether the ssl certificate detected on a website is not expired, suspended, revoked or invalid | [optional] 
**certificate_issuer** | **str** | ssl certificate authority the entity that issued the detected ssl certificate | [optional] 
**certificate_subject** | **str** | ssl certificate subject the entity associated with the public key | [optional] 
**certificate_version** | **str** | ssl certificate version indicates the version of X.509 used by an ssl certificate | [optional] 
**certificate_hash** | **str** | ssl certificate hash the version of the ssl certificate’s hash function | [optional] 
**certificate_expiration_date** | **str** | ssl certificate expiration date the date and time when the ssl certificate expires in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.ssl_info import SslInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SslInfo from a JSON string
ssl_info_instance = SslInfo.from_json(json)
# print the JSON string representation of the object
print(SslInfo.to_json())

# convert the object into a dict
ssl_info_dict = ssl_info_instance.to_dict()
# create an instance of SslInfo from a dict
ssl_info_form_dict = ssl_info.from_dict(ssl_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


