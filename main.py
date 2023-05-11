import datetime

kadai_datas = \
[
 ["応用数学Ⅱ", "課題052", datetime.datetime(2023,5,15)],
 ["ソフトウェア工学","レポート4 (※Teams)2", datetime.datetime(2023,5,23,13,0)],
 ["データベース","第5回課題2", datetime.datetime(2023,5,23)],
 
 # 追加部分
 ["工学実験Ⅴ","第4回分2", datetime.datetime(2023,5,18,9)], 
#  ["工学実験Ⅴ","プレゼンファイル1", datetime.datetime(2023,5,25,13)], 
#  ["工学実験Ⅴ","実験レポート3", datetime.datetime(2023,5,25,13)], 
#  ["工学実験Ⅴ","外部/内部設計書の提出4", datetime.datetime(2023,5,25,13)], 

 # 次回の授業まで
 ["応用物理Ⅱ","プリント課題1", "次回の授業まで"]
 ]

subject_ja2en = \
{"日本語表現法":"nihongo-hyogenhou",
 "技術者倫理":"gijutusya-rinri",
 "保健・体育":"hoken-taiiku",
 "英語Ⅳ":"eigo-4",
 "応用数学Ⅰ":"ouyou-sugaku-1",
 "応用数学Ⅱ":"ouyou-sugaku-2",
 "応用数学Ⅲ":"ouyou-sugaku-3",
 "応用物理Ⅱ":"ouyou-buturi-2",
 "ディジタル回路":"dhijitaru-kairo",
 "ディジタル回路演習":"dhijitaru-kairo-ensyu",
 "離散数学":"risan-sugaku",
 "情報理論":"joho-riron",
 "ソフトウェア工学":"sohutowea-kougaku",
 "データベース":"database",
 "符号理論":"hugo-riron",
 "コンピュータアーキテクチャ":"computer-akitekutya",
 "情報数学":"joho-sugaku",
 "アルゴリズムとデータ構造":"arugorizumu-and-detakouzou",
 "工学実験Ⅴ":"kogaku-jikken-5",
 "工学実験Ⅵ":"kogaku-jikken-6"}

template_html = \
"""
<tr>
    <th>{}</th>
    <td>{}</td>
    <td>{}/{:02d}/{:02d}/{:02d}:{:02d}</td>
    <td><input type="checkbox" class="subject_exist_keys" id="{}" disabled="disabled">　<input type="button" value="変更" onclick="change_checkbox(\'{}\')"></td>
</tr>
"""

template_html_jikaiVer = \
"""
<tr>
    <th>{}</th>
    <td>{}</td>
    <td>{}</td>
    <td><input type="checkbox" class="subject_exist_keys" id="{}" disabled="disabled">　<input type="button" value="変更" onclick="change_checkbox(\'{}\')"></td>
</tr>
"""

f_sample_html = open("./sample.html", "r", encoding="utf-8")
f_index_html = open("./index.html", "w", encoding="utf-8")
f_sample_css = open("./sample.css", "r", encoding="utf-8")
f_index_css = open("./index.css", "w", encoding="utf-8")

# kadai_datasを日付順に並べ替える
changed = True
while changed:
    changed = False
    for index in range(len(kadai_datas)-1):
        if type(kadai_datas[index][2]) == str or type(kadai_datas[index+1][2]) == str:
            continue

        temp_date:datetime.datetime = kadai_datas[index][2]
        next_temp_date:datetime.datetime = kadai_datas[index+1][2]

        # 年のみ
        if temp_date.year > next_temp_date.year:
            temp = kadai_datas[index+1]
            kadai_datas[index+1] = kadai_datas[index]
            kadai_datas[index] = temp
            changed = True

        # 年は同じで、月が違うとき
        if temp_date.year == next_temp_date.year and temp_date.month > next_temp_date.month:
            temp = kadai_datas[index+1]
            kadai_datas[index+1] = kadai_datas[index]
            kadai_datas[index] = temp
            changed = True
        
        # 年と月が同じで日付が違うとき
        if temp_date.year == next_temp_date.year and temp_date.month == next_temp_date.month and temp_date.day > next_temp_date.day:
            temp = kadai_datas[index+1]
            kadai_datas[index+1] = kadai_datas[index]
            kadai_datas[index] = temp
            changed = True

        # 年と月と日付が同じでhourが違うとき
        if temp_date.year == next_temp_date.year and temp_date.month == next_temp_date.month and temp_date.day == next_temp_date.day \
            and temp_date.hour > next_temp_date.hour:
            temp = kadai_datas[index+1]
            kadai_datas[index+1] = kadai_datas[index]
            kadai_datas[index] = temp
            changed = True

min_date = kadai_datas[0][2].day
min_month = kadai_datas[0][2].month

# 書き込むhtmlを生成する
write_html = ""
for index, kadai_data in enumerate(kadai_datas):
    date:datetime.datetime = kadai_data[2]
    star = "<img src='./svg-sample.svg' width='15px' height='15px'>"
    temp_str = ""
    
    if type(date) == str:
        write_html += template_html_jikaiVer.format(kadai_data[0], kadai_data[1][:-1], date, subject_ja2en[kadai_data[0]]+"_"+kadai_data[1][-1], subject_ja2en[kadai_data[0]]+"_"+kadai_data[1][-1])
    else:
        if date.month == min_month and date.day == min_date:
            temp_str = star
            # print(date.month, date.day)
        write_html += template_html.format(temp_str + kadai_data[0], kadai_data[1][:-1], date.year, date.month, date.day, date.hour, date.minute, subject_ja2en[kadai_data[0]]+"_"+kadai_data[1][-1], subject_ja2en[kadai_data[0]]+"_"+kadai_data[1][-1])

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