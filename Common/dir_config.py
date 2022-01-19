import os
#项目顶层目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
screenshot_dir = os.path.join(base_dir,'Outouts/screenshots')
log_dir = os.path.join(base_dir,"Outouts/logs")
htmlreport_dir = os.path.join(base_dir,"Outouts/reports")
print(screenshot_dir)
#在python中\代表转义
