from django.contrib import admin
from django.urls import path, include
from Education import views, account, admin

urlpatterns = [
    path('login/', account.login),
    path('logout/', account.logout),

    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # 学生管理
    path('student/list/', views.student_list),
    path('student/add/', views.student_add),
    path('student/<int:nid>/delete/', views.student_delete),
    path('student/<int:nid>/edit/', views.student_edit),

    # 课程管理
    path('course/list/', views.course_list),
    path('course/add/', views.course_add),
    path('course/<int:nid>/delete/', views.course_delete),
    # 中间传正则表达式
    # http://127.0.0.1:8080/course/10/edit/
    # http://127.0.0.1:8080/course/3/edit/
    path('course/<int:nid>/edit/', views.course_edit),

    # 教师管理
    path('teacher/list/', views.teacher_list),
    path('teacher/add/', views.teacher_add),
    path('teacher/<int:nid>/delete/', views.teacher_delete),
    path('teacher/<int:nid>/edit/', views.teacher_edit),

    # 成绩管理
    path('score/list/', views.score_list),
    path('score/add/', views.score_add),
    path('score/<int:nid>/delete/', views.score_delete),
    path('score/<int:nid>/edit/', views.score_edit),


    # 可视化平台
    path('Edu_visualization/', include("Edu_visualization.urls")),
    # path('score/add/', views.score_add),
    # path('score/<int:nid>/delete/', views.score_delete),
    # path('score/<int:nid>/edit/', views.score_edit),
]
