# bca4abm
# See full license in LICENSE.txt.

import logging

import os.path
import numpy as np
import pandas as pd

from activitysim.core import inject
from activitysim.core import config

from bca4abm import bca4abm as bca


logger = logging.getLogger(__name__)


@inject.table()
def persons(data_dir):

    logger.debug("reading persons table")

    table_settings = config.read_model_settings('tables.yaml')
    df = bca.read_csv_table(table_name="persons", data_dir=data_dir, settings=table_settings)

    # just to be explicit
    assert 'person_id' not in df.columns
    df.index = df.index + 1
    df.index.name = 'person_id'

    return df


# merge table casting households onto persons
@inject.table()
def persons_merged(persons, households):

    return inject.merge_tables(target=persons.name,
                               tables=[persons, households])
