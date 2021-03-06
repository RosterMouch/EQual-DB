import json
import os
from shutil import ExecError
import cudf as cf
import pickle
class DataFrameRecover:
    def __init__(self,targetDataBase,targetDataFrame,authority,user) -> None:
        '''This function is used to initialize the class
        
        Parameters
        ----------
        targetDataBase
            The name of the database to which you want to write the data.
        targetDataFrame
            The name of the dataframe that you want to be imported into the database.
        authority
            The authority of the user.
        
        '''
        self.targetDataBase = targetDataBase
        self.targetDataFrame = targetDataFrame
        self.authority = authority
        self.user = user
    def Recovering(self):
        '''
        Return
        -------
            a message that the operation was done.
        
        '''
        login_user_sys = os.popen("whoami").read().replace("\n", "")
        login_user_sys_authority = (
            os.popen(f"groups {login_user_sys}").read().replace(f"{login_user_sys} : ", "").split(" ")
        )
        try:
            assert self.authority == "Admin" & "sudo" in login_user_sys_authority
            with open(f"./Data/{self.targetDataBase}/{self.targetDataFrame}.rc","w") as RecoverReader:
                read_data = pickle.load(RecoverReader).split("\n","")
                RecoverData = read_data[1]
            df = cf.DataFrame(RecoverData)
            df.to_pickle(f"./Data/{self.targetDataBase}/{self.targetDataFrame}.df")
            rollBackData = read_data[0][read_data.index(":") : ].replace(" ","")
            message = {
                "execCode":"OK",
                "message":f"{self.targetDataFrame} were roll back",
                "rollBackData":rollBackData
            }
            print(json.dumps(message,indent=4,ensure_ascii=True,sort_keys=True))
            return f"{self.targetDataBase}.{self.targetDataFrame} has been roll back to {rollBackData} by {self.user}"
        except AssertionError:
            message = {
                "execCode":"Failed",
                "message":f"You don't have the authority to do this operation!"
            }
            print(json.dumps(message,indent=4,ensure_ascii=True,sort_keys=True))
            return f"{self.user} has trying to roll back dataframe {self.targetDataBase}.{self.targetDataFrame} to {rollBackData} but failed!"
