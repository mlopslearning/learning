import os
import yaml
import pandas as pd
import numpy as np
import argparse
from pkgutil import get_data
from get_data import get_data, read_param
from sklearn.model_selection import train_test_split
from sklearn.metrics import median_absolute_error,mean_squared_error,r2_score
from sklearn.linear_model import ElasticNet
import joblib
import json
import mlflow
from urllib.parse import urlparse

def train_and_eval(config):






if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yml")
    parsed_args= args.parse_args()
    train_and_eval(config_path=parsed_args.config)