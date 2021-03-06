# Update : For the usbility the compatbility to give up using dask API
import json
import pickle
from shutil import ExecError
import cudf as cf
from datetime import datetime
import os
from stat import *
class ImportData:
    def __init__(self,sourcePath,targetDataBase,frameName,encoder,userAuthority,user) -> None:
        """
        The function is used to initialize the class
        
        :param sourcePath: The path to the source file
        :param targetDataBase: The name of the database you want to connect to
        :param frameName: The name of the frame that you want to create
        :param encoder: The encoder to use for the frame
        :param userAuthority: This is the authority of the user who is trying to access the data
        :param user: The user who is running the script
        """
        self.sourcePath = sourcePath
        self.targetDataBase = targetDataBase
        self.frameName = frameName
        self.encoder = encoder
        self.userAuthority = userAuthority
        self.user = user
    def Processing(self):
        """
        This function is used to import data from different source and store it in the database.
        :return: A message.
        """
        try:
            assert self.userAuthority == "Admin"
            if ".csv" in self.sourcePath:
                df = cf.read_csv(self.sourcePath,encoding=self.encoder)
                data = df.to_json(orient=True)
                df.to_pickle(f"./Data/{self.targetDataBase}/{self.frameName}.df")
                with open(f"./Data/{self.targetDataBase}/{self.frameName}.rc","wb") as recover_writter:
                    pickle.dump(f"Recover Chekup create at : {datetime.now()}\n{data}")
                recover_writter.close()
                message = {
                    "execCode":"OK",
                    "message":f"Successfully import data.",
                    "target":{self.targetDataBase}+'.'+{self.frameName},
                    'recordsCount':df.shape,
                    'checkInTime':datetime.now()
                }
                print(json.dumps(message,indent=4,ensure_ascii=True,sort_keys=True))
                return json.dumps(message)
            if ".hdf" in self.sourcePath:
                df = cf.read_hdf(self.sourcePath)
                # dask_proc = pd.from_pandas(tem)
                data = df.to_json(orient=True)
                df.to_pickle(f"./Data/{self.targetDataBase}/{self.frameName}.df")
                with open(f"./Data/{self.targetDataBase}/{self.frameName}.rc","wb") as recover_writter:
                    pickle.dump(f"Recover Chekup create at : {datetime.now()}\n{data}")
                recover_writter.close()
                message = {
                    "execCode":"OK",
                    "message":f"Successfully import data.",
                    "target":{self.targetDataBase}+'.'+{self.frameName},
                    'recordsCount':df.shape,
                    'checkInTime':datetime.now()
                }
                print(json.dumps(message,indent=4,ensure_ascii=True,sort_keys=True))
                return json.dumps(message)
            if ".json" in self.sourcePath:
                df = cf.read_json(self.sourcePath)
                # dask_proc = pd.from_pandas(tem)
                data = df.to_json(orient=True)
                df.to_pickle(f"./Data/{self.targetDataBase}/{self.frameName}.df")
                with open(f"./Data/{self.targetDataBase}/{self.frameName}.rc","wb") as recover_writter:
                    pickle.dump(f"Recover Chekup create at : {datetime.now()}\n{data}")
                recover_writter.close()
                message = {
                    "execCode":"OK",
                    "message":f"Successfully import data.",
                    "target":{self.targetDataBase}+'.'+{self.frameName},
                    'recordsCount':df.shape,
                    'checkInTime':datetime.now()
                }
                print(json.dumps(message,indent=4,ensure_ascii=True,sort_keys=True))
                return json.dumps(message)
            if os.path.exists(f"./Data/{self.targetDataBase}/{self.frameName}.rc"):
                    os.chmod(f"./Data/{self.targetDataBase}/{self.frameName}.rc",S_IREAD)
            else:
                message = {
                    "execCode":'Failed',
                    'message':'Invalid origin data types!'
                }
                print(json.dumps(message,indent=4,ensure_ascii=True,sort_keys=True))
                return "Invalid origin data type!"
        except AssertionError:
            message = {
                'execCode':'Failed',
                'message':f'Invalid user authority,expecting Admin,buy got {self.userAuthority}.'
            }
            print(json.dumps(message,indent=4,ensure_ascii=True,sort_keys=True))
            return f'Invalid user authority,expecting Admin,buy got {self.userAuthority}.'