# coding: utf-8

"""
    

    # Authentication For more information on authorization and gaining an access/refresh token, please visit: [Authentication](/docs/fundamentals/authentication/auth-overview). <SecurityDefinitions /> 

    The version of the OpenAPI document: 
    Contact: ClientServices@tradestation.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from openapi_client.models.heartbeat3 import Heartbeat3
from openapi_client.models.order1 import Order1
from openapi_client.models.stream_order_error_response import StreamOrderErrorResponse
from openapi_client.models.stream_status import StreamStatus
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

STREAMORDERS200RESPONSE_ANY_OF_SCHEMAS = ["Heartbeat3", "Order1", "StreamOrderErrorResponse", "StreamStatus"]

class StreamOrders200Response(BaseModel):
    """
    StreamOrders200Response
    """

    # data type: Order1
    anyof_schema_1_validator: Optional[Order1] = None
    # data type: StreamStatus
    anyof_schema_2_validator: Optional[StreamStatus] = None
    # data type: Heartbeat3
    anyof_schema_3_validator: Optional[Heartbeat3] = None
    # data type: StreamOrderErrorResponse
    anyof_schema_4_validator: Optional[StreamOrderErrorResponse] = None
    if TYPE_CHECKING:
        actual_instance: Union[Heartbeat3, Order1, StreamOrderErrorResponse, StreamStatus]
    else:
        actual_instance: Any
    any_of_schemas: List[str] = Field(STREAMORDERS200RESPONSE_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = StreamOrders200Response.construct()
        error_messages = []
        # validate data type: Order1
        if not isinstance(v, Order1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Order1`")
        else:
            return v

        # validate data type: StreamStatus
        if not isinstance(v, StreamStatus):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StreamStatus`")
        else:
            return v

        # validate data type: Heartbeat3
        if not isinstance(v, Heartbeat3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Heartbeat3`")
        else:
            return v

        # validate data type: StreamOrderErrorResponse
        if not isinstance(v, StreamOrderErrorResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StreamOrderErrorResponse`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in StreamOrders200Response with anyOf schemas: Heartbeat3, Order1, StreamOrderErrorResponse, StreamStatus. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> StreamOrders200Response:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> StreamOrders200Response:
        """Returns the object represented by the json string"""
        instance = StreamOrders200Response.construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[Order1] = None
        try:
            instance.actual_instance = Order1.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[StreamStatus] = None
        try:
            instance.actual_instance = StreamStatus.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[Heartbeat3] = None
        try:
            instance.actual_instance = Heartbeat3.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[StreamOrderErrorResponse] = None
        try:
            instance.actual_instance = StreamOrderErrorResponse.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into StreamOrders200Response with anyOf schemas: Heartbeat3, Order1, StreamOrderErrorResponse, StreamStatus. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


