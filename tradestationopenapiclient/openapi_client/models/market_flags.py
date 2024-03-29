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
from pydantic import BaseModel, Field, StrictBool

class MarketFlags(BaseModel):
    """
    Market specific information for a symbol.
    """
    is_bats: Optional[StrictBool] = Field(None, alias="IsBats", description="Is Bats.")
    is_delayed: Optional[StrictBool] = Field(None, alias="IsDelayed", description="Is delayed.")
    is_halted: Optional[StrictBool] = Field(None, alias="IsHalted", description="Is halted.")
    is_hard_to_borrow: Optional[StrictBool] = Field(None, alias="IsHardToBorrow", description="Is hard to borrow.")
    __properties = ["IsBats", "IsDelayed", "IsHalted", "IsHardToBorrow"]

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
    def from_json(cls, json_str: str) -> MarketFlags:
        """Create an instance of MarketFlags from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MarketFlags:
        """Create an instance of MarketFlags from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MarketFlags.parse_obj(obj)

        _obj = MarketFlags.parse_obj({
            "is_bats": obj.get("IsBats"),
            "is_delayed": obj.get("IsDelayed"),
            "is_halted": obj.get("IsHalted"),
            "is_hard_to_borrow": obj.get("IsHardToBorrow")
        })
        return _obj


