from os import path
from typing import Dict, Optional
from pathlib import Path
import yaml
import json
import jinja2


def load_yaml(filename: str) -> Dict[str, Dict]:
    """Loads a YAML configuration file from s3

    .. versionadded:: 0.0.1

    Parameters
    ----------
        filename : str
            The filname of your yaml.
    Returns
    -------
    Dictionary with values defined in file
        dict.
    """
    if path.exists(filename):
        with open(filename, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
    else:
        raise Exception(f"File does not exist: {filename}")

    return data


def parse_yaml_config(
    yaml_file: str,
    dump_yaml: bool = False,
    dump_file: Optional[Path] = None,
    **kwargs,
) -> Dict:
    """Read a file and parse kwrgs variables with Jinja template.

    Parameters
    ----------
    yaml_file : str
        Path to config file
    dump_yaml : bool, optional
        If true write the yaml contents to file, by default False
    dump_file : Optional[Path], optional
        Path to dump the file, by default None

    Returns
    -------
    Dict
        File config content

    Raises
    ------
    Exception
        If there is an error reading/writing the yaml file
    """
    try:
        config = json.dumps(load_yaml(filename=yaml_file))
        config = jinja2.Template(config).render(
            **{k.upper(): v for k, v in kwargs.items()}
        )
        config_dict = json.loads(config)

        if dump_yaml and dump_file:
            print(f"Saving file to: {dump_file}")
            dump_file.parent.mkdir(exist_ok=True)
            yaml.dump(
                data=config_dict,
                stream=open(dump_file, "w"),
                default_flow_style=False,
                sort_keys=False,
            )
    except Exception:
        raise Exception(f"Error parsing config: {yaml_file}")
    else:
        return config_dict
