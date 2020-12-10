# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Technische Universität Graz
#
# invenio-rdm-pure is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Synchronizer module to facilitate record synchronization of invenio and pure."""

import datetime
import os
from typing import List

from ...utils import get_dates_in_span


class Synchronizer(object):
    """Synchronizer class to facilitate record synchronization of invenio and pure."""

    def __init__(self):
        """Default Constructor of the class Synchronizer."""

    def run_initial_synchronization(self) -> None:
        """Runs the initial synchronization.

        In this case the invenio datawarehouse is empty."""

    def run_scheduled_synchronization(self) -> None:
        """Runs scheduled synchronization.

        In this case the invenio datawarehouse already contains entries."""

    def run_user_synchronization(self, userid: str) -> None:
        """Runs on-demand synchronization for a user."""

    def synchronize(self) -> None:
        """Runs the synchronization."""

    def _get_missing_synchronization_dates(self, days_span: int = 7) -> List[str]:
        """Gets the dates, in which Pure changes have not been synchronized."""
        missing_dates = []
        sync_dates = self._get_synchronization_history()
        date_today = datetime.date.today()
        dates_to_check = get_dates_in_span(
            date_today, date_today - datetime.timedelta(days_span), -1
        )

        for date in dates_to_check:
            if date not in sync_dates:
                missing_dates.append(date)

        return missing_dates

    def _get_synchronization_history(self) -> List[str]:
        """Opens the synchronization history file and returns an ascending list of dates the synchronization ran on."""
        path = os.path.join(
            os.path.dirname(__file__), "../../../data/synchronization_history.txt"
        )
        sync_history = []
        if os.path.isfile(path):
            with open(path) as fp:
                lines = fp.readlines()
                for line in lines:
                    sync_history.append(
                        datetime.datetime.strptime(date_string=line, format="%Y-%m-%d")
                    )
                sync_history = fp.readlines()
        return sync_history
