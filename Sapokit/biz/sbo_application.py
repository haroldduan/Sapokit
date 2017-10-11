
import sys,clr,System
print '\nLoad module names [SAPbobsCOM]... \n' 
current_path = System.AppDomain.CurrentDomain.BaseDirectory
# Output the app path
print '\nThis current application path: \n %s\n' % current_path 
sys.path.append(current_path)
# Output the sys path
print 'This current system envs path: \n %s' % sys.path
clr.AddReferenceToFileAndPath('.\DLLs\Interop.SAPbouiCOM.dll')
from SAPbouiCOM import *

class SBOApplication:
    def __init__(self):
        self._application = None
        pass
    
    def __b1_connect(self):
        try:
            if self._application is None:
                sbo_gui_api = SboGuiApiClass()
                connect_string = '0030002C0030002C00530041005000420044005F00440061007400650076002C0050004C006F006D0056004900490056'
                sbo_gui_api.Connect(connect_string);
                self._application = sbo_gui_api.GetApplication(0);
        except Exception as e:
            raise e
        pass
    
    def get_b1_application(self):
        try:
            if self._application is None:
                __b1_connect()
            return self._application
        except Exception as e:
            raise e
        pass
    
    def get_b1_company(self):
        try:
            if self._application is None:
               self.__b1_connect()
            return self._application.Company.GetDICompany()
        except Exception as e:
            raise e
        pass
    
