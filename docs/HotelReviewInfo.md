# HotelReviewInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | overall hotel rating based on customer votes | [optional] 
**votes_count** | **int** | number of customer votes the number of customer votes included in the calculation of the hotel rating | [optional] 
**mentions** | [**List[ReviewMentionInfo]**](ReviewMentionInfo.md) | hotel mentions information about hotel reviews by criteria | [optional] 
**rating_distribution** | **Dict[str, Optional[int]]** | rating distribution by votes the distribution of votes across the rating in the range from 1 to 5 | [optional] 
**other_sites_reviews** | [**List[OtherSitesReviewsInfo]**](OtherSitesReviewsInfo.md) | reviews on third-party sites reviews from third-paty sites | [optional] 

## Example

```python
from dataforseo_client.models.hotel_review_info import HotelReviewInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HotelReviewInfo from a JSON string
hotel_review_info_instance = HotelReviewInfo.from_json(json)
# print the JSON string representation of the object
print(HotelReviewInfo.to_json())

# convert the object into a dict
hotel_review_info_dict = hotel_review_info_instance.to_dict()
# create an instance of HotelReviewInfo from a dict
hotel_review_info_form_dict = hotel_review_info.from_dict(hotel_review_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


