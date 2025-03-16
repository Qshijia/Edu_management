from pyecharts.charts import Bar
from pyecharts import options as opts
import pandas as pd

excel_path = "D:\桌面\数据可视化\data\education_score.xlsx"
data = pd.read_excel(io=excel_path, header=None)
data.columns = ['id', '学号', '课程号', '分数', '班级']
data301 = data.loc[(data['班级'].map(str) == '301')]["分数"].tolist()
data302 = data.loc[(data['班级'].map(str) == '302')]["分数"].tolist()
data303 = data.loc[(data['班级'].map(str) == '303')]["分数"].tolist()

# 301
count301 = 0  # 人数
sum301 = 0  # 总分
for data in data301:
    sum301 += data
    count301 += 1
count301 = count301/3
aver301 = sum301 / count301

# 302
count302 = 0  # 人数
sum302 = 0  # 总分
for data in data302:
    sum302 += data
    count302 += 1
count302 = count302/3
aver302 = sum302 / count302

# 303
count303 = 0  # 人数
sum303 = 0  # 总分
for data in data303:
    sum303 += data
    count303 += 1
count303 = count303/3
aver303 = sum303 / count303

yaxis_data = []
yaxis_data.append(aver301)
yaxis_data.append(aver302)
yaxis_data.append(aver303)

max = max(yaxis_data)
min = min(yaxis_data)


def bar():
    chart_bar = (
        Bar(init_opts=opts.InitOpts(width='1000px', height='450px'))
        .add_xaxis(['301', '302', '303'])
        .add_yaxis(
            series_name="各班级总成绩平均分排名",
            y_axis=yaxis_data,
            is_show_background=True,
            label_opts=opts.LabelOpts(
                position="right",
                formatter="{b}班：{c}分"
            )
        )
        .reversal_axis()
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            title_opts=opts.TitleOpts(
                title="各班级总成绩平均分排名",
                title_link="#"
            ),
            visualmap_opts=opts.VisualMapOpts(
                dimension=0,
                range_text=['最大值', '最小值'],
                is_calculable=True,
                textstyle_opts=opts.TextStyleOpts(
                     color="rgba(0,0,0,0.5)"
                 ),
                min_=round(min, 2),
                max_=round(max, 2),
            )
        )
    )
    return chart_bar


chart_bar = bar()
chart_bar.render("../../templates/visual/pyecharts_visual/bar_all.html")
