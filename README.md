# Gulf Beds — Shellbed Atlas of South Australia

**An interactive reference map consolidating native bivalve presence data, historical reef records, active restoration sites, marine park boundaries, and community science observations across South Australia's gulf systems.**

Built for [Eyrelab](https://www.eyrelab.org/ourmission), a registered South Australian environmental charity headquartered on the Eyre Peninsula, founded and directed by Emmanuel "Manny" Katz. Developed and maintained by Brian Arruda, researcher at Eyrelab and lead steward of this map. Eyrelab acknowledges the Nauo people as Traditional Owners of the waters this work takes place in.

---

## Live map

🗺️ **[Open the map](https://eyrelab-sa.github.io/South-Australia-Shellfish-Map/)**

---

## Purpose

This is a working research and communication tool, not a regulatory product. It exists to answer one underlying question across four stages: what shellfish reef habitat existed historically, what's confirmed present today, what restoration is actively rebuilding, and what biodiversity is recolonising as a result.

## How the map is organised

The layer panel is a narrative arc, not a flat list of toggles:

1. **Historical record** — pre-collapse reef sites and species presence, digitised from peer-reviewed literature (Martin et al. 2025, Gillies et al. 2018).
2. **Modern presence** — current field surveys and published research confirming where species exist today (Eyrelab 2026 field surveys, Lindsey et al. 2026 Coffin Bay research).
3. **Active restoration** — reef-building programs currently underway across SA (Eyrelab's 25 Reefs, and the separate SA Government / TNC program).
4. **Reef biodiversity recovery** — community and citizen-science observations (iNaturalist, verified community sightings) showing what's recolonising restored and remnant habitat.

Within stages 2 and 4, species are split by role:

- **Tier 1 — reef-building species**: _Ostrea angasi_, _Malleus meridianus_, _Pinna dolabrata_. These are the structural focus of the project — the species whose reefs are being restored and whose recruitment is the primary success metric. They appear at every stage.
- **Tier 2 — associated reef biodiversity**: _Katelysia_ spp., _Equichlamys bifrons_. Not reef-builders themselves, but their presence indicates reef recovery and habitat quality. Shown at reduced visual prominence and off by default.

Marine parks and aquaculture leases sit outside the four-stage arc as spatial/regulatory context layers (see below).

**There is no Change & Disturbance / historic-vs-modern comparison layer on this map as of July 2026.** It existed earlier in the project but was removed — the methodology wasn't reliable enough to stand behind. A separate standalone tool (`historic_vs_modern_comparison.html`, not part of this repo's `index.html`) now handles that comparison per-species with proper source attribution; it is not embedded here.

---

## Interactivity

The map is built on Leaflet.js and is fully interactive out of the box:

- **Pan / zoom** — scroll wheel, +/− buttons, or pinch on touch devices. Marker clustering (iNaturalist and Lindsey layers) expands automatically as you zoom in.
- **Click any marker** — opens a popup with site name, source, status, evidence tier, or (for iNaturalist points) a direct link to the original observation page.
- **Layers panel (top right)** — toggle each data layer independently. Toggling a layer on auto-opens an info panel on the left summarising its source, record count, and caveats.
- **Species lens row** (in the field surveys panel) — re-colours and re-shapes all survey markers to the selected species without reloading the map.
- **Status filters** — show/hide field survey markers by Present / Uncertain / Absent / No data.
- **Basemap toggle** (header) — switch between Esri satellite imagery and an ocean/bathymetry basemap.
- **+ Report sighting** (top centre) — click-to-place mode for submitting a new community observation; pending review before it shows as verified.
- **About this map** (header) — the full methodology, source list, and limitations shown in-app, mirrored in this README.

---

## Reading the markers

Every _O. angasi_-related marker uses the same shell icon (species = shape) across all layers — field surveys, restoration sites, research data, community sightings. Other species use their own distinct shell shapes. Status and context are layered on top via opacity and rings, not colour swaps:

| Encoding                        | Meaning                                                    |
| ------------------------------- | ---------------------------------------------------------- |
| Full opacity                    | Confirmed present / active site                            |
| 55% opacity                     | Uncertain or indirect evidence (field surveys only)        |
| No icon                         | Absent or not yet surveyed                                 |
| Gold halo ring                  | Recruitment (juveniles/spat) confirmed                     |
| Solid / dashed teal ring        | Sanctuary Zone vs Control site (Lindsey et al. layer only) |
| Solid green / dashed amber ring | Verified vs pending community sighting                     |

Marine park polygons use a flat blue outline with light fill — no status ring system, since a park boundary doesn't carry a presence/absence state. Aquaculture leases use solid fill for Active status, dashed outline for Application/Pending/Rejected.

---

## Data layers and sources

### Field surveys — Eyrelab, 2026

In-water dive and snorkel assessments by Brian Arruda and Manny Katz, volunteering with Eyrelab, conducted in support of an independent researcher's _O. angasi_ genetics work. Sites span the Eyre Peninsula, Streaky Bay, Ceduna, and Whyalla.

**Assessment methods:** in-water (dive/snorkel, primary evidence), shore visual (intertidal only — does not confirm subtidal absence), secondhand (always recorded Uncertain).

**Status definitions:** Present = in-water positive ID. Uncertain = indirect evidence. Absent = negative in-water survey. No data = not yet assessed (≠ Absent).

### Research data — Lindsey et al. (2024 fieldwork, published 2026)

> Lindsey, N., Connell, S.D., Katz, E. & McAfee, D. (2026). Community-based marine restoration to generate social licence and ecological knowledge for upscaling oyster reef restoration. _People and Nature_ 8:301–315. [doi:10.1002/pan3.70211](https://doi.org/10.1002/pan3.70211)

Eight Coffin Bay sites (4 Sanctuary Zones, 4 Controls), all confirming _O. angasi_ recruitment via shell-basket restoration units deployed January–April 2024.

### Active restoration — Eyrelab's 25 Reefs Project

Statewide restoration program led by Eyrelab: cleaned oyster shell secured in biodegradable mesh, deployed in ~1-hectare units at sites with existing native oyster populations, built largely through community working-bees. First ecological results are expected ~5 years post-deployment. See [eyrelab.org/25-reefs](https://www.eyrelab.org/25-reefs).

### Active restoration — SA Government / The Nature Conservancy

A separate, larger-scale restoration program — distinct in funding, scale, and governance from Eyrelab's 25 Reefs — run by the [SA Government](https://www.environment.sa.gov.au/topics/coasts/rebuilding-sa-lost-shellfish-reefs) in partnership with The Nature Conservancy, University of Adelaide, and local councils, covering Windara, Glenelg, O'Sullivan Beach, and Nepean Bay.

### Historical record — Martin et al. 2025

> Martin, B., Huveneers, C., Reeves, S. & Baring, R. (2025). Reviving shellfish reef socio-ecological histories for modern management and restoration. _Ocean & Coastal Management_ 261:107540.

Digitised from the paper's supplementary table. Filters applied: _O. angasi_ — high-confidence records, ≤1950 or undated only. _P. dolabrata_ and _M. meridianus_ — high-confidence, **no date cutoff** (too few records to filter further — these two species' historic layer spans into the 1990s, not just pre-1950s).

### Historical record — Gillies et al. 2018

> Gillies, C.L., et al. (2018). Australian shellfish ecosystems: Past distribution, current status and future direction. _PLoS ONE_ 13(2):e0190914.

SA bounding-box subset of the paper's Figshare dataset. Species are not differentiated (_O. angasi_ and _S. glomerata_ combined).

### Community science — iNaturalist (all five species)

**All five iNaturalist layers are filtered to observations the observer annotated "Alive"** under iNaturalist's Life Stage / Alive-or-Dead field — not just species presence, but presence of a _living_ animal. This excludes the large volume of dead-shell-on-the-beach photos that otherwise dominate bivalve records on the platform, and it is a real annotation field, not a heuristic filter Eyrelab invented. Quality grade is mixed (research grade + needs-ID) rather than research-grade-only, since the "Alive" annotation is independent of ID consensus.

Current counts (as of July 2026 — check the live map's layer panel for anything more recent):

| Species          | n     | Date range | Note                                                                                                   |
| ---------------- | ----- | ---------- | ------------------------------------------------------------------------------------------------------ |
| _O. angasi_      | 28    | 2024–2026  | Down from an unfiltered ~4,400                                                                         |
| _M. meridianus_  | 24    | 2021–2026  | Down from an unfiltered ~764                                                                           |
| _P. dolabrata_   | 37    | 2013–2026  | Down from an unfiltered ~3,533                                                                         |
| _Katelysia_ spp. | **3** | 2025       | ⚠ Too few records to support any distribution or density claim — three individual sightings, not a map |
| _E. bifrons_     | 49    | 2013–2026  | Down from an unfiltered ~1,224                                                                         |

**This is a real limitation, not a data-quality bug to fix later:** iNaturalist is photo-based, and underwater photography is a niche, expensive skill — most bivalve observations on the platform are dead shells found on a beach, which is exactly what "Alive" filtering is designed to exclude. Low counts here reflect _annotation coverage_, not necessarily species scarcity — a real live sighting can be missing simply because nobody applied the tag.

### Marine parks — State Marine Park Network (DEW)

South Australia's 19 marine parks, DEW / data.sa.gov.au, CC BY 4.0 AU. The source data ships 31 polygon fragments across those 19 parks (same rack plan per park, no zone-type attribute supplied) — dissolved to one boundary per park and simplified (~95% coordinate reduction) for load performance.

**This layer shows outer park boundaries only.** Internal zoning (Sanctuary Zone, Habitat Protection Zone, Restricted Access Zone, General Managed Use Zone) is not represented in the source data and is not shown — do not use this layer to infer what activity is or isn't permitted inside a given park. Click a park for its gazettal dates, not its activity rules.

### Aquaculture leases — PIRSA

Oyster and mussel aquaculture lease polygons, PIRSA / data.sa.gov.au, CC BY 3.0 AU (601 oyster, 68 mussel). Solid fill = Active; dashed outline = Application/Pending/Rejected. A lease boundary is a licensing polygon, not an indicator of on-water stocking density.

### Reference layers

- **Benthic habitat** — [Seamap Australia](https://seamapaustralia.org) National Benthic Habitat Layer (WMS).
- **Seabed sediment** — [AusSeabed](https://www.ausseabed.gov.au) / Geoscience Australia (WMS, clipped to the SA bounding box but not the precise coastline).

---

## Limitations

- Survey coverage is opportunistic, not systematic — absence from the map does not mean absence in the water.
- Field and community sighting data added via the in-app tool is stored in browser local storage; clearing cache deletes unsaved entries that haven't been committed to the HTML source (see "Updating field data" below).
- Historical coordinates (Martin, Gillies) are digitised approximations, not surveyed positions.
- Gillies harvest data does not differentiate _O. angasi_ from _S. glomerata_.
- The seabed sediment layer is clipped to the SA bounding box, not the precise coastline.
- iNaturalist "Alive" filtering depends on the observer having applied that annotation — it isn't retroactive, so low counts (see _Katelysia_, above) reflect annotation coverage as much as species scarcity.
- Marine park boundaries are outer boundary only — no internal zoning shown.
- The `nativeMussel` field is taxonomically unresolved pending voucher specimens (candidates: _Brachidontes erosus_, _B. rostratus_, _Trichomya hirsuta_, _Mytilus galloprovincialis_).

---

## File structure

```
South-Australia-Shellfish-Map/
├── index.html                      # Main map — self-contained, open in browser
├── README.md                       # This file
└── data/
    ├── inat_angasi.js              # iNaturalist O. angasi, "Alive"-annotated only
    ├── inat_hammerOyster.js        # iNaturalist M. meridianus, "Alive"-annotated only
    ├── inat_razorfish.js           # iNaturalist P. dolabrata, "Alive"-annotated only
    ├── inat_cockle.js              # iNaturalist Katelysia spp., "Alive"-annotated only (n=3)
    ├── inat_scallop.js             # iNaturalist E. bifrons, "Alive"-annotated only
    ├── aquaculture_leases.js       # PIRSA aquaculture lease polygons (344 KB)
    ├── marine_parks.js             # DEW State Marine Park Network, 19 dissolved polygons (452 KB)
    ├── seabed_SA.py                # Processing script: clips Natural Earth coastline to SA bbox
    └── ne_10m_coastline (1)/       # Source shapefile for seabed_SA.py
```

Each `data/*.js` file is loaded as a plain `<script>` tag and registered in a try/catch wrapper — a missing file disables its checkbox in the Layers panel rather than crashing the page.

There is no `change_records.js` in this repo. The Change & Disturbance layer was removed in July 2026 (see "How the map is organised," above) and its data files deleted, not just unlinked.

---

## Updating field data

New sites added via the **+ Report sighting** / field survey UI save to browser local storage only. To commit them permanently:

1. Add/edit sites as normal in the live map.
2. Open browser DevTools → Application → Local Storage → find the relevant `sa-bivalve-*` key.
3. Copy the JSON value and paste it into the corresponding `DEFAULT_*` array in `index.html`.
4. Commit the updated HTML.

To refresh an iNaturalist layer with a new export: filter to "Alive" annotation on iNaturalist before exporting, convert to the `[lat, lng, id, YYYYMMDD, observer]` array format used in the existing `data/inat_*.js` files, and replace the file. Watch the variable name — it does not always match the filename (`inat_hammerOyster.js` exports `INAT_HAMMER`, not `INAT_HAMMEROYSTER`).

---

## Built with

- [Leaflet.js](https://leafletjs.com/) 1.9.4 — map framework
- [Leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster) 1.5.3 — clustering for iNaturalist and Lindsey layers
- Esri World Imagery — satellite basemap
- Esri Ocean Basemap (GEBCO, NOAA, National Geographic, DeLorme, HERE, Geonames.org) — ocean/bathymetry basemap
- [Seamap Australia](https://seamapaustralia.org) — benthic habitat WMS
- [AusSeabed](https://www.ausseabed.gov.au) — seabed sediment WMS
- OpenStreetMap contributors — place labels and coastline reference

---

## Organisation

[Eyrelab](https://www.eyrelab.org/ourmission) is a registered environmental charity on the Eyre Peninsula, South Australia, repairing degraded marine ecosystems through science-led, community-driven shellfish reef restoration, while empowering young people through hands-on marine science and connecting communities, Traditional Owners, researchers, and industry around shared environmental outcomes.

**Emmanuel "Manny" Katz** — Founder & Director, Eyrelab.
**Brian Arruda** — Researcher, Eyrelab; lead developer and steward of this map.

---

## License

Field survey data © Eyrelab. Historical data reproduced under academic fair use — cite the original papers if used in publication. iNaturalist data licensing varies by observation (mostly CC-BY or CC-BY-NC) — verify via the individual observation link before reuse. Marine park data CC BY 4.0 AU (DEW). Aquaculture lease data CC BY 3.0 AU (PIRSA).

---

_Last updated: July 2026_
