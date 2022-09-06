import requests
import json
import os

def load_and_clean_data(d):
    """
    Takes list of dictionaries, cleans and returns clean  list of dictionaries
    """
    clean_article_dict = []
    for article in d:
        clean_article_dict.append(dict([(k,v) for k,v in article.items() if k not in ["author","province","categories"]]))
        # clean_article_dict.append(dict([(k,v) for k,v in article.items() if k in ["id"]]))
    return clean_article_dict

def update_category_json(category_name, jsonfile):
    """
    Takes category_name, json_file and Updates category_name.json
    """
    with open(f"{category_name}.json", "w") as f:
        json.dump(jsonfile, f, indent=4, ensure_ascii=False)

def getJson(category_name):
    """
    Takes Category name and dump into category_name.json
    """
    page_number = 1
    if not os.path.isfile(f"{category_name}.json"):
        with open(f"{category_name}.json", "w") as f:
            json.dump({"page": 0, "items": []}, f, indent=4, ensure_ascii=False)

    # read current category_name.json file
    with open(f"{category_name}.json", "r") as jsonfile:
        jsonfile_dict = json.loads(jsonfile.read())
        page_number = jsonfile_dict["page"]+1
        print("current: page number: ", jsonfile_dict["page"])
        
    while(True):
        try:
            r = requests.get(f"https://bg.annapurnapost.com/api/news/list?page={page_number}&per_page=30&category_alias={category_name}&isCategoryPage=1")
            r.raise_for_status()
            cleaned_article = load_and_clean_data(d=r.json()['data'])
            jsonfile_dict.get("items").extend(cleaned_article)
            jsonfile_dict["page"] = page_number
            update_category_json(f"{category_name}", jsonfile_dict)
            total_page_number = r.json().get("totalPage")
            print(f"{category_name} : ", page_number ," of ", total_page_number)
            # check if it reaches total_page_number
            if page_number == total_page_number:
                print("REACHES TOTAL PAGE NUMBER, EXITING...")
                break

        except Exception as e:
            print(e)
            print("SOMETHING ERROR OCCURED, please check category_name")
    
        page_number += 1

# getJson("corporate")
# getJson("foreign")
# getJson("paurakhi")
# getJson("tech")
# getJson("susashan-special")
# getJson("interesting-world")
# getJson("health")
# getJson("sampurna")
# getJson("fursad")
getJson("gallery")
# getJson("prabas")
# getJson("angkur")
# getJson("social")
# getJson("entertainment")
# getJson("something")