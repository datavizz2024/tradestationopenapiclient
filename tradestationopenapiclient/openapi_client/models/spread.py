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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from openapi_client.models.spread_leg import SpreadLeg

class Spread(BaseModel):
    """
    Spread
    """
    delta: Optional[StrictStr] = Field(None, alias="Delta", description="The expected change in an option position’s value resulting from a one point increase in the price of the underlying security.")
    theta: Optional[StrictStr] = Field(None, alias="Theta", description="The expected decline in an option position’s value resulting from the passage of one day’s time, holding all other variables (price of the underlying, volatility, etc.) constant.")
    gamma: Optional[StrictStr] = Field(None, alias="Gamma", description="The expected change in an option position’s delta resulting from a one point increase in the price of the underlying security.")
    rho: Optional[StrictStr] = Field(None, alias="Rho", description="The expected change in an option position’s value resulting from an increase of one percentage point in the risk-free interest rate (e.g. an increase from 3% to 4%).")
    vega: Optional[StrictStr] = Field(None, alias="Vega", description="The expected change in an option position’s value resulting from an increase of one percentage point in the volatility of the underlying security (e.g. an increase from 26% to 27%).")
    implied_volatility: Optional[StrictStr] = Field(None, alias="ImpliedVolatility", description="The volatility of the underlying implied by an option position’s current price.")
    intrinsic_value: Optional[StrictStr] = Field(None, alias="IntrinsicValue", description="The value of an option position exclusive of the position’s time value.  The value of the option position if it were to expire immediately.")
    extrinsic_value: Optional[StrictStr] = Field(None, alias="ExtrinsicValue", description="The time value of an option position.  The market value of an option position minus the position’s intrinsic value.")
    theoretical_value: Optional[StrictStr] = Field(None, alias="TheoreticalValue", description="The value of an option position based on a theoretical model of option prices (e.g., the Bjerksund-Stensland model).  Calculated using volatility of the underlying.")
    probability_itm: Optional[StrictStr] = Field(None, alias="ProbabilityITM", description="The calculated probability that an option position will have intrinsic value at expiration.  Calculated using volatility of the underlying.")
    probability_otm: Optional[StrictStr] = Field(None, alias="ProbabilityOTM", description="The calculated probability that an option position will not have intrinsic value at expiration.  Calculated using volatility of the underlying.")
    probability_be: Optional[StrictStr] = Field(None, alias="ProbabilityBE", description="The calculated probability that an option position will have a value at expiration that is equal to or greater than the position’s current cost.  Calculated using volatility of the underlying.")
    probability_itm_iv: Optional[StrictStr] = Field(None, alias="ProbabilityITM_IV", description="The calculated probability that an option position will have intrinsic value at expiration.  Calculated using implied volatility.")
    probability_otm_iv: Optional[StrictStr] = Field(None, alias="ProbabilityOTM_IV", description="The calculated probability that an option position will not have intrinsic value at expiration.  Calculated using implied volatility.")
    probability_be_iv: Optional[StrictStr] = Field(None, alias="ProbabilityBE_IV", description="The calculated probability that an option position will have a value at expiration that is equal to or greater than the position’s current cost.  Calculated using implied volatility.")
    theoretical_value_iv: Optional[StrictStr] = Field(None, alias="TheoreticalValue_IV", description="The value of an option position based on a theoretical model of option prices (e.g., the Bjerksund-Stensland model).  Calculated using implied volatility.")
    daily_open_interest: Optional[StrictInt] = Field(None, alias="DailyOpenInterest", description="Total number of open contracts for the option spread.  This value is updated daily.")
    ask: Optional[StrictStr] = Field(None, alias="Ask", description="Ask price. The price a seller is willing to accept for the option spread.")
    bid: Optional[StrictStr] = Field(None, alias="Bid", description="Bid price. The price a buyer is willing to pay for the option spread.")
    mid: Optional[StrictStr] = Field(None, alias="Mid", description="Mathematical average between `Ask` and `Bid`.")
    ask_size: Optional[StrictInt] = Field(None, alias="AskSize", description="Amount of security for the given `Ask` price.")
    bid_size: Optional[StrictInt] = Field(None, alias="BidSize", description="Amount of security for the given `Bid` price.")
    close: Optional[StrictStr] = Field(None, alias="Close", description="The last traded price for the option spread.  This value only updates during the official market session.")
    high: Optional[StrictStr] = Field(None, alias="High", description="Today's highest price for the option spread.")
    last: Optional[StrictStr] = Field(None, alias="Last", description="The last traded price for the option spread.")
    low: Optional[StrictStr] = Field(None, alias="Low", description="Today's lowest traded price for the option spread.")
    net_change: Optional[StrictStr] = Field(None, alias="NetChange", description="Difference between prior `Close` price and current `Close` price for the option spread.")
    net_change_pct: Optional[StrictStr] = Field(None, alias="NetChangePct", description="Percentage changed between prior `Close` price and current `Close` price for the option spread.")
    open: Optional[StrictStr] = Field(None, alias="Open", description="The initial price for the option spread during the official market session.")
    previous_close: Optional[StrictStr] = Field(None, alias="PreviousClose", description="Prior day's Closing price.")
    volume: Optional[StrictInt] = Field(None, alias="Volume", description="The number of contracts traded today.")
    side: Optional[StrictStr] = Field(None, alias="Side", description="Option Chain Side. It can be `Call`, `Put`, or `Both`.")
    strikes: Optional[conlist(StrictStr)] = Field(None, alias="Strikes", description="The strike prices for the option contracts in the legs of this spread.")
    legs: Optional[conlist(SpreadLeg)] = Field(None, alias="Legs", description="The legs of the option spread.")
    __properties = ["Delta", "Theta", "Gamma", "Rho", "Vega", "ImpliedVolatility", "IntrinsicValue", "ExtrinsicValue", "TheoreticalValue", "ProbabilityITM", "ProbabilityOTM", "ProbabilityBE", "ProbabilityITM_IV", "ProbabilityOTM_IV", "ProbabilityBE_IV", "TheoreticalValue_IV", "DailyOpenInterest", "Ask", "Bid", "Mid", "AskSize", "BidSize", "Close", "High", "Last", "Low", "NetChange", "NetChangePct", "Open", "PreviousClose", "Volume", "Side", "Strikes", "Legs"]

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
    def from_json(cls, json_str: str) -> Spread:
        """Create an instance of Spread from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in legs (list)
        _items = []
        if self.legs:
            for _item in self.legs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Legs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Spread:
        """Create an instance of Spread from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Spread.parse_obj(obj)

        _obj = Spread.parse_obj({
            "delta": obj.get("Delta"),
            "theta": obj.get("Theta"),
            "gamma": obj.get("Gamma"),
            "rho": obj.get("Rho"),
            "vega": obj.get("Vega"),
            "implied_volatility": obj.get("ImpliedVolatility"),
            "intrinsic_value": obj.get("IntrinsicValue"),
            "extrinsic_value": obj.get("ExtrinsicValue"),
            "theoretical_value": obj.get("TheoreticalValue"),
            "probability_itm": obj.get("ProbabilityITM"),
            "probability_otm": obj.get("ProbabilityOTM"),
            "probability_be": obj.get("ProbabilityBE"),
            "probability_itm_iv": obj.get("ProbabilityITM_IV"),
            "probability_otm_iv": obj.get("ProbabilityOTM_IV"),
            "probability_be_iv": obj.get("ProbabilityBE_IV"),
            "theoretical_value_iv": obj.get("TheoreticalValue_IV"),
            "daily_open_interest": obj.get("DailyOpenInterest"),
            "ask": obj.get("Ask"),
            "bid": obj.get("Bid"),
            "mid": obj.get("Mid"),
            "ask_size": obj.get("AskSize"),
            "bid_size": obj.get("BidSize"),
            "close": obj.get("Close"),
            "high": obj.get("High"),
            "last": obj.get("Last"),
            "low": obj.get("Low"),
            "net_change": obj.get("NetChange"),
            "net_change_pct": obj.get("NetChangePct"),
            "open": obj.get("Open"),
            "previous_close": obj.get("PreviousClose"),
            "volume": obj.get("Volume"),
            "side": obj.get("Side"),
            "strikes": obj.get("Strikes"),
            "legs": [SpreadLeg.from_dict(_item) for _item in obj.get("Legs")] if obj.get("Legs") is not None else None
        })
        return _obj


