"""
Utils package
"""
from pyspark.sql import DataFrame, SparkSession, Row
from collections import OrderedDict


def load_tsv(spark_session: SparkSession, file_path: str) -> DataFrame:
    """

    :param spark_session:
    :param file_path:
    :return:
    """
    return spark_session.read.csv(file_path,
                                  header=True,
                                  mode='DROPMALFORMED',
                                  sep='\t').load(file_path)


def convert_to_row(d: dict) -> Row:
    """

    :param d:
    :return:
    """
    return Row(**OrderedDict(sorted(d.items())))