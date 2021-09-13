import random
import json
import collections
from rdkit import Chem
from rdkit.Chem import Descriptors
from typing import List

from bentoml import BentoService, api, artifacts
from bentoml.adapters import JsonInput
from bentoml.service.artifacts.common import JSONArtifact
from bentoml.types import JsonSerializable


@artifacts([JSONArtifact("model")])
class Service(BentoService):
    @api(input=JsonInput(), batch=True)
    def calculate(self, input: List[JsonSerializable]):
        """
        Calculate molecular weight
        """
        input = input[0]
        output = []
        for inp in input:
            mol = Chem.MolFromSmiles(inp["input"])
            mw = Descriptors.MolWt(mol)
            output += [{"mw": mw}]
        return [output]
