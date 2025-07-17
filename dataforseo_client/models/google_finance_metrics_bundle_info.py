from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class GoogleFinanceMetricsBundleInfo(BaseModel):
    """
    GoogleFinanceMetricsBundleInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time of the value readout. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2025-02-10 09:40:00 +00:00")
    revenue: Optional[StrictFloat] = Field(default=None, description="revenue value")
    revenue_delta: Optional[StrictFloat] = Field(default=None, description="change in revenue")
    operating_expense: Optional[StrictFloat] = Field(default=None, description="operating expense value")
    operating_expense_delta: Optional[StrictFloat] = Field(default=None, description="change in operating expense")
    net_income: Optional[StrictFloat] = Field(default=None, description="net income value")
    net_income_delta: Optional[StrictFloat] = Field(default=None, description="change in net income")
    net_profit_margin: Optional[StrictFloat] = Field(default=None, description="net profit margin value")
    net_profit_margin_delta: Optional[StrictFloat] = Field(default=None, description="change in net profit margin")
    earnings_per_share: Optional[StrictFloat] = Field(default=None, description="earnings per share value")
    earnings_per_share_delta: Optional[StrictFloat] = Field(default=None, description="change in earnings per share")
    ebitda: Optional[StrictFloat] = Field(default=None, description="earnings before interest, taxes, deprecation, amortisation")
    ebitda_delta: Optional[StrictFloat] = Field(default=None, description="change in ebitda")
    effective_tax_rate: Optional[StrictFloat] = Field(default=None, description="effective tax rate value")
    cash_and_short_term_investments: Optional[StrictFloat] = Field(default=None, description="cash and short-term investments value")
    cash_and_short_term_investments_delta: Optional[StrictFloat] = Field(default=None, description="change in cash and short-term investments")
    total_assets: Optional[StrictFloat] = Field(default=None, description="total assets value")
    total_assets_delta: Optional[StrictFloat] = Field(default=None, description="change in total assets")
    total_liabilities: Optional[StrictFloat] = Field(default=None, description="total liabilities value")
    total_liabilities_delta: Optional[StrictFloat] = Field(default=None, description="change in total liabilities")
    total_equity: Optional[StrictFloat] = Field(default=None, description="total equity value")
    shares_outstanding: Optional[StrictFloat] = Field(default=None, description="outstanding shares value")
    price_to_book: Optional[StrictFloat] = Field(default=None, description="price to book")
    return_on_assets: Optional[StrictFloat] = Field(default=None, description="return on assets")
    return_on_capital: Optional[StrictFloat] = Field(default=None, description="return on capital")
    cash_from_operations: Optional[StrictFloat] = Field(default=None, description="cash from operations")
    cash_from_operations_delta: Optional[StrictFloat] = Field(default=None, description="change in cash from operations")
    cash_from_investing: Optional[StrictFloat] = Field(default=None, description="cash from investing")
    cash_from_investing_delta: Optional[StrictFloat] = Field(default=None, description="change in cash from investing")
    cash_from_financing: Optional[StrictFloat] = Field(default=None, description="cash from financing/em>")
    cash_from_financing_delta: Optional[StrictFloat] = Field(default=None, description="change in cash from financing")
    net_change_in_cash: Optional[StrictFloat] = Field(default=None, description="net change in cash")
    net_change_in_cash_delta: Optional[StrictFloat] = Field(default=None, description="change in net change in cash")
    free_cash_flow: Optional[StrictFloat] = Field(default=None, description="free cash flow value")
    free_cash_flow_delta: Optional[StrictFloat] = Field(default=None, description="change in free cash flow")
    __properties: ClassVar[List[str]] = [
        "type", 
        "timestamp", 
        "revenue", 
        "revenue_delta", 
        "operating_expense", 
        "operating_expense_delta", 
        "net_income", 
        "net_income_delta", 
        "net_profit_margin", 
        "net_profit_margin_delta", 
        "earnings_per_share", 
        "earnings_per_share_delta", 
        "ebitda", 
        "ebitda_delta", 
        "effective_tax_rate", 
        "cash_and_short_term_investments", 
        "cash_and_short_term_investments_delta", 
        "total_assets", 
        "total_assets_delta", 
        "total_liabilities", 
        "total_liabilities_delta", 
        "total_equity", 
        "shares_outstanding", 
        "price_to_book", 
        "return_on_assets", 
        "return_on_capital", 
        "cash_from_operations", 
        "cash_from_operations_delta", 
        "cash_from_investing", 
        "cash_from_investing_delta", 
        "cash_from_financing", 
        "cash_from_financing_delta", 
        "net_change_in_cash", 
        "net_change_in_cash_delta", 
        "free_cash_flow", 
        "free_cash_flow_delta", 
        ]

    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([
        ])

        _dict = {}

        _dict['type'] = self.type
        _dict['timestamp'] = self.timestamp
        _dict['revenue'] = self.revenue
        _dict['revenue_delta'] = self.revenue_delta
        _dict['operating_expense'] = self.operating_expense
        _dict['operating_expense_delta'] = self.operating_expense_delta
        _dict['net_income'] = self.net_income
        _dict['net_income_delta'] = self.net_income_delta
        _dict['net_profit_margin'] = self.net_profit_margin
        _dict['net_profit_margin_delta'] = self.net_profit_margin_delta
        _dict['earnings_per_share'] = self.earnings_per_share
        _dict['earnings_per_share_delta'] = self.earnings_per_share_delta
        _dict['ebitda'] = self.ebitda
        _dict['ebitda_delta'] = self.ebitda_delta
        _dict['effective_tax_rate'] = self.effective_tax_rate
        _dict['cash_and_short_term_investments'] = self.cash_and_short_term_investments
        _dict['cash_and_short_term_investments_delta'] = self.cash_and_short_term_investments_delta
        _dict['total_assets'] = self.total_assets
        _dict['total_assets_delta'] = self.total_assets_delta
        _dict['total_liabilities'] = self.total_liabilities
        _dict['total_liabilities_delta'] = self.total_liabilities_delta
        _dict['total_equity'] = self.total_equity
        _dict['shares_outstanding'] = self.shares_outstanding
        _dict['price_to_book'] = self.price_to_book
        _dict['return_on_assets'] = self.return_on_assets
        _dict['return_on_capital'] = self.return_on_capital
        _dict['cash_from_operations'] = self.cash_from_operations
        _dict['cash_from_operations_delta'] = self.cash_from_operations_delta
        _dict['cash_from_investing'] = self.cash_from_investing
        _dict['cash_from_investing_delta'] = self.cash_from_investing_delta
        _dict['cash_from_financing'] = self.cash_from_financing
        _dict['cash_from_financing_delta'] = self.cash_from_financing_delta
        _dict['net_change_in_cash'] = self.net_change_in_cash
        _dict['net_change_in_cash_delta'] = self.net_change_in_cash_delta
        _dict['free_cash_flow'] = self.free_cash_flow
        _dict['free_cash_flow_delta'] = self.free_cash_flow_delta
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "timestamp": obj.get("timestamp"),
            "revenue": obj.get("revenue"),
            "revenue_delta": obj.get("revenue_delta"),
            "operating_expense": obj.get("operating_expense"),
            "operating_expense_delta": obj.get("operating_expense_delta"),
            "net_income": obj.get("net_income"),
            "net_income_delta": obj.get("net_income_delta"),
            "net_profit_margin": obj.get("net_profit_margin"),
            "net_profit_margin_delta": obj.get("net_profit_margin_delta"),
            "earnings_per_share": obj.get("earnings_per_share"),
            "earnings_per_share_delta": obj.get("earnings_per_share_delta"),
            "ebitda": obj.get("ebitda"),
            "ebitda_delta": obj.get("ebitda_delta"),
            "effective_tax_rate": obj.get("effective_tax_rate"),
            "cash_and_short_term_investments": obj.get("cash_and_short_term_investments"),
            "cash_and_short_term_investments_delta": obj.get("cash_and_short_term_investments_delta"),
            "total_assets": obj.get("total_assets"),
            "total_assets_delta": obj.get("total_assets_delta"),
            "total_liabilities": obj.get("total_liabilities"),
            "total_liabilities_delta": obj.get("total_liabilities_delta"),
            "total_equity": obj.get("total_equity"),
            "shares_outstanding": obj.get("shares_outstanding"),
            "price_to_book": obj.get("price_to_book"),
            "return_on_assets": obj.get("return_on_assets"),
            "return_on_capital": obj.get("return_on_capital"),
            "cash_from_operations": obj.get("cash_from_operations"),
            "cash_from_operations_delta": obj.get("cash_from_operations_delta"),
            "cash_from_investing": obj.get("cash_from_investing"),
            "cash_from_investing_delta": obj.get("cash_from_investing_delta"),
            "cash_from_financing": obj.get("cash_from_financing"),
            "cash_from_financing_delta": obj.get("cash_from_financing_delta"),
            "net_change_in_cash": obj.get("net_change_in_cash"),
            "net_change_in_cash_delta": obj.get("net_change_in_cash_delta"),
            "free_cash_flow": obj.get("free_cash_flow"),
            "free_cash_flow_delta": obj.get("free_cash_flow_delta"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj