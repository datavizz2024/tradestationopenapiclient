# coding: utf-8

"""
    

    # Authentication For more information on authorization and gaining an access/refresh token, please visit: [Authentication](/docs/fundamentals/authentication/auth-overview). <SecurityDefinitions /> 

    The version of the OpenAPI document: 
    Contact: ClientServices@tradestation.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class BODCurrencyDetail(BaseModel):
    """
    Contains beginning of day currency detail information which varies according to account type.
    """
    account_margin_requirement: Optional[StrictStr] = Field(None, alias="AccountMarginRequirement", description="The dollar amount of Beginning Day Margin for the given forex account.")
    account_open_trade_equity: Optional[StrictStr] = Field(None, alias="AccountOpenTradeEquity", description="The dollar amount of Beginning Day Trade Equity for the given account.")
    account_securities: Optional[StrictStr] = Field(None, alias="AccountSecurities", description="The value of special securities that are deposited by the customer with the clearing firm for the sole purpose of increasing purchasing power in their trading account. This number will be reset daily by the account balances clearing file. The entire value of this field will increase purchasing power.")
    cash_balance: Optional[StrictStr] = Field(None, alias="CashBalance", description="The dollar amount of the Beginning Day Cash Balance for the given account.")
    currency: Optional[StrictStr] = Field(None, alias="Currency", description="The currency of the entity.")
    margin_requirement: Optional[StrictStr] = Field(None, alias="MarginRequirement", description="The dollar amount of Beginning Day Margin for the given forex account.")
    open_trade_equity: Optional[StrictStr] = Field(None, alias="OpenTradeEquity", description="The dollar amount of Beginning Day Trade Equity for the given account.")
    securities: Optional[StrictStr] = Field(None, alias="Securities", description="Indicates the dollar amount of Beginning Day Securities")
    __properties = ["AccountMarginRequirement", "AccountOpenTradeEquity", "AccountSecurities", "CashBalance", "Currency", "MarginRequirement", "OpenTradeEquity", "Securities"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BODCurrencyDetail:
        """Create an instance of BODCurrencyDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BODCurrencyDetail:
        """Create an instance of BODCurrencyDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BODCurrencyDetail.parse_obj(obj)

        _obj = BODCurrencyDetail.parse_obj({
            "account_margin_requirement": obj.get("AccountMarginRequirement"),
            "account_open_trade_equity": obj.get("AccountOpenTradeEquity"),
            "account_securities": obj.get("AccountSecurities"),
            "cash_balance": obj.get("CashBalance"),
            "currency": obj.get("Currency"),
            "margin_requirement": obj.get("MarginRequirement"),
            "open_trade_equity": obj.get("OpenTradeEquity"),
            "securities": obj.get("Securities")
        })
        return _obj


