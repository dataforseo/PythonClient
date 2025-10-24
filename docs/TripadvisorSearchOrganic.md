# TripadvisorSearchOrganic

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank among all the listed results<br>absolute position among all reviews on the list |[optional]|
**title** | **string** | name of the business entity |[optional]|
**url_path** | **string** | URL path of the business entity<br>URL path to the Tripadvisor page of the business entity<br>you can use this identifier to collect reviews for the business entity using Tripadvisor Reviews |[optional]|
**is_sponsored** | **boolean** | indicates a sponsored placement<br>if true, related tripadvisor_search_organic item is a paid advertising on Tripadvisor |[optional]|
**reviews_count** | **number** | the total number of reviews |[optional]|
**category** | **string** | place category |[optional]|
**price_rate** | **string** | average price rate |[optional]|
**rating** | **RatingInfo** | the rating score of the establishment submitted by the reviewers |[optional]|