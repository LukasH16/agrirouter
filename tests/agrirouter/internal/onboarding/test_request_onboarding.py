"""Test src/onboarding/messaging.py"""
from agrirouter.api.enums import Gateways, CertificateTypes
from agrirouter.api.env import Qa
from agrirouter.service.onboarding import OnboardParameters
from agrirouter.service.onboarding import SecuredOnboardingService
from tests.agrirouter.common.constants import APPLICATION_ID, PUBLIC_KEY, PRIVATE_KEY


class TestBaseOnboardingRequest:
    reg_code = "8eloz190fd"
    certification_version_id = "13"
    utc_timestamp = "+03:00"
    time_zone = "01-01-2021"
    url = "localhost"
    params = OnboardParameters(
        id_=1,
        application_id=APPLICATION_ID,
        certification_version_id=certification_version_id,
        gateway_id=Gateways.MQTT.value,
        certificate_type=CertificateTypes.PEM.value,
        utc_timestamp=utc_timestamp,
        time_zone=time_zone,
        reg_code=reg_code,
    )
    onboarding = SecuredOnboardingService(
        env=Qa(), public_key=PUBLIC_KEY, private_key=PRIVATE_KEY
    )
    request = onboarding._create_request(params)

    def test_get_data(self):
        assert self.request.get_data()["applicationId"] == APPLICATION_ID
        assert (self.request.get_data()["certificateType"] == CertificateTypes.PEM.value)
        assert (self.request.get_data()["certificateType"] == CertificateTypes.PEM.value)

    def test_get_header(self):
        assert (self.request.get_header()["Authorization"] == "Bearer " + self.reg_code)
        assert (self.request.get_header()["X-Agrirouter-ApplicationId"] == APPLICATION_ID)
