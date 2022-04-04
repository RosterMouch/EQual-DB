# Update : For the usbility the compatbility to give up using dask API
from email import message
import imp
import pickle
from shutil import ExecError
import pandas as pd
from datetime import datetime
import os
from stat import *
class ImportData:
    def __init__(self,sourcePath,targetDataBase,frameName,encoder,userAuthority,user) -> None:
        self.sourcePath = sourcePath
        self.targetDataBase = targetDataBase
        self.frameName = frameName
        self.encoder = encoder
        self.userAuthority = userAuthority
        self.user = user
    def Processing(self):
        if self.userAuthority == "Admin":
            if ".csv" in self.sourcePath:
                df = pd.read_csv(self.sourcePath,encoding=self.encoder)
                data = df.to_json(orient=True)
                df.to_pickle(f"./Data/{self.targetDataBase}/{self.frameName}.df")
                with open(f"./Data/{self.targetDataBase}/{self.frameName}.rc","wb") as recover_writter:
                    pickle.dump(f"Recover Chekup create at : {datetime.now()}\n{data}")
                recover_writter.close()
                message = f"Successfully import data from {self.sourcePath} and storage at {self.targetDataBase}.{self.frameName},imported by {self.user}"
                return message
            if ".excel" in self.sourcePath:
                df = pd.read_excel(self.sourcePath,enconding=self.encoder)
                data = df.to_json(orient=True)
                df.to_pickle(f"./Data/{self.targetDataBase}/{self.frameName}.df")
                with open(f"./Data/{self.targetDataBase}/{self.frameName}.rc","wb") as recover_writter:
                    pickle.dump(f"Recover Chekup create at : {datetime.now()}\n{data}")
                recover_writter.close()
                message = f"Successfully import data from {self.sourcePath} and storage at {self.targetDataBase}.{self.frameName},imported by {self.user}"
                return message
            if "http://" in self.sourcePath:
                df = pd.read_html(self.sourcePath)[0]
                # dask_proc = pd.from_pandas(tem)
                data = df.to_json(orient=True)
                df.to_pickle(f"./Data/{self.targetDataBase}/{self.frameName}.df")
                with open(f"./Data/{self.targetDataBase}/{self.frameName}.rc","wb") as recover_writter:
                    pickle.dump(f"Recover Chekup create at : {datetime.now()}\n{data}")
                recover_writter.close()
                message = f"Successfully import data from {self.sourcePath} and storage at {self.targetDataBase}.{self.frameName},imported by {self.user}"
                return message
            if ".sql" in self.sourcePath:
                df = pd.read_sql(self.sourcePath)
                # dask_proc = pd.from_pandas(tem)
                data = df.to_json(orient=True)
                df.to_pickle(f"./Data/{self.targetDataBase}/{self.frameName}.df")
                with open(f"./Data/{self.targetDataBase}/{self.frameName}.rc","wb") as recover_writter:
                    pickle.dump(f"Recover Chekup create at : {datetime.now()}\n{data}")
                recover_writter.close()
                message = f"Successfully import data from {self.sourcePath} and storage at {self.targetDataBase}.{self.frameName},imported by {self.user}"
                return message
            if os.path.exists(f"./Data/{self.targetDataBase}/{self.frameName}.rc"):
                    os.chmod(f"./Data/{self.targetDataBase}/{self.frameName}.rc",S_IREAD)
            else:
                raise TypeError("Unsupported source datatype,refused!")
        else:
            raise ExecError("ERR : Not as a Adminer to do operation,refused!")