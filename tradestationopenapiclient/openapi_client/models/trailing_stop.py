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

class TrailingStop(BaseModel):
    """
    TrailingStop offset; amount or percent.
    """
    amount: Optional[StrictStr] = Field(None, alias="Amount", description="Currency Offset from current price. Note: Mutually exclusive with Percent.")
    percent: Optional[StrictStr] = Field(None, alias="Percent", description="Percentage offset from current price. Note: Mutually exclusive with Amount.")
    __properties = ["Amount", "Percent"]

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
    def from_json(cls, json_str: str) -> TrailingStop:
        """Create an instance of TrailingStop from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrailingStop:
        """Create an instance of TrailingStop from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrailingStop.parse_obj(obj)

        _obj = TrailingStop.parse_obj({
            "amount": obj.get("Amount"),
            "percent": obj.get("Percent")
        })
        return _obj

