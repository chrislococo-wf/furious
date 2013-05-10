#
# Copyright 2012 WebFilings, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json

import logging

from ..async import async_from_options
from .. import context
from ..processors import run_job


def process_async_task(headers, request_body):
    """Process an Async task and execute the requested function."""
    async_options = json.loads(request_body)
    async = async_from_options(async_options)

    logging.info(async._function_path)

    with context.execution_context_from_async(async):
        run_job()

    return 200, async._function_path



