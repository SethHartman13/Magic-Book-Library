import json
import os
import itertools
import multiprocessing as mp

# Global process lock
process_lock = mp.Lock()


def compare_dict_cb(discrepancies: list[str|None]) -> None:
    """
    Callback function for compare_dict

    Args:
        discrepancies (list[str|None]): List of discrepancies/None objects
    """

    # Use process lock
    global process_lock

    # For each item in the list, if it is not a None object, print the discrepancy with the process_lock
    for discrepancy in discrepancies:
        if discrepancy:
            with process_lock:
                print(discrepancy)

        else:
            pass


def compare_dict(
    dict_obj: dict[str, dict[str, str | int | list[str]]]
) -> list[str | None]:
    """
    Compares the contents of each file dictionary

    Args:
        dict_obj (dict[str, dict[str, str  |  int  |  list[str]]]): Dictionary containing the following file structure:
            {
                "File name": {
                    "Spell name": {
                        "School": "School Name",
                        "Level": 0,
                        "Class": [""] (optional),
                        "Expanded Class": [""] (optional)
                    }
                }
            }

    Returns:
        list[str | None]: Returns a list of descrepancies (or None objects if there isn't a descrepancy)
    """

    # Unpacks file names
    dict_a_name, dict_b_name, *_ = dict_obj.keys()

    # Finds common spells
    common_spells = list(set(dict_obj[dict_a_name]) & set(dict_obj[dict_b_name]))

    # Returns list comprehension containing list
    return [
        f"{dict_a_name} & {dict_b_name}: Discrepancy ({spell_name})" # List spell that has discrepancy
        if (dict_obj[dict_a_name][spell_name] != dict_obj[dict_b_name][spell_name]) # If spell details are not the same
        and (spell_name != "SETTINGS") # And not the SETTINGS entry
        else None # Else, None
        for spell_name in common_spells # For each spell that is common
    ]


def main():
    """
    Main program function
    """

    # Sets current working directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Grabs file names
    json_file_names = os.listdir(f"{os.getcwd()}/jsons/")
    json_files = {}

    # Opens the files and loads them into a dictionary
    for file in json_file_names:
        with open(f"{os.getcwd()}/jsons/{file}") as f:
            json_files.update({file: json.load(f)})

    # Sets the number of processes to the number of processors
    pool = mp.Pool(processes=os.cpu_count())

    # List comprehension of dictionaries containing the information
    mp_list = [
        {dict_a_name: json_files[dict_a_name], dict_b_name: json_files[dict_b_name]} # Create dictionary containing {file_name: file_contents}
        for (dict_a_name, dict_b_name) in list( # For each dictionary name pair
            itertools.combinations(json_file_names, 2) # From each combination pair
        )
    ]

    # Start processing of each file pair
    for dictionary in mp_list:
        pool.apply_async(compare_dict, args=(dictionary,), callback=compare_dict_cb)

    # Close and join pools
    pool.close()
    pool.join()


# If it is executed directly, run main program
if __name__ == "__main__":
    main()
