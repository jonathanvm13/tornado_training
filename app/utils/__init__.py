import json, logging

LOGGER = logging.getLogger("app")

def parseJson(body):
    """
    Parsear el JSON
    """
    jsonDictionary = json.loads(body)
    return jsonDictionary
