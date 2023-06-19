import methods
import datetime

# downloading csv
methods.download_data('https://onlinedata.plzen.eu/data-pd-rychtarka-actual.php', 'rychtarka_actual.csv')
methods.download_data('https://onlinedata.plzen.eu/data-pd-novedivadlo-actual.php', 'nove_divadlo_actual.csv')

# load data
rychtarka_actual = methods.load_data('rychtarka_actual.csv')
nove_divadlo_actual = methods.load_data('nove_divadlo_actual.csv')

print('Volná místa Rychtářka: ', methods.available_places(rychtarka_actual)[0])
print(methods.day_matrix(rychtarka_actual, 'pondělí'))