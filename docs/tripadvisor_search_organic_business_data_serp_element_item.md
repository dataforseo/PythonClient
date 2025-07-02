# TripadvisorSearchOrganicBusinessDataSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | name of the business entity |[optional]|
**url_path** | **StrictStr** | URL path of the business entity<br>URL path to the Tripadvisor page of the business entity<br>you can use this identifier to collect reviews for the business entity using Tripadvisor Reviews |[optional]|
**is_sponsored** | **StrictBool** | indicates a sponsored placement<br>if true, related tripadvisor_search_organic item is a paid advertising on Tripadvisor |[optional]|
**reviews_count** | **StrictInt** | the total number of reviews |[optional]|
**category** | **StrictStr** | place category |[optional]|
**price_rate** | **StrictStr** | average price rate |[optional]|
**rating** | **RatingInfo** | the rating score of the establishment submitted by the reviewers |[optional]|