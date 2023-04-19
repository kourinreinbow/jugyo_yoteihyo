import datetime

kadai_datas = \
[
 ["ディジタル回路演習：レポート", datetime.datetime(2023,5,1,0,0)],
 ["応用数学Ⅱ：課題01", datetime.datetime(2023,4,23,23,59)],
 ["応用数学Ⅱ：課題02", datetime.datetime(2023,4,23,23,59)]
 ]

template_html = \
"""
<tr>
    <th>{}</th>
    <td>{}月{}日{}時{}分</td>
    <td><form method="GET"><input type="checkbox" name="kadai{}">　<input type="submit" value="変更"></form></td>
</tr>
"""

f_sample_html = open("./sample.html", "r", encoding="utf-8")
f_index_html = open("./index.html", "w", encoding="utf-8")
f_sample_css = open("./sample.css", "r", encoding="utf-8")
f_index_css = open("./index.css", "w", encoding="utf-8")

write_html = ""
for index, kadai_data in enumerate(kadai_datas):
    date:datetime.datetime = kadai_data[1]
    write_html += template_html.format(kadai_data[0], date.year, date.month, date.hour, date.minute, index)

# テンプレートのデータを読み込む
f_sample_html_data = f_sample_html.read()
f_sample_css_data = f_sample_css.read()

# 書き込み
f_index_html.write(f_sample_html_data.replace("<article></article>", write_html))
f_index_css.write(f_sample_css_data)

f_sample_html.close()
f_index_html.close()
f_sample_css.close()
f_index_css.close()