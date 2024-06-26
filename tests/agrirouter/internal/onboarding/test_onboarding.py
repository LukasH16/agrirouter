"""Test agrirouter/onboarding/onboarding.py"""

import pytest

from agrirouter.api.enums import Gateways, CertificateTypes
from agrirouter.api.env import Qa
from agrirouter.api.exceptions import WrongCertificationType, WrongGateWayType
from agrirouter.service.onboarding import OnboardParameters
from agrirouter.service.onboarding import SecuredOnboardingService
from tests.agrirouter.common.constants import PUBLIC_KEY, PRIVATE_KEY, APPLICATION_ID


class TestSoftwareOnboarding:
    def test__create_request(self):
        params = OnboardParameters(
            id_=1,
            application_id=APPLICATION_ID,
            certification_version_id="13",
            gateway_id=Gateways.MQTT.value,
            certificate_type=CertificateTypes.PEM.value,
            utc_timestamp="+03:00",
            time_zone="01-01-2021",
            reg_code="8eloz190fd",
        )
        service = SecuredOnboardingService(
            env=Qa(), public_key=PUBLIC_KEY, private_key=PRIVATE_KEY
        )
        assert service._create_request(params)

        params = OnboardParameters(
            id_=2,
            application_id=APPLICATION_ID,
            certification_version_id="13",
            gateway_id=Gateways.MQTT.value,
            certificate_type="wrong_certificate",
            utc_timestamp="+03:00",
            time_zone="01-01-2021",
            reg_code="8eloz190fd",
        )
        service = SecuredOnboardingService(
            env=Qa(), public_key=PUBLIC_KEY, private_key=PRIVATE_KEY
        )
        with pytest.raises(WrongCertificationType):
            assert service._create_request(params)

        params = OnboardParameters(
            id_=3,
            application_id=APPLICATION_ID,
            certification_version_id="13",
            gateway_id="wrong_gateway_id",
            certificate_type=CertificateTypes.PEM.value,
            utc_timestamp="+03:00",
            time_zone="01-01-2021",
            reg_code="8eloz190fd",
        )
        service = SecuredOnboardingService(
            env=Qa(), public_key=PUBLIC_KEY, private_key=PRIVATE_KEY
        )
        with pytest.raises(WrongGateWayType):
            assert service._create_request(params)
