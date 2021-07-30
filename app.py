from flask import Flask, render_template, redirect, url_for, request
from chart import bar_base, gauge_base, pie_base, table_base, stack_line_base, wordcnt_base
import warnings

warnings.filterwarnings("ignore")
app = Flask(__name__, static_folder="templates")
app.secret_key = 'flaskBI'  # 设置表单交互密钥


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@app.route("/barChart", methods=['GET', "POST"])
def get_bar_chart():
    return bar_base().dump_options_with_quotes()


@app.route("/pieChart", methods=['GET', "POST"])
def get_pie_chart():
    return pie_base().dump_options_with_quotes()


@app.route("/table", methods=['GET', "POST"])
def get_table():
    return {"data": table_base().html_content}


@app.route("/stackline", methods=['GET', "POST"])
def get_stackline():
    return stack_line_base().dump_options_with_quotes()


@app.route("/wordcnt", methods=['GET', "POST"])
def get_wordcnt():
    return wordcnt_base().dump_options_with_quotes()


@app.route("/gaugeChart", methods=["POST"])
def get_gauge_chart():
    y = float(request.form['value'])
    return gauge_base(y).dump_options_with_quotes()


if __name__ == "__main__":
    app.run(debug=True)
