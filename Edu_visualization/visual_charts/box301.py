from pyecharts.charts import Boxplot
from pyecharts import options as opts
import pandas as pd

excel_path = "D:\桌面\数据可视化\data\education_score.xlsx"
data = pd.read_excel(io=excel_path, header=None)
data.columns = ['id', '学号', '课程号', '分数', '班级']
yaxis_data1 = data.loc[(data['课程号'].map(str) == '1') & (data['班级'].map(str) == '301')]["分数"].tolist()
yaxis_data2 = data.loc[(data['课程号'].map(str) == '2') & (data['班级'].map(str) == '301')]["分数"].tolist()
yaxis_data3 = data.loc[(data['课程号'].map(str) == '3') & (data['班级'].map(str) == '301')]["分数"].tolist()
yaxis_data=[]
yaxis_data.append(yaxis_data1)
yaxis_data.append(yaxis_data2)
yaxis_data.append(yaxis_data3)
# print(yaxis_data)


def boxplot():
    chart_box = (
        Boxplot(
            init_opts=opts.InitOpts(
                width='700px',
                height='450px',
            )
        )
        .add_xaxis(['语文', '数学', '英语'])
        .add_yaxis(
            '301班学科分数分布',
            Boxplot().prepare_data(yaxis_data),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='301班学科成绩分布',  # 主标题
                title_link='#',  # 主标题点击跳转链接
                title_target='blank',  # blank新窗口打开（默认），self当前窗口打开
            ),
            yaxis_opts=opts.AxisOpts(
                min_=50
            )
        )
    )
    return chart_box


chart_boxplot = boxplot()
chart_boxplot.render("../../templates/visual/pyecharts_visual/box301.html")
