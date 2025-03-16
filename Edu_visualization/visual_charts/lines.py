from pyecharts.charts import Line
from pyecharts import options as opts
import pandas as pd

excel_path = "D:\桌面\数据可视化\data\education_score.xlsx"
data = pd.read_excel(io=excel_path, header=None)
data.columns = ['id', '学号', '课程号', '分数', '班级']
xaxis_data1 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '301')]["学号"].map(str).tolist()
yaxis_data1 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '301')]["分数"].tolist()
# print(yaxis_data)
# print(xaxis_data)
# max1 = max(yaxis_data1)
# print(max1)
# min1 = min(yaxis_data1)
# print(min1)
xaxis_data2 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '301')]["学号"].map(str).tolist()
yaxis_data2 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '301')]["分数"].tolist()
xaxis_data3 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '301')]["学号"].map(str).tolist()
yaxis_data3 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '301')]["分数"].tolist()

xaxis_data4 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '302')]["学号"].map(str).tolist()
yaxis_data4 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '302')]["分数"].tolist()
xaxis_data5 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '302')]["学号"].map(str).tolist()
yaxis_data5 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '302')]["分数"].tolist()
xaxis_data6 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '302')]["学号"].map(str).tolist()
yaxis_data6 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '302')]["分数"].tolist()

xaxis_data7 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '303')]["学号"].map(str).tolist()
yaxis_data7 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '303')]["分数"].tolist()
xaxis_data8 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '303')]["学号"].map(str).tolist()
yaxis_data8 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '303')]["分数"].tolist()
xaxis_data9 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '303')]["学号"].map(str).tolist()
yaxis_data9 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '303')]["分数"].tolist()


