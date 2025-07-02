# ContentCommentInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rating** | **ContentRatingInfo** | product’s rating<br>contains information about the rating a customer has given to the product |[optional]|
**title** | **StrictFloat** | title of the customer’s comment |[optional]|
**publish_date** | **StrictStr** | date when the comment was published |[optional]|
**author** | **StrictStr** | author of the comment |[optional]|
**have_form** | **StrictBool** |  |[optional]|
**primary_content** | **List[Optional[SectionContentItemInfo]]** | primary content on the page<br>you can find more information about content priority calculation in this help center article |[optional]|