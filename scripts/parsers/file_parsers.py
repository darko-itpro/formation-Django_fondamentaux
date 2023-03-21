import logging

def load_museums_from_csv(file_path, sep=";"):
    """
    Valeur retour : Région administrative;Département;Identifiant Muséofile;identifiant musée;Commune;Nom officiel du musée;Adresse;Lieu;Code Postal;Téléphone;URL;Latitude;Longitude
    :param file_path:
    :param sep:
    :return:
    """
    with open(file_path) as museum_file:
        header = museum_file.readline()

        for line in museum_file:
            region, departement, museofile_id, city, museum_name, address, place, zip_code, phone, museum_url, lat, long, museum_id, *_ = line.split(sep)
            yield region, departement, museofile_id, museum_id, city, museum_name, address, place, zip_code, phone, museum_url, lat, long


def load_museum_access_from_csv(file_path, sep=";"):
    with open(file_path) as museum_file:
        header = museum_file.readline()

        for line in museum_file:
            try:
                museum_ref, museum_name, year, region, city, _, paying_visitors, free_visitors, all_visitors, _, museofile_id, departement, note = line.split(sep)
                yield museum_ref, museum_name, year, region, city, paying_visitors, free_visitors, all_visitors, museofile_id, departement, note
            except ValueError:
                logging.error(f'{line.split(sep)}')


