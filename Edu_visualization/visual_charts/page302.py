from pyecharts.charts import Page
from Edu_visualization.visual_charts import bar_all, line302, liquid302, box302


def first_run():
    chartline = line302.line()
    chartliquid01, chartliquid02, chartliquid03 = liquid302.liquids()
    charBxplot = box302.boxplot()
    chartBar = bar_all.bar()
    page = Page(page_title="教育数据可视化大屏", layout=Page.DraggablePageLayout)
    page.add(chartline, chartliquid01, chartliquid02, chartliquid03, charBxplot, chartBar)
    page.render("../../templates/visual/pyecharts_visual/render302.html")


def second_run():
    Page.save_resize_html(source='../../templates/visual/pyecharts_visual/render302.html', cfg_file="./chart_config302.json", dest="../../templates/visual/pyecharts_visual/result_302.html")


if __name__ == '__main__':
    # first_run()
    second_run()
