from pyecharts import options as opts
from pyecharts.charts import Liquid
import pandas as pd
from pyecharts.globals import SymbolType

excel_path = "D:\桌面\数据可视化\data\education_score.xlsx"
data = pd.read_excel(io=excel_path, header=None)
data.columns = ['id', '学号', '课程号', '分数', '班级']
data1 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '301')]["分数"].tolist()
data2 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '301')]["分数"].tolist()
data3 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '301')]["分数"].tolist()
data4 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '302')]["分数"].tolist()
data5 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '302')]["分数"].tolist()
data6 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '302')]["分数"].tolist()
data7 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '303')]["分数"].tolist()
data8 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '303')]["分数"].tolist()
data9 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '303')]["分数"].tolist()

count1 = 0
sum1 = 0
for data in data1:
    sum1 += 1
    if float(data) >= 80.0:
        count1 += 1

count2 = 0
sum2 = 0
for data in data2:
    sum2 += 1
    if float(data) >= 80.0:
        count2 += 1
# print(count2)
# print(sum2)

count3 = 0
sum3 = 0
for data in data3:
    sum3 += 1
    if float(data) >= 80.0:
        count3 += 1

count4 = 0
sum4 = 0
for data in data4:
    sum4 += 1
    if float(data) >= 80.0:
        count4 += 1

count5 = 0
sum5 = 0
for data in data5:
    sum5 += 1
    if float(data) >= 80.0:
        count5 += 1

count6 = 0
sum6 = 0
for data in data6:
    sum6 += 1
    if float(data) >= 80.0:
        count6 += 1

count7 = 0
sum7 = 0
for data in data7:
    sum7 += 1
    if float(data) >= 80.0:
        count7 += 1

count8 = 0
sum8 = 0
for data in data8:
    sum8 += 1
    if float(data) >= 80.0:
        count8 += 1

count9 = 0
sum9 = 0
for data in data9:
    sum9 += 1
    if float(data) >= 80.0:
        count9 += 1
# print(count9)
# print(sum9)


def liquids():
    chart_liquid30101 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="301班语文学科优秀率",
            data=[count1 / sum1, 0.3],
            center=["45%", "50%"],
            color='white',
            background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="301班语文学科优秀率",
                title_link="/Edu_visualization/teacher_visual/show_liquid30101/",
            )
        )
    )
    chart_liquid30102 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="301班数学学科优秀率",
            data=[count2 / sum2, 0.3],
            center=["45%", "50%"],
            # color='white',
            # background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="301班数学学科优秀率",
                title_link="/Edu_visualization/teacher_visual/show_liquid30102/",
            )
        )
    )

    chart_liquid30103 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="301班英语学科优秀率",
            data=[count3 / sum3, 0.3],
            center=["45%", "50%"],
            color='white',
            background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="301班英语学科优秀率",
                title_link="/Edu_visualization/teacher_visual/show_liquid30103/",
            )
        )
    )

    chart_liquid30201 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="302班语文学科优秀率",
            data=[count4 / sum4, 0.3],
            center=["45%", "50%"],
            color='white',
            background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="302班语文学科优秀率",
                title_link="/Edu_visualization/teacher_visual/show_liquid30201/",
            )
        )
    )

    chart_liquid30202 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="302班数学学科优秀率",
            data=[count5 / sum5, 0.3],
            center=["45%", "50%"],
            # color='white',
            # background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="302班数学学科优秀率",
                title_link="/Edu_visualization/teacher_visual/show_liquid30202/",
            )
        )
    )

    chart_liquid30203 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="302班英语学科优秀率",
            data=[count6 / sum6, 0.3],
            center=["45%", "50%"],
            color='white',
            background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="302班英语学科优秀率",
                title_link="/Edu_visualization/teacher_visual/show_liquid30203/",
            )
        )
    )

    chart_liquid30301 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="303班语文学科优秀率",
            data=[count7 / sum7, 0.3],
            center=["45%", "50%"],
            color='white',
            background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="303班语文学科优秀率",
                title_link="/Edu_visualization/teacher_visual/show_liquid30301/",
            )
        )
    )

    chart_liquid30302 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="303班数学学科优秀率",
            data=[count8 / sum8, 0.3],
            center=["45%", "50%"],
            # color='white',
            # background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="303班数学学科优秀率",
                title_link="/Edu_visualization/teacher_visual/show_liquid30302/",
            )
        )
    )

    chart_liquid30303 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="303班英语学科优秀率",
            data=[count9 / sum9, 0.3],
            center=["45%", "50%"],
            color='white',
            background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="303班英语学科优秀率",
                title_link="/Edu_visualization/teacher_visual/show_liquid30303/",
            )
        )
    )

    return chart_liquid30101, chart_liquid30102, chart_liquid30103,\
        chart_liquid30201, chart_liquid30202, chart_liquid30203,\
        chart_liquid30301, chart_liquid30302, chart_liquid30303


chart_liquid30101_, chart_liquid30102_, chart_liquid30103_,\
    chart_liquid30201_, chart_liquid30202_, chart_liquid30203_,\
    chart_liquid30301_, chart_liquid30302_, chart_liquid30303_ = liquids()


chart_liquid30101_.render('../../templates/visual/pyecharts_visual/liquid30101.html')
chart_liquid30102_.render('../../templates/visual/pyecharts_visual/liquid30102.html')
chart_liquid30103_.render('../../templates/visual/pyecharts_visual/liquid30103.html')

chart_liquid30201_.render('../../templates/visual/pyecharts_visual/liquid30201.html')
chart_liquid30202_.render('../../templates/visual/pyecharts_visual/liquid30202.html')
chart_liquid30203_.render('../../templates/visual/pyecharts_visual/liquid30203.html')

chart_liquid30301_.render('../../templates/visual/pyecharts_visual/liquid30301.html')
chart_liquid30302_.render('../../templates/visual/pyecharts_visual/liquid30302.html')
chart_liquid30303_.render('../../templates/visual/pyecharts_visual/liquid30303.html')
