# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messaging/response/payload/feed/push-notification.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from agrirouter.generated.commons import message_pb2 as commons_dot_message__pb2
from agrirouter.generated.commons import chunk_pb2 as commons_dot_chunk__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='messaging/response/payload/feed/push-notification.proto',
  package='agrirouter.feed.push.notification',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7messaging/response/payload/feed/push-notification.proto\x12!agrirouter.feed.push.notification\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\x1a\x15\x63ommons/message.proto\x1a\x13\x63ommons/chunk.proto\"\xea\x04\n\x10PushNotification\x12Q\n\x08messages\x18\x01 \x03(\x0b\x32?.agrirouter.feed.push.notification.PushNotification.FeedMessage\x1a\xff\x02\n\x06Header\x12\x13\n\x0breceiver_id\x18\x01 \x01(\t\x12\x1e\n\x16technical_message_type\x18\x02 \x01(\t\x12\x1b\n\x13team_set_context_id\x18\x03 \x01(\t\x12\x39\n\rchunk_context\x18\x04 \x01(\x0b\x32\".agrirouter.commons.ChunkComponent\x12\x14\n\x0cpayload_size\x18\x05 \x01(\x03\x12\x32\n\x0esent_timestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0fsequence_number\x18\x07 \x01(\x03\x12\x11\n\tsender_id\x18\x08 \x01(\t\x12.\n\ncreated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nmessage_id\x18\n \x01(\t\x12.\n\x08metadata\x18\x0b \x01(\x0b\x32\x1c.agrirouter.commons.Metadata\x1a\x80\x01\n\x0b\x46\x65\x65\x64Message\x12J\n\x06header\x18\x01 \x01(\x0b\x32:.agrirouter.feed.push.notification.PushNotification.Header\x12%\n\x07\x63ontent\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,commons_dot_message__pb2.DESCRIPTOR,commons_dot_chunk__pb2.DESCRIPTOR,])




_PUSHNOTIFICATION_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='agrirouter.feed.push.notification.PushNotification.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='receiver_id', full_name='agrirouter.feed.push.notification.PushNotification.Header.receiver_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='technical_message_type', full_name='agrirouter.feed.push.notification.PushNotification.Header.technical_message_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='team_set_context_id', full_name='agrirouter.feed.push.notification.PushNotification.Header.team_set_context_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_context', full_name='agrirouter.feed.push.notification.PushNotification.Header.chunk_context', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload_size', full_name='agrirouter.feed.push.notification.PushNotification.Header.payload_size', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sent_timestamp', full_name='agrirouter.feed.push.notification.PushNotification.Header.sent_timestamp', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='agrirouter.feed.push.notification.PushNotification.Header.sequence_number', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender_id', full_name='agrirouter.feed.push.notification.PushNotification.Header.sender_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='agrirouter.feed.push.notification.PushNotification.Header.created_at', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='agrirouter.feed.push.notification.PushNotification.Header.message_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='agrirouter.feed.push.notification.PushNotification.Header.metadata', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=686,
)

_PUSHNOTIFICATION_FEEDMESSAGE = _descriptor.Descriptor(
  name='FeedMessage',
  full_name='agrirouter.feed.push.notification.PushNotification.FeedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='agrirouter.feed.push.notification.PushNotification.FeedMessage.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='agrirouter.feed.push.notification.PushNotification.FeedMessage.content', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=689,
  serialized_end=817,
)

_PUSHNOTIFICATION = _descriptor.Descriptor(
  name='PushNotification',
  full_name='agrirouter.feed.push.notification.PushNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='agrirouter.feed.push.notification.PushNotification.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PUSHNOTIFICATION_HEADER, _PUSHNOTIFICATION_FEEDMESSAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=817,
)

_PUSHNOTIFICATION_HEADER.fields_by_name['chunk_context'].message_type = commons_dot_chunk__pb2._CHUNKCOMPONENT
_PUSHNOTIFICATION_HEADER.fields_by_name['sent_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PUSHNOTIFICATION_HEADER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PUSHNOTIFICATION_HEADER.fields_by_name['metadata'].message_type = commons_dot_message__pb2._METADATA
_PUSHNOTIFICATION_HEADER.containing_type = _PUSHNOTIFICATION
_PUSHNOTIFICATION_FEEDMESSAGE.fields_by_name['header'].message_type = _PUSHNOTIFICATION_HEADER
_PUSHNOTIFICATION_FEEDMESSAGE.fields_by_name['content'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_PUSHNOTIFICATION_FEEDMESSAGE.containing_type = _PUSHNOTIFICATION
_PUSHNOTIFICATION.fields_by_name['messages'].message_type = _PUSHNOTIFICATION_FEEDMESSAGE
DESCRIPTOR.message_types_by_name['PushNotification'] = _PUSHNOTIFICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PushNotification = _reflection.GeneratedProtocolMessageType('PushNotification', (_message.Message,), {

  'Header' : _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
    'DESCRIPTOR' : _PUSHNOTIFICATION_HEADER,
    '__module__' : 'messaging.response.payload.feed.push_notification_pb2'
    # @@protoc_insertion_point(class_scope:agrirouter.feed.push.notification.PushNotification.Header)
    })
  ,

  'FeedMessage' : _reflection.GeneratedProtocolMessageType('FeedMessage', (_message.Message,), {
    'DESCRIPTOR' : _PUSHNOTIFICATION_FEEDMESSAGE,
    '__module__' : 'messaging.response.payload.feed.push_notification_pb2'
    # @@protoc_insertion_point(class_scope:agrirouter.feed.push.notification.PushNotification.FeedMessage)
    })
  ,
  'DESCRIPTOR' : _PUSHNOTIFICATION,
  '__module__' : 'messaging.response.payload.feed.push_notification_pb2'
  # @@protoc_insertion_point(class_scope:agrirouter.feed.push.notification.PushNotification)
  })
_sym_db.RegisterMessage(PushNotification)
_sym_db.RegisterMessage(PushNotification.Header)
_sym_db.RegisterMessage(PushNotification.FeedMessage)


# @@protoc_insertion_point(module_scope)
