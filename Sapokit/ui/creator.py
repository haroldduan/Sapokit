
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from biz import *
from biz.sbo_company import SBOCompany

__all__ = ['Creator',
    'BoDataStructureTypes'
]

BoDataStructureTypes = {
    'System' : 1,
    'User-Defined' : 2
}

class Creator(UserControl):
    def __init__(self):
        self.InitializeComponent()
        self.initialize()
    
    def InitializeComponent(self):
        treeNode16 = System.Windows.Forms.TreeNode("Node1")
        treeNode17 = System.Windows.Forms.TreeNode("Node2")
        treeNode18 = System.Windows.Forms.TreeNode("Node4")
        treeNode19 = System.Windows.Forms.TreeNode("Node3", System.Array[System.Windows.Forms.TreeNode](
            [treeNode18]))
        treeNode110 = System.Windows.Forms.TreeNode("Node0", System.Array[System.Windows.Forms.TreeNode](
            [treeNode16,
            treeNode17,
            treeNode19]))
        self._rbtn_bySystem = System.Windows.Forms.RadioButton()
        self._rbtn_byLocal = System.Windows.Forms.RadioButton()
        self._pnl_modes = System.Windows.Forms.Panel()
        self._txt_localPath = System.Windows.Forms.TextBox()
        self._btn_getLocalPath = System.Windows.Forms.Button()
        self._gbx_tree = System.Windows.Forms.GroupBox()
        self._cmbx_structureTypes = System.Windows.Forms.ComboBox()
        self._tvw_tree = System.Windows.Forms.TreeView()
        self._btn_add = System.Windows.Forms.Button()
        self._btn_delete = System.Windows.Forms.Button()
        self._btn_edit = System.Windows.Forms.Button()
        self._btn_pull = System.Windows.Forms.Button()
        self._btn_push = System.Windows.Forms.Button()
        self._gbx_contents = System.Windows.Forms.GroupBox()
        self._cmbx_objtypes = System.Windows.Forms.ComboBox()
        self._lab_title = System.Windows.Forms.Label()
        self._txt_title = System.Windows.Forms.TextBox()
        self._txt_desc = System.Windows.Forms.TextBox()
        self._lab_desc = System.Windows.Forms.Label()
        self._lab_type = System.Windows.Forms.Label()
        self._cmbx_type = System.Windows.Forms.ComboBox()
        self._txt_len = System.Windows.Forms.TextBox()
        self._lab_len = System.Windows.Forms.Label()
        self._cmbx_structure = System.Windows.Forms.ComboBox()
        self._lab_structure = System.Windows.Forms.Label()
        self._cmbx_validation = System.Windows.Forms.ComboBox()
        self._lab_validation = System.Windows.Forms.Label()
        self._ckbx_defValue = System.Windows.Forms.CheckBox()
        self._ckbx_manField = System.Windows.Forms.CheckBox()
        self._txt_defValue = System.Windows.Forms.TextBox()
        self._btn_ok = System.Windows.Forms.Button()
        self._btn_cancel = System.Windows.Forms.Button()
        self._dgv_validValues = System.Windows.Forms.DataGridView()
        self._btn_new = System.Windows.Forms.Button()
        self._btn_remove = System.Windows.Forms.Button()
        self._Value = System.Windows.Forms.DataGridViewTextBoxColumn()
        self._Description = System.Windows.Forms.DataGridViewTextBoxColumn()
        self._pnl_modes.SuspendLayout()
        self._gbx_tree.SuspendLayout()
        self._gbx_contents.SuspendLayout()
        self._dgv_validValues.BeginInit()
        self.SuspendLayout()
        # 
        # rbtn_bySystem
        # 
        self._rbtn_bySystem.Location = System.Drawing.Point(263, 3)
        self._rbtn_bySystem.Name = "rbtn_bySystem"
        self._rbtn_bySystem.Size = System.Drawing.Size(122, 24)
        self._rbtn_bySystem.TabIndex = 0
        self._rbtn_bySystem.TabStop = True
        self._rbtn_bySystem.Text = "LoadBySystem"
        self._rbtn_bySystem.UseVisualStyleBackColor = True
        self._rbtn_bySystem.CheckedChanged += self.Rbtn_bySystemCheckedChanged
        # 
        # rbtn_byLocal
        # 
        self._rbtn_byLocal.Location = System.Drawing.Point(3, 3)
        self._rbtn_byLocal.Name = "rbtn_byLocal"
        self._rbtn_byLocal.Size = System.Drawing.Size(122, 24)
        self._rbtn_byLocal.TabIndex = 1
        self._rbtn_byLocal.TabStop = True
        self._rbtn_byLocal.Text = "LoadByLocal"
        self._rbtn_byLocal.UseVisualStyleBackColor = True
        self._rbtn_byLocal.CheckedChanged += self.Rbtn_byLocalCheckedChanged
        # 
        # pnl_modes
        # 
        self._pnl_modes.Controls.Add(self._cmbx_structureTypes)
        self._pnl_modes.Controls.Add(self._btn_getLocalPath)
        self._pnl_modes.Controls.Add(self._txt_localPath)
        self._pnl_modes.Controls.Add(self._rbtn_bySystem)
        self._pnl_modes.Controls.Add(self._rbtn_byLocal)
        self._pnl_modes.Location = System.Drawing.Point(3, 3)
        self._pnl_modes.Name = "pnl_modes"
        self._pnl_modes.Size = System.Drawing.Size(511, 51)
        self._pnl_modes.TabIndex = 2
        # 
        # txt_localPath
        # 
        self._txt_localPath.Enabled = False
        self._txt_localPath.Location = System.Drawing.Point(22, 25)
        self._txt_localPath.Name = "txt_localPath"
        self._txt_localPath.Size = System.Drawing.Size(486, 21)
        self._txt_localPath.TabIndex = 2
        self._txt_localPath.Text = "Select local files path..."
        # 
        # btn_getLocalPath
        # 
        self._btn_getLocalPath.Location = System.Drawing.Point(3, 25)
        self._btn_getLocalPath.Name = "btn_getLocalPath"
        self._btn_getLocalPath.Size = System.Drawing.Size(18, 21)
        self._btn_getLocalPath.TabIndex = 3
        self._btn_getLocalPath.Text = "@"
        self._btn_getLocalPath.UseVisualStyleBackColor = True
        # 
        # gbx_tree
        # 
        self._gbx_tree.Controls.Add(self._btn_push)
        self._gbx_tree.Controls.Add(self._btn_pull)
        self._gbx_tree.Controls.Add(self._btn_edit)
        self._gbx_tree.Controls.Add(self._btn_delete)
        self._gbx_tree.Controls.Add(self._btn_add)
        self._gbx_tree.Controls.Add(self._tvw_tree)
        self._gbx_tree.Location = System.Drawing.Point(3, 58)
        self._gbx_tree.Name = "gbx_tree"
        self._gbx_tree.Size = System.Drawing.Size(511, 329)
        self._gbx_tree.TabIndex = 3
        self._gbx_tree.TabStop = False
        self._gbx_tree.Text = "Structures Tree"
        # 
        # cmbx_structureTypes
        # 
        self._cmbx_structureTypes.FormattingEnabled = True
        self._cmbx_structureTypes.Location = System.Drawing.Point(387, 3)
        self._cmbx_structureTypes.Name = "cmbx_structureTypes"
        self._cmbx_structureTypes.Size = System.Drawing.Size(121, 20)
        self._cmbx_structureTypes.TabIndex = 0
        # 
        # tvw_tree
        # 
        self._tvw_tree.Location = System.Drawing.Point(6, 20)
        self._tvw_tree.Name = "tvw_tree"
        treeNode16.Name = "Node1"
        treeNode16.Text = "Node1"
        treeNode17.Name = "Node2"
        treeNode17.Text = "Node2"
        treeNode18.Name = "Node4"
        treeNode18.Text = "Node4"
        treeNode19.Name = "Node3"
        treeNode19.Text = "Node3"
        treeNode110.Name = "Node0"
        treeNode110.Text = "Node0"
        self._tvw_tree.Nodes.AddRange(System.Array[System.Windows.Forms.TreeNode](
            [treeNode110]))
        self._tvw_tree.Size = System.Drawing.Size(473, 303)
        self._tvw_tree.TabIndex = 0
        # 
        # btn_add
        # 
        self._btn_add.Font = System.Drawing.Font("等线", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 134)
        self._btn_add.Location = System.Drawing.Point(483, 93)
        self._btn_add.Name = "btn_add"
        self._btn_add.Size = System.Drawing.Size(23, 23)
        self._btn_add.TabIndex = 1
        self._btn_add.Text = "+"
        self._btn_add.UseVisualStyleBackColor = True
        self._btn_add.Click += self.Btn_addClick
        # 
        # btn_delete
        # 
        self._btn_delete.Font = System.Drawing.Font("等线", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 134)
        self._btn_delete.Location = System.Drawing.Point(483, 151)
        self._btn_delete.Name = "btn_delete"
        self._btn_delete.Size = System.Drawing.Size(23, 23)
        self._btn_delete.TabIndex = 2
        self._btn_delete.Text = "x"
        self._btn_delete.UseVisualStyleBackColor = True
        self._btn_delete.Click += self.Btn_deleteClick
        # 
        # btn_edit
        # 
        self._btn_edit.Font = System.Drawing.Font("等线", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._btn_edit.Location = System.Drawing.Point(483, 122)
        self._btn_edit.Name = "btn_edit"
        self._btn_edit.Size = System.Drawing.Size(23, 23)
        self._btn_edit.TabIndex = 3
        self._btn_edit.Text = "√"
        self._btn_edit.UseVisualStyleBackColor = True
        self._btn_edit.Click += self.Btn_editClick
        # 
        # btn_pull
        # 
        self._btn_pull.Font = System.Drawing.Font("宋体", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 134)
        self._btn_pull.Location = System.Drawing.Point(483, 20)
        self._btn_pull.Name = "btn_pull"
        self._btn_pull.Size = System.Drawing.Size(23, 23)
        self._btn_pull.TabIndex = 4
        self._btn_pull.Text = "←"
        self._btn_pull.UseVisualStyleBackColor = True
        self._btn_pull.Click += self.Btn_pullClick
        # 
        # btn_push
        # 
        self._btn_push.Font = System.Drawing.Font("宋体", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 134)
        self._btn_push.Location = System.Drawing.Point(483, 300)
        self._btn_push.Name = "btn_push"
        self._btn_push.Size = System.Drawing.Size(23, 23)
        self._btn_push.TabIndex = 5
        self._btn_push.Text = "→"
        self._btn_push.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._btn_push.UseVisualStyleBackColor = True
        self._btn_push.Click += self.Btn_pushClick
        # 
        # gbx_contents
        # 
        self._gbx_contents.Controls.Add(self._btn_remove)
        self._gbx_contents.Controls.Add(self._btn_new)
        self._gbx_contents.Controls.Add(self._dgv_validValues)
        self._gbx_contents.Controls.Add(self._btn_cancel)
        self._gbx_contents.Controls.Add(self._btn_ok)
        self._gbx_contents.Controls.Add(self._txt_defValue)
        self._gbx_contents.Controls.Add(self._ckbx_manField)
        self._gbx_contents.Controls.Add(self._ckbx_defValue)
        self._gbx_contents.Controls.Add(self._cmbx_validation)
        self._gbx_contents.Controls.Add(self._lab_validation)
        self._gbx_contents.Controls.Add(self._cmbx_structure)
        self._gbx_contents.Controls.Add(self._lab_structure)
        self._gbx_contents.Controls.Add(self._txt_len)
        self._gbx_contents.Controls.Add(self._lab_len)
        self._gbx_contents.Controls.Add(self._cmbx_type)
        self._gbx_contents.Controls.Add(self._lab_type)
        self._gbx_contents.Controls.Add(self._txt_desc)
        self._gbx_contents.Controls.Add(self._lab_desc)
        self._gbx_contents.Controls.Add(self._txt_title)
        self._gbx_contents.Controls.Add(self._lab_title)
        self._gbx_contents.Controls.Add(self._cmbx_objtypes)
        self._gbx_contents.Location = System.Drawing.Point(521, 6)
        self._gbx_contents.Name = "gbx_contents"
        self._gbx_contents.Size = System.Drawing.Size(386, 375)
        self._gbx_contents.TabIndex = 4
        self._gbx_contents.TabStop = False
        self._gbx_contents.Text = "Contents"
        # 
        # cmbx_objtypes
        # 
        self._cmbx_objtypes.Enabled = False
        self._cmbx_objtypes.FormattingEnabled = True
        self._cmbx_objtypes.Location = System.Drawing.Point(6, 15)
        self._cmbx_objtypes.Name = "cmbx_objtypes"
        self._cmbx_objtypes.Size = System.Drawing.Size(163, 20)
        self._cmbx_objtypes.TabIndex = 4
        # 
        # lab_title
        # 
        self._lab_title.Location = System.Drawing.Point(7, 42)
        self._lab_title.Name = "lab_title"
        self._lab_title.Size = System.Drawing.Size(45, 18)
        self._lab_title.TabIndex = 5
        self._lab_title.Text = "Title"
        # 
        # txt_title
        # 
        self._txt_title.Location = System.Drawing.Point(57, 39)
        self._txt_title.Name = "txt_title"
        self._txt_title.Size = System.Drawing.Size(112, 21)
        self._txt_title.TabIndex = 6
        # 
        # txt_desc
        # 
        self._txt_desc.Location = System.Drawing.Point(255, 39)
        self._txt_desc.Name = "txt_desc"
        self._txt_desc.Size = System.Drawing.Size(125, 21)
        self._txt_desc.TabIndex = 8
        # 
        # lab_desc
        # 
        self._lab_desc.Location = System.Drawing.Point(175, 42)
        self._lab_desc.Name = "lab_desc"
        self._lab_desc.Size = System.Drawing.Size(74, 18)
        self._lab_desc.TabIndex = 7
        self._lab_desc.Text = "Description"
        # 
        # lab_type
        # 
        self._lab_type.Location = System.Drawing.Point(7, 66)
        self._lab_type.Name = "lab_type"
        self._lab_type.Size = System.Drawing.Size(45, 18)
        self._lab_type.TabIndex = 9
        self._lab_type.Text = "Type"
        # 
        # cmbx_type
        # 
        self._cmbx_type.FormattingEnabled = True
        self._cmbx_type.Location = System.Drawing.Point(57, 63)
        self._cmbx_type.Name = "cmbx_type"
        self._cmbx_type.Size = System.Drawing.Size(112, 20)
        self._cmbx_type.TabIndex = 4
        # 
        # txt_len
        # 
        self._txt_len.Location = System.Drawing.Point(255, 63)
        self._txt_len.Name = "txt_len"
        self._txt_len.Size = System.Drawing.Size(51, 21)
        self._txt_len.TabIndex = 11
        # 
        # lab_len
        # 
        self._lab_len.Location = System.Drawing.Point(175, 66)
        self._lab_len.Name = "lab_len"
        self._lab_len.Size = System.Drawing.Size(74, 18)
        self._lab_len.TabIndex = 10
        self._lab_len.Text = "Length"
        # 
        # cmbx_structure
        # 
        self._cmbx_structure.FormattingEnabled = True
        self._cmbx_structure.Location = System.Drawing.Point(57, 86)
        self._cmbx_structure.Name = "cmbx_structure"
        self._cmbx_structure.Size = System.Drawing.Size(112, 20)
        self._cmbx_structure.TabIndex = 12
        # 
        # lab_structure
        # 
        self._lab_structure.Location = System.Drawing.Point(7, 89)
        self._lab_structure.Name = "lab_structure"
        self._lab_structure.Size = System.Drawing.Size(51, 18)
        self._lab_structure.TabIndex = 13
        self._lab_structure.Text = "SubType"
        # 
        # cmbx_validation
        # 
        self._cmbx_validation.FormattingEnabled = True
        self._cmbx_validation.Location = System.Drawing.Point(57, 109)
        self._cmbx_validation.Name = "cmbx_validation"
        self._cmbx_validation.Size = System.Drawing.Size(112, 20)
        self._cmbx_validation.TabIndex = 14
        # 
        # lab_validation
        # 
        self._lab_validation.Location = System.Drawing.Point(7, 112)
        self._lab_validation.Name = "lab_validation"
        self._lab_validation.Size = System.Drawing.Size(45, 18)
        self._lab_validation.TabIndex = 15
        self._lab_validation.Text = "Valid"
        # 
        # ckbx_defValue
        # 
        self._ckbx_defValue.Location = System.Drawing.Point(7, 274)
        self._ckbx_defValue.Name = "ckbx_defValue"
        self._ckbx_defValue.Size = System.Drawing.Size(197, 24)
        self._ckbx_defValue.TabIndex = 16
        self._ckbx_defValue.Text = "Set Defa&ult Value for Field"
        self._ckbx_defValue.UseVisualStyleBackColor = True
        # 
        # ckbx_manField
        # 
        self._ckbx_manField.Location = System.Drawing.Point(6, 324)
        self._ckbx_manField.Name = "ckbx_manField"
        self._ckbx_manField.Size = System.Drawing.Size(198, 24)
        self._ckbx_manField.TabIndex = 17
        self._ckbx_manField.Text = "M&andatory Field"
        self._ckbx_manField.UseVisualStyleBackColor = True
        # 
        # txt_defValue
        # 
        self._txt_defValue.Location = System.Drawing.Point(7, 297)
        self._txt_defValue.Name = "txt_defValue"
        self._txt_defValue.Size = System.Drawing.Size(373, 21)
        self._txt_defValue.TabIndex = 18
        # 
        # btn_ok
        # 
        self._btn_ok.Location = System.Drawing.Point(242, 346)
        self._btn_ok.Name = "btn_ok"
        self._btn_ok.Size = System.Drawing.Size(66, 23)
        self._btn_ok.TabIndex = 19
        self._btn_ok.Text = "Ok"
        self._btn_ok.UseVisualStyleBackColor = True
        # 
        # btn_cancel
        # 
        self._btn_cancel.Location = System.Drawing.Point(314, 346)
        self._btn_cancel.Name = "btn_cancel"
        self._btn_cancel.Size = System.Drawing.Size(66, 23)
        self._btn_cancel.TabIndex = 20
        self._btn_cancel.Text = "Cancel"
        self._btn_cancel.UseVisualStyleBackColor = True
        # 
        # dgv_validValues
        # 
        self._dgv_validValues.AllowUserToAddRows = False
        self._dgv_validValues.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        self._dgv_validValues.Columns.AddRange(System.Array[System.Windows.Forms.DataGridViewColumn](
            [self._Value,
            self._Description]))
        self._dgv_validValues.Location = System.Drawing.Point(6, 133)
        self._dgv_validValues.Name = "dgv_validValues"
        self._dgv_validValues.RowTemplate.Height = 23
        self._dgv_validValues.Size = System.Drawing.Size(300, 135)
        self._dgv_validValues.TabIndex = 21
        # 
        # btn_new
        # 
        self._btn_new.Location = System.Drawing.Point(314, 174)
        self._btn_new.Name = "btn_new"
        self._btn_new.Size = System.Drawing.Size(66, 23)
        self._btn_new.TabIndex = 22
        self._btn_new.Text = "New"
        self._btn_new.UseVisualStyleBackColor = True
        # 
        # btn_remove
        # 
        self._btn_remove.Location = System.Drawing.Point(314, 203)
        self._btn_remove.Name = "btn_remove"
        self._btn_remove.Size = System.Drawing.Size(66, 23)
        self._btn_remove.TabIndex = 23
        self._btn_remove.Text = "Delete"
        self._btn_remove.UseVisualStyleBackColor = True
        # 
        # Value
        # 
        self._Value.HeaderText = "Value"
        self._Value.Name = "Value"
        # 
        # Description
        # 
        self._Description.HeaderText = "Desc"
        self._Description.Name = "Description"
        self._Description.Width = 200
        # 
        # Creator
        # 
        self.Controls.Add(self._gbx_contents)
        self.Controls.Add(self._gbx_tree)
        self.Controls.Add(self._pnl_modes)
        self.Name = "Creator"
        self.Size = System.Drawing.Size(910, 390)
        self._pnl_modes.ResumeLayout(False)
        self._pnl_modes.PerformLayout()
        self._gbx_tree.ResumeLayout(False)
        self._gbx_contents.ResumeLayout(False)
        self._gbx_contents.PerformLayout()
        self._dgv_validValues.EndInit()
        self.ResumeLayout(False)
    
    def Rbtn_byLocalCheckedChanged(self, sender, e):
        try:
            self._rbtn_bySystem.Enabled = False \
            if self._rbtn_byLocal.Checked else True
            self._cmbx_structureTypes.Enabled = False \
            if self._rbtn_byLocal.Checked else True
            self._btn_getLocalPath.Enabled = True \
            if self._rbtn_byLocal.Checked else False
            self._rbtn_bySystem.Enabled = True \
            if self._rbtn_byLocal.Checked else False
            self._rbtn_byLocal.Enabled = False \
            if self._rbtn_byLocal.Checked else True
        except Exception as e:
            MessageBox.Show(str(e))
        pass

    def Rbtn_bySystemCheckedChanged(self, sender, e):
        try:
            self._rbtn_bySystem.Enabled = True \
            if self._rbtn_bySystem.Checked else False
            self._cmbx_structureTypes.Enabled = True \
            if self._rbtn_bySystem.Checked else False
            self._btn_getLocalPath.Enabled = False \
            if self._rbtn_bySystem.Checked else True
            self._rbtn_bySystem.Enabled = False \
            if self._rbtn_bySystem.Checked else True
            self._rbtn_byLocal.Enabled = True \
            if self._rbtn_bySystem.Checked else False
        except Exception as e:
            MessageBox.Show(str(e))
        pass

    def Btn_addClick(self, sender, e):
        pass

    def Btn_editClick(self, sender, e):
        pass

    def Btn_deleteClick(self, sender, e):
        pass
    
    def Btn_pullClick(self, sender, e):
        pass

    def Btn_pushClick(self, sender, e):
        pass
    
    def initialize(self):
        self.load_structure_types()
        self._rbtn_bySystem.Checked = True
        pass
    
    def load_structure_types(self):
        try:
            for item in BoDataStructureTypes :
                self._cmbx_structureTypes.Items.Add(item)
            if self._cmbx_structureTypes.Items.Count > 0:
                self._cmbx_structureTypes.SelectedIndex = 1
        except Exception as e:
            MessageBox.Show(str(e))
        pass
    
