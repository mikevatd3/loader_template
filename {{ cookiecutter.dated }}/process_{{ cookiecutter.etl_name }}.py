from {{ cookiecutter.parent_package }} import setup_logging

from extract import extract_{{ cookiecutter.etl_name }}
from transform import transform_{{ cookiecutter.etl_name }}
from load import load_{{ cookiecutter.etl_name }}


logger = setup_logging()


extract_{{ cookiecutter.etl_name }}(logger)
transform_{{ cookiecutter.etl_name }}(logger)
load_{{ cookiecutter.etl_name }}(logger)

