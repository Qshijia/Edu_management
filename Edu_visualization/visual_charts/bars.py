from pyecharts.charts import Bar
from pyecharts import options as opts
import pandas as pd


excel_path = "D:\桌面\数据可视化\data\education_score.xlsx"
data = pd.read_excel(io=excel_path, header=None)
data.columns = ['id', '学号', '课程号', '分数', '班级']
# xaxis_data1 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '301')]["学号"].map(str).tolist()
data1 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '301')]["分数"].tolist()
data2 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '301')]["分数"].tolist()
data3 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '301')]["分数"].tolist()
data4 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '302')]["分数"].tolist()
data5 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '302')]["分数"].tolist()
data6 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '302')]["分数"].tolist()
data7 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '303')]["分数"].tolist()
data8 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '303')]["分数"].tolist()
data9 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '303')]["分数"].tolist()

# 30101
count1 = 0  # 人数
sum1 = 0  # 学科总分
for data in data1:
    sum1 += data
    count1 += 1
aver1 = sum1 / count1
# 30102
count2 = 0
sum2 = 0
for data in data2:
    sum2 += data
    count2 += 1
aver2 = sum2 / count2
# 30103
count3 = 0
sum3 = 0
for data in data3:
    sum3 += data
    count3 += 1
aver3 = sum3 / count3
# 30201
count4 = 0
sum4 = 0
for data in data4:
    sum4 += data
    count4 += 1
aver4 = sum4 / count4
# 30202
count5 = 0  # 人数
sum5 = 0  # 学科总分
for data in data5:
    sum5 += data
    count5 += 1
aver5 = sum5 / count5
# 30203
count6 = 0  # 人数
sum6 = 0  # 学科总分
for data in data6:
    sum6 += data
    count6 += 1
aver6 = sum6 / count6
# 30301
count7 = 0  # 人数
sum7 = 0  # 学科总分
for data in data7:
    sum7 += data
    count7 += 1
aver7 = sum7 / count7

# 30302
count8 = 0  # 人数
sum8 = 0  # 学科总分
for data in data8:
    sum8 += data
    count8 += 1
aver8 = sum8 / count8

# 30303
count9 = 0  # 人数
sum9 = 0  # 学科总分
for data in data9:
    sum9 += data
    count9 += 1
aver9 = sum9 / count9

# 01
yaxis_data01 = []
yaxis_data01.append(aver1)
yaxis_data01.append(aver4)
yaxis_data01.append(aver7)
max01 = max(yaxis_data01)
min01 = min(yaxis_data01)
# 02
yaxis_data02 = []
yaxis_data02.append(aver2)
yaxis_data02.append(aver5)
yaxis_data02.append(aver8)
max02 = max(yaxis_data02)
min02 = min(yaxis_data02)
# 03
yaxis_data03 = []
yaxis_data03.append(aver3)
yaxis_data03.append(aver6)
yaxis_data03.append(aver9)
max03 = max(yaxis_data03)
min03 = min(yaxis_data03)


def bars():
    chart_bar01 = (
        Bar(
            init_opts=opts.InitOpts(width='700px', height='450px')
        )
        .add_xaxis(['301', '302', '303'])
        .add_yaxis(
            series_name="语文学科平均分排名",
            y_axis=yaxis_data01,
            is_show_background=True,
            label_opts=opts.LabelOpts(
                position="right",
                formatter="{b}班：{c}分"
            )
        )
        .reversal_axis()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=True), min_=60),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            title_opts=opts.TitleOpts(
                title="语文学科平均分排名",
                title_link="/Edu_visualization/teacher_visual/show_bar01/"
            ),
            visualmap_opts=opts.VisualMapOpts(
                dimension=0,
                range_text=['最大值', '最小值'],
                is_calculable=True,
                textstyle_opts=opts.TextStyleOpts(
                     color="rgba(0,0,0,0.5)"
                 ),
                min_=round(min01, 2),
                max_=round(max01, 2),
            )
        )
    )
    chart_bar02 = (
        Bar(
            init_opts=opts.InitOpts(width='700px', height='450px')
        )
        .add_xaxis(['301', '302', '303'])
        .add_yaxis(
            series_name="数学学科平均分排名",
            y_axis=yaxis_data02,
            is_show_background=True,
            label_opts=opts.LabelOpts(
                position="right",
                formatter="{b}班：{c}分"
            )
        )
        .reversal_axis()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=True), min_=60),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            title_opts=opts.TitleOpts(
                title="数学学科平均分排名",
                title_link="/Edu_visualization/teacher_visual/show_bar02/"
            ),
            visualmap_opts=opts.VisualMapOpts(
                dimension=0,
                range_text=['最大值', '最小值'],
                is_calculable=True,
                textstyle_opts=opts.TextStyleOpts(
                    color="rgba(0,0,0,0.5)"
                ),
                min_=round(min02, 2),
                max_=round(max02, 2),
            )
        )
    )
    chart_bar03 = (
        Bar(
            init_opts=opts.InitOpts(width='700px', height='450px')
        )
        .add_xaxis(['301', '302', '303'])
        .add_yaxis(
            series_name="英语学科平均分排名",
            y_axis=yaxis_data03,
            is_show_background=True,
            label_opts=opts.LabelOpts(
                position="right",
                formatter="{b}班：{c}分"
            )
        )
        .reversal_axis()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=True), min_=60),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            title_opts=opts.TitleOpts(
                title="英语学科平均分排名",
                title_link="/Edu_visualization/teacher_visual/show_bar03/"
            ),
            visualmap_opts=opts.VisualMapOpts(
                dimension=0,
                range_text=['最大值', '最小值'],
                is_calculable=True,
                textstyle_opts=opts.TextStyleOpts(
                    color="rgba(0,0,0,0.5)"
                ),
                min_=round(min03, 2),
                max_=round(max03, 2),
            )
        )
    )
    return chart_bar01, chart_bar02, chart_bar03


chart_bar01_, chart_bar02_, chart_bar03_ = bars()
chart_bar01_.render('../../templates/visual/pyecharts_visual/bar01.html')
chart_bar02_.render('../../templates/visual/pyecharts_visual/bar02.html')
chart_bar03_.render('../../templates/visual/pyecharts_visual/bar03.html')
