
import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *
from biz import *
from biz.sbo_company import SBOCompany
from biz.sbo_application import SBOApplication

__all__ = ['Loginer'
]

class Loginer(UserControl):
    def __init__(self):
        self.InitializeComponent()
        self._company = None
        self._application = None
        self.initialize()
        self._rbtn_byUI.Checked = True
        pass
    
    def InitializeComponent(self):
        self._gpb_login = System.Windows.Forms.GroupBox()
        self._rbtn_byUI = System.Windows.Forms.RadioButton()
        self._rbtn_byDI = System.Windows.Forms.RadioButton()
        self._gpb_loginMode = System.Windows.Forms.GroupBox()
        self._gpb_loginInfo = System.Windows.Forms.GroupBox()
        self._cmb_dbServerType = System.Windows.Forms.ComboBox()
        self._txt_dbUser = System.Windows.Forms.TextBox()
        self._txt_dbServer = System.Windows.Forms.TextBox()
        self._txt_dbPassword = System.Windows.Forms.TextBox()
        self._btn_refresh = System.Windows.Forms.Button()
        self._txt_licenseServer = System.Windows.Forms.TextBox()
        self._txt_user = System.Windows.Forms.TextBox()
        self._txt_password = System.Windows.Forms.TextBox()
        self._btn_connect = System.Windows.Forms.Button()
        self._btn_disconnect = System.Windows.Forms.Button()
        self._dgv_companys = System.Windows.Forms.DataGridView()
        self._col_companyDB = System.Windows.Forms.DataGridViewTextBoxColumn()
        self._col_companyName = System.Windows.Forms.DataGridViewTextBoxColumn()
        self._gpb_login.SuspendLayout()
        self._gpb_loginMode.SuspendLayout()
        self._gpb_loginInfo.SuspendLayout()
        self._dgv_companys.BeginInit()
        self.SuspendLayout()
        # 
        # gpb_login
        # 
        self._gpb_login.Controls.Add(self._gpb_loginInfo)
        self._gpb_login.Controls.Add(self._gpb_loginMode)
        self._gpb_login.Location = System.Drawing.Point(3, 3)
        self._gpb_login.Name = "gpb_login"
        self._gpb_login.Size = System.Drawing.Size(900, 380)
        self._gpb_login.TabIndex = 0
        self._gpb_login.TabStop = False
        self._gpb_login.Text = "Login"
        # 
        # rbtn_byUI
        # 
        self._rbtn_byUI.Location = System.Drawing.Point(6, 20)
        self._rbtn_byUI.Name = "rbtn_byUI"
        self._rbtn_byUI.Size = System.Drawing.Size(104, 24)
        self._rbtn_byUI.TabIndex = 0
        self._rbtn_byUI.TabStop = True
        self._rbtn_byUI.Text = "By UI"
        self._rbtn_byUI.UseVisualStyleBackColor = True
        self._rbtn_byUI.CheckedChanged += self.Rbtn_byUICheckedChanged
        # 
        # rbtn_byDI
        # 
        self._rbtn_byDI.Location = System.Drawing.Point(6, 50)
        self._rbtn_byDI.Name = "rbtn_byDI"
        self._rbtn_byDI.Size = System.Drawing.Size(104, 24)
        self._rbtn_byDI.TabIndex = 1
        self._rbtn_byDI.TabStop = True
        self._rbtn_byDI.Text = "By DI"
        self._rbtn_byDI.UseVisualStyleBackColor = True
        self._rbtn_byDI.CheckedChanged += self.Rbtn_byDICheckedChanged
        # 
        # gpb_loginMode
        # 
        self._gpb_loginMode.Controls.Add(self._rbtn_byDI)
        self._gpb_loginMode.Controls.Add(self._rbtn_byUI)
        self._gpb_loginMode.Location = System.Drawing.Point(8, 21)
        self._gpb_loginMode.Name = "gpb_loginMode"
        self._gpb_loginMode.Size = System.Drawing.Size(200, 341)
        self._gpb_loginMode.TabIndex = 2
        self._gpb_loginMode.TabStop = False
        self._gpb_loginMode.Text = "Login Mode"
        # 
        # gpb_loginInfo
        # 
        self._gpb_loginInfo.Controls.Add(self._btn_disconnect)
        self._gpb_loginInfo.Controls.Add(self._btn_connect)
        self._gpb_loginInfo.Controls.Add(self._txt_password)
        self._gpb_loginInfo.Controls.Add(self._txt_user)
        self._gpb_loginInfo.Controls.Add(self._txt_licenseServer)
        self._gpb_loginInfo.Controls.Add(self._dgv_companys)
        self._gpb_loginInfo.Controls.Add(self._btn_refresh)
        self._gpb_loginInfo.Controls.Add(self._txt_dbPassword)
        self._gpb_loginInfo.Controls.Add(self._txt_dbServer)
        self._gpb_loginInfo.Controls.Add(self._txt_dbUser)
        self._gpb_loginInfo.Controls.Add(self._cmb_dbServerType)
        self._gpb_loginInfo.Location = System.Drawing.Point(215, 21)
        self._gpb_loginInfo.Name = "gpb_loginInfo"
        self._gpb_loginInfo.Size = System.Drawing.Size(679, 341)
        self._gpb_loginInfo.TabIndex = 3
        self._gpb_loginInfo.TabStop = False
        self._gpb_loginInfo.Text = "Login Info"
        # 
        # cmb_dbServerType
        # 
        self._cmb_dbServerType.FormattingEnabled = True
        self._cmb_dbServerType.Location = System.Drawing.Point(7, 20)
        self._cmb_dbServerType.Name = "cmb_dbServerType"
        self._cmb_dbServerType.Size = System.Drawing.Size(150, 20)
        self._cmb_dbServerType.TabIndex = 0
        # 
        # txt_dbUser
        # 
        self._txt_dbUser.Location = System.Drawing.Point(7, 46)
        self._txt_dbUser.Name = "txt_dbUser"
        self._txt_dbUser.Size = System.Drawing.Size(150, 21)
        self._txt_dbUser.TabIndex = 1
        self._txt_dbUser.Text = "sa"
        # 
        # txt_dbServer
        # 
        self._txt_dbServer.Location = System.Drawing.Point(163, 19)
        self._txt_dbServer.Name = "txt_dbServer"
        self._txt_dbServer.Size = System.Drawing.Size(200, 21)
        self._txt_dbServer.TabIndex = 2
        self._txt_dbServer.Text = "(local)"
        # 
        # txt_dbPassword
        # 
        self._txt_dbPassword.Location = System.Drawing.Point(163, 46)
        self._txt_dbPassword.Name = "txt_dbPassword"
        self._txt_dbPassword.PasswordChar = "*"
        self._txt_dbPassword.Size = System.Drawing.Size(200, 21)
        self._txt_dbPassword.TabIndex = 3
        # 
        # btn_refresh
        # 
        self._btn_refresh.Location = System.Drawing.Point(369, 19)
        self._btn_refresh.Name = "btn_refresh"
        self._btn_refresh.Size = System.Drawing.Size(75, 48)
        self._btn_refresh.TabIndex = 4
        self._btn_refresh.Text = "Refresh"
        self._btn_refresh.UseVisualStyleBackColor = True
        self._btn_refresh.Click += self.Btn_refreshClick
        # 
        # txt_licenseServer
        # 
        self._txt_licenseServer.Location = System.Drawing.Point(450, 73)
        self._txt_licenseServer.Name = "txt_licenseServer"
        self._txt_licenseServer.Size = System.Drawing.Size(223, 21)
        self._txt_licenseServer.TabIndex = 6
        self._txt_licenseServer.Text = "localhost:30000"
        # 
        # txt_user
        # 
        self._txt_user.Location = System.Drawing.Point(450, 100)
        self._txt_user.Name = "txt_user"
        self._txt_user.Size = System.Drawing.Size(100, 21)
        self._txt_user.TabIndex = 7
        self._txt_user.Text = "manager"
        # 
        # txt_password
        # 
        self._txt_password.Location = System.Drawing.Point(556, 100)
        self._txt_password.Name = "txt_password"
        self._txt_password.PasswordChar = "*"
        self._txt_password.Size = System.Drawing.Size(116, 21)
        self._txt_password.TabIndex = 8
        self._txt_password.Text = "avatech"
        # 
        # btn_connect
        # 
        self._btn_connect.Location = System.Drawing.Point(449, 127)
        self._btn_connect.Name = "btn_connect"
        self._btn_connect.Size = System.Drawing.Size(101, 23)
        self._btn_connect.TabIndex = 9
        self._btn_connect.Text = "Connect"
        self._btn_connect.UseVisualStyleBackColor = True
        self._btn_connect.Click += self.Btn_connectClick
        # 
        # btn_disconnect
        # 
        self._btn_disconnect.Location = System.Drawing.Point(556, 127)
        self._btn_disconnect.Name = "btn_disconnect"
        self._btn_disconnect.Size = System.Drawing.Size(117, 23)
        self._btn_disconnect.TabIndex = 10
        self._btn_disconnect.Text = "Disconnect"
        self._btn_disconnect.UseVisualStyleBackColor = True
        self._btn_disconnect.Click += self.Btn_disconnectClick
        # 
        # dgv_companys
        # 
        self._dgv_companys.AllowDrop = True
        self._dgv_companys.AllowUserToAddRows = False
        self._dgv_companys.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        self._dgv_companys.Columns.AddRange(System.Array[System.Windows.Forms.DataGridViewColumn](
            [self._col_companyDB,
            self._col_companyName]))
        self._dgv_companys.Location = System.Drawing.Point(7, 73)
        self._dgv_companys.MultiSelect = False
        self._dgv_companys.Name = "dgv_companys"
        self._dgv_companys.RowTemplate.Height = 23
        self._dgv_companys.Size = System.Drawing.Size(437, 262)
        self._dgv_companys.TabIndex = 5
        # 
        # col_companyDB
        # 
        self._col_companyDB.HeaderText = "CompanyDB"
        self._col_companyDB.Name = "col_companyDB"
        self._col_companyDB.ReadOnly = True
        self._col_companyDB.Width = 150
        # 
        # col_companyName
        # 
        self._col_companyName.HeaderText = "CompanyName"
        self._col_companyName.Name = "col_companyName"
        self._col_companyName.ReadOnly = True
        self._col_companyName.Width = 250
        # 
        # Login
        # 
        self.Controls.Add(self._gpb_login)
        self.Name = "Login"
        self.Size = System.Drawing.Size(910, 390)
        self._gpb_login.ResumeLayout(False)
        self._gpb_loginMode.ResumeLayout(False)
        self._gpb_loginInfo.ResumeLayout(False)
        self._gpb_loginInfo.PerformLayout()
        self._dgv_companys.EndInit()
        self.ResumeLayout(False)

    def Btn_refreshClick(self, sender, e):
        try:
            companys = self._company.get_company_dbs(self._txt_dbPassword.Text,\
            self._txt_dbUser.Text,self._txt_dbServer.Text)
            self._dgv_companys.Rows.Clear()
            if companys is not None:
                if companys.Rows.Count > 0:
                    for row in companys.Rows:
                        self._dgv_companys.Rows.Add();
                        self._dgv_companys.Rows[self._dgv_companys.Rows.Count - 1].Cells['col_CompanyDB'].Value = row['CompanyDB']
                        self._dgv_companys.Rows[self._dgv_companys.Rows.Count - 1].Cells['col_CompanyName'].Value = row['CompanyName']
                    self._dgv_companys.Rows[0].Selected = True
        except Exception as e:
            MessageBox.Show(str(e))
        pass
    
    def Btn_connectClick(self, sender, e):
        try:
            if self._rbtn_byUI.Checked:
                cmp = self._application.get_b1_company()
                self._company.set_b1_compay(cmp)
                error = '%s is connected!' % cmp.CompanyName
            else:
                if self._dgv_companys.SelectedRows.Count <= 0:
                    error = 'Please select the company to login!'
                else:
                    server_type = BoDataServerTypes[self._cmb_dbServerType.SelectedItem]
                    company_db = self._dgv_companys.SelectedRows[0].Cells['col_CompanyDB'].Value
                    error = self._company.connect_b1(server_type,self._txt_dbPassword.Text,company_db,\
                    self._txt_dbUser.Text,self._txt_dbServer.Text,self._txt_licenseServer.Text,\
                    self._txt_user.Text,self._txt_password.Text)
            MessageBox.Show(error)
        except Exception as e:
            MessageBox.Show(str(e))
        finally:
            pass
        pass
    
    def Btn_disconnectClick(self, sender, e):
        try:
            self._company.disconnect_b1()
            MessageBox.Show('Company is disconnected!')
        except Exception as e:
            MessageBox.Show(str(e))
        pass
    
    def Rbtn_byUICheckedChanged(self, sender, e):
