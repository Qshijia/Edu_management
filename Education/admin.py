from django.contrib import admin
from django.shortcuts import render, redirect
from Education import models
from django import forms
from django.core.exceptions import ValidationError
from Education.utils.encrypt import md5


# Register your models here.


def admin_list(request):
    """管理员列表"""
    # 检查用户是否已登录，已登录，继续向下走，未登录，跳转回登录页面
    # 用户发来请求，获取cookie随机字符串，拿着随机字符串看看session中有没有。
    info = request.session.get("info")
    if not info:
        return redirect('/login/')

    # 搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data
    # 根据搜索条件去数据库获取
    admin_list = models.Admin.objects.filter(**data_dict)
    context = {
        "admin_list": admin_list,
        "search_data": search_data,
    }
    return render(request, "admin_list.html", context)


class AdminModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加了class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 去数据库校验当前密码和新输入的密码是否一致
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("不能与以前的密码相同")
        return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么
        return confirm


def admin_add(request):
    """添加管理员"""
    title = "新建管理员信息"
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, "change.html", {"title": title, "form": form})

    # 用户POST提交数据，数据校验。
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect("/admin/list")
    # 校验失败（在页面上显示错误信息）
    return render(request, "change.html", {"title": title, "form": form})


class AdminEditModelForm(forms.ModelForm):

    class Meta:
        model = models.Admin
        fields = ["username"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加了class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def admin_edit(request, nid):
    """编辑管理员"""
    title = "编辑管理员信息"
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        # return render(request, 'error.html', {"msg": "数据不存在"})
        return redirect('/admin/list/')
    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行数据(对象)
        form = AdminEditModelForm(instance=row_object)  # 显示需要修改的原数据
        return render(request, "change.html", {"title": title, "form": form})
    #
    # # 用户POST提交数据，数据校验。
    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect("/admin/list")
    # 校验失败（在页面上显示错误信息）
    return render(request, "change.html", {"title": title, "form": form})


def admin_delete(request, nid):
    """删除管理员"""
    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list")


class AdminResetModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加了class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 去数据库校验当前密码和新输入的密码是否一致
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("不能与以前的密码相同")
        return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么
        return confirm


def admin_reset(request, nid):
    """重置密码"""
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')
    title = "重置密码-{}".format(row_object.username)

    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, "change.html", {"title": title, "form": form})

    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list")
    return render(request, "change.html", {"title": title, "form": form})
