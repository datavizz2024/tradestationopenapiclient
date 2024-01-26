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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openapi_client.models.market_activation_rules import MarketActivationRules
from openapi_client.models.time_activation_rules import TimeActivationRules
from openapi_client.models.trailing_stop import TrailingStop

class AdvancedOptions(BaseModel):
    """
    AdvancedOptions
    """
    add_liquidity: Optional[StrictBool] = Field(None, alias="AddLiquidity", description="This option allows you to place orders that will only add liquidity on the route you selected. To place an Add Liquidity order, the user must also select Book Only order type. Valid values `true` and `false`.  Valid for Equities only.")
    all_or_none: Optional[StrictBool] = Field(None, alias="AllOrNone", description="Use this advanced order feature when you do not want a partial fill. Your order will be filled in its entirety or not at all. Valid values `true` and `false`.  Valid for Equities and Options.")
    book_only: Optional[StrictBool] = Field(None, alias="BookOnly", description="This option restricts the destination you choose in the direct routing from re-routing your order to another destination. This type of order is useful in controlling your execution costs by avoiding fees the Exchanges can charge for rerouting your order to another market center. Valid values `true` and `false`.  Valid for Equities only.")
    discretionary_price: Optional[StrictStr] = Field(None, alias="DiscretionaryPrice", description="You can use this option to reflect a Bid/Ask at a lower/higher price than you are willing to pay using a specified price increment. Valid for `Limit` and `Stop Limit` orders only. Valid for Equities only.")
    market_activation_rules: Optional[conlist(MarketActivationRules)] = Field(None, alias="MarketActivationRules", description="Does not apply to Crypto orders.")
    non_display: Optional[StrictBool] = Field(None, alias="NonDisplay", description="When you send a non-display order, it will not be reflected in either the Market Depth display or ECN books. Valid values `true` and `false`.  Valid for Equities only.")
    peg_value: Optional[StrictStr] = Field(None, alias="PegValue", description="This order type is useful to achieve a fair price in a fast or volatile market. Valid values `BEST` and `MID`. Valid for Equities only.")
    show_only_quantity: Optional[StrictStr] = Field(None, alias="ShowOnlyQuantity", description="Hides the true number of shares intended to be bought or sold. Valid for `Limit` and `StopLimit` order types. Not valid for all exchanges. For Equities and Futures.")
    time_activation_rules: Optional[conlist(TimeActivationRules)] = Field(None, alias="TimeActivationRules", description="Does not apply to Crypto orders.")
    trailing_stop: Optional[TrailingStop] = Field(None, alias="TrailingStop")
    __properties = ["AddLiquidity", "AllOrNone", "BookOnly", "DiscretionaryPrice", "MarketActivationRules", "NonDisplay", "PegValue", "ShowOnlyQuantity", "TimeActivationRules", "TrailingStop"]

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
    def from_json(cls, json_str: str) -> AdvancedOptions:
        """Create an instance of AdvancedOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in market_activation_rules (list)
        _items = []
        if self.market_activation_rules:
            for _item in self.market_activation_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['MarketActivationRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in time_activation_rules (list)
        _items = []
        if self.time_activation_rules:
            for _item in self.time_activation_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TimeActivationRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of trailing_stop
        if self.trailing_stop:
            _dict['TrailingStop'] = self.trailing_stop.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvancedOptions:
        """Create an instance of AdvancedOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvancedOptions.parse_obj(obj)

        _obj = AdvancedOptions.parse_obj({
            "add_liquidity": obj.get("AddLiquidity"),
            "all_or_none": obj.get("AllOrNone"),
            "book_only": obj.get("BookOnly"),
            "discretionary_price": obj.get("DiscretionaryPrice"),
            "market_activation_rules": [MarketActivationRules.from_dict(_item) for _item in obj.get("MarketActivationRules")] if obj.get("MarketActivationRules") is not None else None,
            "non_display": obj.get("NonDisplay"),
            "peg_value": obj.get("PegValue"),
            "show_only_quantity": obj.get("ShowOnlyQuantity"),
            "time_activation_rules": [TimeActivationRules.from_dict(_item) for _item in obj.get("TimeActivationRules")] if obj.get("TimeActivationRules") is not None else None,
            "trailing_stop": TrailingStop.from_dict(obj.get("TrailingStop")) if obj.get("TrailingStop") is not None else None
        })
        return _obj