def lines():
    chart_line30101 = (
        Line(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add_xaxis(xaxis_data=xaxis_data1)
        .add_yaxis(
            series_name="301班语文成绩",
            y_axis=yaxis_data1,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )

        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), type_='category', boundary_gap=False),
            yaxis_opts=opts.AxisOpts(min_=50),
            title_opts=opts.TitleOpts(title="301班语文学科成绩", title_link="/Edu_visualization/teacher_visual/show_line30101/"),
            datazoom_opts=opts.DataZoomOpts(orient="horizontal"),
            tooltip_opts=opts.TooltipOpts(trigger='axis'),
        )
    )
    chart_line30102 = (
        Line(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add_xaxis(xaxis_data=xaxis_data2)
        .add_yaxis(
            series_name="301班数学成绩",
            y_axis=yaxis_data2,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )

        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), type_='category', boundary_gap=False),
            yaxis_opts=opts.AxisOpts(min_=50),
            title_opts=opts.TitleOpts(title="301班数学学科成绩", title_link="/Edu_visualization/teacher_visual/show_line30102/"),
            datazoom_opts=opts.DataZoomOpts(orient="horizontal"),
            tooltip_opts=opts.TooltipOpts(trigger='axis'),
        )
    )
    chart_line30103 = (
        Line(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add_xaxis(xaxis_data=xaxis_data3)
        .add_yaxis(
            series_name="301班英语成绩",
            y_axis=yaxis_data3,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )

        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), type_='category', boundary_gap=False),
            yaxis_opts=opts.AxisOpts(min_=50),
            title_opts=opts.TitleOpts(title="301班英语学科成绩", title_link="/Edu_visualization/teacher_visual/show_line30103/"),
            datazoom_opts=opts.DataZoomOpts(orient="horizontal"),
            tooltip_opts=opts.TooltipOpts(trigger='axis'),
        )
    )
    chart_line30201 = (
        Line(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add_xaxis(xaxis_data=xaxis_data4)
        .add_yaxis(
            series_name="302班语文成绩",
            y_axis=yaxis_data4,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )

        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), type_='category', boundary_gap=False),
            yaxis_opts=opts.AxisOpts(min_=50),
            title_opts=opts.TitleOpts(title="302班语文学科成绩", title_link="/Edu_visualization/teacher_visual/show_line30201/"),
            datazoom_opts=opts.DataZoomOpts(orient="horizontal"),
            tooltip_opts=opts.TooltipOpts(trigger='axis'),
        )
    )
    chart_line30202 = (
        Line(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add_xaxis(xaxis_data=xaxis_data5)
        .add_yaxis(
            series_name="302班数学成绩",
            y_axis=yaxis_data5,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )

        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), type_='category', boundary_gap=False),
            yaxis_opts=opts.AxisOpts(min_=50),
            title_opts=opts.TitleOpts(title="302班数学学科成绩", title_link="/Edu_visualization/teacher_visual/show_line30202/"),
            datazoom_opts=opts.DataZoomOpts(orient="horizontal"),
            tooltip_opts=opts.TooltipOpts(trigger='axis'),
        )
    )
    chart_line30203 = (
        Line(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add_xaxis(xaxis_data=xaxis_data6)
        .add_yaxis(
            series_name="302班英语成绩",
            y_axis=yaxis_data6,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )

        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), type_='category', boundary_gap=False),
            yaxis_opts=opts.AxisOpts(min_=50),
            title_opts=opts.TitleOpts(title="302班英语学科成绩", title_link="/Edu_visualization/teacher_visual/show_line30203/"),
            datazoom_opts=opts.DataZoomOpts(orient="horizontal"),
            tooltip_opts=opts.TooltipOpts(trigger='axis'),
        )
    )
    chart_line30301 = (
        Line(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add_xaxis(xaxis_data=xaxis_data7)
        .add_yaxis(
            series_name="303班语文成绩",
            y_axis=yaxis_data7,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )

        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), type_='category', boundary_gap=False),
            yaxis_opts=opts.AxisOpts(min_=50),
            title_opts=opts.TitleOpts(title="303班语文学科成绩", title_link="/Edu_visualization/teacher_visual/show_line30301/"),
            datazoom_opts=opts.DataZoomOpts(orient="horizontal"),
            tooltip_opts=opts.TooltipOpts(trigger='axis'),
        )
    )
    chart_line30302 = (
        Line(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add_xaxis(xaxis_data=xaxis_data8)
        .add_yaxis(
            series_name="303班数学成绩",
            y_axis=yaxis_data8,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )

        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), type_='category', boundary_gap=False),
            yaxis_opts=opts.AxisOpts(min_=50),
            title_opts=opts.TitleOpts(title="303班数学学科成绩", title_link="/Edu_visualization/teacher_visual/show_line30302/"),
            datazoom_opts=opts.DataZoomOpts(orient="horizontal"),
            tooltip_opts=opts.TooltipOpts(trigger='axis'),
        )
    )
    chart_line30303 = (
        Line(init_opts=opts.InitOpts(width='740px', height='450px'))
        .add_xaxis(xaxis_data=xaxis_data9)
        .add_yaxis(
            series_name="303班英语成绩",
            y_axis=yaxis_data9,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  # 面积图
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average")]
            )
        )

        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), type_='category', boundary_gap=False),
            yaxis_opts=opts.AxisOpts(min_=50),
            title_opts=opts.TitleOpts(title="303班英语学科成绩", title_link="/Edu_visualization/teacher_visual/show_line30303/"),
            datazoom_opts=opts.DataZoomOpts(orient="horizontal"),
            tooltip_opts=opts.TooltipOpts(trigger='axis'),
        )
    )
    return chart_line30101, chart_line30102, chart_line30103, \
        chart_line30201, chart_line30202, chart_line30203, \
        chart_line30301, chart_line30302, chart_line30303


chart_Line30101_, chart_Line30102_, chart_Line30103_, \
    chart_Line30201_, chart_Line30202_, chart_Line30203_, \
    chart_Line30301_, chart_Line30302_, chart_Line30303_ = lines()

chart_Line30101_.render("../../templates/visual/pyecharts_visual/line30101.html")
chart_Line30102_.render("../../templates/visual/pyecharts_visual/line30102.html")
chart_Line30103_.render("../../templates/visual/pyecharts_visual/line30103.html")

chart_Line30201_.render("../../templates/visual/pyecharts_visual/line30201.html")
chart_Line30202_.render("../../templates/visual/pyecharts_visual/line30202.html")
chart_Line30203_.render("../../templates/visual/pyecharts_visual/line30203.html")

chart_Line30301_.render("../../templates/visual/pyecharts_visual/line30301.html")
chart_Line30302_.render("../../templates/visual/pyecharts_visual/line30302.html")
chart_Line30303_.render("../../templates/visual/pyecharts_visual/line30303.html")
