# Copyright 2010-2021, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

{
  'variables': {
    'relative_dir': 'engine',
    'gen_out_dir': '<(SHARED_INTERMEDIATE_DIR)/<(relative_dir)',
  },
  'targets': [
    {
      'target_name': 'modules',
      'type': 'static_library',
      'sources': [
        '<(gen_out_dir)/../dictionary/pos_matcher_impl.inc',
        'modules.cc',
      ],
      'dependencies': [
        '<(mozc_oss_src_dir)/base/absl.gyp:absl_status',
        '<(mozc_oss_src_dir)/base/absl.gyp:absl_strings',
        '<(mozc_oss_src_dir)/base/base.gyp:base',
        '<(mozc_oss_src_dir)/converter/converter_base.gyp:connector',
        '<(mozc_oss_src_dir)/converter/converter_base.gyp:segmenter',
        '<(mozc_oss_src_dir)/dictionary/dictionary.gyp:dictionary_impl',
        '<(mozc_oss_src_dir)/dictionary/dictionary.gyp:suffix_dictionary',
        '<(mozc_oss_src_dir)/dictionary/dictionary_base.gyp:pos_matcher',
        '<(mozc_oss_src_dir)/dictionary/dictionary_base.gyp:suppression_dictionary',
        '<(mozc_oss_src_dir)/dictionary/dictionary_base.gyp:user_dictionary',
        '<(mozc_oss_src_dir)/dictionary/dictionary_base.gyp:user_pos',
        '<(mozc_oss_src_dir)/dictionary/system/system_dictionary.gyp:system_dictionary',
        '<(mozc_oss_src_dir)/dictionary/system/system_dictionary.gyp:value_dictionary',
        '<(mozc_oss_src_dir)/prediction/prediction_base.gyp:suggestion_filter',
        '<(mozc_oss_src_dir)/protocol/protocol.gyp:commands_proto',
        '<(mozc_oss_src_dir)/protocol/protocol.gyp:user_dictionary_storage_proto',
      ],
      'export_dependent_settings': [
        '<(mozc_oss_src_dir)/dictionary/dictionary_base.gyp:pos_matcher',
        '<(mozc_oss_src_dir)/protocol/protocol.gyp:user_dictionary_storage_proto',
      ],
    },
  ],
}