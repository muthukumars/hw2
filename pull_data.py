import os
import requests

credentialFile='login.txt'
url1 = 'https://www.kaggle.com/c/titanic/download/train.csv'
url2 = 'https://www.kaggle.com/c/titanic/download/test.csv'
trainFile ='train.csv'
testFile = 'test.csv'
#Function reads file, takes in file name as argument, returns list of lines
def readingCredentialFile(filename):
        try:
                file=open(filename,'r')
                lines = file.read()
                splitLines = lines.splitlines()
                #####------------print(lines)
        except:
                print("Something wrong reading file")
        return(splitLines)


def downloadFile(downFile,url,usr,pwd):
        print(downFile)
        print(url)
        print(usr)
        print(pwd)
        r = requests.get(url)
        print(r.status_code)
        payload= {'UserName': usr, 'Password': pwd}
        r = requests.post(r.url,data=payload)
        print(r.text)
        f = open(downFile, 'wb')
        f.write(r.content)
        f.close()

def main():

        if os.path.exists(credentialFile):
                credentialsRead = readingCredentialFile(credentialFile)
                print("01-Credential File exists")

                userid,password=credentialsRead
                print(userid)
                print(password);
                downloadFile(trainFile, url1, userid,password)
                downloadFile(testFile,url2,userid,password)
        else:
                print('file does not exists')

if  __name__ =='__main__':
    main()