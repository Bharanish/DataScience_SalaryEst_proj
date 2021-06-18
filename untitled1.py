# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:52:07 2021

@author: Harshi
"""

import glassdoor_scrapper as gs
import pandas as pd

path = "D:/BharanishKumar/Projects/DataScience_SalaryEst/chromedriver"
df = gs.get_jobs('data scientist', 15, False, path, 15)