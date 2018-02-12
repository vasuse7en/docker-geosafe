class Constant:
    FG_CCC_REST_END_POINT = 'https://vspccc.mpower.in:8443/apiman-gateway/FLUENTGRID/ALERTSAPI/1.1'
    FG_CCC_REST_END_POINT_USER = 'VizagUser'
    FG_CCC_REST_END_POINT_PASS = 'vizAg@123'
    FG_CCC_REST_END_POINT_API_KEY = '5640156d-25b7-44ef-ae92-571604f3db39'
    FG_CCC_SSO_END_POINT = 'https://vspccc.mpower.in:8443/auth/realms/Simulation/protocol/openid-connect/token'
    FG_CCC_SSO_END_POINT_USER = 'VizagUser'
    FG_CCC_SSO_END_POINT_PASS = 'flUentgr$d'

class Certainty:
    Observed = 'Observed'
    Likely = 'Likely'
    Possible = 'Possible'
    Unlikely = 'Unlikely'
    Unknown = 'Unknown'

class Urgency:
    Immediate = 'Immediate'
    Expected = 'Expected'
    Future = 'Future'
    Past = 'Past'
    Unknown = 'Unknown'

class IntegrationCCCSystem:
    FG_CCC = 'Fluentgrid CCC'
    IBM_IOC = 'IBM IOC'