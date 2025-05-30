# PageContentInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**header** | **PageSectionContentInfo** | content of the header of the table |[optional]|
**footer** | **PageSectionContentInfo** | content of the footer of the table |[optional]|
**main_topic** | **List[Optional[TopicInfo]]** | main topic on the page<br>you can find more information about topic priority calculation in this help center article |[optional]|
**secondary_topic** | **List[Optional[TopicInfo]]** | secondary topic on the page<br>you can find more information about topic priority calculation in this help center article |[optional]|
**ratings** | **List[Optional[ContentRatingInfo]]** | contains objects with rating information for the products displayed on the page |[optional]|
**offers** | **List[Optional[ContentOfferInfo]]** | array of products displayed on the page<br>contains objects with information on products displayed on the page |[optional]|
**comments** | **List[Optional[ContentCommentInfo]]** | array of comments displayed on the page<br>contains objects with information on comments related to displayed products |[optional]|
**contacts** | **Contacts** | contact information<br>contains contact information displayed on the page |[optional]|