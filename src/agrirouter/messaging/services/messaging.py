from src.agrirouter.api.enums import TechnicalMessageType, CapabilityType
from src.agrirouter.generated.commons.chunk_pb2 import ChunkComponent
from src.agrirouter.generated.commons.message_pb2 import Metadata
from src.agrirouter.generated.messaging.request.payload.account.endpoints_pb2 import ListEndpointsQuery
from src.agrirouter.generated.messaging.request.payload.efdi.efdi_pb2 import TimeLog, ISO11783_TaskData
from src.agrirouter.generated.messaging.request.payload.endpoint.capabilities_pb2 import CapabilitySpecification
from src.agrirouter.generated.messaging.request.payload.endpoint.subscription_pb2 import Subscription
from src.agrirouter.generated.messaging.request.payload.feed.feed_requests_pb2 import MessageConfirm, MessageDelete, \
    MessageQuery
from src.agrirouter.generated.messaging.request.request_pb2 import RequestEnvelope
from src.agrirouter.messaging.encode import encode_message
from src.agrirouter.messaging.messages import EncodedMessage
from src.agrirouter.messaging.parameters.dto import SendMessageParameters, ChunkedMessageParameters
from src.agrirouter.messaging.parameters.service import MessageHeaderParameters, MessagePayloadParameters, \
    CapabilitiesParameters, FeedConfirmParameters, FeedDeleteParameters, ListEndpointsParameters, \
    SubscriptionParameters, QueryHeaderParameters, QueryMessageParameters, ImageParameters, TaskParameters, \
    EfdiParameters
from src.agrirouter.messaging.services.commons import AbstractService
from src.agrirouter.utils.type_url import TypeUrl
from src.agrirouter.utils.uuid_util import new_uuid


class CapabilitiesService(AbstractService):
    """
    Service for sending capabilities to the src.
    """

    @staticmethod
    def encode(parameters: CapabilitiesParameters) -> EncodedMessage:
        """
        Encode the parameters to a message.
        :param parameters: Parameters for the message.
        """
        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("DIRECT"),
            technical_message_type=TechnicalMessageType.CAPABILITIES.value
        )

        capability_specification = CapabilitySpecification(
            app_certification_id=parameters.get_application_id(),
            app_certification_version_id=parameters.get_certification_version_id(),
            enable_push_notifications=parameters.get_enable_push_notification()
        )
        if parameters.get_capability_parameters():
            capability_specification.capabilities.extend(parameters.get_capability_parameters())

        message_payload_parameters = MessagePayloadParameters(
            type_url=TypeUrl.get_type_url(CapabilitySpecification),
            value=capability_specification.SerializeToString()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class FeedConfirmService(AbstractService):

    @staticmethod
    def encode(parameters: FeedConfirmParameters) -> EncodedMessage:
        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("DIRECT"),
            technical_message_type=TechnicalMessageType.FEED_CONFIRM.value
        )

        message_confirm = MessageConfirm(
            message_ids=parameters.get_message_ids()
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=TypeUrl.get_type_url(MessageConfirm),
            value=message_confirm.SerializeToString()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class FeedDeleteService(AbstractService):

    @staticmethod
    def encode(parameters: FeedDeleteParameters) -> EncodedMessage:
        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("DIRECT"),
            technical_message_type=TechnicalMessageType.FEED_DELETE.value
        )

        message_delete = MessageDelete(
            message_ids=parameters.get_message_ids(),
            senders=parameters.get_senders(),
            validity_period=parameters.get_validity_period()
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=TypeUrl.get_type_url(MessageDelete),
            value=message_delete.SerializeToString()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class ListEndpointsService(AbstractService):

    @staticmethod
    def encode(parameters: ListEndpointsParameters) -> EncodedMessage:
        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("DIRECT"),
            technical_message_type=TechnicalMessageType.LIST_ENDPOINTS.value if parameters.is_filtered()
            else TechnicalMessageType.LIST_ENDPOINTS_UNFILTERED.value
        )

        list_endpoints_query = ListEndpointsQuery(
            technical_message_type=parameters.get_technical_message_type(),
            direction=parameters.get_direction()
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=TypeUrl.get_type_url(ListEndpointsQuery),
            value=list_endpoints_query.SerializeToString()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class QueryMessagesService(AbstractService):

    @staticmethod
    def encode(parameters: QueryMessageParameters) -> EncodedMessage:
        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("DIRECT"),
            technical_message_type=TechnicalMessageType.FEED_MESSAGE_QUERY.value
        )

        message_query = MessageQuery(
            senders=parameters.get_senders(),
            message_ids=parameters.get_message_ids(),
            validity_period=parameters.get_validity_period(),
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=TypeUrl.get_type_url(MessageQuery),
            value=message_query.SerializeToString()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class QueryHeaderService(AbstractService):
    """
    Service to receive the headers of the messages
    """

    @staticmethod
    def encode(parameters: QueryHeaderParameters) -> EncodedMessage:
        """
        Encode the parameters into a message
        parameters: QueryHeaderParameters for the service
        """
        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("DIRECT"),
            technical_message_type=TechnicalMessageType.FEED_HEADER_QUERY.value
        )

        message_query = MessageQuery(
            senders=parameters.get_senders(),
            message_ids=parameters.get_message_ids(),
            validity_period=parameters.get_validity_period(),
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=TypeUrl.get_type_url(MessageQuery),
            value=message_query.SerializeToString()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class SubscriptionService(AbstractService):
    """
    Service for sending subscription messages to the src.
    """

    @staticmethod
    def encode(parameters: SubscriptionParameters) -> EncodedMessage:
        """
        Encode the parameters into a subscription message.
        parameters: Parameters for the subscription message.
        """
        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("DIRECT"),
            technical_message_type=TechnicalMessageType.SUBSCRIPTION.value
        )

        subscription = Subscription(
            technical_message_types=parameters.get_subscription_items(),
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=TypeUrl.get_type_url(Subscription),
            value=subscription.SerializeToString()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class SendMessageService(AbstractService):
    """
    Service for sending messages to the src
    """

    @staticmethod
    def encode(parameters: SendMessageParameters) -> EncodedMessage:
        """
        Encode the parameters into a message.
        parameters: Parameters for the message service.
        """
        message_header_parameters = MessageHeaderParameters(
            technical_message_type=parameters.get_technical_message_type(),
            mode=parameters.get_mode(),
            team_set_context_id=parameters.get_team_set_context_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            recipients=parameters.get_recipients(),
            chunk_component=parameters.get_chunk_component(),
            application_message_id=parameters.get_application_message_id()
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=parameters.get_type_url() or TechnicalMessageType.EMPTY.value,
            value=parameters.get_base64_message_content(),
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)

        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class SendChunkedMessageService(AbstractService):
    """
    Service for sending chunked messages to the src
    """

    @staticmethod
    def encode(parameters: ChunkedMessageParameters):
        """
        parameters: Chunked Message Parameters required
        """
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=parameters.get_encoded_chunked_messages(),
        )
        return encoded_message


