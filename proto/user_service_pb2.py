# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'user_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12user_service.proto\x12\x0cuser_service\"\r\n\x0bUserRequest\"1\n\x0cUserResponse\x12!\n\x05users\x18\x01 \x03(\x0b\x32\x12.user_service.User\"#\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t2S\n\x0bUserService\x12\x44\n\x0bGetAllUsers\x12\x19.user_service.UserRequest\x1a\x1a.user_service.UserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERREQUEST']._serialized_start=36
  _globals['_USERREQUEST']._serialized_end=49
  _globals['_USERRESPONSE']._serialized_start=51
  _globals['_USERRESPONSE']._serialized_end=100
  _globals['_USER']._serialized_start=102
  _globals['_USER']._serialized_end=137
  _globals['_USERSERVICE']._serialized_start=139
  _globals['_USERSERVICE']._serialized_end=222
# @@protoc_insertion_point(module_scope)