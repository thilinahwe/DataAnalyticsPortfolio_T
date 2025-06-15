import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'notebooks')))

import pandas as pd
from utils import load_student_data

# Load cleaned, feature-engineered data
df = load_student_data()

# Export to CSV
export_path = "../data/StudentPerformance_Tableau.csv"
df.to_csv(export_path, index=False)
print(f"Exported to {export_path}")