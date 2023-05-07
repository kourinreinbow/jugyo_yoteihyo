const datas = localStorage;

const finished_color = "#FF0000";
const unfinished_color = "#FFFFFF";

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
        emement_pearent.style.backgroundColor = "#FF0000";
    }
    else
    {
        emement_pearent.style.backgroundColor = "#FFFFFF";
    }

    saveData(key, element.checked);

}

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
            emement_pearent.style.backgroundColor = "#FF0000";
        }
        else
        {
            emement_pearent.style.backgroundColor = "#FFFFFF";
        }
        element.checked = setValue;
    }
}

// localStrageに存在し、実際の課題としては出ていない場合は削除する。
for(key in localStorage)
{
    if (localStorage.hasOwnProperty(key)){
        if(subject_exist_keys.indexOf(key) == -1)
        {
            removeData(key);
        }
    }
}