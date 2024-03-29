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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class SpreadLeg(BaseModel):
    """
    Provides information about one leg of the option spread.
    """
    symbol: Optional[StrictStr] = Field(None, alias="Symbol", description="Option contract symbol or underlying symbol to be traded for this leg.")
    ratio: Optional[StrictInt] = Field(None, alias="Ratio", description="The number of option contracts or underlying shares for this leg, relative to the other legs. A positive number represents a buy trade and a negative number represents a sell trade. For example, a Butterfly spread can be represented using ratios of 1, -2, and 1: buy 1 contract of the first leg, sell 2 contracts of the second leg, and buy 1 contract of the third leg.")
    strike_price: Optional[StrictStr] = Field(None, alias="StrikePrice", description="The strike price of the option contract for this leg.")
    expiration: Optional[datetime] = Field(None, alias="Expiration", description="Date on which the contract expires, e.g. `2021-12-17T00:00:00Z`.")
    option_type: Optional[StrictStr] = Field(None, alias="OptionType", description="The option type. It can be `Call` or `Put`.")
    asset_type: Optional[StrictStr] = Field(None, alias="AssetType", description="The asset category for this leg.")
    __properties = ["Symbol", "Ratio", "StrikePrice", "Expiration", "OptionType", "AssetType"]

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
    def from_json(cls, json_str: str) -> SpreadLeg:
        """Create an instance of SpreadLeg from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpreadLeg:
        """Create an instance of SpreadLeg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpreadLeg.parse_obj(obj)

        _obj = SpreadLeg.parse_obj({
            "symbol": obj.get("Symbol"),
            "ratio": obj.get("Ratio"),
            "strike_price": obj.get("StrikePrice"),
            "expiration": obj.get("Expiration"),
            "option_type": obj.get("OptionType"),
            "asset_type": obj.get("AssetType")
        })
        return _obj


