
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from biz import *
from biz.sbo_company import SBOCompany

__all__ = ['Importer'
]

class Importer(UserControl):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self.SuspendLayout()
        # 
        # Importer
        # 
        self.Name = "Importer"
        self.Size = System.Drawing.Size(910, 390)
        self.ResumeLayout(False)

