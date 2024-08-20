from urllib.request import urlopen
import json
import api

def requested(circuit_name,session_type):
    print(f'{circuit_name}{session_type} is requested')