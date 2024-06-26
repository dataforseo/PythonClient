# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.commercial_units_dataforseo_labs_serp_element_item import CommercialUnitsDataforseoLabsSerpElementItem

class TestCommercialUnitsDataforseoLabsSerpElementItem(unittest.TestCase):
    """CommercialUnitsDataforseoLabsSerpElementItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommercialUnitsDataforseoLabsSerpElementItem:
        """Test CommercialUnitsDataforseoLabsSerpElementItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommercialUnitsDataforseoLabsSerpElementItem`
        """
        model = CommercialUnitsDataforseoLabsSerpElementItem()
        if include_optional:
            return CommercialUnitsDataforseoLabsSerpElementItem(
                rank_group = 56,
                rank_absolute = 56,
                position = '',
                xpath = '',
                title = '',
                items = [
                    dataforseo_client.models.commercial_units_element.CommercialUnitsElement(
                        type = '', 
                        title = '', 
                        url = '', 
                        domain = '', 
                        price = dataforseo_client.models.price_info.PriceInfo(
                            current = 1.337, 
                            regular = 1.337, 
                            max_value = 1.337, 
                            currency = '', 
                            is_price_range = True, 
                            displayed_price = '', ), 
                        source = '', 
                        rating = dataforseo_client.models.rating_info.RatingInfo(
                            rating_type = '', 
                            value = 1.337, 
                            votes_count = 56, 
                            rating_max = 56, ), )
                    ]
            )
        else:
            return CommercialUnitsDataforseoLabsSerpElementItem(
        )
        """

    def testCommercialUnitsDataforseoLabsSerpElementItem(self):
        """Test CommercialUnitsDataforseoLabsSerpElementItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
