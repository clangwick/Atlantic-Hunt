#init
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# setup stereographic view.
map = Basemap(projection='stere',lat_0=45,lon_0=-40,rsphere=6371200.,width=10000000,height=7500000,resolution='l')

# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.fillcontinents(color='#cc9966',lake_color='aqua')

# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='aqua')

# draw lat/lon grid lines every 30 degrees.
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))

#plot the map
plt.title('submarine hunting patterns')
plt.show()
