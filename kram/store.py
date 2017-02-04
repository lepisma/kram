"""
Kram store module
"""

import hashlib
import json
import time
from pathlib import Path
from typing import Dict

import crayons
import numpy as np
import yaml
from tinydb import Query, TinyDB
from tinydb.storages import JSONStorage
from tinydb_serialization import SerializationMiddleware, Serializer


class TableExists(Exception):
    pass


class NpSerializer(Serializer):
    """
    Serializer for numpy arrays
    """

    OBJ_CLASS = np.ndarray

    def encode(self, array):
        return array.tolist()

    def decode(self, ser):
        return np.array(ser)


class KramRun:
    """
    Run class for each run of an experiment using a configuration
    """

    def __init__(self, config: Dict, db: TinyDB, force: bool=False) -> None:
        """
        Create a new table for given configuration
        """

        serialized_config = json.dumps(config, sort_keys=True)
        self.identifier = hashlib.md5(serialized_config.encode(
            "utf-8")).hexdigest()

        if self.identifier in db.tables():
            if force:
                db.purge_table(self.identifier)
            else:
                raise TableExists(
                    "This experiment run already exists, use force=True for overwriting"
                )

        self.tb = db.table(self.identifier)

        # Write config
        self.config = config
        self.tb.insert({"type": "config", "value": config})

    def append(self, data: Dict):
        """
        Append data as result into the table
        """

        entry = {"type": "data", "time": time.time(), "value": data}
        self.tb.insert(entry)


class KramExperiment:
    """
    Experiment class wrapping around one tinydb database
    """

    def __init__(self, exp_name: str, store_path: Path) -> None:
        """
        Initialize a database for the experiment
        """

        exp_file = "exp_{}_.json".format(exp_name)

        serialization = SerializationMiddleware()
        serialization.register_serializer(NpSerializer(), "TinyNp")

        self.db = TinyDB(store_path.joinpath(exp_file), storage=serialization)
        self.exp_name = exp_name


class KramStore:
    """
    Data store for a project. A project has a directory and database files for
    experiments.
    """

    def __init__(self, root_path: str, project_name: str) -> None:
        """
        Create store directory if not found
        """

        self.path = Path(root_path).joinpath("kramlogs")
        try:
            self.path.mkdir()
        except FileExistsError:
            print(crayons.red("kram store already exists"))
            return

        self.config = {"name": project_name}

        # Write config
        with self.path.joinpath("config.yaml").open("w") as cfg:
            yaml.dump(self.config, cfg)
