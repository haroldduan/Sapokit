
import sys,clr,System
clr.AddReference('System.Data')
from System.Data import *
from System.Data.SqlClient import *
print '\nLoad module names [SAPbobsCOM]... \n' 
current_path = System.AppDomain.CurrentDomain.BaseDirectory
# Output the app path
print '\nThis current application path: \n %s\n' % current_path 
sys.path.append(current_path)
# Output the sys path
print 'This current system envs path: \n %s' % sys.path
clr.AddReferenceToFileAndPath('.\DLLs\Interop.SAPbobsCOM.dll')
from SAPbobsCOM import *

class SBOCompany:
    def __init__(self):
        self._company = None
        if self._company is None:
            self._company = CompanyClass()
        pass
    
    def get_company_dbs(self,password,user='sa',server='127.0.0.1',*args, **kw):
        try:
            connect_string = 'Data Source={0};Initial Catalog=SLDModel.SLDData;' \
            'Persist Security Info=True;User ID={1};Password={2};'
            query_string = 'select N\'N\' "Choosed","Name" "CompanyDB","CompanyName" from "CompanyDBs" '
            connect_string = connect_string.format(server,user,password)
            sql_conn = SqlConnection(connect_string)
            sql_conn.Open()
            data_adapter = SqlDataAdapter(query_string, sql_conn)
            data_set = DataSet();
            data_adapter.Fill(data_set, "companys")
            table = data_set.Tables["companys"]
            sql_conn.Close()
            return table
        except Exception as e:
            raise e
        pass
    
    def connect_b1(self,db_server_type,db_password,company_db,db_user='sa',db_server='127.0.0.1',\
    license_server='127.0.0.1:30000',user='manager',password='manager',\
    *args, **kw):
        try:
            if self._company is None:
                self._company = CompanyClass()
            if not self._company.Connected:
                self._company.LicenseServer = license_server
                self._company.Server = db_server
                self._company.DbServerType = db_server_type
                self._company.CompanyDB = company_db
                self._company.DbUserName = db_user
                self._company.DbPassword = db_password
                self._company.UserName = user
                self._company.Password = password
                self._company.UseTrusted = False
                error_code = self._company.Connect()
                error = '%s is connected!' % self._company.CompanyName \
                if error_code == 0 else self._company.GetLastErrorDescription()
            else:
                error = '%s is connected!' % self._company.CompanyName
            return error
        except Exception as e:
            raise e
        finally:
            pass
        pass
    
    def get_b1_company(self):
        ret_val = None
        if self._company is not None:
            if self._company.Connected:
                ret_val = self._company
        return ret_val
        pass
    
    def set_b1_compay(self,b1_company):
        try:
            if b1_company is None:
                raise Exception('b1_company is invalid!')
            if self._company is not None:
                self._company = None
            self._company = b1_company
        except Exception as e:
            raise e
        pass
    
    def disconnect_b1(self):
        try:
            if self._company is not None:
                if self._company.Connected:
                    self._company.Disconnect()
        except Exception as e:
            raise e
        pass
