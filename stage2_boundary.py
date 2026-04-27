import geopandas as gpd

import matplotlib.pyplot as plt

# Load Nigeria shapefile (level 1 = states)
nigeria = gpd.read_file("data/raw/gadm41_NGA_1.shp")

# Check available states
print(nigeria['NAME_1'].unique())

# Filter Ondo State only
ondo = nigeria[nigeria['NAME_1'] == 'Ondo']
print(ondo)

# Save Ondo boundary
ondo.to_file("data/raw/ondo_boundary.shp")
print("✅ Ondo State boundary saved!")

# Plot it
ondo.plot(color='green', edgecolor='black')
plt.title("Ondo State, Nigeria")
plt.savefig("outputs/ondo_boundary.png", dpi=150)
plt.show()
print("✅ Map saved to outputs/ondo_boundary.png")


