import pandas as pd 
import numpy as np
import random
from sklearn.base import BaseEstimator, TransformerMixin

class Imputer(BaseEstimator,TransformerMixin):
	def __init__(self,variable):
		self.variable = variable
		self.mean = 0
		self.median =0
		self.mode=0

	def fit(self,X):
		self.mean=X.mean()
		self.median=X.median()
		self.mode=X.mode()

		return self

	def impute(self,cols):
		r=[self.mean,self.median,self.mode]
		if pd.isnull(cols):
			return random.choices(r)[0]
		return cols


	def transform(self,X):
		Y=X.copy()
		Y[self.variable]=Y[self.variable].apply(self.impute)
		return Y[self.variable]