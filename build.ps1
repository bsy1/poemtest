# �������⻷��
python -m venv .\venv

# �������⻷��
.\venv\Scripts\Activate

# ��װ��������
#pip install pyside6
#pip install pyinstaller
rm  .\build\dist\*
# �����ļ���build�ļ���
Copy-Item -Path ".\sever_core\sever_core.py" -Destination ".\build\" -Force
Copy-Item -Path ".\PythonApplication1\init.py" -Destination ".\build\data.py" -Force
Copy-Item -Path ".\PythonApplication1\poem.db" -Destination ".\build\" -Force
Copy-Item -Path ".\PythonApplication1\poem.db" -Destination ".\build\dist\" -Force
# ����build�ļ���
cd .\build

# ʹ��pyinstaller���Ϊexe��������ڽű���server_code.py
pyinstaller --onefile --noconsole sever_core.py
cd ../
# �˳����⻷��
deactivate