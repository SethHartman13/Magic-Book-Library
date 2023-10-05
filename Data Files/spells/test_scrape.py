from bs4 import BeautifulSoup
import json
from random import uniform as random
from zenrows import ZenRowsClient
import os
from config import Tokens


class Data_Holder:
    def __init__(self, names: list[str], levels: list[str], schools: list[str]) -> None:
        """
        Object to hold data taken from data scrapping

        Args:
            names (list[str]): List of spell names
            levels (list[str]): List of spell levels
            schools (list[str]): List of spell schools
        """
        
        self.names = names
        self.levels = levels
        self.schools = schools


def send_request(url: str) -> Data_Holder:
    """
    Handles the collection and packaging of necessary scraped data

    Args:
        url (str): URL target

    Returns:
        Data_Holder: Data object holding scraped data
    """
    
    # Creates client object
    client = ZenRowsClient(Tokens.zenrows)

    # Sends and received response
    response = client.get(url)
    
    # Parses data
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Level mapping table
    level_map = {
        "Cantrip": 0,
        "1st": 1,
        "2nd": 2,
        "3rd": 3,
        "4th": 4,
        "5th": 5,
        "6th": 6,
        "7th": 7,
        "8th": 8,
        "9th": 9,
    }

    return Data_Holder(
        [
            "".join(str(name).split(">")[1].split("<")[0]).replace("\u2019", "'") # Removes HTML tags
            for name in soup.select(".info .row.spell-name .name a") # Grabs specified html content
        ],
        [
            level_map["".join(str(level).split(">")[1].split("<")[0])] # Removes HTML tags and run through level mapping table
            for level in soup.select(".info .row.spell-level span") # Grabs specified content
        ],
        [
            "".join(str(school).split(">")[1].split("<")[0]) # Removes HTML tags
            for school in soup.select(".info .row.spell-name span span:first-child") # Grabs specified content
        ],
    )


def run_calls(
    json_data: dict,
    class_map: dict,
    file_name: str,
    source_id: int,
) -> None:
    """
    Runs the calls and edits the JSON file

    Args:
        json_data (dict): JSON file contents
        class_map (dict): Class mapping table
        file_name (str): Name of file
        source_id (int): Source id of sourcebook
    """
    
    # For each class
    for class_name in class_map.keys():
        
        # Set starting values
        i = 1
        run = True
        data = Data_Holder([], [], [])
        
        # While true
        while run:
            
            # Set old data to data and request new data
            old_data = data
            data = send_request(
                f"https://www.dndbeyond.com/spells?page={i}&filter-class=0&filter-class={class_map[class_name]}&filter-partnered-content=t&filter-search=&filter-source={source_id}"
            )

            # If old data is not new data
            if old_data.names != data.names:
                
                # For each spell name scraped
                for name in data.names:
                    
                    # If the spell exists
                    if name in json_data.keys():
                        
                        # If the class is not in the class list, add the class
                        if not class_name in json_data[name]["Class"]:
                            json_data[name]["Class"].append(class_name)

                        # If the class is not in the class list, pass
                        else:
                            pass

                    # If the spell does not exist, create new entry
                    else:
                        json_data[name] = {
                            "School": data.schools[data.names.index(name)],
                            "Schools": data.levels[data.names.index(name)],
                            "Class": [class_name],
                        }

                # Increment page number
                i += 1

            # If old data is new data, stop while loop
            else:
                run = False

        # Prints that the class is done
        print(f"{class_name} done")

    # Writes finished JSON to file
    with open(f"{os.getcwd()}/jsons/{file_name}", "w") as f:
        f.write(json.dumps(json_data, indent=4))



def main() -> None:
    """
    Main program function
    """
    
    # Sets current working directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Source mapping table
    SOURCE_MAP = {
        "basic_rules": 1,
        "acquisitions_incorporated": 44,
        "elemental_evil_players_companion": 4,
        "explorers_guide_to_wildemount": 59,
        "fizbans_treasury_of_dragons": 81,
        "guildmasters_guide_to_ravnica": 38,
        "icewind_dale_rime_of_the_frostmaiden": 66,
        "lost_laboratory_of_kwalish": 40,
        "players_handbook": 2,
        "spelljammer_adventures_in_space": 90,
        "strixhaven_a_curriculum_of_chaos": 80,
        "sword_coast_adventurers_guide": 13,
        "taldorei_campaign_setting_reborn": 123,
        "tashas_cauldron_of_everything": 67,
        "xanthars_guide_to_everything": 27
    }

    # Class mapping table
    CLASS_MAP = {
        "Bard": 1,
        "Cleric": 2,
        "Druid": 3,
        "Paladin": 4,
        "Ranger": 5,
        "Sorcerer": 6,
        "Warlock": 7,
        "Wizard": 8,
        "Artificer": 252717,
    }
    
    # Loads json file (creates one if necessary)
    with open(f"{os.getcwd()}/jsons/{file_name}", "r") as f:
        json_file = json.load(f)

    # For each file in the source mapping table
    for file_name, source_id in SOURCE_MAP.items():
        run_calls(json_file, CLASS_MAP, f"{file_name}.json", source_id)
        print(f"{file_name} done\n")

    # Prints All done
    print("All done")

# If it is the main program executing, it executes
if __name__ == "__main__":
    main()
