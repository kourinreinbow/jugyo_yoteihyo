import datetime

kadai_datas = \
[
 ["ディジタル回路演習：レポート", datetime.datetime(2023,5,1,0,0)],
 ["応用数学Ⅱ：課題01", datetime.datetime(2023,4,23,23,59)],
 ["応用数学Ⅱ：課題02", datetime.datetime(2023,4,23,23,59)],
 ["情報理論：第1章,章末問題", datetime.datetime(2023,5,8)],
 ["ソフトウェア工学：PERT図", datetime.datetime(2023,4,25,13,0)],
 [" データベース：第２回課題", datetime.datetime(2023,4,25)],
 ["工学実験Ⅴ：第１回分", datetime.datetime(2023,4,20,8,40)],
 ["応用物理Ⅱ：プリント課題", "次回の授業まで"]
 ]

template_html = \
"""
<tr>
    <th>{}</th>
    <td>{}/{:02d}/{:02d}/{:02d}:{:02d}</td>
    <!--<td><form method="GET"><input type="checkbox" name="kadai{}">　<input type="submit" value="変更"></form></td>-->
</tr>
"""

template_html_jikaiVer = \
"""
<tr>
    <th>{}</th>
    <td>{}</td>
    <!--<td><form method="GET"><input type="checkbox" name="kadai{}">　<input type="submit" value="変更"></form></td>-->
</tr>
"""

f_sample_html = open("./sample.html", "r", encoding="utf-8")
f_index_html = open("./index.html", "w", encoding="utf-8")
f_sample_css = open("./sample.css", "r", encoding="utf-8")
f_index_css = open("./index.css", "w", encoding="utf-8")

write_html = ""
for index, kadai_data in enumerate(kadai_datas):
    date:datetime.datetime = kadai_data[1]
    if type(date) == str:
        write_html += template_html_jikaiVer.format(kadai_data[0], date, index)
    else:
        write_html += template_html.format(kadai_data[0], date.year, date.month, date.day, date.hour, date.minute, index)

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