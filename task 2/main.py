import requests
from bs4 import BeautifulSoup as BS
import json
import time, datetime


start_time = time.time()

def get_data():

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Mobile Safari/537.36"
    }

    url = "https://ru.m.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    
    #Списки для хранения слов по алфавиту
    a_animals_data = []
    b_animals_data = []
    v_animals_data = []
    g_animals_data = []
    d_animals_data = []
    e_animals_data = []
    ee_animals_data = []
    zh_animals_data = []
    z_animals_data = []
    i_animals_data = []
    ii_animals_data = []
    k_animals_data = []
    l_animals_data = []
    m_animals_data = []
    n_animals_data = []
    o_animals_data = []
    p_animals_data = []
    r_animals_data = []
    s_animals_data = []
    t_animals_data = []
    u_animals_data = []
    f_animals_data = []
    h_animals_data = []
    c_animals_data = []
    ch_animals_data = []
    sh_animals_data = []
    shh_animals_data = []
    ye_animals_data = []
    yu_animals_data = []
    ya_animals_data = []

    all_animals_data = []

    n = 0

    response = requests.get(url=url, headers=headers).text
    
    while True:

        soup = BS(response, "lxml")

        n+=1

        #Выполнение цикла для русского алфавита
        sercher = soup.find("div", id="mw-pages").find("div", class_="mw-category-group").find("h3").text
        if sercher == 'A':
            break
        else:
            #Сбор названий животных
            animals = soup.find("div", id="mw-pages").find_all("li")   
            for animal_text in animals:
                animals_title = animal_text.find("a").text.strip()
                print(animals_title)

                #Сортировка по первой букве
                symbol = animals_title[0]
                if symbol == "А":
                    a_animals_data.append (
                        animals_title
                    )
                elif symbol == "Б":
                    b_animals_data.append (
                        animals_title
                    )
                elif symbol == "В":
                    v_animals_data.append (
                        animals_title
                    )
                elif symbol == "Г":
                    g_animals_data.append (
                        animals_title
                    )
                elif symbol == "Д":
                    d_animals_data.append (
                        animals_title
                    )
                elif symbol == "Е":
                    e_animals_data.append (
                        animals_title
                    )
                elif symbol == "Ё":
                    ee_animals_data.append (
                        animals_title
                    )
                elif symbol == "Ж":
                    zh_animals_data.append (
                        animals_title
                    )
                elif symbol == "З":
                    z_animals_data.append (
                        animals_title
                    )
                elif symbol == "И":
                    i_animals_data.append (
                        animals_title
                    )
                elif symbol == "Й":
                    ii_animals_data.append (
                        animals_title
                    )
                elif symbol == "К":
                    k_animals_data.append (
                        animals_title
                    )
                elif symbol == "Л":
                    l_animals_data.append (
                        animals_title
                    )
                elif symbol == "М":
                    m_animals_data.append (
                        animals_title
                    )
                elif symbol == "Н":
                    n_animals_data.append (
                        animals_title
                    )
                elif symbol == "О":
                    o_animals_data.append (
                        animals_title
                    )
                elif symbol == "П":
                    p_animals_data.append (
                        animals_title
                    )
                elif symbol == "Р":
                    r_animals_data.append (
                        animals_title
                    )
                elif symbol == "С":
                    s_animals_data.append (
                        animals_title
                    )
                elif symbol == "Т":
                    t_animals_data.append (
                        animals_title
                    )
                elif symbol == "У":
                    u_animals_data.append (
                        animals_title
                    )
                elif symbol == "Ф":
                    f_animals_data.append (
                        animals_title
                    )
                elif symbol == "Х":
                    h_animals_data.append (
                        animals_title
                    )
                elif symbol == "Ц":
                    z_animals_data.append (
                        animals_title
                    )
                elif symbol == "Ч":
                    ch_animals_data.append (
                        animals_title
                    )
                elif symbol == "Ш":
                    sh_animals_data.append (
                        animals_title
                    )
                elif symbol == "Щ":
                    shh_animals_data.append (
                        animals_title
                    )
                elif symbol == "Э":
                    ye_animals_data.append (
                        animals_title
                    )
                elif symbol == "Ю":
                    yu_animals_data.append (
                        animals_title
                    )
                elif symbol == "Я":
                    ya_animals_data.append (
                        animals_title
                    )
                else:
                    break
            time.sleep(1)

            #Переход на следующую страницу
            next_page = soup.find('div', id='mw-pages').find_all('a')
            for a in next_page:
                if a.text == 'Следующая страница':
                    url = 'https://ru.wikipedia.org/' + a.get('href')
                    response = requests.get(url).text
            
    print(f"\n\nОбработано страниц: {n}\n\n")

    #Добавление данных в списки        
    all_animals_data.append(
        {
            "А": a_animals_data,
            "Б": b_animals_data,
            "В": v_animals_data,
            "Г": g_animals_data,
            "Д": d_animals_data,
            "Е": e_animals_data,
            "Ё": ee_animals_data,
            "Ж": zh_animals_data,
            "З": z_animals_data,
            "И": i_animals_data,
            "Й": ii_animals_data,
            "К": k_animals_data,
            "Л": l_animals_data,
            "М": m_animals_data,
            "Н": n_animals_data,
            "О": o_animals_data,
            "П": p_animals_data,
            "Р": r_animals_data,
            "С": s_animals_data,
            "Т": t_animals_data,
            "У": u_animals_data,
            "Ф": f_animals_data,
            "Х": h_animals_data,
            "Ц": c_animals_data,
            "Ч": ch_animals_data,
            "Ш": sh_animals_data,
            "Щ": shh_animals_data,
            "Э": ye_animals_data,
            "Ю": yu_animals_data,
            "Я": ya_animals_data
        }
    )

    #Добавление в json файл
    with open("task 2\Tetrika.json", "w", encoding='utf=8') as file:
        json.dump(all_animals_data, file, indent=4, ensure_ascii=False)

              
    print("А: ",len(a_animals_data))
    print("Б: ",len(b_animals_data))
    print("В: ",len(v_animals_data))
    print("Г: ",len(g_animals_data))
    print("Д: ",len(d_animals_data))
    print("Е: ",len(e_animals_data))
    print("Ё: ",len(ee_animals_data))
    print("Ж: ",len(zh_animals_data))
    print("З: ",len(z_animals_data))
    print("И: ",len(i_animals_data))
    print("Й: ",len(ii_animals_data))
    print("К: ",len(k_animals_data))
    print("Л: ",len(l_animals_data))
    print("М: ",len(m_animals_data))
    print("Н: ",len(n_animals_data))
    print("О: ",len(o_animals_data))
    print("П: ",len(p_animals_data))
    print("Р: ",len(r_animals_data))
    print("С: ",len(s_animals_data))
    print("Т: ",len(t_animals_data))
    print("У: ",len(u_animals_data))
    print("Ф: ",len(f_animals_data))
    print("Х: ",len(h_animals_data))
    print("Ц: ",len(z_animals_data))
    print("Ч: ",len(ch_animals_data))
    print("Ш: ",len(sh_animals_data))
    print("Щ: ",len(shh_animals_data))
    print("Э: ",len(ye_animals_data))
    print("Ю: ",len(yu_animals_data))
    print("Я: ",len(ya_animals_data))

def main():
    get_data()
    finish_time = time.time() - start_time
    print(f"\n\nВремя выполнения: {finish_time:.1f} секунд")

if __name__ == '__main__':
    main()
