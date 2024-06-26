# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.event_item_serp_element_item import EventItemSerpElementItem

class TestEventItemSerpElementItem(unittest.TestCase):
    """EventItemSerpElementItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventItemSerpElementItem:
        """Test EventItemSerpElementItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventItemSerpElementItem`
        """
        model = EventItemSerpElementItem()
        if include_optional:
            return EventItemSerpElementItem(
                rank_group = 56,
                rank_absolute = 56,
                position = '',
                xpath = '',
                title = '',
                description = '',
                url = '',
                image_url = '',
                event_dates = dataforseo_client.models.event_dates.EventDates(
                    start_datetime = '', 
                    end_datetime = '', 
                    displayed_dates = '', ),
                location_info = dataforseo_client.models.location_info.LocationInfo(
                    name = '', 
                    address = '', 
                    url = '', 
                    cid = '', 
                    feature_id = '', ),
                information_and_tickets = [
                    dataforseo_client.models.information_and_tickets_element.InformationAndTicketsElement(
                        type = '', 
                        title = '', 
                        description = '', 
                        url = '', 
                        domain = '', )
                    ]
            )
        else:
            return EventItemSerpElementItem(
        )
        """

    def testEventItemSerpElementItem(self):
        """Test EventItemSerpElementItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
