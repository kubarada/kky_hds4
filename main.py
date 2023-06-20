import methods
import datetime

# downloading csv
#methods.download_data('https://onlinedata.plzen.eu/data-pd-rychtarka-actual.php', 'rychtarka_actual.csv')
#methods.download_data('https://onlinedata.plzen.eu/data-pd-novedivadlo-actual.php', 'nove_divadlo_actual.csv')
#methods.download_data('https://onlinedata.plzen.eu/data-pd-rychtarka.php', 'rychtarka_hist.csv')
#methods.download_data('https://onlinedata.plzen.eu/data-pd-novedivadlo.php', 'nove_divadlo_hist.csv')

# load data
rychtarka_actual = methods.load_data('rychtarka_actual.csv')
nove_divadlo_actual = methods.load_data('nove_divadlo_actual.csv')
rychtarka_hist = methods.load_data('rychtarka_hist.csv')
nove_divadlo_hist = methods.load_data('nove_divadlo_hist.csv')

print('Volná místa Nové divadlo: ', methods.available_places(nove_divadlo_actual)[0])
print('Průměr ve středu na Rychtářce: ', methods.stats(methods.day_matrix(rychtarka_actual, 'úterý')))
print('Obsazeno na Rychtářce: ', 100- methods.stats(methods.day_matrix(rychtarka_actual, 'úterý'))[2], '%')
print('Průměr v 16:00:00 na Rychtářce: ', methods.stats(methods.hour_matrix(rychtarka_hist, '2:01:00')))