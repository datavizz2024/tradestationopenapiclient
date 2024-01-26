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
import datetime

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr


class Bar(BaseModel):
    """
    Barchart data, starting from a starting date. Each bar filling quantity of unit.
    """

    close: Optional[StrictStr] = Field(
        None, alias="Close", description="The close price of the current bar."
    )
    down_ticks: Optional[StrictInt] = Field(
        None,
        alias="DownTicks",
        description="A trade made at a price less than the previous trade price or at a price equal to the previous trade price. Does not apply to bars for crypto symbols.",
    )
    down_volume: Optional[StrictInt] = Field(
        None,
        alias="DownVolume",
        description="Volume traded on downticks. A tick is considered a downtick if  the previous tick was a downtick or the price is lower than the previous tick. Does not apply to bars for crypto symbols.",
    )
    epoch: Optional[StrictInt] = Field(
        None, alias="Epoch", description="The Epoch time."
    )
    high: Optional[StrictStr] = Field(
        None, alias="High", description="The high price of the current bar."
    )
    is_end_of_history: Optional[StrictBool] = Field(
        None,
        alias="IsEndOfHistory",
        description="Conveys that all historical bars in the request have been delivered. Does not apply to bars for crypto symbols.",
    )
    is_realtime: Optional[StrictBool] = Field(
        None,
        alias="IsRealtime",
        description='Set when there is data in the bar and the data is being built in "real time" from a trade. Does not apply to bars for crypto symbols.',
    )
    low: Optional[StrictStr] = Field(
        None, alias="Low", description="The low price of the current bar."
    )
    open: Optional[StrictStr] = Field(
        None, alias="Open", description="The open price of the current bar."
    )
    open_interest: StrictStr = Field(
        None,
        alias="OpenInterest",
        description="For Options or Futures only. Number of open contracts. Does not apply to bars for crypto symbols.",
    )
    time_stamp: datetime.datetime = Field(
        None,
        alias="TimeStamp",
        description="Timestamp represented as an RFC3339 formatted date, a profile of the ISO 8601 date standard.  E.g. `2023-01-01T23:30:30Z`.",
    )
    total_ticks: Optional[StrictInt] = Field(
        None,
        alias="TotalTicks",
        description="Total number of ticks (upticks and downticks together). Does not apply to bars for crypto symbols.",
    )
    total_volume: Optional[StrictStr] = Field(
        None, alias="TotalVolume", description="The sum of up volume and down volume."
    )
    unchanged_ticks: Optional[StrictInt] = Field(
        None,
        alias="UnchangedTicks",
        description="The number of securities with a current price that is the same as the previous day's close. Does not apply to bars for crypto symbols.",
    )
    unchanged_volume: Optional[StrictInt] = Field(
        None,
        alias="UnchangedVolume",
        description="The volume of securities with a current price that is the same as the previous day's close. Does not apply to bars for crypto symbols.",
    )
    up_ticks: Optional[StrictInt] = Field(
        None,
        alias="UpTicks",
        description="A trade made at a price greater than the previous trade price, or at a price equal to the previous trade price. Does not apply to bars for crypto symbols.",
    )
    up_volume: Optional[StrictInt] = Field(
        None,
        alias="UpVolume",
        description="Volume traded on upticks. A tick is considered an uptick if the  previous tick was an uptick or the price is higher than the previous tick. Does not apply to bars for crypto symbols.",
    )
    bar_status: Optional[StrictStr] = Field(
        None,
        alias="BarStatus",
        description="Indicates if bar is Open or Closed. Does not apply to bars for crypto symbols.",
    )
    __properties = [
        "Close",
        "DownTicks",
        "DownVolume",
        "Epoch",
        "High",
        "IsEndOfHistory",
        "IsRealtime",
        "Low",
        "Open",
        "OpenInterest",
        "TimeStamp",
        "TotalTicks",
        "TotalVolume",
        "UnchangedTicks",
        "UnchangedVolume",
        "UpTicks",
        "UpVolume",
        "BarStatus",
    ]

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
    def from_json(cls, json_str: str) -> Bar:
        """Create an instance of Bar from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Bar:
        """Create an instance of Bar from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Bar.parse_obj(obj)

        _obj = Bar.parse_obj(
            {
                "close": obj.get("Close"),
                "down_ticks": obj.get("DownTicks"),
                "down_volume": obj.get("DownVolume"),
                "epoch": obj.get("Epoch"),
                "high": obj.get("High"),
                "is_end_of_history": obj.get("IsEndOfHistory"),
                "is_realtime": obj.get("IsRealtime"),
                "low": obj.get("Low"),
                "open": obj.get("Open"),
                "open_interest": obj.get("OpenInterest"),
                "time_stamp": obj.get("TimeStamp"),
                "total_ticks": obj.get("TotalTicks"),
                "total_volume": obj.get("TotalVolume"),
                "unchanged_ticks": obj.get("UnchangedTicks"),
                "unchanged_volume": obj.get("UnchangedVolume"),
                "up_ticks": obj.get("UpTicks"),
                "up_volume": obj.get("UpVolume"),
                "bar_status": obj.get("BarStatus"),
            }
        )
        return _obj