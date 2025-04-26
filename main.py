import pandas as pd
import random
import string
from wilson import wilson_lower_bound

def generate_random_data(num_rows):
    """
    Generates random data with three columns: random hex, positive (bool), negative (bool).
    """
    data = []
    for _ in range(num_rows):  
        positive = random.randint(0, 100)
        negative = random.randint(0, 100)
        data.append([positive, negative])
    return data

def main():
    """
    Generates random data, calculates Wilson lower bound for each row, and prints the results.
    """
    num_rows = 2000
    data = generate_random_data(num_rows)
    df = pd.DataFrame(data, columns=['positive', 'negative'])
    df['total_count'] = df['positive'] + df['negative']
    df['wilson_score'] = df.apply(lambda row: wilson_lower_bound(row['positive'], row['total_count'],confidence=0.95), axis=1)
    # print(df)

    df.to_csv('wilson_score_95.csv', index=False)

    num_rows = 400
    data = generate_random_data(num_rows)
    df = pd.DataFrame(data, columns=['positive', 'negative'])
    df['total_count'] = df['positive'] + df['negative']
    df['wilson_score'] = df.apply(lambda row: wilson_lower_bound(row['positive'], row['total_count'],confidence=0.95), axis=1)
    # print(df)

    df.to_csv('wilson_score_95_test.csv', index=False)

if __name__ == "__main__":
    main()
