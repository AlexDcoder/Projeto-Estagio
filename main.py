import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Analise:
    def __init__(self, data: str):
        self.data = pd.read_csv(data, sep=';')

    def calcular_valores(self):
        pass

    def generate_graphs(self):
        pass

    def generate_report(self):
        pass
