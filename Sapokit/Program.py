import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Windows.Forms import Application
from shell import Shell

Application.EnableVisualStyles()
form = Shell()
print '\n Application is running... \n'
Application.Run(form)
