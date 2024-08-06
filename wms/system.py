# -*- coding: utf-8 -*-
"""
    open-wms.system
    ~~~~~~~~~~~~~~~


"""
from __future__ import annotations

import datetime as dt


import pandas as pd
import penguin
from loris import ComponentException, Configurations


class System(penguin.System):

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        # TODO: Configure system

    def run(
        self,
        start: pd.Timestamp | dt.datetime = None,
        end: pd.Timestamp | dt.datetime = None,
        **kwargs
    ) -> pd.DataFrame:
        # TODO: Implement core water management routine
        pass
