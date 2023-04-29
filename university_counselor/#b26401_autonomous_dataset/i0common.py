import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data
