from pyecharts.charts import Line
from pyecharts import options as opts
import pandas as pd

excel_path = "D:\桌面\数据可视化\data\education_score.xlsx"
data = pd.read_excel(io=excel_path, header=None)
data.columns = ['id', '学号', '课程号', '分数', '班级']
xaxis_data = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '303')]["学号"].map(str).tolist()
yaxis_data1 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '303')]["分数"].tolist()
yaxis_data2 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '303')]["分数"].tolist()
yaxis_data3 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '303')]["分数"].tolist()
max1 = max(yaxis_data1)
min1 = min(yaxis_data1)
max2 = max(yaxis_data2)
min2 = min(yaxis_data2)
max3 = max(yaxis_data3)
min3 = min(yaxis_data3)


def line():
    chart_line = (
        Line()
        .add_xaxis(xaxis_data=xaxis_data)
        .add_yaxis(
            series_name="语文成绩",
            y_axis=yaxis_data1,
            stack='堆叠',
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )
        .add_yaxis(
            series_name="数学成绩",
            y_axis=yaxis_data2,
            stack='堆叠',
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )
        .add_yaxis(
            series_name="英语成绩",
            y_axis=yaxis_data3,
            stack='堆叠',
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), type_='category', boundary_gap=False),
            yaxis_opts=opts.AxisOpts(min_=50),
            title_opts=opts.TitleOpts(title="303班各学科学生成绩", title_link="#"),
            datazoom_opts=opts.DataZoomOpts(orient="horizontal"),
            tooltip_opts=opts.TooltipOpts(trigger='axis'),
        )
    )
    return chart_line


chartLine = line()
chartLine.render("../../templates/visual/pyecharts_visual/line303.html")
