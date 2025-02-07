import os
import yaml
import pandas as pd
import numpy as np
import argparse
from pkgutil import get_data

def get_data(config_path):
    config = read_param(config_path)
    #print(config_path)
    data_path = config["load_data"]["clean_data"]
    df = pd.read_csv(data_path, sep=',', encoding='utf-8')
    #print(df)
    return df

def read_param(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
        return config




if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yml")
    parsed_args= args.parse_args()
    data = get_data(config_path=parsed_args.config)