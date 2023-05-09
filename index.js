const datas = localStorage;

let finished_color = "#FF0000";
let unfinished_color = "#FFFFFF";

window.onload = function()
{
    let fin_col = getData("finished_color");
    console.log(fin_col);
    let unfin_col = getData("unfinished_color");
    if(fin_col != null)
    {
        finished_color = fin_col;
    }
    if(unfin_col != null)
    {
        unfinished_color = unfin_col;
    }

    render();
}

function isColor (color) 
{
    // https://zukucode.com/2017/04/javascript-color-check.html
    return color.match(/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/) !== null;
}

function get_finished_color()
{
    let color = document.getElementById("fcolor");
    console.log(color.value);
    if(isColor(color.value))
    {
        finished_color = color.value;
        saveData("finished_color", finished_color);
        render();
    }
    else
    {
        alert(color.value + "is not color code.");
    }
}

function get_unfinished_color()
{
    let color = document.getElementById("ufcolor");
    console.log(color.value);
    if(isColor(color.value))
    {
        unfinished_color = color.value;
        saveData("unfinished_color", unfinished_color);
        render();
    }
    else
    {
        alert(color.value + "is not color code.");
    }
}

function saveData(name, value) {
    datas.setItem(name, value);
}

function getData(name) {
    return datas.getItem(name);
}

function removeData(name) {
    datas.removeItem(name);
}

function clearData() {
    datas.clear();
}

function list_to_string(list)
{
    let str = "";
    for (let i = 0; i < list.length; i++) {
        str += list[i] + ",";
    }
    
    return str.slice(0,-1);
}

function string_to_list(string)
{
    return string.split(",");
}

function change_checkbox(key)
{
    let element = document.getElementById(key);
    let emement_pearent = element.parentNode.parentNode;
    element.checked = !element.checked;
    if(element.checked)
    {
        emement_pearent.style.backgroundColor = finished_color;
    }
    else
    {
        emement_pearent.style.backgroundColor = unfinished_color;
    }

    saveData(key, element.checked);

}


function render()
{
    // subject_exist_keys が、実際に出ている宿題のkey。
    let subject_exist_elements = document.getElementsByClassName("subject_exist_keys")
    let subject_exist_keys = [];
    for(let i=0; i<subject_exist_elements.length; i++){
        // console.log(subject_exist_elements[i].id);
        let key = subject_exist_elements[i].id;
        subject_exist_keys[i] = key;
        // 宿題がストレージに登録されていない場合に登録する。
        var gottenData = getData(key);
        if(gottenData == null)
        {
            saveData(key, false);
        }
        else
        {
            // 登録されている and checkedの場合は、idを検索し、checkedに変える。
            let element = document.getElementById(key);
            let emement_pearent = element.parentNode.parentNode;

            let setValue = false;
            if(gottenData == "true")
            {
                setValue = true;
                emement_pearent.style.backgroundColor = finished_color;
            }
            else
            {
                emement_pearent.style.backgroundColor = unfinished_color;
            }
            element.checked = setValue;
        }
    }

    // localStrageに存在し、実際の課題としては出ていない場合は削除する。
    for(key in localStorage)
    {
        if(key == "finished_color" || key == "unfinished_color")
        {
            continue;
        }
        if (localStorage.hasOwnProperty(key)){
            if(subject_exist_keys.indexOf(key) == -1)
            {
                removeData(key);
            }
        }
    }
}