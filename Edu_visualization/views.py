from django.http import HttpResponse
from django.shortcuts import render, redirect

from Education import models

# Create your views here.


def student_visual(request):
    data_dict = {}
    search_data = request.GET.get('sid', "")
    if search_data:
        data_dict["sid"] = search_data
    # 1.获取数据库中的所有用户数据
    print(search_data)
    score_list = models.Score.objects.filter(sid=search_data)
    # course_list = models.Course.objects.all()

    grade_sum = 0
    for score in score_list:
        # print(score.grade)
        grade_sum += float(score.grade)
    # student_list = models.Student.objects.all()
    # for student in student_list:
    #     # print(student.sid)
    #     score_order = models.Score.objects.filter(sid=student.sid)
    #     # print(" ")
    #     sum=0.0
    #     for score in score_order:
    #         print(score.grade)
    #         sum += float(score.grade)
        #     sum = 0
        #     for score in score_order:
        #         sum += float(score.grade)
        # print(sum)

    return render(request, "visual/student_visual.html",
                  {"score_list": score_list, "search_data": search_data, "grade_sum": grade_sum})


def teacher_visual(request):
    data_dict = {}
    search_data = request.GET.get('tid', "")
    if search_data:
        data_dict["tid"] = search_data
        # print(search_data)
    # 1.获取数据库中的所有用户数据
    teacher_list = models.Teacher.objects.filter(tid=search_data)
    # print(teacher_list)
    for teacher in teacher_list:
        cid = teacher.cid
        classnum = teacher.classnum
        # print(cid)
        # print(classnum)
        score_list = models.Score.objects.filter(cid=cid, classnum=classnum)
        # score_grade=[]
        # for score in score_list:
        #     score_grade.append(float(score.grade))
        # print(score_grade)

        return render(request, "visual/teacher_visual.html", {"score_list": score_list, "search_data": search_data,
                                                              "teacher": teacher})
    return render(request, "visual/teacher_visual.html")


def class_visual301(request):
    # return HttpResponse("班级301")
    return render(request, "visual/pyecharts_visual/result_301.html")


def class_visual302(request):
    return render(request, "visual/pyecharts_visual/result_302.html")


def class_visual303(request):
    return render(request, "visual/pyecharts_visual/result_303.html")


def visual_line_30101(request):
    return render(request, 'visual/pyecharts_visual/line30101.html')


def visual_line_30102(request):
    return render(request, 'visual/pyecharts_visual/line30102.html')


def visual_line_30103(request):
    return render(request, 'visual/pyecharts_visual/line30103.html')


def visual_line_30201(request):
    return render(request, 'visual/pyecharts_visual/line30201.html')


def visual_line_30202(request):
    return render(request, 'visual/pyecharts_visual/line30202.html')


def visual_line_30203(request):
    return render(request, 'visual/pyecharts_visual/line30203.html')


def visual_line_30301(request):
    return render(request, 'visual/pyecharts_visual/line30301.html')


def visual_line_30302(request):
    return render(request, 'visual/pyecharts_visual/line30302.html')


def visual_line_30303(request):
    return render(request, 'visual/pyecharts_visual/line30303.html')


def visual_liquid_30101(request):
    return render(request, 'visual/pyecharts_visual/liquid30101.html')


def visual_liquid_30102(request):
    return render(request, 'visual/pyecharts_visual/liquid30102.html')


def visual_liquid_30103(request):
    return render(request, 'visual/pyecharts_visual/liquid30103.html')


def visual_liquid_30201(request):
    return render(request, 'visual/pyecharts_visual/liquid30201.html')


def visual_liquid_30202(request):
    return render(request, 'visual/pyecharts_visual/liquid30202.html')


def visual_liquid_30203(request):
    return render(request, 'visual/pyecharts_visual/liquid30203.html')


def visual_liquid_30301(request):
    return render(request, 'visual/pyecharts_visual/liquid30301.html')


def visual_liquid_30302(request):
    return render(request, 'visual/pyecharts_visual/liquid30302.html')


def visual_liquid_30303(request):
    return render(request, 'visual/pyecharts_visual/liquid30303.html')


def visual_box_30101(request):
    return render(request, 'visual/pyecharts_visual/box30101.html')


def visual_box_30102(request):
    return render(request, 'visual/pyecharts_visual/box30102.html')


def visual_box_30103(request):
    return render(request, 'visual/pyecharts_visual/box30103.html')


def visual_box_30201(request):
    return render(request, 'visual/pyecharts_visual/box30201.html')


def visual_box_30202(request):
    return render(request, 'visual/pyecharts_visual/box30202.html')


def visual_box_30203(request):
    return render(request, 'visual/pyecharts_visual/box30203.html')


def visual_box_30301(request):
    return render(request, 'visual/pyecharts_visual/box30301.html')


def visual_box_30302(request):
    return render(request, 'visual/pyecharts_visual/box30302.html')


def visual_box_30303(request):
    return render(request, 'visual/pyecharts_visual/box30303.html')


def visual_bar_01(request):
    return render(request, 'visual/pyecharts_visual/bar01.html')


def visual_bar_02(request):
    return render(request, 'visual/pyecharts_visual/bar02.html')


def visual_bar_03(request):
    return render(request, 'visual/pyecharts_visual/bar03.html')
