# HotelReviewInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**value** | **StrictFloat** | overall hotel rating based on customer votes |[optional]|
**votes_count** | **StrictInt** | number of customer votes<br>the number of customer votes included in the calculation of the hotel rating |[optional]|
**mentions** | **List[Optional[ReviewMentionInfo]]** | hotel mentions<br>information about hotel reviews by criteria |[optional]|
**rating_distribution** | **Dict[str, Optional[StrictInt]]** | rating distribution by votes<br>the distribution of votes across the rating in the range from 1 to 5 |[optional]|
**other_sites_reviews** | **List[Optional[OtherSitesReviewsInfo]]** | reviews on third-party sites<br>reviews from third-paty sites |[optional]|