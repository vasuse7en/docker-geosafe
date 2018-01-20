class Constant:
    FG_CCC_REST_END_POINT = 'https://10.10.39.113:8443/apiman-gateway/Fluentgrid/SimulationAPI/1.0'
    FG_CCC_REST_END_POINT_USER = 'VizagUser'
    FG_CCC_REST_END_POINT_PASS = 'vizAg@123'
    FG_CCC_REST_END_POINT_API_KEY = '9a186887-9582-49f3-b3b6-e4aa79d692c1'

class Certainty:
    OBSERVED = 'Observed'
    LIKELY = 'Likely'
    POSSIBLE = 'Possible'
    UNLIKELY = 'Unlikely'
    UNKNOWN = 'Unknown'

class Urgency:
    IMMEDIATE = 'Immediate'
    EXPECTED = 'Expected'
    FUTURE = 'Future'
    PAST = 'Past'
    UNKNOWN = 'Unknown'

class IntegrationCCCSystem:
    FG_CCC = 'Fluentgrid CCC'
    IBM_IOC = 'IBM IOC'