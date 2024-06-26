# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.data_amazon_amazon_product_info_serp_element_item import DataAmazonAmazonProductInfoSerpElementItem

class TestDataAmazonAmazonProductInfoSerpElementItem(unittest.TestCase):
    """DataAmazonAmazonProductInfoSerpElementItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataAmazonAmazonProductInfoSerpElementItem:
        """Test DataAmazonAmazonProductInfoSerpElementItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataAmazonAmazonProductInfoSerpElementItem`
        """
        model = DataAmazonAmazonProductInfoSerpElementItem()
        if include_optional:
            return DataAmazonAmazonProductInfoSerpElementItem(
                rank_group = 56,
                rank_absolute = 56,
                position = '',
                xpath = '',
                title = '',
                details = '',
                image_url = '',
                author = '',
                data_asin = '',
                parent_asin = '',
                product_asins = [
                    ''
                    ],
                price_from = 1.337,
                price_to = 1.337,
                currency = '',
                is_amazon_choice = True,
                rating = dataforseo_client.models.rating_element.RatingElement(
                    type = '', 
                    position = '', 
                    rating_type = '', 
                    value = '', 
                    votes_count = 56, 
                    rating_max = 56, ),
                is_newer_model_available = True,
                newer_model = dataforseo_client.models.amazon_product_newer_model_info.AmazonProductNewerModelInfo(
                    title = '', 
                    newer_model_asin = '', ),
                categories = [
                    dataforseo_client.models.product_category_info.ProductCategoryInfo(
                        category = '', 
                        url = '', )
                    ],
                product_information = [
                    dataforseo_client.models.base_product_information_item.BaseProductInformationItem()
                    ],
                product_images_list = [
                    ''
                    ],
                product_videos_list = [
                    ''
                    ],
                description = '',
                is_available = True
            )
        else:
            return DataAmazonAmazonProductInfoSerpElementItem(
        )
        """

    def testDataAmazonAmazonProductInfoSerpElementItem(self):
        """Test DataAmazonAmazonProductInfoSerpElementItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
