"""
自定义的分页组件，以后如果想要使用这个分页组件，你需要做如下几件事：

在视图函数中：
def student_list(request):
    # 1.根据自己的情况去筛选自己的数据
    queryset = Student.objects.all()
    # 2.实例化分页对象
    page_object = Pagination(request)

    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,  # 分页的数据
        "page_string": page_object.html()  # 页码
    }

    return render(request, "student_list.html", context)
在HTML页面中：
    {% for obj in queryset %}
        {{ obj.xx }}
    {% endfor %}

    <ul class="pagination">
        {{ page_string }}
    </ul>
"""
from django.utils.safestring import mark_safe
import copy


class Pagination(object):
    def __init__(self, queryset,request, page_size = 10, page_param="page", plus=5):
        """
        :param queryset: 请求的对象
        :param request: 符合条件的数据（根据这个数据给他进行分页处理）
        :param page_size: 每页显示多少条数据
        :param page_param: 在URL中传递的获取分页的参数。例如：/student/list/?page=12
        :param plus: 显示当前页的 前或后几页 （页码）
        """

        # query_dict = copy.deepcopy(request.GET)
        # query_dict._mutable = True
        # self.page_dict = q
        # 根据用户想要访问的页码，计算出起始位置
        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]

        # 数据总条数
        total_count = queryset.count()
        # 总页码
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 计算出，显示当前页的前五页，后五页

        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库中的数据比较少，都没有达到11页。
            start_page = 1
            end_page = self.total_page_count
        else:
            # 数据库中的手机壳i比较多 > 11页

            # 当前页<5时 (小极值)
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页 > 5
                # 当前页+5 > 总页数
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页码
        page_str_list = []

        # 首页
        page_str_list.append('<li><a href="?page={}">首页</a></li>'.format(1))

        # 上一页
        if self.page > 1:
            prev = '<li><a href="?page={}">上一页</a></li>'.format(self.page - 1)
        else:
            prev = '<li><a href="?page={}">上一页</a></li>'.format(1)
        page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            if i == self.page:
                ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
            else:
                ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
            page_str_list.append(ele)
        # 下一页
        if self.page < self.total_page_count:
            prev = '<li><a href="?page={}">下一页</a></li>'.format(self.page + 1)
        else:
            prev = '<li><a href="?page={}">下一页</a></li>'.format(self.total_page_count)
        page_str_list.append(prev)

        # 尾页
        page_str_list.append('<li><a href="?page={}">尾页</a></li>'.format(self.total_page_count))

        search_string = """
            <li>
                <form style="float: left; margin-left: -1px;" method="get">
                    <input name="page" style="position: relative; float: left; display: inline-block; width: 80px; border-radius: 0" type="text" class="form-control" placeholder="页码">
                    <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
                </form>
            </li>
        """
        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string
