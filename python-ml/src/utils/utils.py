"""
utils.py
Stage 2: Utility functions
"""

import os
import logging
import random
import numpy as np
import pandas as pd

def setup_logger(name="AKI-ML", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger

def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)

def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)

def save_csv(df: pd.DataFrame, path: str):
    ensure_dir(os.path.dirname(path))
    df.to_csv(path, index=False)

def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)
