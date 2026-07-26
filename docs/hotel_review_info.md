# HotelReviewInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**value** | **StrictFloat** | <em>overall hotel rating based on customer votes</em> |[optional]|
**votes_count** | **StrictInt** | <em>number of customer votes</em><br>the number of customer votes included in the calculation of the hotel rating |[optional]|
**mentions** | **List[Optional[ReviewMentionInfo]]** | <em>hotel mentions</em><br>information about hotel reviews by criteria |[optional]|
**rating_distribution** | **Dict[str, Optional[StrictInt]]** | <em>rating distribution by votes</em><br>the distribution of votes across the rating in the range from 1 to 5 |[optional]|
**other_sites_reviews** | **List[Optional[OtherSitesReviewsInfo]]** | <em>reviews on third-party sites</em><br>reviews from third-party sites |[optional]|