import os
import json


def search_list(query: str, key_list: list[str]) -> list[str] | None:
    """
    Function that handles searching for all matches within a lsit

    Args:
        query (str): Search item
        key_list (list[str]): Search list

    Returns:
        list[str] | None: List of matching items, None if no matches
    """

    # Creates list to store matches
    key_results = []

    # Checks each item if a match occurs
    for key in key_list:
        # If matches
        if query.lower() in key.lower():
            key_results.append(key)

        else:
            pass

    # Finds at least 1 match
    if len(key_results) > 0:
        return key_results

    # If it finds no matches
    else:
        return None


def main():
    """
    Main program function
    """
   

    # Sets current working directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Grabs file names
    json_file_names = os.listdir(f"{os.getcwd()}/jsons/")

    for file_name in json_file_names:
        with open(f"{os.getcwd()}/jsons/{file_name}") as f:
            json_file = dict(json.load(f))

        if search_list(query_spell, json_file.keys()):
            print(f"Found in {file_name}")
        
        else:
            print(f"Not found in {file_name}")


# If it is executed directly, run main program
if __name__ == "__main__":
    query_spell = input("What spell do you need to find: ")
    main()