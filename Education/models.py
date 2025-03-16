from django.db import models

# Create your models here.


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)


class Student(models.Model):
    """学生表"""
    sid = models.CharField(verbose_name='学号', max_length=225)
    username = models.CharField(verbose_name='学生姓名', max_length=225)
    classnum = models.CharField(verbose_name='所在班级', max_length=225)
    password = models.CharField(verbose_name='密码', max_length=255)


class Teacher(models.Model):
    """教师表"""
    tid = models.CharField(verbose_name='教师号', max_length=225)
    username = models.CharField(verbose_name='教师名', max_length=255)
    classnum = models.CharField(verbose_name='所带班级', max_length=225)
    cid = models.CharField(verbose_name='课程号', max_length=225)
    # cid = models.ForeignKey(to="Course", to_field="cid", on_delete=models.CASCADE)
    appointment_choices=(
        (0, "学科教师"),
        (1, "班主任"),
    )
    appointment = models.IntegerField(verbose_name='职务', choices=appointment_choices)
    password = models.CharField(verbose_name='密码', max_length=255)


class Course(models.Model):
    """课程表"""
    cid = models.CharField(verbose_name='课程号', max_length=225)
    cname = models.CharField(verbose_name='课程名', max_length=255)


class Score(models.Model):
    """成绩表"""
    sid = models.CharField(verbose_name='学号', max_length=225)
    cid = models.CharField(verbose_name='课程号', max_length=225)
    grade = models.CharField(verbose_name='成绩', max_length=225)
    classnum = models.CharField(verbose_name='班级', max_length=225)
