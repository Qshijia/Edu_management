from pyecharts.charts import Page
from Edu_visualization.visual_charts import bar_all, line301, liquid301, box301


def first_run():
    chartline = line301.line()
    chartliquid01, chartliquid02, chartliquid03 = liquid301.liquids()
    charBxplot = box301.boxplot()
    chartBar = bar_all.bar()
    page = Page(page_title="教育数据可视化大屏", layout=Page.DraggablePageLayout)
    page.add(chartline, chartliquid01, chartliquid02, chartliquid03, charBxplot, chartBar)
    page.render("../../templates/visual/pyecharts_visual/render301.html")


def second_run():
    Page.save_resize_html(source='../../templates/visual/pyecharts_visual/render301.html', cfg_file="./chart_config301.json", dest="../../templates/visual/pyecharts_visual/result_301.html")


if __name__ == '__main__':
    # first_run()
    second_run()
