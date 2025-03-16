from pyecharts.charts import Boxplot
from pyecharts import options as opts
import pandas as pd

excel_path = "D:\桌面\数据可视化\data\education_score.xlsx"
data = pd.read_excel(io=excel_path, header=None)
data.columns = ['id', '学号', '课程号', '分数', '班级']
yaxis_data1 = [data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '301')]["分数"].tolist()]
yaxis_data2 = [data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '301')]["分数"].tolist()]
yaxis_data3 = [data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '301')]["分数"].tolist()]

yaxis_data4 = [data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '302')]["分数"].tolist()]
yaxis_data5 = [data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '302')]["分数"].tolist()]
yaxis_data6 = [data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '302')]["分数"].tolist()]

yaxis_data7 = [data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '303')]["分数"].tolist()]
yaxis_data8 = [data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '303')]["分数"].tolist()]
yaxis_data9 = [data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '303')]["分数"].tolist()]


def boxplots():
    chart_box30101 = (
        Boxplot(
            init_opts=opts.InitOpts(
                width='700px',
                height='450px',
            )
        )
        .add_xaxis(['301班语文学科'])
        .add_yaxis(
            '301班语文学科',
            Boxplot().prepare_data(yaxis_data1),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='301班语文学科成绩分布',  # 主标题
                title_link='/Edu_visualization/teacher_visual/show_box30101/',  # 主标题点击跳转链接
            ),
            # yaxis_opts=opts.AxisOpts(min_=50)
        )
    )

    chart_box30102 = (
        Boxplot(
            init_opts=opts.InitOpts(
                width='700px',
                height='450px',
            )
        )
        .add_xaxis(['301班数学学科'])
        .add_yaxis(
            '301班数学学科',
            Boxplot().prepare_data(yaxis_data2),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='301班数学学科成绩分布',  # 主标题
                title_link='/Edu_visualization/teacher_visual/show_box30102/',  # 主标题点击跳转链接
            ),
            # yaxis_opts=opts.AxisOpts(min_=50)
        )
    )

    chart_box30103 = (
        Boxplot(
            init_opts=opts.InitOpts(
                width='700px',
                height='450px',
            )
        )
        .add_xaxis(['301班英语学科'])
        .add_yaxis(
            '301班英语学科',
            Boxplot().prepare_data(yaxis_data3),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='301班英语学科成绩分布',  # 主标题
                title_link='/Edu_visualization/teacher_visual/show_box30103/',
            ),
            # yaxis_opts=opts.AxisOpts(min_=50)
        )
    )

    chart_box30201 = (
        Boxplot(
            init_opts=opts.InitOpts(
                width='700px',
                height='450px',
            )
        )
        .add_xaxis(['302班语文学科'])
        .add_yaxis(
            '302班语文学科',
            Boxplot().prepare_data(yaxis_data4),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='302班语文学科成绩分布',  # 主标题
                title_link='/Edu_visualization/teacher_visual/show_box30201/',  # 主标题点击跳转链接
            ),
            # yaxis_opts=opts.AxisOpts(min_=50)
        )
    )

    chart_box30202 = (
        Boxplot(
            init_opts=opts.InitOpts(
                width='700px',
                height='450px',
            )
        )
        .add_xaxis(['302班数学学科'])
        .add_yaxis(
            '302班数学学科',
            Boxplot().prepare_data(yaxis_data5),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='302班数学学科成绩分布',  # 主标题
                title_link='/Edu_visualization/teacher_visual/show_box30202/',  # 主标题点击跳转链接
            ),
            # yaxis_opts=opts.AxisOpts(min_=50)
        )
    )

    chart_box30203 = (
        Boxplot(
            init_opts=opts.InitOpts(
                width='700px',
                height='450px',
            )
        )
        .add_xaxis(['302班英语学科'])
        .add_yaxis(
            '302班英语学科',
            Boxplot().prepare_data(yaxis_data6),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='302班英语学科成绩分布',  # 主标题
                title_link='/Edu_visualization/teacher_visual/show_box30203/',
            ),
            # yaxis_opts=opts.AxisOpts(min_=50)
        )
    )

    chart_box30301 = (
        Boxplot(
            init_opts=opts.InitOpts(
                width='700px',
                height='450px',
            )
        )
        .add_xaxis(['303班语文学科'])
        .add_yaxis(
            '303班语文学科',
            Boxplot().prepare_data(yaxis_data7),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='303班语文学科成绩分布',  # 主标题
                title_link='/Edu_visualization/teacher_visual/show_box30301/',  # 主标题点击跳转链接
            ),
            # yaxis_opts=opts.AxisOpts(min_=50)
        )
    )

    chart_box30302 = (
        Boxplot(
            init_opts=opts.InitOpts(
                width='700px',
                height='450px',
            )
        )
        .add_xaxis(['303班数学学科'])
        .add_yaxis(
            '303班数学学科',
            Boxplot().prepare_data(yaxis_data8),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='303班数学学科成绩分布',  # 主标题
                title_link='/Edu_visualization/teacher_visual/show_box30302/',  # 主标题点击跳转链接
            ),
            # yaxis_opts=opts.AxisOpts(min_=50)
        )
    )

    chart_box30303 = (
        Boxplot(
            init_opts=opts.InitOpts(
                width='700px',
                height='450px',
            )
        )
        .add_xaxis(['303班英语学科'])
        .add_yaxis(
            '303班英语学科',
            Boxplot().prepare_data(yaxis_data9),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='303班英语学科成绩分布',  # 主标题
                title_link='/Edu_visualization/teacher_visual/show_box30303/',
            ),
            # yaxis_opts=opts.AxisOpts(min_=50)
        )
    )
    return chart_box30101, chart_box30102, chart_box30103, \
        chart_box30201, chart_box30202, chart_box30203, \
        chart_box30301, chart_box30302, chart_box30303


chart_box30101_, chart_box30102_, chart_box30103_, \
    chart_box30201_, chart_box30202_, chart_box30203_, \
    chart_box30301_, chart_box30302_, chart_box30303_ = boxplots()


chart_box30101_.render('../../templates/visual/pyecharts_visual/box30101.html')
chart_box30102_.render('../../templates/visual/pyecharts_visual/box30102.html')
chart_box30103_.render('../../templates/visual/pyecharts_visual/box30103.html')

chart_box30201_.render('../../templates/visual/pyecharts_visual/box30201.html')
chart_box30202_.render('../../templates/visual/pyecharts_visual/box30202.html')
chart_box30203_.render('../../templates/visual/pyecharts_visual/box30203.html')

chart_box30301_.render('../../templates/visual/pyecharts_visual/box30301.html')
chart_box30302_.render('../../templates/visual/pyecharts_visual/box30302.html')
chart_box30303_.render('../../templates/visual/pyecharts_visual/box30303.html')
