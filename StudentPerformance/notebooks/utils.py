# utils.py

import pandas as pd

def load_student_data(filepath='../data/StudentsPerformance.csv'):
    df = pd.read_csv(filepath)

    # Feature Engineering
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
    df['performance_level'] = pd.cut(df['average_score'], bins=[0, 60, 80, 100], labels=['Low', 'Medium', 'High'])
    df['performance_label'] = df['performance_level'].map({'Low': 0, 'Medium': 1, 'High': 2})

    return df