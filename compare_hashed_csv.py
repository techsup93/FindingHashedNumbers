import hashlib
import pandas as pd


# Step0: Create a Sample Hashed CSV file 0-20

def hashedNUM_csv():
    with open('hashed.csv', 'w+') as f:
        f.write("Col0" + "," + "Col1" + '\n')
        for step in range(0, 20):
            message = str(step).encode()
            hashed = hashlib.sha256(message).hexdigest()
            print("SHA-256:", hashed)
            f.write(str(step) + "," + str(hashed) + '\n')
        f.close()


# Step1: Create a Sample Hashed CSV file Student Grades

def hashedGRD_csv():
    data2 = {"Col0": ["Michael", "Freddie", "Avril", "Tupac", "Unknown", "Napoleon"],
             "Col1": ['9400f1b21cb527d7fa3d3eabba93557a18ebe7a2ca4e471cfe5e4c5b4ca7f767',
                      'f5ca38f748a1d6eaf726b8a42fb575c3c71f1864a8143301782de13da2d9202b',
                      '4523540f1504cd17100c4835e85b7eefd49911580f8efff0599a8f283be6b9e3',
                      'b17ef6d19c7a5b1ee83b907c595526dcb1eb06db8227d650d5dda0a9f4ce8cd9',
                      'D56ef6d19c7a5b1ee83b907c595521334b06db8227d650d5dda0a9f42w2356',
                      '6b51d431df5d7f141cbececcf79edf3dd861c3b4069f0b11661a3eefacbba918']}
    df2 = pd.DataFrame(data2)
    df2.to_csv("grades.csv", index=None)
    print((df2['Col0'] + " with grade: " + df2['Col1']))


# Step2: Read CSV Files

def readCOMP_csv():
    data1 = pd.read_csv('hashed.csv')
    data2 = pd.read_csv('grades.csv')
    d1frame = pd.DataFrame(data1, columns=['Col0', 'Col1'])
    d2frame = pd.DataFrame(data2, columns=['Col0', 'Col1'])

    # Step3: Compare CSV Files & Print

    print(d1frame[d1frame.Col1.isin(d2frame.Col1)].sort_values(by=['Col1'], axis=0, ascending=False))
    print(d2frame[d2frame.Col1.isin(d1frame.Col1)].sort_values(by=['Col1'], axis=0, ascending=False))


#Call Functions Section:

hashedNUM_csv()
hashedGRD_csv()
readCOMP_csv()
