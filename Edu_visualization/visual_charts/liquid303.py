from pyecharts import options as opts
from pyecharts.charts import Liquid
import pandas as pd

excel_path = "D:\桌面\数据可视化\data\education_score.xlsx"
data = pd.read_excel(io=excel_path, header=None)
data.columns = ['id', '学号', '课程号', '分数', '班级']
data1 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '303')]["分数"].tolist()
data2 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '303')]["分数"].tolist()
data3 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '303')]["分数"].tolist()

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


count3 = 0
sum3 = 0
for data in data3:
    sum3 += 1
    if float(data) >= 80.0:
        count3 += 1


def liquids():
    chart_liquid01 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="303班语文学科优秀率",
            data=[count1 / sum1, 0.3],
            center=["25%", "40%"],
            color='white',
            background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="303班语文学科优秀率",
                title_link="#",
            )
        )
    )
    chart_liquid02 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="303班数学学科优秀率",
            data=[count2 / sum2, 0.3],
            center=["25%", "40%"],
            # color='white',
            # background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="303班数学学科优秀率",
                title_link="#",
            )
        )
    )

    chart_liquid03 = (
        Liquid(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add(
            series_name="303班英语学科优秀率",
            data=[count3 / sum3, 0.3],
            center=["25%", "40%"],
            color='white',
            background_color='lightskyblue',
            is_outline_show=False,
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="303班英语学科优秀率",
                title_link="#",
            )
        )
    )
    return chart_liquid01, chart_liquid02, chart_liquid03


chart_liquid01_, chart_liquid02_, chart_liquid03_ = liquids()


chart_liquid01_.render('../../templates/visual/pyecharts_visual/liquid_c3_01.html')
chart_liquid02_.render('../../templates/visual/pyecharts_visual/liquid_c3_02.html')
chart_liquid03_.render('../../templates/visual/pyecharts_visual/liquid_c3_03.html')
