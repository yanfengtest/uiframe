

if __name__ == '__main__':
    import pytest
    import alluer
    pytest.main(["-s","-v","--alluredir","reports"])
    # -s: 显示程序中的print / logging输出
    # -v: 丰富信息模式, 输出更详细的用例执行信息
    # -q: 安静模式, 不输出环境信息
    # -k：关键字匹配，用and区分：匹配范围（文件名、类名、函数名）