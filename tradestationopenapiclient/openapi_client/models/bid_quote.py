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

class BidQuote(BaseModel):
    """
    BidQuote
    """
    time_stamp: Optional[datetime] = Field(None, alias="TimeStamp", description="Timestamp of the quote, represented as an RFC3339 formatted date, a profile of the ISO 8601 date standard.  E.g. `2022-06-28T12:34:56Z`.")
    side: Optional[StrictStr] = Field(None, alias="Side", description="The `Bid` side of the quote.")
    price: Optional[StrictStr] = Field(None, alias="Price", description="The price of the quote.")
    size: Optional[StrictStr] = Field(None, alias="Size", description="The total number of shares requested by this participant for the Bid.")
    order_count: Optional[StrictInt] = Field(None, alias="OrderCount", description="The number of orders aggregated together for this quote by the participant (market maker or ECN). For options the OrderCount will always be 0 because this information is not reported by the exchange.")
    name: Optional[StrictStr] = Field(None, alias="Name", description="The name of the participant associated with this quote.")
    __properties = ["TimeStamp", "Side", "Price", "Size", "OrderCount", "Name"]

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
    def from_json(cls, json_str: str) -> BidQuote:
        """Create an instance of BidQuote from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BidQuote:
        """Create an instance of BidQuote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BidQuote.parse_obj(obj)

        _obj = BidQuote.parse_obj({
            "time_stamp": obj.get("TimeStamp"),
            "side": obj.get("Side"),
            "price": obj.get("Price"),
            "size": obj.get("Size"),
            "order_count": obj.get("OrderCount"),
            "name": obj.get("Name")
        })
        return _obj


