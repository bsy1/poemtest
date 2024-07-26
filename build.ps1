# 创建虚拟环境
python -m venv .\venv

# 激活虚拟环境
.\venv\Scripts\Activate

# 安装所需依赖
#pip install pyside6
#pip install pyinstaller
rm  .\build\dist\*
# 复制文件到build文件夹
Copy-Item -Path ".\sever_core\sever_core.py" -Destination ".\build\" -Force
Copy-Item -Path ".\PythonApplication1\init.py" -Destination ".\build\data.py" -Force
Copy-Item -Path ".\PythonApplication1\poem.db" -Destination ".\build\" -Force
Copy-Item -Path ".\PythonApplication1\poem.db" -Destination ".\build\dist\" -Force
# 进入build文件夹
cd .\build

# 使用pyinstaller打包为exe，假设入口脚本是server_code.py
pyinstaller --onefile --noconsole sever_core.py
cd ../
# 退出虚拟环境
deactivate