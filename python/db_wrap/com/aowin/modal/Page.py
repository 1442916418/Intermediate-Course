"""
    分页查询
"""


class Page:
    def __init__(self):
        self.pageNum = 1  # 当前页码
        self.pageTotal = None  # 总页吗
        self.countTotal = None  # 总条数
        self.pageSize = 10  # 每页显示5条数据
        self.data = None  # 放查询数据

