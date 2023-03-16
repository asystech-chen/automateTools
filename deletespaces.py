import win32com.client

def remove_spaces():
    # 获取当前活动文档对象
    word = win32com.client.Dispatch("Word.Application")
    doc = word.ActiveDocument
    
    # 遍历每个段落
    for para in doc.Paragraphs:
        # 替换段落中的空格
        para.Range.Text = para.Range.Text.replace(" ", "")
    
    # 遍历每个表格单元格
    for table in doc.Tables:
        for cell in table.Range.Cells:
            # 替换单元格中的空格
            cell.Range.Text = cell.Range.Text.replace(" ", "")
    
    # 关闭Word应用程序
    word.Quit()

# 注册为Office插件
class AutoRemoveSpaces:
    def OnOpenDocument(self, doc):
        remove_spaces()

# 创建COM对象
word = win32com.client.Dispatch("Word.Application")
# 注册插件
word.Application.Events.RegisterXLL("path/to/your/addin.xll")
