# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Technische Universität Graz
#
# invenio-rdm-pure is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""File description."""

import os
from datetime import date

dirpath = os.path.dirname(os.path.abspath(__file__))

data_setup_path = f"{dirpath}/data_setup"
# data_setup_path = "/opt/invenio/var/instance/data_setup"
# data_setup_path = f"{dirpath}/../../tugraz-repo/app_data/data_setup"

# Deletes log files (reports/ directory) after x days
days_keep_log = 30

# Reduce the number of lines in data/successful_changes.txt
lines_successful_changes = 90

# Time gap between RDM post requests
push_dist_sec = 0.8
# Too many requests sent to RDM server (waits 15 minutes (900/60 = 15))
# 429 is the HTTP response code
wait_429 = 900

# OTHER
iso6393_file_name = f"{dirpath}/source/iso6393.json"
pure_uuid_length = 36

# Pure import
pure_import_path = "templates/invenio_rdm_pure/temporary_files"
pure_import_file = f"{dirpath}/{pure_import_path}/pure_import.xml"

# EMAIL     -------- TO REVIEW ------------------
email_smtp_server = "smtp.gmail.com"
email_smtp_port = 587
email_subject = "Delete Pure file"
email_message = (
    """Subject: """ + email_subject + """Please remove from pure uuid {} the file {}."""
)

# RESTRICTIONS
possible_record_restrictions = ["groups", "owners", "ip_range", "ip_single"]

# ACCESS RIGHTS
accessright_pure_to_rdm = {
    "Open": "open",
    "Embargoed": "embargoed",
    "Restricted": "restricted",
    "Closed": "closed",
    "Unknown": "closed",
    "Indeterminate": "closed",
    "None": "closed",
}

# RESOURCE TYPE
resourcetype_pure_to_rdm = {
    "Article": "publication",
    "Chapter": "publication",
    "Diploma Thesis": "publication",
    "Master's Thesis": "publication",
    "Doctoral Thesis": "publication",
    "Book": "publication",
    "Paper": "publication",
    "Lecture or Presentation": "presentation",
    "Conference contribution": "presentation",
    "Poster": "poster",
    "Software": "software",
    "Data set/Database": "dataset",
    "Other report": "other",
}

# DATABASE
database_uri = {
    "db_host": f"{data_setup_path}/db_host.txt",
    "db_name": f"{data_setup_path}/db_name.txt",
    "db_user": f"{data_setup_path}/db_user.txt",
    "db_password": f"{data_setup_path}/db_password.txt",
}


# REPORT LOGS
reports_full_path = f"{dirpath}/reports/"
base_path = f"{reports_full_path}{date.today()}"
log_files_name = {
    "groups": f"{base_path}_groups.log",
    "owners": f"{base_path}_owners.log",
    "pages": f"{base_path}_pages.log",
    "console": f"{base_path}_console.log",
    "changes": f"{base_path}_changes.log",
}

# DATA FILES NAME
base_path = f"{dirpath}/data"
data_files_name = {
    "successful_changes": f"{base_path}/successful_changes.txt",
    "user_ids_match": f"{base_path}/user_ids_match.txt",
    "all_rdm_records": f"{base_path}/all_rdm_records.txt",
    "rdm_record_owners": f"{base_path}/rdm_record_owners.txt",
    "transfer_uuid_list": f"{base_path}/to_transmit.txt",
    "delete_recid_list": f"{base_path}/to_delete.txt",
}

# TEMPORARY FILES (used to keep truck of the data received and transmitted)
base_path = f"{dirpath}/data/temporary_files"
temporary_files_name = {
    "base_path": f"{base_path}",
    "get_pure_metadata": f"{base_path}/get_pure_metadata.json",
    "get_rdm_metadata": f"{base_path}/get_rdm_metadata.json",
    "post_rdm_response": f"{base_path}/post_rdm_response.json",
    "post_rdm_metadata": f"{base_path}/post_rdm_metadata.json",
}

# Percentage of updated items to considere the upload task successful
upload_percent_accept = 90

# VERSIONING
versioning_running = False
