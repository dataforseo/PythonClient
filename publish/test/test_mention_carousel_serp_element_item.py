# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.mention_carousel_serp_element_item import MentionCarouselSerpElementItem

class TestMentionCarouselSerpElementItem(unittest.TestCase):
    """MentionCarouselSerpElementItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MentionCarouselSerpElementItem:
        """Test MentionCarouselSerpElementItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MentionCarouselSerpElementItem`
        """
        model = MentionCarouselSerpElementItem()
        if include_optional:
            return MentionCarouselSerpElementItem(
                rank_group = 56,
                rank_absolute = 56,
                position = '',
                xpath = '',
                title = '',
                items = [
                    dataforseo_client.models.mention_carousel_element.MentionCarouselElement(
                        type = '', 
                        title = '', 
                        price = dataforseo_client.models.price_info.PriceInfo(
                            current = 1.337, 
                            regular = 1.337, 
                            max_value = 1.337, 
                            currency = '', 
                            is_price_range = True, 
                            displayed_price = '', ), 
                        rating = dataforseo_client.models.rating_info.RatingInfo(
                            rating_type = '', 
                            value = 1.337, 
                            votes_count = 56, 
                            rating_max = 56, ), 
                        mentioned_in = [
                            dataforseo_client.models.link_element.LinkElement(
                                type = '', 
                                title = '', 
                                snippet = '', 
                                description = '', 
                                url = '', 
                                domain = '', 
                                xpath = '', )
                            ], )
                    ],
                rectangle = dataforseo_client.models.rectangle.Rectangle(
                    x = 1.337, 
                    y = 1.337, 
                    width = 1.337, 
                    height = 1.337, )
            )
        else:
            return MentionCarouselSerpElementItem(
        )
        """

    def testMentionCarouselSerpElementItem(self):
        """Test MentionCarouselSerpElementItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
