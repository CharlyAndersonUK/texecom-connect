#!/usr/bin/env python
#
# Decoder for Texecom Connect API/Protocol
#
# Copyright (C) 2018 Joseph Heenan
# Updates Jul 2020 Charly Anderson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class User:
    def __init__(self):
        self.passcode = None
        self.tag = None
        self.name = None
        self.areas = None
        self.modifiers = None
        self.locks = None
        self.doors = None
        self.config = None

    def valid(self):
        return self.passcode != "" or self.tag != ""
