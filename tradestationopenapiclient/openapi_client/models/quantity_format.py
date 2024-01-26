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
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from openapi_client.models.increment_schedule_row import IncrementScheduleRow

class QuantityFormat(BaseModel):
    """
    Conveys number formatting information for symbol quantity fields.
    """
    format: Optional[StrictStr] = Field(None, alias="Format", description="The format of the quantity.")
    decimals: Optional[StrictStr] = Field(None, alias="Decimals", description="The number of decimals precision, applies to the `Decimal` format only.")
    increment_style: Optional[StrictStr] = Field(None, alias="IncrementStyle", description="The incremental style. Valid values are: `Simple` and `Schedule`.")
    increment: Optional[StrictStr] = Field(None, alias="Increment", description="The decimal increment for all quantity movements, applies to the `Simple` Increment Style only.")
    increment_schedule: Optional[conlist(IncrementScheduleRow)] = Field(None, alias="IncrementSchedule")
    minimum_trade_quantity: Optional[StrictStr] = Field(None, alias="MinimumTradeQuantity", description="The minimum quantity of an asset that can be traded.")
    maximum_trade_quantity: Optional[StrictStr] = Field(None, alias="MaximumTradeQuantity", description="The maximum quantity of an asset that can be traded, `Crypto` assets only.")
    __properties = ["Format", "Decimals", "IncrementStyle", "Increment", "IncrementSchedule", "MinimumTradeQuantity", "MaximumTradeQuantity"]

    @validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Decimal'):
            raise ValueError("must be one of enum values ('Decimal')")
        return value

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
    def from_json(cls, json_str: str) -> QuantityFormat:
        """Create an instance of QuantityFormat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in increment_schedule (list)
        _items = []
        if self.increment_schedule:
            for _item in self.increment_schedule:
                if _item:
                    _items.append(_item.to_dict())
            _dict['IncrementSchedule'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QuantityFormat:
        """Create an instance of QuantityFormat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QuantityFormat.parse_obj(obj)

        _obj = QuantityFormat.parse_obj({
            "format": obj.get("Format"),
            "decimals": obj.get("Decimals"),
            "increment_style": obj.get("IncrementStyle"),
            "increment": obj.get("Increment"),
            "increment_schedule": [IncrementScheduleRow.from_dict(_item) for _item in obj.get("IncrementSchedule")] if obj.get("IncrementSchedule") is not None else None,
            "minimum_trade_quantity": obj.get("MinimumTradeQuantity"),
            "maximum_trade_quantity": obj.get("MaximumTradeQuantity")
        })
        return _obj

