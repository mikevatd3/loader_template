# How to setup and use this Python ETL package template

## Install cookiecutter and poetry in your *base Python 3 installation*

With no environment activated, make sure you're using the right Python version. First, try `python -V`. If this doesn't work then try `python3 -V`, or `python3.10 -V`, and finally `python3.12 -V`. So long as the version that is returned is *at least* 3.10 and *at most* 3.12, you're good to go.

Then install poetry and cookiecutter (use whichever python version worked in the last step).

```bash
python -m pip install poetry cookiecutter
```

## 'Cookie Cut' the template to create your new project

1. If you haven't cloned this repository already, clone it somewhere on your computer that makes sense for your workflow.
2. If you have cloned the repo, do a `git pull` to make sure everything is up to date.
3. `cd` to the folder where you'd like your new ETL project folder to live.
4. Run the following command
```bash
python -m cookiecutter ./path/to/this/repo
```
5. Fill in the prompts from the cookiecutter workflow

This should leave you with a brand-new file structure under the 'slug' name you provided to cookiecutter.


## Use poetry to install the dependencies

Now that you have your folder structure all set up, next

1. `cd` into the folder that you just created.
2. Run `poetry shell` to spawn a new virtual environment and activate it.
3. Run `poetry install` to install all dependencies.


## Building a clean-up process

The file structure created from the template will look something like this:

```
.
├── config.toml
├── load_<project name>.py <- clean-up files start with 'load_'
├── logging_config.json
├── logs
├── poetry.lock
├── pyproject.toml
├── raw
├── README.md
└── <project name>
    ├── __init__.py
    └── utility_file_one.py <- multi-use utility functions at this level
```

The Python scripts that do the loading live at the top level. The convention is that they all start with 'load_'. The `<project name>` directory is where you can define functions and other clean-up tools and code. Functions here may be used across 'load_' files. For example, you should probably apply the same cleaning function to parcel number, taxpayer name, or address fields on different datasets from Detroit Open Data portal, to increase the likelihood of successful joins, etc.

### What a dataset load_* file looks like

```python
imports ...


logger = logging.getLogger(config["name"])


class OutputSchema(pa.DataFrameModel):
    """
    This is an OPTIONAL pandera DataFrameModel that you can use to 
    validate data from your 'cleanup_function.' See the pandera
    documentation to see how to build this.
    """


def cleanup_function(input_file: pd.DataFrame):
    """
    This function can do anything with the input, so long as it returns
    a DataFrame or GeoDataFrame.
    """

    logger.info(input_file.columns) # This logger prints to std out and to file
    
    # StopThePresses is a special exception that can be used almost like a
    # debugger step.
    raise StopThePresses("Break in the clean up function.")
    
    return input_file


def main():
    workflow = build_workflow(
        config,
        "target_table_name",
        Path.cwd(),
        cleanup_function,
        db_engine,
        LoadFileType.CSV,
    )

    workflow()


if __name__ == "__main__":
    main()
```
