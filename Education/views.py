from django.shortcuts import render, HttpResponse, redirect
from Education import models
from Education.models import Course, Teacher, Student, Score
from django import forms
from django.utils.safestring import mark_safe
from Education.utils.pagination import Pagination


# Create your views here.
def student_list(request):
    """学生信息管理"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data

    # 根据用户想要访问的页码，计算出起始位置
    page = int(request.GET.get('page', 1))
    page_size = 10  # 每页显示10条数据
    start = (page - 1) * page_size
    end = page * page_size

    # 1.获取数据库中的所有用户数据
    # queryset [对象，对象，对象]
    student_list = Student.objects.filter(**data_dict).order_by("id")[start:end]

    # 数据总条数
    total_count = Student.objects.filter(**data_dict).order_by("sid").count()
    # 总页码
    total_page_count, div = divmod(total_count, page_size)
    if div:
        total_page_count += 1

    # 计算出，显示当前页的前五页和后五页
    plus = 5
    if total_page_count <= 2*plus + 1:
        # 数据库中的数据比较少，都没有达到11页。
        start_page = 1
        end_page = total_page_count
    else:
        # 数据库中的手机壳i比较多 > 11页

        # 当前页<5时 (小极值)
        if page <= plus:
            start_page = 1
            end_page = 2*plus + 1
        else:
            # 当前页 > 5
            # 当前页+5 > 总页数
            if (page + plus) > total_page_count:
                start_page = total_page_count - 2*plus
                end_page = total_page_count
            else:
                start_page = page - plus
                end_page = page + plus

    # 页码
    page_str_list=[]

    # 首页
    page_str_list.append('<li><a href="?page={}">首页</a></li>'.format(1))

    # 上一页
    if page > 1:
        prev = '<li><a href="?page={}">上一页</a></li>'.format(page - 1)
    else:
        prev = '<li><a href="?page={}">上一页</a></li>'.format(1)
    page_str_list.append(prev)

    for i in range(start_page, end_page+1):
        if i == page:
            ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
        else:
            ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_str_list.append(ele)
    # 下一页
    if page < total_page_count:
        prev = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
    else:
        prev = '<li><a href="?page={}">下一页</a></li>'.format(total_page_count)
    page_str_list.append(prev)

    # 尾页
    page_str_list.append('<li><a href="?page={}">尾页</a></li>'.format(total_page_count))

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
    return render(request, "student_list.html", {"student_list": student_list, "search_data": search_data, "page_string": page_string})
# def student_list(request):
#     """学生信息管理"""
#     data_dict = {}
#     search_data = request.GET.get('q', "")
#     if search_data:
#         data_dict["sname__contains"] = search_data
#
#     # 1.获取数据库中的所有用户数据
#     # queryset [对象，对象，对象]
#     queryset = Student.objects.filter(**data_dict).order_by("sid")
#     page_object = Pagination(request, queryset)
#     context = {
#         "search_data": search_data,
#         "queryset": page_object.page_queryset,
#         "page_string": page_object.html()
#     }
#
#     return render(request, "student_list.html", context)


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ["sid", "username", "classnum", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加了class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def student_add(request):
    title = "新建学生信息"
    if request.method == "GET":
        form = StudentModelForm()
        return render(request, "change.html", {"title": title, "form": form})

    # 用户POST提交数据，数据校验。
    form = StudentModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect("/student/list")

    # 校验失败（在页面上显示错误信息）
    return render(request, "change.html", {"title": title, "form": form})


def student_delete(request, nid):
    Student.objects.filter(id=nid).delete()
    return redirect("/student/list")


def student_edit(request, nid):
    """编辑学生信息"""
    title = "编辑学生信息"
    row_object = models.Student.objects.filter(id=nid).first()
    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行数据(对象)
        form = StudentModelForm(instance=row_object)  # 显示需要修改的原数据
        return render(request, "change.html", {"title": title, "form": form})

    # 用户POST提交数据，数据校验。
    form = StudentModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect("/student/list")
    # 校验失败（在页面上显示错误信息）
    return render(request, "change.html", {"title": title, "form": form})


def course_list(request):
    """课程信息管理"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["cname__contains"] = search_data
    # 1.获取数据库中的所有用户数据
    # queryset [对象，对象，对象]
    course_list = Course.objects.filter(**data_dict).order_by("id")
    return render(request, "course_list.html", {"course_list": course_list, "search_data": search_data})


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ["cid", "cname"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加了class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def course_add(request):
    """添加课程"""
    title = "新建课程信息"
    if request.method == "GET":
        form = CourseModelForm()
        return render(request, "change.html", {"title": title, "form": form})
    form = CourseModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/course/list")
    return render(request, "change.html", {"title": title, "form": form})


def course_delete(request, nid):
    """删除课程"""
    Course.objects.filter(id=nid).delete()
    return redirect("/course/list")


def course_edit(request, nid):
    """编辑课程信息"""
    title = "编辑课程信息"
    row_object = models.Course.objects.filter(id=nid).first()
    if request.method == "GET":
        form = CourseModelForm(instance=row_object)
        return render(request, "change.html", {"title": title, "form": form})
    form = CourseModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/course/list")
    return render(request, "change.html", {"title": title, "form": form})


def teacher_list(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data
    # 1.获取数据库中的所有用户数据
    teacher_list = Teacher.objects.filter(**data_dict).order_by("id")
    # for obj in teacher_list:
    #     obj.get_appointment_display()
    return render(request, "teacher_list.html", {"teacher_list": teacher_list, "search_data": search_data})


class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ["tid", "username", "classnum", "cid", "appointment", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加了class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def teacher_add(request):
    title = "新建教师信息"
    if request.method == "GET":
        form = TeacherModelForm()
        return render(request, "change.html", {"title": title, "form": form})
    form = TeacherModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/teacher/list")
    return render(request, "change.html", {"title": title, "form": form})


def teacher_delete(request, nid):
    Teacher.objects.filter(id=nid).delete()
    return redirect("/teacher/list")


def teacher_edit(request, nid):
    """修改教师信息"""
    title = "编辑教师信息"
    row_object = models.Teacher.objects.filter(id=nid).first()
    if request.method == "GET":
        form = TeacherModelForm(instance=row_object)
        return render(request, "change.html", {"title": title, "form": form})
    form = TeacherModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/teacher/list")
    return render(request, "change.html", {"title": title, "form": form})


def score_list(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["sid"] = search_data
    # 1.获取数据库中的所有用户数据
    score_list = Score.objects.filter(**data_dict).order_by("id")
    return render(request, "score_list.html", {"score_list": score_list, "search_data": search_data})


class ScoreModelForm(forms.ModelForm):
    class Meta:
        model = models.Score
        fields = ["sid", "cid", "grade", "classnum"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加了class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def score_add(request):
    title = "新建成绩数据"
    if request.method == "GET":
        form = ScoreModelForm()
        return render(request, "change.html", {"title": title, "form": form})
    form = ScoreModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/score/list")
    return render(request, "change.html", {"title": title, "form": form})


def score_delete(request, nid):
    Score.objects.filter(id=nid).delete()
    return redirect("/score/list")


def score_edit(request, nid):
    """修改课程"""
    title = "编辑成绩数据"
    row_object = models.Score.objects.filter(id=nid).first()
    if request.method == "GET":
        form = ScoreModelForm(instance=row_object)
        return render(request, "change.html", {"title": title, "form": form})
    form = ScoreModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/score/list")
    return render(request, "change.html", {"title": title, "form": form})
