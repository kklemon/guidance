# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _serialization.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14_serialization.proto\x12\x08guidance\"3\n\x07Grammar\x12(\n\x05nodes\x18\x01 \x03(\x0b\x32\x19.guidance.GrammarFunction\"\xa5\x03\n\x12\x45ngineCallResponse\x12\x11\n\tnew_bytes\x18\x01 \x01(\x0c\x12\x14\n\x0cis_generated\x18\x02 \x01(\x08\x12\x16\n\x0enew_bytes_prob\x18\x03 \x01(\x02\x12G\n\x0e\x63\x61pture_groups\x18\x04 \x03(\x0b\x32/.guidance.EngineCallResponse.CaptureGroupsEntry\x12W\n\x17\x63\x61pture_group_log_probs\x18\x05 \x03(\x0b\x32\x36.guidance.EngineCallResponse.CaptureGroupLogProbsEntry\x12\x17\n\x0fnew_token_count\x18\x06 \x01(\x05\x1a\x45\n\x12\x43\x61ptureGroupsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.guidance.Value:\x02\x38\x01\x1aL\n\x19\x43\x61ptureGroupLogProbsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.guidance.Value:\x02\x38\x01\"\x80\x01\n\x05Value\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x15\n\x0b\x62ytes_value\x18\x02 \x01(\x0cH\x00\x12\x15\n\x0b\x66loat_value\x18\x03 \x01(\x02H\x00\x12)\n\nlist_value\x18\x04 \x01(\x0b\x32\x13.guidance.ListValueH\x00\x42\x06\n\x04kind\",\n\tListValue\x12\x1f\n\x06values\x18\x01 \x03(\x0b\x32\x0f.guidance.Value\"w\n\x04\x42yte\x12\x0c\n\x04\x62yte\x18\x01 \x01(\x0c\x12\x0e\n\x06hidden\x18\x02 \x01(\x08\x12\x14\n\x0c\x63ommit_point\x18\x03 \x01(\x08\x12\x10\n\x08nullable\x18\x04 \x01(\x08\x12\x14\n\x0c\x63\x61pture_name\x18\x05 \x01(\t\x12\x13\n\x0btemperature\x18\x06 \x01(\x02\"p\n\tByteRange\x12\x12\n\nbyte_range\x18\x01 \x01(\x0c\x12\x0e\n\x06hidden\x18\x03 \x01(\x08\x12\x14\n\x0c\x63ommit_point\x18\x04 \x01(\x08\x12\x14\n\x0c\x63\x61pture_name\x18\x05 \x01(\t\x12\x13\n\x0btemperature\x18\x06 \x01(\x02\"\x06\n\x04Null\"k\n\rModelVariable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06hidden\x18\x02 \x01(\x08\x12\x14\n\x0c\x63ommit_point\x18\x03 \x01(\x08\x12\x14\n\x0c\x63\x61pture_name\x18\x04 \x01(\t\x12\x10\n\x08nullable\x18\x05 \x01(\x08\"\x86\x01\n\x04Join\x12\x10\n\x08nullable\x18\x01 \x01(\x08\x12\x0e\n\x06values\x18\x02 \x03(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06hidden\x18\x04 \x01(\x08\x12\x14\n\x0c\x63ommit_point\x18\x05 \x01(\x08\x12\x14\n\x0c\x63\x61pture_name\x18\x06 \x01(\t\x12\x12\n\nmax_tokens\x18\x07 \x01(\x05\"\x9b\x01\n\x06Select\x12\x10\n\x08nullable\x18\x01 \x01(\x08\x12\x0e\n\x06values\x18\x02 \x03(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06hidden\x18\x04 \x01(\x08\x12\x14\n\x0c\x63ommit_point\x18\x05 \x01(\x08\x12\x14\n\x0c\x63\x61pture_name\x18\x06 \x01(\t\x12\x12\n\nmax_tokens\x18\x07 \x01(\x05\x12\x11\n\trecursive\x18\x08 \x01(\x08\"\xe4\x01\n\x0fGrammarFunction\x12\x1e\n\x04join\x18\x01 \x01(\x0b\x32\x0e.guidance.JoinH\x00\x12\"\n\x06select\x18\x02 \x01(\x0b\x32\x10.guidance.SelectH\x00\x12\x1e\n\x04\x62yte\x18\x03 \x01(\x0b\x32\x0e.guidance.ByteH\x00\x12)\n\nbyte_range\x18\x04 \x01(\x0b\x32\x13.guidance.ByteRangeH\x00\x12\x31\n\x0emodel_variable\x18\x05 \x01(\x0b\x32\x17.guidance.ModelVariableH\x00\x42\x0f\n\rfunction_typeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, '_serialization_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ENGINECALLRESPONSE_CAPTUREGROUPSENTRY']._options = None
  _globals['_ENGINECALLRESPONSE_CAPTUREGROUPSENTRY']._serialized_options = b'8\001'
  _globals['_ENGINECALLRESPONSE_CAPTUREGROUPLOGPROBSENTRY']._options = None
  _globals['_ENGINECALLRESPONSE_CAPTUREGROUPLOGPROBSENTRY']._serialized_options = b'8\001'
  _globals['_GRAMMAR']._serialized_start=34
  _globals['_GRAMMAR']._serialized_end=85
  _globals['_ENGINECALLRESPONSE']._serialized_start=88
  _globals['_ENGINECALLRESPONSE']._serialized_end=509
  _globals['_ENGINECALLRESPONSE_CAPTUREGROUPSENTRY']._serialized_start=362
  _globals['_ENGINECALLRESPONSE_CAPTUREGROUPSENTRY']._serialized_end=431
  _globals['_ENGINECALLRESPONSE_CAPTUREGROUPLOGPROBSENTRY']._serialized_start=433
  _globals['_ENGINECALLRESPONSE_CAPTUREGROUPLOGPROBSENTRY']._serialized_end=509
  _globals['_VALUE']._serialized_start=512
  _globals['_VALUE']._serialized_end=640
  _globals['_LISTVALUE']._serialized_start=642
  _globals['_LISTVALUE']._serialized_end=686
  _globals['_BYTE']._serialized_start=688
  _globals['_BYTE']._serialized_end=807
  _globals['_BYTERANGE']._serialized_start=809
  _globals['_BYTERANGE']._serialized_end=921
  _globals['_NULL']._serialized_start=923
  _globals['_NULL']._serialized_end=929
  _globals['_MODELVARIABLE']._serialized_start=931
  _globals['_MODELVARIABLE']._serialized_end=1038
  _globals['_JOIN']._serialized_start=1041
  _globals['_JOIN']._serialized_end=1175
  _globals['_SELECT']._serialized_start=1178
  _globals['_SELECT']._serialized_end=1333
  _globals['_GRAMMARFUNCTION']._serialized_start=1336
  _globals['_GRAMMARFUNCTION']._serialized_end=1564
# @@protoc_insertion_point(module_scope)
