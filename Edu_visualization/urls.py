from django.contrib import admin
from django.urls import path
from Edu_visualization import views, userlogin

urlpatterns = [
    path('userlogin/', userlogin.userlogin),
    path('logout/', userlogin.userlogin),
    # 学生板块
    path('student_visual/', views.student_visual),
    path('teacher_visual/', views.teacher_visual),
    path('class_visual301/', views.class_visual301),
    path('class_visual302/', views.class_visual302),
    path('class_visual303/', views.class_visual303),
    # pyecharts # lines
    path('teacher_visual/show_line30101/', views.visual_line_30101),
    path('teacher_visual/show_line30102/', views.visual_line_30102),
    path('teacher_visual/show_line30103/', views.visual_line_30103),

    path('teacher_visual/show_line30201/', views.visual_line_30201),
    path('teacher_visual/show_line30202/', views.visual_line_30202),
    path('teacher_visual/show_line30203/', views.visual_line_30203),

    path('teacher_visual/show_line30301/', views.visual_line_30301),
    path('teacher_visual/show_line30302/', views.visual_line_30302),
    path('teacher_visual/show_line30303/', views.visual_line_30303),
    # liquids
    path('teacher_visual/show_liquid30101/', views.visual_liquid_30101),
    path('teacher_visual/show_liquid30102/', views.visual_liquid_30102),
    path('teacher_visual/show_liquid30103/', views.visual_liquid_30103),

    path('teacher_visual/show_liquid30201/', views.visual_liquid_30201),
    path('teacher_visual/show_liquid30202/', views.visual_liquid_30202),
    path('teacher_visual/show_liquid30203/', views.visual_liquid_30203),

    path('teacher_visual/show_liquid30301/', views.visual_liquid_30301),
    path('teacher_visual/show_liquid30302/', views.visual_liquid_30302),
    path('teacher_visual/show_liquid30303/', views.visual_liquid_30303),
    # boxs
    path('teacher_visual/show_box30101/', views.visual_box_30101),
    path('teacher_visual/show_box30102/', views.visual_box_30102),
    path('teacher_visual/show_box30103/', views.visual_box_30103),

    path('teacher_visual/show_box30201/', views.visual_box_30201),
    path('teacher_visual/show_box30202/', views.visual_box_30202),
    path('teacher_visual/show_box30203/', views.visual_box_30203),

    path('teacher_visual/show_box30301/', views.visual_box_30301),
    path('teacher_visual/show_box30302/', views.visual_box_30302),
    path('teacher_visual/show_box30303/', views.visual_box_30303),
    # bars
    path('teacher_visual/show_bar01/', views.visual_bar_01),
    path('teacher_visual/show_bar02/', views.visual_bar_02),
    path('teacher_visual/show_bar03/', views.visual_bar_03),
]
