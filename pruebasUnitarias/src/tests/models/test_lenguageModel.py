
from src.models.lenguageModel  import LenguageModel

def test_get_lenguages_not_none():
     lenguages = LenguageModel.getLenguage
     assert lenguages != None
