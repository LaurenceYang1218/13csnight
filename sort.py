import pandas as pd

def main():
    df = pd.read_csv('data.csv')
    df = df.sort_values(by=['score'], ascending=False)
    df = df.reset_index(drop=True)
    df.to_csv('sort.csv', index=False)
    
if __name__ == '__main__':
    main()