import os
import jsonschema as js
import json
import multiprocessing as mp

# Creates global error list
error_list = []

# Helper class and functions
# ============================================================================


# Formatting Class
class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


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


def find_input(user_input: str, json_list: list[str]) -> str:
    """
    Function to take user input to find file.

    Args:
        user_input (str): Input of user
        json_list (list[str]): List of JSON file names

    Returns:
        str: file_name match
    """

    # Searches json_list for user_input
    result_key = search_list(user_input, json_list)

    # If it has found at least one match
    if result_key:
        # If it found exactly one match
        if len(result_key) == 1:
            return result_key[0]

        # If it has found more than one match, insert header and assert False
        else:
            result_key.insert(
                0, "\n" + color.BOLD + "Multiple Matches Found:" + color.END
            )
            assert False, "\n".join(result_key)

    # If it has found no matches, assert False
    else:
        assert False, f"{user_input} did not provide a match"


# MP portion of program
# ============================================================================


def start_cb(something: None | list[str]) -> None:
    """
    Callback function for start

    Args:
        something (None | list[str]): None object or list of errors
    """

    # Grabs global error_list
    global error_list

    # If it is a None object
    if not something:
        pass

    # If it is a list of errors
    else:
        # For each error, add it to the global error list
        for item in something:
            error_list.append(item)


def start(spell_name: str, spell_dictionary: dict) -> None | list[str]:
    """
    MP function to check spell details

    Args:
        spell_name (str): Name of spell
        spell_dictionary (dict): Dictionary containing spell details

    Returns:
        None | list[str]: None (if no errors) or list of errors
    """

    # Setup local error_list and class_list
    error_list = []
    class_list = [
        "Artificer",
        "Bard",
        "Cleric",
        "Druid",
        "Paladin",
        "Ranger",
        "Sorcerer",
        "Warlock",
        "Wizard",
    ]

    # Tries to check School key
    try:
        # The school in the data is valid
        if spell_dictionary["School"] in [
            "Abjuration",
            "Conjuration",
            "Divination",
            "Enchantment",
            "Evocation",
            "Illusion",
            "Necromancy",
            "Transmutation",
        ]:
            pass

        # The school in the data is invalid, add to local error list
        else:
            error_list.append(
                f"{spell_name} > School: Invalid Value ({spell_dictionary['School']})"
            )

    # There is no School key, add to local error list
    except:
        error_list.append(f"{spell_name} > School: Missing Key")

    # Tries to check Level key
    try:
        # The level in the data is valid
        if spell_dictionary["Level"] in [i for i in range(0, 11)]:
            pass

        # The level in the data is invalid, add to local error list
        else:
            error_list.append(
                f"{spell_name} > Level: Invalid Value ({spell_dictionary})"
            )

    # There is no Level key, add to local error list
    except:
        error_list.append(f"{spell_name} > Level: Missing Key")

    # Tries to check Class key
    try:
        # For each class within the class list
        for class_name in spell_dictionary["Class"]:
            # The class in the data is valid
            if class_name in class_list:
                pass

            # The class in the data is invalid, add to local error list
            else:
                error_list.append(f"{spell_name} > Class: Invalid Value ({class_name})")

    # There is no Class key, add to local error list
    except:
        error_list.append(f"{spell_name} > Class: Missing Key")

    # Tries to check Expanded Class key
    try:
        # For each class within the expanded class list
        for class_name in spell_dictionary["Expanded Class"]:
            # The Expanded Class in the data is valid
            if class_name in class_list:
                pass

            # The Expanded Class in the data in invalid, add to local error list
            else:
                error_list.append(
                    f"{spell_name} > Expanded Class: Invalid Value ({class_name})"
                )

    # There is no Expanded Class key, do nothing
    except:
        pass

    # Send local error_list to callback
    return error_list


# Main Program
# ============================================================================


def main() -> None:
    """
    Main program function
    """

    # Grabs global error list
    global error_list

    # Sets current working directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Collects target file name
    file_name = find_input(
        input("What file do you need to check? "), os.listdir(f"{os.getcwd()}/jsons/")
    )

    # Opens file and stores the data as a dictionary
    with open(f"{os.getcwd()}/jsons/{file_name}") as f:
        data_json = dict(json.load(f))

    # Tries to check SETTINGS key
    try:
        data_json["SETTINGS"]

        # Tries to check Homebrew Key
        try:
            # The boolean in the data is valid
            if data_json["SETTINGS"]["Homebrew"] in [True, False]:
                pass

            # The value in the data is not valid, add to global error list
            else:
                error_list.append(
                    f"SETTINGS > Homebrew: Invalid Value ({data_json['SETTINGS']['Homebrew']})"
                )

        # There is no Homebrew key, add to global error list
        except:
            error_list.append("SETTINGS > Homebrew: Key missing")

        # Tries to check Partnered Content key
        try:
            # The boolean in the data is valid
            if data_json["SETTINGS"]["Partnered Content"] in [True, False]:
                pass

            # The value in the data is not valid, add to global error list
            else:
                error_list.append(
                    f"SETTINGS > Partnered Content: Invalid Value ({data_json['SETTINGS']['Partnered Content']})"
                )

        # There is no Partnered Content key, add to global error list
        except:
            error_list.append("SETTINGS > Partnered Content: Key missing")

    # There is not SETTINGS key, add to global error list
    except:
        error_list.append("SETTINGS: Key missing")

    # Removes SETTINGS from dictionary
    data_json.pop("SETTINGS")

    # Sets the pool to creates processes equal to number of processors
    pool = mp.Pool(processes=os.cpu_count())

    # For each spell name and dictionary, add to pool for start to run
    for spell_name, spell_value in data_json.items():
        pool.apply_async(
            start,
            args=(
                spell_name,
                spell_value,
            ),
            callback=start_cb,
        )

    # Closes and joins the pools
    pool.close()
    pool.join()

    # If there are no errors
    if len(error_list) == 0:
        print(f"{file_name} has no errors")

    # If there are errors, print them.
    else:
        print(f"{file_name} had the following errors:")
        print("\n".join(error_list))


# Makes the program run it it is executed directly
if __name__ == "__main__":
    main()
    input("Press enter to exit")
