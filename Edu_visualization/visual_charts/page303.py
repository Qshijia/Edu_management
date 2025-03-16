from pyecharts.charts import Page
from Edu_visualization.visual_charts import bar_all, line303, liquid303, box303


def first_run():
    chartline = line303.line()
    chartliquid01, chartliquid02, chartliquid03 = liquid303.liquids()
    charBxplot = box303.boxplot()
    chartBar = bar_all.bar()
    page = Page(page_title="教育数据可视化大屏", layout=Page.DraggablePageLayout)
    page.add(chartline, chartliquid01, chartliquid02, chartliquid03, charBxplot, chartBar)
    page.render("../../templates/visual/pyecharts_visual/render303.html")


def second_run():
    Page.save_resize_html(source='../../templates/visual/pyecharts_visual/render303.html', cfg_file="./chart_config303.json", dest="../../templates/visual/pyecharts_visual/result_303.html")


if __name__ == '__main__':
    # first_run()
    second_run()
