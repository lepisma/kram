"""
Kram store module
"""

from pathlib import Path

import crayons
import numpy as np
import yaml
from tinydb import TinyDB
from tinydb.storages import JSONStorage
from tinydb_serialization import SerializationMiddleware, Serializer


class NpSerializer(Serializer):
    """
    Serializer for numpy arrays
    """

    OBJ_CLASS = np.ndarray

    def encode(self, array):
        return array.tolist()

    def decode(self, s):
        return np.array(s)


class KramStore:
    """
    Data store for a project. A project has a directory and database files for
    experiments.
    """

    def __init__(self, root_path, project_name):
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

        # serialization = SerializationMiddleware()
        # serialization.register_serializer(NpSerializer(), "TinyNp")
