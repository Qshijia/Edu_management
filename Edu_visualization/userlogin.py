from django.http import HttpResponse
from django.shortcuts import render, redirect
from Education import models
from django import forms


class UserloginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


def userlogin(request):
    """登录"""
    if request.method == "GET":
        form = UserloginForm()
        return render(request, 'visual/userlogin.html', {'form': form})
    form = UserloginForm(data=request.POST)
    if form.is_valid():
        # 验证成功，获取到的用户名和密码
        print(form.cleaned_data)
        # 去数据库校验用户名和密码是否正确,获取用户对象
        student_object = models.Student.objects.filter(**form.cleaned_data).first()
        teacher_object = models.Teacher.objects.filter(**form.cleaned_data).first()
        # print(student_object.sid)

        if student_object:
            request.session["info"] = {'id': student_object.sid, "sname": student_object.username,
                                       "classnum": student_object.classnum}
            # return render(request, "visual/student_visual.html")
            return redirect("/Edu_visualization/student_visual/")
        elif teacher_object:
            request.session["info"] = {'id': teacher_object.tid, "tname": teacher_object.username,
                                       "cid": teacher_object.cid, "classnum": teacher_object.classnum,
                                       "appointment": teacher_object.appointment}
            return redirect("/Edu_visualization/teacher_visual/")
        else:
            form.add_error("password", "用户名或密码错误")
            # return HttpResponse("提交失败")
            return render(request, 'visual/userlogin.html', {'form': form})

    return render(request, 'visual/userlogin.html', {'form': form})


def logout(request):
    """注销"""
    request.session.clear()
    return redirect('/Edu_visualization/userlogin/')
