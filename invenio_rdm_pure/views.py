# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Technische Universität Graz.
#
# invenio-rdm-pure is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module that adds pure."""

import os

from flask import Blueprint
from flask_babelex import gettext as _

from .setup import dirpath, pure_import_file
from .source.pure.requests_pure import get_research_outputs
from .source.rdm.run.groups import user_externalid
from .source.rdm.run.synchronizer import Synchronizer
import time

blueprint = Blueprint(
    "invenio_rdm_pure",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@blueprint.route("/pure_import_xml")
def index1():
    """Render pure_import_xml view."""
    # Check if the XML file does not exist
    if not os.path.isfile(pure_import_file):
        # Run pure_import task to create the XML file
        os.system(f"python {dirpath}/cli.py pure_import")
    return open(pure_import_file, "r").read()


@blueprint.route("/user_import_records")
def index3():
    """Render user_import_records view."""
    externalId = user_externalid()
    if not externalId:
        return "No user is logged in"

    command = "python /home/bootcamp/src/cli2/invenio-rdm-pure/invenio_rdm_pure/cli.py "
    command += f"owner --identifier='externalId' --identifierValue='{externalId}'"
    os.system(command)
    return "Task successfully completed"


@blueprint.route("/test")
def test():
    """Test."""
    start_time = time.time()
    synchronizer = Synchronizer()
    synchronizer.run_initial_synchronization()
    print("Synchronization took: " + str((time.time() - start_time)))
    # pure_api_key = "6d02a3dc-1b13-49c0-b5b3-d7b3e79ccada"
    # pure_api_url = "https://pure01.tugraz.at/ws/api/516/"
    # converter = Converter()
    # for i in range(0, 10000):
    #     record = get_research_outputs(pure_api_key, pure_api_url, 1, 40000 + i)[0]
    #     converter.convert_pure_json_to_marc21_xml(record)
    #     print("Converted " + str(i) + "/ 10000 records")
    return "Task successfully completed"
