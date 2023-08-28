import csv

def region_parser(insee_file_path, sep=","):
    with open(insee_file_path) as insee_region_file:

        reader = csv.reader(insee_region_file, delimiter=sep)
        next(reader)

        for line in reader:
            code_region, code_chef_lieu, name_type, name, rich_name, label = line
            yield code_region, code_chef_lieu, name_type, name, rich_name, label

def departement_parser(insee_file_path, sep=","):
    with open(insee_file_path) as insee_departement_file:

        reader = csv.reader(insee_departement_file, delimiter=sep)
        next(reader)

        for line in reader:
            code_departement, code_region, code_chef_lieu, name_type, name, rich_name, label = line
            yield code_departement, code_region, code_chef_lieu, name_type, name, rich_name, label
