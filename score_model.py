import pickle, csv, pandas as pd
from train_model import prepareData
from sklearn.metrics import classification_report

MyModelFile="MuthkumarSrinivasanModelFile.pkl"

#Step 2a of Main Program
def readCSVfiles():
    try:
        test_df = pd.read_csv("test.csv")
        X_test = pd.read_csv("x_test.csv")
        y_test = pd.read_csv("y_test.csv")
    except:
        print("Could not read files")
    
    X_test.drop(X_test.columns[[0]], axis=1, inplace=True)
    y_test.drop(y_test.columns[[0]], axis=1, inplace=True)
    X_test.drop(X_test.index[0], inplace=True)
    return([X_test, y_test, test_df])

###Step2b - of Main program

def readModelFile(file):
    try:
     	p = open(file, 'rb')
     	openedModel = pickle.load(p)
    except:
       	print("Could not open", file)
    return(openedModel)

#### Step 2 

def main():
    ##Step-2a - read all CSV Files
    X_test, y_test, test_df = readCSVfiles()
    print(X_test)	
    ##Step-2b - read model file 
    myModel=readModelFile(MyModelFile)
    print(myModel)
  
    ## Calculate Score
    calScoreXY=myModel.score(X_test,y_test)
    print (calScoreXY)


####### Step 1 - Load Main ()

if  __name__ =='__main__':
    main()