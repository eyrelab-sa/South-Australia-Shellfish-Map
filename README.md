# Gulf Beds — Shellbed Atlas of South Australia

**An interactive reference map consolidating native bivalve presence data, historical reef records, restoration program sites, and community science observations across South Australia's gulf systems.**

Built by [Eyre Lab](https://www.eyrelab.org/) Educating Youth in Restoration Ecology.
Field survey data collected by Brian Arruda and Manny Katz.

---

## Live map

Open `oyster_site_map.html` in any modern browser — no server required. The file is fully self-contained (all assets and data are embedded).

---

## What the map shows

The map layers four types of data:

### Field surveys — Eyre Lab

In-water dive and snorkel assessments conducted by Eyre Lab volunteers in support of an independent _Ostrea angasi_ genetics research project. Sites are on the Eyre Peninsula, Streaky Bay, and Ceduna coastlines.

**Species tracked:**
| Key | Latin name | Notes |
|-----|-----------|-------|
| `angasi` | _Ostrea angasi_ | Flat / mud / Port Lincoln oyster |
| `hammerOyster` | _Malleus meridianus_ | Southern hammer oyster |
| `razorfish` | _Pinna bicolor_ | Pen shell / razor fish |
| `cockle` | _Katelysia spp._ | Venus clam (_K. scalarina_, _K. rhytiphora_) |
| `scallop` | _Equichlamys bifrons_ | Southern bay scallop |
| `nativeMussel` | _Brachidontes / Mytilus spp._ | Taxonomically unresolved — see caveats |

**Status tiers:**

- **Present** — confirmed in-water positive ID
- **Uncertain** — shell material, shore visual, or secondhand report
- **Absent** — in-water survey, species not detected
- **No data** — site not assessed for that species (≠ absent)

**Map encoding:** Shape identifies species (your SVG icons). Fill colour encodes status (green / amber / white+slash / gray). Stroke / border colour also identifies species — it persists regardless of status so the species is always readable. Gold halo = recruitment (juveniles/spat) confirmed.

### Restoration programs — 25 Reefs Project

Active and proposed _Ostrea angasi_ reef restoration sites across SA. 20 sites total. Sites with confirmed recruitment are marked. Sites with `approximate: true` have centroid-level coordinates only.

**Sites with links:**

- [Glenelg Reef](https://www.google.com/maps/place/Glenelg+Shellfish+Reef/@-34.9727278,138.4951943,1178m/)
- [Windara Reef](https://www.researchgate.net/figure/Australias-first-large-scale-oyster-reef-restoration-project-Windara-Reef-is-located_fig1_343076485)
- [Kingscote Reef](https://www.landscape.sa.gov.au/ki/native-plants-and-animals/supporting-biodiversity/oyster-reef-restoration)

### Historical layers — Martin et al. 2025

Digitised historical shellfish reef positions from the peer-reviewed literature.

> Martin, B., Huveneers, C., Reeves, S. & Baring, R. (2025). Reviving shellfish reef socio-ecological histories for modern management and restoration. _Ocean & Coastal Management_ 261:107540.

**Source file:** `martin_2025_shellfish_reef_sites.csv` (extracted from paper supplementary mmc2.xlsx).

Filters applied in this map:

- _O. angasi_: high-confidence records, ≤1950 or undated only
- _P. bicolor_, _M. meridianus_: high-confidence, no date cutoff (too few records to filter further)

**Known data issue:** Gillies et al. 2018 Table 1 lists _P. bicolor_ distribution as WA/NT/QLD/NSW (omitting SA), but the same paper's body text and Comments column confirm SA gulf occurrence. Martin et al. 2025 coordinates are used here and are considered reliable.

### Historical layers — Gillies et al. 2018

Historical harvest evidence, aquaculture locations, and oyster-related place names, filtered to the SA bounding box.

> Gillies, C.L., et al. (2018). Australian shellfish ecosystems: Past distribution, current status and future direction. _PLoS ONE_ 13(2):e0190914.

**Source:** Figshare dataset 5766144. Species not differentiated in this dataset (_O. angasi_ and _S. glomerata_ combined).

**Evidence tiers (harvest layer):**

- Tier 1: locality name only
- Tier 2: + historical harvest record _(sheet unlabeled in source — tier inferred by numeric reconciliation)_
- Tier 3: + current/historical aquaculture use

**Source files:** `gillies_2018_harvest_SA.csv`, `gillies_2018_aqua_SA.csv`, `gillies_2018_names_SA.csv`

### Community science — iNaturalist

All research-grade _Ostrea angasi_ observations from iNaturalist, SA bounding box, exported 2026-06-28.

**Source file:** `inat_ostrea_angasi_research_grade.csv` (4,429 records, 2011–2026).

**Geographic note:** ~3,900 records are in the Adelaide metro area. The Eyre Peninsula has only ~47 records — this reflects observer effort on iNaturalist, not population abundance. Do not interpret record density as a proxy for reef density.

Each map marker links directly to the individual iNaturalist observation page.

---

## How to use the map

| Control               | Location                   | Function                                                                               |
| --------------------- | -------------------------- | -------------------------------------------------------------------------------------- |
| **Layers** button     | Top right                  | Toggle all data layers on/off                                                          |
| **Info panel**        | Left side                  | Shows source info for the active layer; opens automatically when a layer is toggled on |
| **Species lens row**  | In the field surveys panel | Switch between species to re-colour and re-shape all survey markers                    |
| **Status filters**    | Below lens row             | Show/hide markers by status (Present / Uncertain / Absent / No data)                   |
| **Satellite / Ocean** | Header                     | Switch basemap between Esri satellite and GEBCO ocean bathymetry                       |
| **About this map**    | Header                     | Full methodology notes, data source descriptions, and limitations                      |
| **+ Add site**        | Survey panel footer        | Click to enter placement mode, then click the map to add a new field site              |

---

## File structure

```
gulf-beds/
├── oyster_site_map.html              # Main map (self-contained, open in browser)
├── README.md                         # This file
│
├── data/
│   ├── field_surveys/
│   │   └── field_surveys_eyre_lab.csv         # Eyre Lab dive survey records
│   │
│   ├── historical/
│   │   ├── martin_2025_shellfish_reef_sites.csv   # Full mmc2.xlsx table (142 sites)
│   │   ├── gillies_2018_harvest_SA.csv            # SA harvest evidence (n=70, tiered)
│   │   ├── gillies_2018_aqua_SA.csv               # SA aquaculture locations (n=7)
│   │   └── gillies_2018_names_SA.csv              # SA oyster place names (n=7)
│   │
│   └── citizen_science/
│       └── inat_ostrea_angasi_research_grade.csv  # iNaturalist research-grade obs
│
└── source_exports/
    └── observations-753365.csv       # Original iNaturalist export (unmodified)
```

> **Tip:** Move the CSVs into this structure. The `oyster_site_map.html` file has all data embedded — the CSVs are for external reference and re-processing only.

---

## Updating field data

Field survey data is stored in two places:

1. **In the browser** — new sites added via the map UI are saved to browser local storage. This is the live working version.
2. **In the HTML source** — the `DEFAULT_SITES` array (search for `const DEFAULT_SITES`) is the seed dataset that loads if no browser storage is found.

To commit new field data to the source:

1. Open the map and use the UI to add/edit sites as normal.
2. Open browser DevTools → Application → Local Storage → find the `sa-bivalve-sites-v3` key.
3. Copy the JSON value.
4. Paste it into `DEFAULT_SITES` in `oyster_site_map.html` (replacing the existing array).
5. Commit the updated HTML.

> **Warning:** Clearing browser cache will delete any sites added via the UI that haven't been committed to the HTML source.

---

## Data caveats

- **Coordinate precision:** Historical coordinates from Martin et al. 2025 and Gillies et al. 2018 are digitised approximate positions — do not interpret at fine spatial scales.
- **Taxonomic flag:** The `nativeMussel` field is unresolved. Voucher specimens are needed to determine whether records represent _Brachidontes erosus_, _B. rostratus_, _Trichomya hirsuta_, or _Mytilus galloprovincialis_ — all formally recognised SA ecosystem-forming species (Gillies et al. 2018 Table 1).
- **iNaturalist:** Records represent presence only. Some may be cultivated/aquaculture specimens. Observer identity can be verified via the individual observation link.
- **Survey coverage:** Field sites reflect access and opportunity, not a systematic survey design. Absence of a location from the map does not imply no bivalves are present there.
- **Substrate layer:** The AusSeabed sediment layer is clipped to the SA bounding box but not to the precise SA coastline.

---

## Built with

- [Leaflet.js](https://leafletjs.com/) 1.9.4 — map framework
- [Leaflet.MarkerCluster](https://github.com/Leaflet/Leaflet.markercluster) 1.5.3 — iNaturalist cluster layer
- [Esri World Imagery](https://www.arcgis.com/) — satellite basemap
- [Esri Ocean Basemap](https://www.arcgis.com/) — ocean/bathymetry basemap (GEBCO, NOAA)
- [Seamap Australia](https://seamapaustralia.org/) — benthic habitat WMS
- [AusSeabed](https://www.ausseabed.gov.au/) — seabed sediment samples WMS

Map development assisted by Claude (Anthropic).

---

## Credits

**Eyre Lab for Restoration Ecology** — [eyrelab.org](https://www.eyrelab.org/)

Field surveys: Brian McQuillan, Manny Katz  
Data sources: iNaturalist community contributors, Martin et al. 2025, Gillies et al. 2018  
25 Reefs Project data: OzFish Unlimited, The Nature Conservancy Australia, SARDI

---

## License

Field survey data © Eyre Lab for Restoration Ecology.  
Historical data reproduced under academic fair use — cite original papers if used in publications.  
iNaturalist data: individual observation licenses vary (see `license` column in CSV); most are CC-BY or CC-BY-NC.

---

_Last updated: June 2026_
