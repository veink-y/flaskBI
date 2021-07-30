from random import randrange
from pyecharts import options as opts
from pyecharts.charts import Bar, Gauge, Pie, Line, WordCloud
from sqlalchemy import create_engine
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts

from pyecharts.globals import SymbolType

sqlite_engine = create_engine('sqlite:///log.db')

fn = """
    function(params) {
        if(params.name == '其他')
            return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
        return params.name + ' : ' + params.value + '%';
    }
    """


def new_label_opts():
    return opts.LabelOpts(formatter=JsCode(fn), position="center")


def bar_base() -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
            .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar", subtitle="test"))
    )
    return c


def gauge_base(perce: float) -> Gauge:
    c = (
        Gauge(init_opts=opts.InitOpts(width="600px", height="800px"))
            .add(series_name="业务指标", data_pair=[["完成率", perce]])
            .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(
                is_show=True, formatter="{a} <br/>{b} : {c}%"),
            title_opts=opts.TitleOpts(title="Gauge", subtitle="test"))
    )
    return c


def table_base():
    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    # headers = []
    rows = [
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Adelaide", 1295, 1158259, 600.5],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
    table = Table().add(headers, rows,
                        attributes={"border": "1", "cellspacing": '0'})
    return table


def pie_base():
    c = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(["剧情", "其他"], [25, 75])],
            center=["20%", "30%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
            .add(
            "",
            [list(z) for z in zip(["奇幻", "其他"], [24, 76])],
            center=["55%", "30%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
            .add(
            "",
            [list(z) for z in zip(["爱情", "其他"], [14, 86])],
            center=["20%", "70%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
            .add(
            "",
            [list(z) for z in zip(["惊悚", "其他"], [11, 89])],
            center=["55%", "70%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
    )
    return c


def wordcnt_base():
    words = [
        ("Sam S Club", 10000),
        ("Macys", 6181),
        ("Amy Schumer", 4386),
        ("Jurassic World", 4055),
        ("Charter Communications", 2467),
        ("Chick Fil A", 2244),
        ("Planet Fitness", 1868),
        ("Pitch Perfect", 1484),
        ("Express", 1112),
        ("Home", 865),
        ("Johnny Depp", 847),
        ("Lena Dunham", 582),
        ("Lewis Hamilton", 555),
        ("KXAN", 550),
        ("Mary Ellen Mark", 462),
        ("Farrah Abraham", 366),
        ("Rita Ora", 360),
        ("Serena Williams", 282),
        ("NCAA baseball tournament", 273),
        ("Point Break", 265),
    ]
    c = (
        WordCloud()
            .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    )
    return c


def stack_line_base():
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data = [820, 932, 901, 934, 1290, 1330, 1320]

    c = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="邮件营销",
            stack="总量",
            y_axis=[120, 132, 101, 134, 90, 230, 210],
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            series_name="联盟广告",
            stack="总量",
            y_axis=[220, 182, 191, 234, 290, 330, 310],
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            series_name="视频广告",
            stack="总量",
            y_axis=[150, 232, 201, 154, 190, 330, 410],
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            series_name="直接访问",
            stack="总量",
            y_axis=[320, 332, 301, 334, 390, 330, 320],
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            series_name="搜索引擎",
            stack="总量",
            y_axis=[820, 932, 901, 934, 1290, 1330, 1320],
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=True, position="top"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="堆叠区域图"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
    )
    return c


if __name__ == '__main__':
    print(table_base().html_content)
