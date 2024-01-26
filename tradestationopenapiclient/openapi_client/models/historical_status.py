# coding: utf-8

"""
    

    # Authentication For more information on authorization and gaining an access/refresh token, please visit: [Authentication](/docs/fundamentals/authentication/auth-overview). <SecurityDefinitions /> 

    The version of the OpenAPI document: 
    Contact: ClientServices@tradestation.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class HistoricalStatus(str, Enum):
    """
    The status of an order. Status filters can be used according to the order category:   - Open:     - ACK - Received     - ASS - Option Assignment     - BRC - Bracket Canceled     - BRF - Bracket Filled     - BRO - Broken     - CHG - Change     - CND – Condition Met     - COR - Fill Corrected     - CSN - Cancel Sent     - DIS - Dispatched     - DOA - Dead     - DON – Queued     - ECN - Expiration Cancel Request     - EXE - Option Exercise     - FPR - Partial Fill (Alive)     - LAT - Too Late to Cancel     - OPN - Sent     - OSO - OSO Order     - OTHER - OrderStatus not mapped     - PLA - Sending     - REC - Big Brother Recall Request     - RJC – Cancel Request Rejected     - RPD - Replace Pending     - RSN – Replace Sent     - STP - Stop Hit     - STT - OrderStatus Message     - SUS - Suspended     - UCN - Cancel Sent   - Canceled:     - CAN - Canceled     - EXP - Expired     - OUT - UROut     - RJR - Change Request Rejected     - SCN - Big Brother Recall     - TSC – Trade Server Canceled     - UCH - Replaced   - Rejected:     - REJ - Rejected   - Filled:     - FLL - Filled     - FLP - Partial Fill (UROut)
    """

    """
    allowed enum values
    """
    ACK = 'ACK'
    ASS = 'ASS'
    BRC = 'BRC'
    BRF = 'BRF'
    BRO = 'BRO'
    CHG = 'CHG'
    CND = 'CND'
    COR = 'COR'
    CSN = 'CSN'
    DIS = 'DIS'
    DOA = 'DOA'
    DON = 'DON'
    ECN = 'ECN'
    EXE = 'EXE'
    FPR = 'FPR'
    LAT = 'LAT'
    OPN = 'OPN'
    OSO = 'OSO'
    OTHER = 'OTHER'
    PLA = 'PLA'
    REC = 'REC'
    RJC = 'RJC'
    RPD = 'RPD'
    RSN = 'RSN'
    STP = 'STP'
    STT = 'STT'
    SUS = 'SUS'
    UCN = 'UCN'
    CAN = 'CAN'
    EXP = 'EXP'
    OUT = 'OUT'
    RJR = 'RJR'
    SCN = 'SCN'
    TSC = 'TSC'
    UCH = 'UCH'
    REJ = 'REJ'
    FLL = 'FLL'
    FLP = 'FLP'

    @classmethod
    def from_json(cls, json_str: str) -> HistoricalStatus:
        """Create an instance of HistoricalStatus from a JSON string"""
        return HistoricalStatus(json.loads(json_str))


