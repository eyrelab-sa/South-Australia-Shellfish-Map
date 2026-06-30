import fiona
from shapely.geometry import shape, box
from shapely.geometry import mapping

# -----------------------------
# INPUT / OUTPUT
# -----------------------------
input_file = "ne_10m_coastline.shp"
output_file = "SA_coastline.gpkg"

# -----------------------------
# SOUTH AUSTRALIA BBOX
# -----------------------------
sa_bbox = box(129, -39, 141, -26)

count = 0

with fiona.open(input_file, "r") as src:

    schema = src.schema
    crs = src.crs

    with fiona.open(
        output_file,
        "w",
        driver="GPKG",
        schema=schema,
        crs=crs
    ) as dst:

        for feat in src:
            geom = shape(feat["geometry"])

            if not geom.intersects(sa_bbox):
                continue

            dst.write(feat)
            count += 1

print("Done. SA features:", count)