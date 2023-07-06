"""Functions to help Azara and Rui locate pirate treasure."""
def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.
 
    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]
def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.
 
    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    coord=[]
    for letter in coordinate:
        coord.append(letter)
    return tuple(coord)
def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.
 
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    list1=list(azara_record)
    list2=list(rui_record)
    apex=list2[1][0]+list2[1][1]
    apex2=list1[1]
    return apex2==apex
        
def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.
 
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    print(azara_record)
    print(rui_record)
    list1=list(azara_record)
    list2=list(rui_record)
    print(list1)
    print(list2)
    apex=list2[1][0]+list2[1][1]
    apex2=list1[1]
    if apex2==apex:
        azara_record+=rui_record
        return azara_record
    return 'not a match'
def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.
 
    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.
 
    The return statement should be a multi-lined string with items separated by newlines.
 
    (see HINTS.md for an example).
    """
    report = ''
    for record in combined_record_group:
        cleaned_record = (
            record[0],
            record[2],
            record[3],
            record[4]
        )
        report += str(cleaned_record) + '\n'
    return report
