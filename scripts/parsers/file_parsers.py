import logging
import csv

def load_museums_from_csv(file_path, sep=";"):
    """
    Script simple de chargement de valeurs. Certaines données ne seront pas chargées du fait de la simplicité
    du script par rapport au format CSV.

    Valeur retour : Région administrative;Département;Identifiant Muséofile;identifiant musée;Commune;Nom officiel du musée;Adresse;Lieu;Code Postal;Téléphone;URL;Latitude;Longitude
    :param file_path:
    :param sep:
    :return:
    """
    with open(file_path) as museum_file:
        reader = csv.reader(museum_file, delimiter=sep)
        next(reader)

        for line in reader:
            try:
                region, departement, museofile_id, city, museum_name, address, place, zip_code, phone, museum_url, lat, long, museum_id, geolocation, appellation_date = line
            except ValueError:
                logging.error(f"{line.rstrip()} - {len(line.split(';'))}/15 éléments")
                continue
            yield region, departement, museofile_id, museum_id, city, museum_name, address, place, zip_code, phone, museum_url, lat, long, geolocation, appellation_date


def load_museum_access_from_csv(file_path, sep=";"):
    with open(file_path) as museum_file:
        reader = csv.reader(museum_file, delimiter=sep)
        next(reader)

        for line in reader:
            try:
                museum_ref, museum_name, year, region, city, _, paying_visitors, free_visitors, all_visitors, _, museofile_id, departement, note = line
                yield museum_ref, museum_name, year, region, city, paying_visitors, free_visitors, all_visitors, museofile_id, departement, note
            except ValueError:
                logging.error(f'{line.split(sep)}')


