import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

from ui.loginer import Loginer
from ui.creator import Creator
from ui.importer import Importer

class Shell(Form):
    def __init__(self):
        self.InitializeComponent()
        self.load_modules()
    
    def InitializeComponent(self):
        self._tls_menus = System.Windows.Forms.ToolStrip()
        self._tsb_help = System.Windows.Forms.ToolStripButton()
        self._tbc_functions = System.Windows.Forms.TabControl()
        self._tbp_login = System.Windows.Forms.TabPage()
        self._tbp_create = System.Windows.Forms.TabPage()
        self._tbp_import = System.Windows.Forms.TabPage()
        self._sts_status = System.Windows.Forms.StatusStrip()
        self._tls_menus.SuspendLayout()
        self._tbc_functions.SuspendLayout()
        self.SuspendLayout()
        # 
        # tls_menus
        # 
        self._tls_menus.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._tsb_help]))
        self._tls_menus.Location = System.Drawing.Point(0, 0)
        self._tls_menus.Name = "tls_menus"
        self._tls_menus.Size = System.Drawing.Size(930, 25)
        self._tls_menus.TabIndex = 0
        self._tls_menus.Text = "Toolkits"
        # 
        # tsb_help
        # 
        self._tsb_help.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        self._tsb_help.ImageTransparentColor = System.Drawing.Color.Magenta
        self._tsb_help.Name = "tsb_help"
        self._tsb_help.Size = System.Drawing.Size(23, 22)
        self._tsb_help.Text = "Help"
        # 
        # tbc_functions
        # 
        self._tbc_functions.Controls.Add(self._tbp_login)
        self._tbc_functions.Controls.Add(self._tbp_create)
        self._tbc_functions.Controls.Add(self._tbp_import)
        self._tbc_functions.Location = System.Drawing.Point(0, 29)
        self._tbc_functions.Name = "tbc_functions"
        self._tbc_functions.SelectedIndex = 0
        self._tbc_functions.Size = System.Drawing.Size(930, 426)
        self._tbc_functions.TabIndex = 1
        # 
        # tbp_login
        # 
        self._tbp_login.Location = System.Drawing.Point(4, 22)
        self._tbp_login.Name = "tbp_login"
        self._tbp_login.Padding = System.Windows.Forms.Padding(3)
        self._tbp_login.Size = System.Drawing.Size(922, 400)
        self._tbp_login.TabIndex = 0
        self._tbp_login.Text = "Loginer"
        self._tbp_login.UseVisualStyleBackColor = True
        # 
        # tbp_create
        # 
        self._tbp_create.Location = System.Drawing.Point(4, 22)
        self._tbp_create.Name = "tbp_create"
        self._tbp_create.Padding = System.Windows.Forms.Padding(3)
        self._tbp_create.Size = System.Drawing.Size(922, 400)
        self._tbp_create.TabIndex = 1
        self._tbp_create.Text = "Creator"
        self._tbp_create.UseVisualStyleBackColor = True
        # 
        # tbp_import
        # 
        self._tbp_import.Location = System.Drawing.Point(4, 22)
        self._tbp_import.Name = "tbp_import"
        self._tbp_import.Padding = System.Windows.Forms.Padding(3)
        self._tbp_import.Size = System.Drawing.Size(922, 400)
        self._tbp_import.TabIndex = 2
        self._tbp_import.Text = "Importer"
        self._tbp_import.UseVisualStyleBackColor = True
        # 
        # sts_status
        # 
        self._sts_status.Location = System.Drawing.Point(0, 458)
        self._sts_status.Name = "sts_status"
        self._sts_status.Size = System.Drawing.Size(930, 22)
        self._sts_status.TabIndex = 2
        self._sts_status.Text = "statusStrip1"
        # 
        # Shell
        # 
        self.ClientSize = System.Drawing.Size(930, 480)
        self.Controls.Add(self._sts_status)
        self.Controls.Add(self._tbc_functions)
        self.Controls.Add(self._tls_menus)
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow
        self.Name = "Shell"
        self.Text = "Sapokit"
        self._tls_menus.ResumeLayout(False)
        self._tls_menus.PerformLayout()
        self._tbc_functions.ResumeLayout(False)
        self.ResumeLayout(False)
        self.PerformLayout()
    
    def load_modules(self):
        try:
            item = Loginer()
            self._tbp_login.Controls.Add(item)
            item = Creator()
            self._tbp_create.Controls.Add(item)
            item = Importer()
            self._tbp_import.Controls.Add(item)
        except Exception as e:
            MessageBox.Show(str(e))
        pass