class ImageService(AbstractService):
    @staticmethod
    def encode(parameters: ImageParameters) -> EncodedMessage:
        metadata = Metadata()
        metadata.file_name = parameters.get_image_filename()

        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            recipients=parameters.get_recipients(),
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("DIRECT"),
            technical_message_type=CapabilityType.IMG_JPEG.value,
            metadata=metadata
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=TechnicalMessageType.EMPTY.value,
            value=parameters.get_image_encoded()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class TaskService(AbstractService):
    @staticmethod
    def encode(parameters: TaskParameters) -> EncodedMessage:
        metadata = Metadata()
        metadata.file_name = parameters.get_task_filename()
        # Add ChunkComponent
        chunkcomponent = ChunkComponent()
        chunkcomponent.context_id = parameters.get_chunk_context_id()
        chunkcomponent.current = parameters.get_chunk_current()
        chunkcomponent.total = parameters.get_chunk_total()
        chunkcomponent.total_size = parameters.get_chunk_total_size()

        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            recipients=parameters.get_recipients(),
            chunk_component=chunkcomponent,
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("DIRECT"),
            technical_message_type=CapabilityType.ISO_11783_TASK_DATA_ZIP.value,
            metadata=metadata
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=TechnicalMessageType.EMPTY.value,
            value=parameters.get_task_encoded()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class EfdiTimelogService(AbstractService):
    @staticmethod
    def encode(parameters: EfdiParameters) -> EncodedMessage:

        if parameters.get_efdi_filename() is not None:
            metadata = Metadata()
            metadata.file_name = parameters.get_efdi_filename()
        else:
            metadata = None

        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            recipients=parameters.get_recipients(),
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("DIRECT"),
            technical_message_type=CapabilityType.ISO_11783_TIMELOG.value,
            metadata=metadata
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=TypeUrl.get_type_url(TimeLog),
            value=parameters.get_efdi()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class EfdiTimelogPublishService(AbstractService):
    @staticmethod
    def encode(parameters: EfdiParameters) -> EncodedMessage:

        if parameters.get_efdi_filename() is not None:
            metadata = Metadata()
            metadata.file_name = parameters.get_efdi_filename()
        else:
            metadata = None

        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("PUBLISH"),
            technical_message_type=CapabilityType.ISO_11783_TIMELOG.value,
            metadata=metadata
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=TypeUrl.get_type_url(TimeLog),
            value=parameters.get_efdi()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message


class EfdiDeviceDscService(AbstractService):
    @staticmethod
    def encode(parameters: EfdiParameters) -> EncodedMessage:

        if parameters.get_efdi_filename() is not None:
            metadata = Metadata()
            metadata.file_name = parameters.get_efdi_filename()
        else:
            metadata = None

        message_header_parameters = MessageHeaderParameters(
            application_message_id=parameters.get_application_message_id(),
            application_message_seq_no=parameters.get_application_message_seq_no(),
            team_set_context_id=parameters.get_team_set_context_id(),
            mode=RequestEnvelope.Mode.Value("PUBLISH"),
            technical_message_type=CapabilityType.ISO_11783_DEVICE_DESCRIPTION.value,
            metadata=metadata
        )

        message_payload_parameters = MessagePayloadParameters(
            type_url=TypeUrl.get_type_url(ISO11783_TaskData),
            value=parameters.get_efdi()
        )

        message_content = encode_message(message_header_parameters, message_payload_parameters)
        encoded_message = EncodedMessage(
            id_=new_uuid(),
            content=message_content
        )

        return encoded_message