#        self._gpb_loginInfo.Enabled = False if self._rbtn_byUI.Checked else True
        self.set_items_enabled(False if self._rbtn_byUI.Checked else True)
        pass

    def Rbtn_byDICheckedChanged(self, sender, e):
#        self._gpb_loginInfo.Enabled = True if self._rbtn_byDI.Checked else False
        self.set_items_enabled(True if self._rbtn_byDI.Checked else False)
        pass
    
    def initialize(self):
        self.load_database_types()
        if self._company is None:
            self._company = SBOCompany()
        if self._application is None:
            self._application = SBOApplication()
        pass
    
    def load_database_types(self):
        try:
            for item in BoDataServerTypes :
                self._cmb_dbServerType.Items.Add(item)
            if self._cmb_dbServerType.Items.Count > 0:
                self._cmb_dbServerType.SelectedIndex = 0
        except Exception as e:
            MessageBox.Show(str(e))
        pass
    
    def set_items_enabled(self,enabled=True):
        try:
            self._cmb_dbServerType.Enabled = enabled
            self._txt_dbUser.Enabled = enabled
            self._txt_dbServer.Enabled = enabled
            self._txt_dbPassword.Enabled = enabled
            self._btn_refresh.Enabled = enabled
            self._txt_licenseServer.Enabled = enabled
            self._txt_user.Enabled = enabled
            self._txt_password.Enabled = enabled
            self._dgv_companys.Enabled = enabled
        except Exception as e:
            MessageBox.Show(str(e))
        pass
    