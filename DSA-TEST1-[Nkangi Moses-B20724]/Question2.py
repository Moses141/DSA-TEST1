# List of Catholic Martyrs
catholic_martyrs = ["Achileo Kiwanuka","Adolphus Ludigo Mukasa","Ambrosius Kibuuka","Anatoli Kiriggwajjo","Andrew Kaggwa","Antanansio Bazzekuketta","Bruno Sserunkuuma","Charles Lwanga","Denis Ssebuggwawo Wasswa","Gonzaga Gonza","Gyavira Musoke","James Buuzaabalyaawo","John Maria Muzeeyi","Joseph Mukasa","Kizito","Lukka Baanabakintu","Matiya Mulumba","Mbaga Tuzinde","Mugagga Lubowa","Mukasa Kiriwawanvu","Nowa Mawaggali","Ponsiano Ngondwe"]


# List of Anglican Martyrs
anglican_martyrs = ["Aaron Lubega","Apollo Kivebulaya","Eria Sebukyala","Fredrick Kizza","George Kizza","James Hannington","Janani Luwum","Joseph Balikuddembe","Kizito","Mark Kakumba","Matiya Mulumba",  "Nuhu Mbegu","Robert Munyagayirwa","Samwiri Mukasa","Yefusa Namayanja","Yohana Mukasa","Yosefu Lugalama","Yowana Kitaka","Yowana Maria Mukasa","Yowana Mukiibi","Yusufu Lugalama","Zakayo Lubega"]

catholic_martyrs_set = set(catholic_martyrs)
anglican_martyrs_set = set(anglican_martyrs)

# Find the common names between the sets
common_names = catholic_martyrs_set.intersection(anglican_martyrs_set)

# Convert the sets back to lists and remove the common names
catholic_martyrs = list(catholic_martyrs_set - common_names)
anglican_martyrs = list(anglican_martyrs_set - common_names)

# Print the updated lists
print("Catholic Martyrs:")
print(catholic_martyrs)

print("\nAnglican Martyrs:")
print(anglican_martyrs)

def martyr_count(martyr_name):
    # Check if the martyr's name is in the Catholic martyrs list
    if martyr_name in catholic_martyrs:
        return "Catholic"
    # Check if the martyr's name is in the Anglican martyrs list
    elif martyr_name in anglican_martyrs:
        return "Anglican"
    else:
        return "Not found in either group"

# Accept input from the user and call the function
martyr_name = input("Enter a martyr's name: ")
group = martyr_count(martyr_name)
print(f"{martyr_name} belongs to the {group} group.")


def is_uganda_martyr(name):
    # Check if the name is in the Catholic martyrs list or the Anglican martyrs list
    if name in catholic_martyrs or name in anglican_martyrs:
        return True
    else:
        return False

# Test the function
input_name = input("Enter a name to check if it's a Uganda Martyr: ")
if is_uganda_martyr(input_name):
    print(f"{input_name} is a Uganda Martyr.")
else:
    print(f"{input_name} is not a Uganda Martyr.")