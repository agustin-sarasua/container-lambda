import sys
import pandas as pd

def handler(event, context): 
    return 'Hello from AWS Lambda using Python' + sys.version + '!'