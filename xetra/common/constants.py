"""
File to store constants
"""

from enum import Enum

class S3FileTypes(Enum):
    """
    Supported file types for S3BucketConnector
    """
    CSV = 'csv'
    PARQUET = 'parquet'


class MetaProcessFormat(Enum):
    """
    formation for Metaprocess class
    """

    META_DATE_FORMAT = '%Y-%m-%d'
    META_PROCESS_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    META_SOUREC_DATE_COL = 'source_date'
    META_PROCESS_COL =  'datetime_of_processing'
    META_FILE_FORMAT = 'csv'