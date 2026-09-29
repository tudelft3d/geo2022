# Paper cross-check (2026-09-28)

The archive holds 312 theses, 22 of which already link a paper. The other 290 were compared against the GDMC publication list (838 scientific/conference papers), Crossref (searched per thesis on title and student author) and OpenAlex works of their supervisors and students, scoring candidates on co-authorship, title similarity and abstract similarity.

Accepted papers go into the entry's `paper:` field in _data/geotheses.yml (optionally `paper_label:`); rejected candidates go into scripts/verified_papers.yml with `verdict: not related` so they stop reappearing.

## Likely (106 theses)

Strong signals: student or supervisor co-authorship plus a clear title or abstract overlap.

- **Martijn Meijers (2006)** — Implementation and testing of variable scale topological data structures
  1. "A storage and transfer efficient data structure for variable scale vector data" — Chapter in: Advances in GIScience (Sester, Bernard, Paelke, eds.), pp., 2009 — [conference paper](https://doi.org/10.1007/978-3-642-00318-9_18)
     - authors: Martijn Meijers (student), Peter van Oosterom (supervisor: van Oosterom), Wilko Quak (supervisor: Quak)
     - title similarity 0.43; abstract similarity n/a; year +3  (source: GDMC)
  2. "A data model for multi-scale topographical data" — Chapter in: Headway in Spatial Data Handling (A. Ruas, C.M. Gold, eds., 2008 — [conference paper](https://doi.org/10.1007/978-3-540-68566-1_14)
     - authors: J.E. Stoter, J.M. Morales, R.L.G. Lemmens, M. Meijers (student), P.J.M. van Oosterom (supervisor: van Oosterom), C.W. Quak (supervisor: Quak), H.T. Uitermark, L. van den Brink
     - title similarity 0.42; abstract similarity n/a; year +2  (source: GDMC)
  3. "Comparing the vario-scale approach with a discrete multi-representation based approach for automated generalisation of topographic data" — Proceedings of the 15th Workshop of the ICA Commission on Generalisati, 2012 — [conference paper](https://www.gdmc.nl/publications/2012/vario-scale_approach_versus_multi-representation_approach.pdf)
     - authors: Martijn Meijers (student), Jantien Stoter, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.37; abstract similarity 0.37; year +6  (source: GDMC)
  4. "5D Modelling - applications and advantages" — Geospatial World Forum, Amsterdam, pp. 9, 2012 — [conference paper](https://www.gdmc.nl/publications/2012/5D_modeling_applications.pdf)
     - authors: Jantien Stoter, Hugo Ledoux, Martijn Meijers (student), Ken Arroyo Ohori, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.28; abstract similarity 0.43; year +6  (source: GDMC)
  5. "Parallel Creation of Vario-Scale Data Structures for Large Datasets" — ISPRS Archives Volume XL-4/W7, 4th ISPRS International Workshop on Web, 2015 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-4-w7-1-2015)
     - authors: Martijn Meijers (student), Radan &Scaron;uba, Peter van Oosterom (supervisor: van Oosterom), R. Šuba
     - title similarity 0.56; abstract similarity 0.15; year +9  (source: GDMC)
  6. "Evaluation of the dual half-edge data structure for implementation of a vario-scale model" — The international archives of the photogrammetry, remote sensing and, 2024 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-4-w11-2024-25-2024)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (student), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.39; abstract similarity 0.35; year +18  (source: OpenAlex)
  7. "Web-based dissemination of continuously generalized space-scale cube data for smooth user interaction" — International Journal of Cartography, 2020 — [journal article](https://doi.org/10.1080/23729333.2019.1705144)
     - authors: Martijn Meijers (student), Peter van Oosterom (supervisor: van Oosterom), Mattijs Driel, Radan Šuba
     - title similarity 0.43; abstract similarity 0.29; year +14  (source: OpenAlex)
  8. "2D to 1D and 2D to 0D Geometry Generalization Based on the Straight Skeleton by the Dual-Half Edge Structure" — The international archives of the photogrammetry, remote sensing and, 2025 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-g-2025-513-2025)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (student), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.44; abstract similarity 0.24; year +19  (source: OpenAlex)
  9. "Towards a true vario-scale structure supporting smooth-zoom" — Proceedings of the 14th Workshop of the ICA Commission on Generalisati, 2011 — [conference paper](https://www.gdmc.nl/publications/2011/True_vario-scale_structure.pdf)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Martijn Meijers (student)
     - title similarity 0.40; abstract similarity n/a; year +5  (source: GDMC)
  10. "SplitArea: een algoritme om vlakken te splitsen voor de tGAP datastructuren" — Research Repository (Delft University of Technology), 2013 — [journal article](https://openalex.org/W2122823746)
     - authors: Martijn Meijers (student), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.45; abstract similarity 0.02; year +7  (source: OpenAlex)
  … and 12 more likely candidates; re-run with --limit/--surname to see them all.
- **Arnoud de Boer (2007)** — Label placement in 3D georeferenced and oriented digital photographs using GIS t
  1. "Processing 3D Geo-Information for Augmenting Georeferenced and Oriented Photographs with Text Labels" — Lecture notes in geoinformation and cartography, 2008 — [book-chapter](https://doi.org/10.1007/978-3-540-68566-1_20)
     - authors: Arnoud De Boer (student), Eduardo Dias (supervisor: Dias), Edward Verbree (supervisor: Verbree)
     - title similarity 0.58; abstract similarity n/a; year +1  (source: OpenAlex)
- **Steven Pluymaekers (2007)** — A data analysis to bed dynamics in the Western Scheldt estuary
  1. "A deformation analysis of a dynamic estuary using two-weekly MBES surveying" — OCEANS 2007 - Europe, 2007 — [conference paper](https://doi.org/10.1109/oceanse.2007.4302305)
     - authors: Steven Pluymaekers (student), Roderik Lindenbergh (supervisor: Lindenbergh), Dick Simons, John de Ronde
     - title similarity 0.47; abstract similarity n/a; year +0  (source: Crossref)
- **Cornelis Slobbe (2007)** — Towards a combined estimation of Greenland’s ice sheet mass balance using GRACE 
  1. "Estimating the rates of mass change, ice volume change and snow volume change in Greenland from ICESat and GRACE data" — Geophysical Journal International, 2009 — [journal article](https://doi.org/10.1111/j.1365-246x.2008.03978.x)
     - authors: D. C. Slobbe (student), P. Ditmar (supervisor: Ditmar), R. C. Lindenbergh (supervisor: Lindenbergh)
     - title similarity 0.40; abstract similarity n/a; year +2  (source: Crossref)
  2. "Estimation of volume change rates of Greenland's ice sheet from ICESat data using overlapping footprints" — Remote Sensing of Environment, 2008 — [journal article](https://doi.org/10.1016/j.rse.2008.07.004)
     - authors: D SLOBBE, R LINDENBERGH (supervisor: Lindenbergh), P DITMAR (supervisor: Ditmar)
     - title similarity 0.49; abstract similarity n/a; year +1  (source: Crossref)
- **Arjen Hofman (2008)** — Developing a vario-scale IMGeo using the constrained tGAP structure
  1. "Using the constrained tGAP for generalisation of IMGeo to TOP10NL model" — Proceedings of the 11th ICA International Workshop on Generalization, , 2008 — [conference paper](https://www.gdmc.nl/publications/2008/Constrained_tGAP.pdf)
     - authors: Arjen Hofman (student), Arta Dilo (supervisor: Dilo), Peter van Oosterom (supervisor: van Oosterom), Nicole Borkens
     - title similarity 0.45; abstract similarity n/a; year +0  (source: GDMC)
  2. "Harmonising and Integrating Two Domain Models Topography" — Chapter in: SDI Convergence - Research, Emerging Trends and Critical A, 2009 — [conference paper](https://www.gdmc.nl/publications/2009/Topography_Domain_Models.pdf)
     - authors: Jantien Stoter, Wilko Quak, Arjen Hofman (student)
     - title similarity 0.35; abstract similarity n/a; year +1  (source: GDMC)
- **Sami Samiei-Esfahany (2008)** — Improving Persistent Scatterer Interferometry Results for Deformation Monitoring
  1. "Radar transponders and their combination with GNSS for deformation monitoring" — 2012 IEEE International Geoscience and Remote Sensing Symposium, 2012 — [conference paper](https://doi.org/10.1109/igarss.2012.6350562)
     - authors: Pooja Mahapatra, Hans van der Marel, Ramon Hanssen (supervisor: Hanssen), Rachel Holley, Sami Samiei-Esfahany (student), Marko Komac, Alan Fromberg
     - title similarity 0.54; abstract similarity n/a; year +4  (source: Crossref)
  2. "On the Use of Transponders as Coherent Radar Targets for SAR Interferometry" — IEEE Transactions on Geoscience and Remote Sensing, 2014 — [journal article](https://doi.org/10.1109/tgrs.2013.2255881)
     - authors: Pooja S. Mahapatra, Sami Samiei-Esfahany (student), Hans van der Marel, Ramon F. Hanssen (supervisor: Hanssen)
     - title similarity 0.39; abstract similarity n/a; year +6  (source: Crossref)
- **Doğan Altundağ (2009)** — De-noising terrestrial laser scanning data for roughness characterization of roc
  1. "Influence of range measurement noise on roughness characterization of rock surfaces using terrestrial laser scanning" — International Journal of Rock Mechanics and Mining Sciences, 2011 — [journal article](https://doi.org/10.1016/j.ijrmms.2011.09.007)
     - authors: Kourosh Khoshelham (supervisor: Khoshelham), Dogan Altundag (student), Dominique Ngan-Tillard (supervisor: Ngan-Tillard), Massimo Menenti (supervisor: Menenti)
     - title similarity 0.54; abstract similarity n/a; year +2  (source: Crossref)
- **Ramses Amadeus Molijn (2009)** — ICESat full waveform signal analysis for the classification of land cover types 
  1. "ICESat laser full waveform analysis for the classification of land cover types over the cryosphere" — International Journal of Remote Sensing, 2011 — [journal article](https://doi.org/10.1080/01431161.2010.547532)
     - authors: R. A. Molijn (student), R. C. Lindenbergh (supervisor: Lindenbergh), B. C. Gunter (supervisor: Gunter)
     - title similarity 0.93; abstract similarity n/a; year +2  (source: Crossref)
- **Endang Widiastuti (2009)** — Data assimilation of GRACE terrestrial water storage data into a hydrological mo
  1. "Data assimilation of GRACE terrestrial water storage estimates into a regional hydrological model of the Rhine River basin" — ?, 2014 — [posted-content](https://doi.org/10.5194/hessd-11-11837-2014)
     - authors: N. Tangdamrongsub, S. C. Steele-Dunne (supervisor: Steele-Dunne), B. C. Gunter (supervisor: Gunter), P. G. Ditmar, A. H. Weerts
     - title similarity 0.72; abstract similarity 0.57; year +5  (source: Crossref)
  2. "Data assimilation of GRACE terrestrial water storage estimates into a regional hydrological model of the Rhine River basin" — Hydrology and Earth System Sciences, 2015 — [journal article](https://doi.org/10.5194/hess-19-2079-2015)
     - authors: N. Tangdamrongsub, S. C. Steele-Dunne (supervisor: Steele-Dunne), B. C. Gunter (supervisor: Gunter), P. G. Ditmar, A. H. Weerts
     - title similarity 0.72; abstract similarity 0.56; year +6  (source: Crossref)
- **Ken Arroyo Ohori (2010)** — Validation and automatic repair of planar partitions using a constrained triangu
  1. "Validation and Automatic Repair of Planar Partitions Using a Constrained Triangulation" — Photogrammetrie, Fernerkundung und Geoinformation (PFG), 2012(5), pp. , 2012 — [journal article](https://doi.org/10.1127/1432-8364/2012/0143)
     - authors: Ken Arroyo Ohori (student), Hugo Ledoux (supervisor: Ledoux), Martijn Meijers (supervisor: Meijers)
     - title similarity 1.00; abstract similarity n/a; year +2  (source: GDMC)
  2. "Automatically repairing invalid polygons with a constrained triangulation" — Proceedings of the AGILE 2012 International Conference (J. Gensel, D. , 2012 — [conference paper](https://www.gdmc.nl/publications/2012/Automatically_repairing_with_constrained_triangulation.pdf)
     - authors: Hugo Ledoux (supervisor: Ledoux), Ken Arroyo Ohori (student), Martijn Meijers (supervisor: Meijers)
     - title similarity 0.65; abstract similarity n/a; year +2  (source: GDMC)
  3. "Automatically repairing polygons and planar partitions with prepair and pprepair" — Proceedings of the 4th Open Source GIS UK Conference, Nottingham, pp. , 2012 — [conference paper](https://www.gdmc.nl/publications/2012/Automatically_repairing_polygons_and_planar_partitions.pdf)
     - authors: Ken Arroyo Ohori (student), Hugo Ledoux (supervisor: Ledoux), Martijn Meijers (supervisor: Meijers)
     - title similarity 0.52; abstract similarity n/a; year +2  (source: GDMC)
  4. "Edge-matching polygons with a constrained triangulation" — Proceedings of the GIS Ostrava 2011 Symposium, pp. 11, 2011 — [conference paper](https://www.gdmc.nl/publications/2011/Edge-matching_polygons.pdf)
     - authors: H. Ledoux (supervisor: Ledoux), K. Arroyo Ohori (student)
     - title similarity 0.59; abstract similarity n/a; year +1  (source: GDMC)
  5. "Solving the horizontal conflation problem with a constrained Delaunay triangulation" — Journal of Geographical Systems, 2016 — [journal article](https://doi.org/10.1007/s10109-016-0237-7)
     - authors: Hugo Ledoux (supervisor: Ledoux), Ken Arroyo Ohori (student)
     - title similarity 0.52; abstract similarity n/a; year +6  (source: Crossref)
  6. "Modelling Higher Dimensional Data for GIS Using Generalised Maps" — Chapter in: Proceedings 13th International Conference on Computational, 2013 — [conference paper](https://doi.org/10.1007/978-3-642-39637-3_41)
     - authors: Ken Arroyo Ohori (student), Hugo Ledoux (supervisor: Ledoux), Jantien Stoter
     - title similarity 0.38; abstract similarity n/a; year +3  (source: GDMC)
  7. "A dimension-independent extrusion algorithm using generalised maps" — International Journal of Geographical Information Science, 2015 — [journal article](https://doi.org/10.1080/13658816.2015.1010535)
     - authors: Ken Arroyo Ohori (student), Hugo Ledoux (supervisor: Ledoux), Jantien Stoter
     - title similarity 0.36; abstract similarity n/a; year +5  (source: Crossref)
  8. "Validation of Planar Partitions using Constrained Triangulations" — Proceedings of the Joint International Conference on Theory, Data Hand, 2010 — [conference paper](https://www.gdmc.nl/publications/2010/Validation_planar_partitions.pdf)
     - authors: Hugo Ledoux (supervisor: Ledoux), Martijn Meijers (supervisor: Meijers)
     - title similarity 0.85; abstract similarity n/a; year +0  (source: GDMC)
- **Maja Bitenc (2010)** — Evaluation of a laser Land-based Mobile Mapping System for measuring sandy coast
  1. "Evaluation of a LIDAR Land-Based Mobile Mapping System for Monitoring Sandy Coasts" — Remote Sensing, 2011 — [journal article](https://doi.org/10.3390/rs3071472)
     - authors: Maja Bitenc (student), Roderik Lindenbergh (supervisor: Lindenbergh), Kourosh Khoshelham (supervisor: Khoshelham), A. Pieter Van Waarden
     - title similarity 0.84; abstract similarity 0.59; year +1  (source: Crossref)
  2. "EVALUATION OF WAVELET AND NON-LOCAL MEAN DENOISING OF TERRESTRIAL LASER SCANNING DATA FOR SMALL-SCALE JOINT ROUGHNESS ESTIMATION" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2016 — [journal article](https://doi.org/10.5194/isprsarchives-xli-b3-181-2016)
     - authors: M. Bitenc (student), D. S. Kieffer, K. Khoshelham (supervisor: Khoshelham)
     - title similarity 0.39; abstract similarity 0.17; year +6  (source: Crossref)
- **Menno Bloemsma (2010)** — Semi-automatic core characterisation based on geochemical logging data
  1. "From Routine to Integrated Core Analysis: Setting Up the Database for Reservoir Quality Modelling" — Proceedings, 2018 — [conference paper](https://doi.org/10.3997/2214-4609.201801136)
     - authors: S. Henares Ladron de Guevara, G.J. Weltje (supervisor: Weltje), M.E. Donselaar, M. Bloemsma (student), R. Tjallingii, B. De Wijn
     - title similarity 0.41; abstract similarity n/a; year +8  (source: Crossref)
- **Dinesh Sharma Kalpoe (2010)** — Vibration Measurement of a Model Wind Turbine using High Speed Photogrammetry
  1. "Vibration measurement of a model wind turbine using high speed photogrammetry" — Proceedings of SPIE, the International Society for Optical Engineering, 2011 — [conference paper](https://doi.org/10.1117/12.889440)
     - authors: Dinesh Kalpoe (student), Kourosh Khoshelham (supervisor: Khoshelham), Ben Gorte (supervisor: Gorte)
     - title similarity 1.00; abstract similarity 0.55; year +1  (source: OpenAlex)
- **Hang Yu (2010)** — Monitoring Glacier Elevation Changes over the Tibetan Plateau Using ALOS PRISM a
  1. "Monitoring glacial thickness changes in the Tibetan Plateau derived from ICESat data" — Science and Technology Development Journal, 2016 — [journal article](https://doi.org/10.32508/stdj.v19i2.677)
     - authors: Vu Hien Phan, Roderik Lindenbergh (supervisor: Lindenbergh), Massimo Menenti (supervisor: Menenti)
     - title similarity 0.65; abstract similarity 0.49; year +6  (source: Crossref)
  2. "Orientation dependent glacial changes at the Tibetan Plateau derived from 2003–2009 ICESat laser altimetry" — ?, 2014 — [posted-content](https://doi.org/10.5194/tcd-8-2425-2014)
     - authors: V. H. Phan, R. C. Lindenbergh (supervisor: Lindenbergh), M. Menenti (supervisor: Menenti)
     - title similarity 0.51; abstract similarity 0.47; year +4  (source: Crossref)
  3. "Supplementary material to &quot;Orientation dependent glacial changes at the Tibetan Plateau derived from 2003–2009 ICESat laser altimetry&quot;" — ?, 2014 — [posted-content](https://doi.org/10.5194/tcd-8-2425-2014-supplement)
     - authors: V. H. Phan, R. C. Lindenbergh (supervisor: Lindenbergh), M. Menenti (supervisor: Menenti)
     - title similarity 0.46; abstract similarity n/a; year +4  (source: Crossref)
- **Mohamed Saleh (2011)** — Sediment classification using Sub-bottom profiler
  1. "Seabed sub-bottom sediment classification using parametric sub-bottom profiler" — NRIAG Journal of Astronomy and Geophysics, 2016 — [journal article](https://doi.org/10.1016/j.nrjag.2016.01.004)
     - authors: Mohamed Saleh (student), Mostafa Rabah
     - title similarity 0.78; abstract similarity n/a; year +5  (source: Crossref)
  2. "Supply Chain Performance Measurement Approaches: Review and Classification" — The Journal of Organizational Management Studies, 2012 — [journal article](https://doi.org/10.5171/2012.872753)
     - authors: Nedaa Agami, Mohamed Saleh (student), Mohamed Rasmy
     - title similarity 0.36; abstract similarity n/a; year +1  (source: Crossref)
- **Bas van Goor (2011)** — Change detection and deformation analysis using Terrestrial Laser Scanning
  1. "Scatterer identification and analysis using combined InSAR and laser data" — Geophysical Research Abstracts (online), EGU General Assembly 2018, 20, 2018 — [conference paper](https://meetingorganizer.copernicus.org/EGU2018/EGU2018-17008.pdf)
     - authors: Ramon Hanssen (supervisor: Hanssen), Adriaan van Natijne, Roderik Lindenbergh (supervisor: Lindenbergh), Prabu Dheenathayalan, Mengshi Yang, Ling Chang, Freek van Leijen, Paco Lopez Dekker, Jippe van der Maaden, Peter van Oosterom, Hanjiang Xiong, PingBo Hu, Zhang Zhan
     - title similarity 0.55; abstract similarity n/a; year +7  (source: GDMC)
  2. "Change detection and deformation analysis using static and mobile laser scanning" — Applied Geomatics, 2015 — [journal article](https://doi.org/10.1007/s12518-014-0151-y)
     - authors: Roderik Lindenbergh (supervisor: Lindenbergh), Peter Pietrzyk
     - title similarity 0.88; abstract similarity n/a; year +4  (source: Crossref)
- **Josafat Isaí Guerrero Iñiguez (2012)** — Three-dimensional reconstruction of underground utilities for real-time visualiz
  1. "Multi-robot coalition formation in real-time scenarios" — Robotics and Autonomous Systems, 2012 — [journal article](https://doi.org/10.1016/j.robot.2012.06.004)
     - authors: José Guerrero (student), Gabriel Oliver
     - title similarity 0.39; abstract similarity n/a; year +0  (source: Crossref)
  2. "Auction and Swarm Multi-Robot Task Allocation Algorithms in Real Time Scenarios" — Multi-Robot Systems, Trends and Development, 2011 — [book-chapter](https://doi.org/10.5772/13281)
     - authors: Gabriel Oliver, Jos Guerrero (student)
     - title similarity 0.42; abstract similarity n/a; year -1  (source: Crossref)
  3. "3D Visualisation of Underground Pipelines: Best Strategy for 3D Scene Creation" — Chapter in: ISPRS Annals Volume II-2/W1, Proceedings of the ISPRS 8th , 2013 — [conference paper](https://doi.org/10.5194/isprsannals-ii-2-w1-139-2013)
     - authors: J. Guerrero. S. Zlatanova (supervisor: Zlatanova), M. Meijers (supervisor: Meijers)
     - title similarity 0.53; abstract similarity n/a; year +1  (source: GDMC)
- **Simeon Nedkov (2012)** — Knowledge-based optimisation of three-dimensional city models for car navigation
  1. "Enabling obstacle avoidance for Google Maps' navigation service" — Proceedings Gi4DM 2011, Antalya (O. Altan, R. Backhous, P. Boccardo, D, 2011 — [conference paper](https://www.gdmc.nl/publications/2011/Enabling_obstacle_avoidance.pdf)
     - authors: Simeon Nedkov (student), Sisi Zlatanova
     - title similarity 0.38; abstract similarity n/a; year -1  (source: GDMC)
- **Ravi Peters (2012)** — A Voronoi- and surface-based approach for the automatic generation of depth-cont
  1. "A Voronoi-based approach to generating depth-contours for hydrographic charts" — Marine Geodesy, 37(2), pp. 145-166, 2014 — [journal article](https://doi.org/10.1080/01490419.2014.902882)
     - authors: Ravi Peters (student), Hugo Ledoux (supervisor: Ledoux), Martijn Meijers
     - title similarity 0.83; abstract similarity n/a; year +2  (source: GDMC)
  2. "Generation and generalization of safe depth-contours for hydrographic charts using a surface-based approach" — Proceedings of the 16th ICA Generalisation Workshop (D. Burghardt, ed., 2013 — [conference paper](https://www.gdmc.nl/publications/2013/Safe_depth-contours_hydrographic_charts.pdf)
     - authors: R.Y. Peters (student), H. Ledoux (supervisor: Ledoux), M. Meijers
     - title similarity 0.64; abstract similarity n/a; year +1  (source: GDMC)
- **Marija Krūminaitė (2014)** — Space subdivision for indoor navigation
  1. "Indoor Space Subdivision for Indoor Navigation" — Chapter in: Proceedings of the 6th ACM SIGSPATIAL International Worksh, 2014 — [conference paper](https://doi.org/10.1145/2676528.2676529)
     - authors: Marija Krūminaitė (student), Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 1.00; abstract similarity n/a; year +0  (source: GDMC)
  2. "A 3D Model Based Indoor Navigation System for Hubei Provincial Museum" — ISPRS Archives Volume XL-4/W4, ISPRS Acquisition and Modelling of Indo, 2013 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-4-w4-51-2013)
     - authors: W. Xu, M. Kruminaite (student), B. Onrust, H. Liu, Q. Xiong, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.40; abstract similarity n/a; year -1  (source: GDMC)
  3. "A Conceptual Framework of Space Subdivision for Indoor Navigation" — Chapter in: Proceedings of the Fifth ACM SIGSPATIAL International Work, 2013 — [conference paper](https://doi.org/10.1145/2533810.2533819)
     - authors: Sisi Zlatanova (supervisor: Zlatanova), Liu Liu, George Sithole
     - title similarity 0.76; abstract similarity n/a; year -1  (source: GDMC)
  4. "Spatial subdivision of complex indoor environments for 3D indoor navigation" — International Journal of Geographical Information Science, 2017 — [journal article](https://doi.org/10.1080/13658816.2017.1376066)
     - authors: Abdoulaye A. Diakité, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.65; abstract similarity n/a; year +3  (source: Crossref)
  5. "A Two-level Path-finding Strategy for Indoor Navigation" — Chapter in: Intelligent Systems for Crisis Management (S. Zlatanova, R, 2013 — [conference paper](https://doi.org/10.1007/978-3-642-33218-0_3)
     - authors: Liu Liu, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.59; abstract similarity n/a; year -1  (source: GDMC)
  6. "Space-based Navigation Models" — Seamless 3D Navigation in Indoor and Outdoor Spaces, 2022 — [book-chapter](https://doi.org/10.1201/9781003281146-3)
     - authors: Jinjin Yan, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.56; abstract similarity n/a; year +8  (source: Crossref)
- **Haicheng Liu (2014)** — Comparing NetCDF and a multidimensional array database on managing and querying 
  1. "Managing large multidimensional hydrologic datasets: A case study comparing NetCDF and SciDB" — Journal of Hydroinformatics, IWA Publishing, 20(5), pp. 1058-1070, 2018 — [journal article](https://doi.org/10.2166/hydro.2018.136)
     - authors: Haicheng Liu (student), Peter van Oosterom (supervisor: van Oosterom), Theo Tijssen (supervisor: Tijssen), Tom Commandeur (supervisor: Commandeur), Wen Wang
     - title similarity 0.77; abstract similarity 0.66; year +4  (source: GDMC)
  2. "Managing Large Multidimensional Array Hydrologic Datasets: A Case Study Comparing NetCDF and SciDB" — Procedia Engineering, 154, pp. 207-214, 2016 — [journal article](https://doi.org/10.1016/j.proeng.2016.07.449)
     - authors: Haicheng Liu (student), Peter van Oosterom (supervisor: van Oosterom), Chengfang Hu, Wen Wang
     - title similarity 0.85; abstract similarity 0.83; year +2  (source: GDMC)
  3. "Towards a relational database Space Filling Curve (SFC) interface specification for managing nD-PointClouds" — Geoinformationssysteme 2019, Beiträge zur 6. Münchner GI-Runde (Thomas, 2019 — [conference paper](https://www.gdmc.nl/publications/2019/DBMS-nD-PC-GI-Runde2019.pdf)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Martijn Meijers, Edward Verbree, Haicheng Liu (student), Theo Tijssen (supervisor: Tijssen)
     - title similarity 0.37; abstract similarity n/a; year +5  (source: GDMC)
  4. "The design and application of histogram trees for querying massive LiDAR point clouds" — Proceedings of 5th China LiDAR Conference, Xiamen, China, pp. 1-8, 201, 2019 — [conference paper](https://www.gdmc.nl/publications/2019/Design_Application_Histogram_Trees_Massive_LiDAR_Point_Clouds.pdf)
     - authors: Haicheng Liu (student), Xuefeng Guan, Martijn Meijers, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.37; abstract similarity n/a; year +5  (source: GDMC)
  5. "Comparing NetCDF and SciDB on managing and querying 5D hydrologic dataset" — IOP Conference Series: Earth and Environmental Science, 2016 — [journal article](https://doi.org/10.1088/1755-1315/46/1/012031)
     - authors: Haicheng Liu (student), Xiao Xiao
     - title similarity 0.69; abstract similarity n/a; year +2  (source: Crossref)
- **Elise Tierie (2014)** — Visualisation conformity of three dimensional IMGeo for emergency response
  1. "Trauma-Related Clinical Practice Variation in Dutch Emergency Departments" — Healthcare, 2023 — [journal article](https://doi.org/10.3390/healthcare11050748)
     - authors: Elise L. Tierie (student), Dennis G. Barten, Laura M. Esteve Cuevas, Rebekka Veugelers, Menno I. Gaakeer
     - title similarity 0.35; abstract similarity 0.06; year +9  (source: Crossref)
  2. "Validation of Three-Dimensional Geometries" — Encyclopedia of GIS, 2017 — [reference-entry](https://doi.org/10.1007/978-3-319-17885-1_1550)
     - authors: Paul Colley, Baris M. Kazar, Ravi Kothuri, Peter van Oosterom (supervisor: van Oosterom), Siva Ravada
     - title similarity 0.67; abstract similarity n/a; year +3  (source: OpenAlex)
  3. "Validation of Three-Dimensional Geometries" — Encyclopedia of GIS, 2015 — [reference-entry](https://doi.org/10.1007/978-3-319-23519-6_1550-1)
     - authors: Paul Colley, Baris M. Kazar, Ravi Kothuri, Peter van Oosterom (supervisor: van Oosterom), Siva Ravada
     - title similarity 0.67; abstract similarity n/a; year +1  (source: OpenAlex)
  4. "On Valid and Invalid Three-Dimensional Geometries" — Lecture notes in geoinformation and cartography, 2008 — [book-chapter](https://doi.org/10.1007/978-3-540-72135-2_2)
     - authors: Baris M. Kazar, Ravi Kothuri, Peter van Oosterom (supervisor: van Oosterom), Siva Ravada
     - title similarity 0.59; abstract similarity n/a; year -6  (source: OpenAlex)
- **Weilin Xu (2014)** — Spatial model-aided indoor tracking
  1. "LEVERAGING SPATIAL MODEL TO IMPROVE INDOOR TRACKING" — The International Archives of the Photogrammetry, Remote Sensing and S, 2015 — [journal article](https://doi.org/10.5194/isprsarchives-xl-4-w5-75-2015)
     - authors: L. Liu (supervisor: Liu), W. Xu (student), W. Penard, S. Zlatanova
     - title similarity 0.74; abstract similarity 0.33; year +1  (source: Crossref)
  2. "A 3D Model Based Indoor Navigation System for Hubei Provincial Museum" — ISPRS Archives Volume XL-4/W4, ISPRS Acquisition and Modelling of Indo, 2013 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-4-w4-51-2013)
     - authors: W. Xu (student), M. Kruminaite, B. Onrust, H. Liu (supervisor: Liu), Q. Xiong, S. Zlatanova
     - title similarity 0.42; abstract similarity n/a; year -1  (source: GDMC)
  3. "A pedestrian tracking algorithm using grid-based indoor model" — Automation in Construction, 2018 — [journal article](https://doi.org/10.1016/j.autcon.2018.03.031)
     - authors: Weilin Xu (student), Liu Liu (supervisor: Liu), Sisi Zlatanova, Wouter Penard, Qing Xiong
     - title similarity 0.38; abstract similarity n/a; year +4  (source: Crossref)
- **Milo Janssen (2015)** — 3D Intersection operations for voxel data represented as surfaces in GIS
  1. "Installed base registration of decentralised solar panels with applications in crisis management" — ISPRS Archives Volume XL-3/W3, ISPRS Geospatial Week 2015 (S. Zlatanov, 2015 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-3-w3-219-2015)
     - authors: R. Aarsen, M. Janssen (student), M. Ramkisoen, F. Biljecki, C.W. Quak, E. Verbree
     - title similarity 0.39; abstract similarity n/a; year +0  (source: GDMC)
- **Antigoni Makri (2015)** — Indoor Signposting and Wayfinding through an Adaptation of the Dutch cyclist Jun
  1. "An Approach for Indoor Wayfinding replicating main Principles of an outdoor Navigation System for Cyclists" — ISPRS Archives Volume XL-4/W5, Indoor-Outdoor Seamless Modelling, Mapp, 2015 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-4-w5-29-2015)
     - authors: A. Makri (student), S. Zlatanova, E. Verbree (supervisor: Verbree)
     - title similarity 0.40; abstract similarity 0.58; year +0  (source: GDMC)
  2. "Indoor Signposting and Wayfinding through an Adaptation of the Dutch Cyclist Junction Network System" — Proceedings of the 11th International Symposium on Location-Based Serv, 2014 — [conference paper](https://www.gdmc.nl/publications/2014/Indoor_Signposting_and_Wayfinding.pdf)
     - authors: Antigoni Makri (student), Edward Verbree (supervisor: Verbree)
     - title similarity 1.00; abstract similarity n/a; year -1  (source: GDMC)
- **Benny Onrust (2015)** — Automatic generation of plant distributions for existing and future natural envi
  1. "Ecologically Sound Procedural Generation of Natural Environments" — International Journal of Computer Games Technology, 2017 — [journal article](https://doi.org/10.1155/2017/7057141)
     - authors: Benny Onrust (student), Rafael Bidarra, Robert Rooseboom, Johan van de Koppel
     - title similarity 0.45; abstract similarity 0.35; year +2  (source: Crossref)
  2. "Procedural generation and interactive web visualization of natural environments" — Proceedings of the 20th International Conference on 3D Web Technology, 2015 — [conference paper](https://doi.org/10.1145/2775292.2775306)
     - authors: Benny Onrust (student), Rafael Bidarra, Robert Rooseboom, Johan van de Koppel
     - title similarity 0.50; abstract similarity n/a; year +0  (source: Crossref)
- **Maarten Pronk (2015)** — Storing massive TINs in a DBMS - A comparison and a prototype implementation of 
  1. "COMPARATIVE ANALYSIS OF DATA STRUCTURES FOR STORING MASSIVE TINS IN A DBMS" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2016 — [journal article](https://doi.org/10.5194/isprsarchives-xli-b2-123-2016)
     - authors: K. Kumar, H. Ledoux (supervisor: Ledoux), J. Stoter (supervisor: Stoter)
     - title similarity 0.34; abstract similarity 0.57; year +1  (source: Crossref)
- **Haoxiang Wu (2015)** — Integration of 2D architectural floor plans into Indoor OpenStreetMap for recons
  1. "Extrusion-to-Masoning: Robotic 3D Concrete Printing of Concrete Shells As Building Floor System" — CAADRIA proceedings, 2023 — [conference paper](https://doi.org/10.52842/conf.caadria.2023.2.139)
     - authors: Hao Wu (student), Sijia Gu, Xiaofan Gao, Jiaxiang Luo, Philip F. Yuan*
     - title similarity 0.37; abstract similarity n/a; year +8  (source: Crossref)
- **Kaixuan Zhou (2015)** — Exploring Regularities for Improving Quality of Facade Reconstruction from Point
  1. "EXPLORING REGULARITIES FOR IMPROVING FAÇADE RECONSTRUCTION FROM POINT CLOUDS" — The International Archives of the Photogrammetry, Remote Sensing and S, 2016 — [journal article](https://doi.org/10.5194/isprs-archives-xli-b5-749-2016)
     - authors: K. Zhou (student), B. Gorte (supervisor: Gorte), S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.93; abstract similarity 0.61; year +1  (source: Crossref)
- **Florian W. Fichtner (2016)** — Semantic enrichment of a point cloud based on an octree for multi-storey pathfin
  1. "Semantic enrichment of octree structured point clouds for multi‐story 3D pathfinding" — Transactions in GIS, 2018 — [journal article](https://doi.org/10.1111/tgis.12308)
     - authors: Florian W. Fichtner (student), Abdoulaye A. Diakité (supervisor: Diakite), Sisi Zlatanova (supervisor: Zlatanova), Robert Voûte
     - title similarity 0.76; abstract similarity 0.59; year +2  (source: Crossref)
  2. "UKIS-CSMASK: A PYTHON PACKAGE FOR MULTI-SENSOR CLOUD AND CLOUD SHADOW SEGMENTATION" — The International Archives of the Photogrammetry, Remote Sensing and S, 2022 — [journal article](https://doi.org/10.5194/isprs-archives-xliii-b3-2022-217-2022)
     - authors: M. Wieland, F. Fichtner (student), S. Martinis
     - title similarity 0.39; abstract similarity 0.27; year +6  (source: Crossref)
  3. "Using a linear octree to identify empty space in indoor point clouds for 3D pathfinding" — Proceedings of the 19th AGILE International Conference on Geographic I, 2016 — [conference paper](https://www.gdmc.nl/publications/2016/Linear_octree_identify_empty_space_indoor_point_clouds.pdf)
     - authors: Tom Broersen, Florian W. Fichtner (student), Erik J. Heeres, Ivo de Liefde, Olivier B.P.M. Rodenberg, Edward Verbree, Robert Vo&ucirc;te
     - title similarity 0.49; abstract similarity n/a; year +0  (source: GDMC)
  4. "S1S2-Water: A global dataset for semantic segmentation of water bodies from Sentinel-1 and Sentinel-2 satellite images" — ?, 2023 — [posted-content](https://doi.org/10.36227/techrxiv.24081582)
     - authors: Marc Wieland, Florian Fichtner (student), Sandro Martinis, Sandro Groth, Christian Krullikowski, Simon Plank, Mahdi Motagh
     - title similarity 0.38; abstract similarity 0.06; year +7  (source: Crossref)
- **Eftychia Kalogianni (2016)** — Linking the legal with the physical reality of 3D objects in the context of Land
  1. "INTERLIS Language for Modelling Legal 3D Spaces and Physical 3D Objects by Including Formalized Implementable Constraints and Meaningful Code Lists" — ISPRS International Journal of Geo-Information, MDPI AG, 6(10), pp. 31, 2017 — [journal article](https://doi.org/10.3390/ijgi6100319)
     - authors: Eftychia Kalogianni (student), Efi Dimopoulou, Wilko Quak (supervisor: Quak), Michael Germann, Lorenz Jenni, Peter van Oosterom (supervisor: van Oosterom), Ruba Jaljolie, Sagi Dalyot
     - title similarity 0.45; abstract similarity 0.48; year +1  (source: GDMC)
  2. "Modelling the legal spaces of 3D underground objects in 3D land administration systems" — Land Use Policy, Elsevier BV, 127, pp. 106537, 2023 — [journal article](https://www.sciencedirect.com/science/article/pii/S0264837723000030)
     - authors: Rohit Ramlakhan, Eftychia Kalogianni (student), Peter van Oosterom (supervisor: van Oosterom), Behnam Atazadeh
     - title similarity 0.56; abstract similarity 0.36; year +7  (source: GDMC)
  3. "Modelling 3D legal spaces of Public Law Restrictions within the context of LADM revision" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:a116493a-2cb6-4781-b2c4-3f2c94611ad8)
     - authors: Dimitrios Kitsakis, Eftychia Kalogianni (student), Efi Dimopoulou, Jaap Zevenbergen, Peter van Oosterom (supervisor: van Oosterom), Kitsakis, Dimitrios, Kalogianni, Eftychia (student), Dimopoulou, Efi, Zevenbergen, Jaap, van Oosterom, Peter
     - title similarity 0.43; abstract similarity 0.33; year +5  (source: GDMC)
  4. "Modelling 3D underground legal spaces in 3D Land Administration Systems" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:4a499efb-f348-456b-9965-65c47519337a)
     - authors: Rohit Ramlakhan, Eftychia Kalogianni (student), Peter van Oosterom (supervisor: van Oosterom), Ramlakhan, Rohit, Kalogianni, Eftychia (student), van Oosterom , Peter
     - title similarity 0.43; abstract similarity 0.33; year +5  (source: GDMC)
  5. "The Foundation of Edition II of the Land Administration Domain Model" — Proceedings of the FIG Working Week 2021, Online, pp. 17, 2021 — [conference paper](https://fig.net/resources/proceedings/fig_proceedings/fig2021/papers/ws_03.4/WS_03.4_abdullah_indrajit_et_al_11163.pdf)
     - authors: Christiaan Lemmen, Alattas Abdullah, Agung Indrajit, Kalogianni Eftychia (student), Abdullah Kara, Peter van Oosterom (supervisor: van Oosterom), Peter Oukes, Abdullah Alattas, Eftychia Kalogianni (student)
     - title similarity 0.51; abstract similarity 0.25; year +5  (source: GDMC)
  6. "BIM Models as input for 3D Land Administration Systems for Apartment Registration" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:5e240a06-5fdf-4354-9e6d-09c675f1cd8b)
     - authors: Marjan Broekhuizen, Eftychia Kalogianni (student), Peter van Oosterom (supervisor: van Oosterom), Broekhuizen, Marjan, Kalogianni, Eftychia (student), van Oosterom, Peter
     - title similarity 0.40; abstract similarity 0.33; year +5  (source: GDMC)
  7. "Refining the survey model of the LADM ISO 19152–2: Land registration" — Land Use Policy, Elsevier BV, 141, pp. 107125, 2024 — [journal article](https://www.sciencedirect.com/science/article/pii/S0264837724000772)
     - authors: Eftychia Kalogianni (student), Efi Dimopoulou, Hans-Christoph Gruler, Erik Stubkjær, Javier Morales, Christiaan Lemmen, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.37; abstract similarity 0.40; year +8  (source: GDMC)
  8. "Bridging Sustainable Development Goals and Land Administration: The Role of the ISO 19152 Land Administration Domain Model in SDG Indicator Formalization" — Land, MDPI AG, 13(491), pp. 27, 2024 — [journal article](https://doi.org/10.3390/land13040491)
     - authors: Mengying Chen, Peter Van Oosterom (supervisor: van Oosterom), Eftychia Kalogianni (student), Paula Dijkstra, Christiaan Lemmen
     - title similarity 0.48; abstract similarity 0.17; year +8  (source: GDMC)
  9. "Land administration domain model and 3D land administration" — Survey Review, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2561263)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Abdullah Kara, Eftychia Kalogianni (student)
     - title similarity 0.41; abstract similarity 0.22; year +9  (source: OpenAlex)
  10. "The land administration domain model: advancement and implementation" — Proceedings of the Annual World Bank Conference on Land and Poverty, W, 2020 — [conference paper](https://www.gdmc.nl/publications/2020/03-08-Lemmen-697_paper.pdf)
     - authors: Chrit Lemmen, Peter van Oosterom (supervisor: van Oosterom), Eva-Maria Unger, Eftychia Kalogianni (student), Anna Shnaidman, Abdullah Kara, Abdullah Alattas, Agung Indrajit, Katherine Smyth, Aurélie Milledrogues, Rohan Bennett, Peter Oukes, Hans-Christoph Gruler, Daniel Casalprim, Golgi Alvarez, Trias Aditya, Ketut Gede Ary Sucaya, Javier Morales, Marisa Balas, Nur Amalina Zulkifli, Cornelis De Zeeuw, Lemmen, Christiaan, Van Oosterom, Peter, Unger, Eva-Maria, Kalogianni, Eftychia (student), Shnaidman, Anna, Kara, Abdullah, Indrajit, Agung, Smyth, Katherine, Milledrogues, Aurélie, Bennett, Rohan, Gruler, Hans-Christoph, Casalprim, Daniel, Alvarez, Golgi, Aditya, Trias, Sucaya, Ketut Gede Ary, Morales, Javier, Balas, Marisa, Zulkifli, Nur Amalina, De Zeeuw, Cornelis
     - title similarity 0.42; abstract similarity 0.12; year +4  (source: GDMC)
  … and 15 more likely candidates; re-run with --limit/--surname to see them all.
- **Martijn Koopman (2016)** — 3D Path-finding in a voxelized model of an indoor environment
  1. "Universal path planning for an indoor drone" — Automation in Construction, 2018 — [journal article](https://doi.org/10.1016/j.autcon.2018.07.025)
     - authors: Fangyu Li, Sisi Zlatanova (supervisor: Zlatanova), Martijn Koopman (student), Xueying Bai, Abdoulaye Diakité
     - title similarity 0.48; abstract similarity n/a; year +2  (source: Crossref)
- **Olivier Rodenberg (2016)** — The effect of A* pathfinding characteristics on the path length and performance 
  1. "Indoor A* Pathfinding through an Octree Representation of a Point Cloud" — Chapter in: ISPRS Annals Volume IV-2/W1, 11th 3D Geoinfo Conference (E, 2016 — [conference paper](https://doi.org/10.5194/isprs-annals-iv-2-w1-249-2016)
     - authors: O. Rodenberg (student), E. Verbree (supervisor: Verbree), S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.60; abstract similarity 0.65; year +0  (source: GDMC)
  2. "Using a linear octree to identify empty space in indoor point clouds for 3D pathfinding" — Proceedings of the 19th AGILE International Conference on Geographic I, 2016 — [conference paper](https://www.gdmc.nl/publications/2016/Linear_octree_identify_empty_space_indoor_point_clouds.pdf)
     - authors: Tom Broersen, Florian W. Fichtner, Erik J. Heeres, Ivo de Liefde, Olivier B.P.M. Rodenberg (student), Edward Verbree (supervisor: Verbree), Robert Vo&ucirc;te
     - title similarity 0.36; abstract similarity n/a; year +0  (source: GDMC)
- **Adrie Rovers (2016)** — Exploring the use of a generic spatial access method for caching and efficient r
  1. "Using a generic spatial access method for caching and efficient retrieval of vario-scale data in a server-client architecture" — Proceedings of the 20th AGILE Conference on Geographic Information Sci, 2017 — [conference paper](https://www.gdmc.nl/publications/2017/SpatialAccessMethodVarioScaleServer.pdf)
     - authors: Adrie Rovers (student), Martijn Meijers (supervisor: Meijers), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.88; abstract similarity n/a; year +1  (source: GDMC)
- **Yuxuan Kang (2017)** — Straightening and simplifying a multi-view stereo mesh of a city
  1. "A2B: Identifying movement patterns from largescale Wi-Fi based location data" — Proceedings of the 13th International Conference on Location Based Ser, 2016 — [conference paper](https://www.gdmc.nl/publications/2016/A2B_Identifying_movement_patterns_largescale_Wi-Fi.pdf)
     - authors: S.C. van der Spek, E. Verbree, M. Bon, X.A. den Duijn, B. Dukai, S.J. Griffioen, Y. Kang (student), M. Vermeer
     - title similarity 0.39; abstract similarity n/a; year -1  (source: GDMC)
- **Stella Psomadaki (2017)** — Using a Space Filling Curve for the Management of Dynamic Point Cloud Data in a 
  1. "Using a Space Filling Curve Approach for the Management of Dynamic Point Clouds" — Chapter in: ISPRS Annals Volume IV-2/W1, 11th 3D Geoinfo Conference (E, 2016 — [conference paper](https://doi.org/10.5194/isprs-annals-iv-2-w1-107-2016)
     - authors: Stella Psomadaki (student), Peter van Oosterom (supervisor: van Oosterom), Theo Tijssen (supervisor: Tijssen), Fedor Baart
     - title similarity 0.81; abstract similarity 0.68; year -1  (source: GDMC)
  2. "Utilizing a Discrete Global Grid System for Handling Point Clouds with Varying Locations, Times, and Levels of Detail" — Cartographica, University of Toronto Press, 51(1), pp. 4-15, 2019 — [journal article](https://doi.org/10.3138/cart.54.1.2018-0009)
     - authors: Neeraj Sirdeshmukh, Edward Verbree, Peter van Oosterom (supervisor: van Oosterom), Stella Psomadaki (student), Martin Kodde
     - title similarity 0.40; abstract similarity 0.47; year +2  (source: GDMC)
  3. "Towards a relational database Space Filling Curve (SFC) interface specification for managing nD-PointClouds" — Geoinformationssysteme 2019, Beiträge zur 6. Münchner GI-Runde (Thomas, 2019 — [conference paper](https://www.gdmc.nl/publications/2019/DBMS-nD-PC-GI-Runde2019.pdf)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Martijn Meijers, Edward Verbree, Haicheng Liu, Theo Tijssen (supervisor: Tijssen)
     - title similarity 0.49; abstract similarity n/a; year +2  (source: GDMC)
  4. "Mathematical morphology directly applied to point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 168, , 2020 — [journal article](https://doi.org/10.1016/j.isprsjprs.2020.08.011)
     - authors: Jes&uacute;s Balado, Peter van Oosterom (supervisor: van Oosterom), Luc&iacute;a D&iacute;az-Vilari&ntilde;o, Martijn Meijers, Lucía Díaz-Vilariño
     - title similarity 0.39; abstract similarity 0.46; year +3  (source: GDMC)
- **Pieter Soffers (2017)** — Designing an integrated future data model for survey data and cadastral mapping
  1. "The new, LADM inspired, data model of the Dutch cadastral map" — Land Use Policy, 2022 — [journal article](https://doi.org/10.1016/j.landusepol.2022.106074)
     - authors: Eric Hagemans, Eva-Maria Unger, Pieter Soffers (student), Tom Wortel, Christiaan Lemmen
     - title similarity 0.53; abstract similarity n/a; year +5  (source: Crossref)
  2. "Model driven architecture engineered land administration in conformance with international standards - illustrated with the Hellenic Cadastre" — Open Geospatial Data, Software and Standards, 1(3), 2016 — [journal article](https://doi.org/10.1186/s40965-016-0002-3)
     - authors: Styliani Psomadaki, Efi Dimopoulou, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.32; abstract similarity 0.46; year -1  (source: GDMC)
- **Bart Staats (2017)** — Identification of walkable space in a voxel model, derived from a point cloud an
  1. "AUTOMATIC GENERATION OF INDOOR NAVIGABLE SPACE USING A POINT CLOUD AND ITS SCANNER TRAJECTORY" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2017 — [journal article](https://doi.org/10.5194/isprs-annals-iv-2-w4-393-2017)
     - authors: B. R. Staats (student), A. A. Diakité, R. L. Voûte, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.59; abstract similarity 0.61; year +0  (source: Crossref)
  2. "Detection of doors in a voxel model, derived from a point cloud and its scanner trajectory, to improve the segmentation of the walkable space" — International Journal of Urban Sciences, 2018 — [journal article](https://doi.org/10.1080/12265934.2018.1553685)
     - authors: B. R. Staats (student), A. A. Diakité, R. L. Voûte, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.61; abstract similarity n/a; year +1  (source: Crossref)
  3. "AUTOMATIC EXTRACTION OF A NAVIGATION GRAPH INTENDED FOR INDOORGML FROM AN INDOOR POINT CLOUD" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2019 — [journal article](https://doi.org/10.5194/isprs-annals-iv-2-w5-271-2019)
     - authors: P. Flikweert, R. Peters, L. Díaz-Vilariño, R. Voûte, B. Staats (student)
     - title similarity 0.43; abstract similarity 0.51; year +2  (source: Crossref)
- **Oscar Willems (2017)** — Exploring a pure landmark-based approach for indoor localisation
  1. "Building Rhythms: Reopening the Workspace with Indoor Localisation" — Chapter in: LBS 2021: Proceedings of the 16th International Conference, 2021 — [conference paper](https://doi.org/10.34726/1741)
     - authors: Guilherme Spinoza Andreo, Ioannis Dardavesis, Michiel de Jong, Pratyush Kumar, Maundri Prihanggo, Georgios Triantafyllou, Niels van der Vaart, Edward Verbree (supervisor: Verbree), Zhenyu Liu, Runnan Fu, Linjun Wang, Yuzhen Jin, Theodoros Papakostas, Xenia Una Mainelli, Robert Voûte
     - title similarity 0.56; abstract similarity n/a; year +4  (source: GDMC)
- **Barbara Cemellini (2018)** — Web-based visualization of 3D cadastre
  1. "Usability testing of a web-based 3D Cadastral visualization system" — Proceedings of the 6th International Workshop on 3D Cadastres (Peter v, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/3DCadWorkshop2018_29.pdf)
     - authors: Barbara Cemellini (student), Rod Thompson (supervisor: Thompson), Peter van Oosterom (supervisor: van Oosterom), Marian de Vries (supervisor: de Vries)
     - title similarity 0.53; abstract similarity n/a; year +0  (source: GDMC)
  2. "Results of the Public Usability Testing of a Web-Based 3D Cadastral Visualization System" — Proceedings of the FIG Working Week 2019, Hanoi, Vietnam, pp. 15, 2019 — [conference paper](http://www.fig.net/resources/proceedings/fig_proceedings/fig2019/papers/ts06c/TS06C_van_oosterom_de_vries_et_al_10082.pdf)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Marian de Vries (supervisor: de Vries), Barbara Cemellini (student), Rod Thompson (supervisor: Thompson)
     - title similarity 0.44; abstract similarity n/a; year +1  (source: GDMC)
  3. "Developing an LADM Compliant Dissemination and Visualization System for 3D Spatial Units" — Proceedings of the 7th Land Administration Domain Model Workshop, Zagr, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/07-26_LADM_2018.pdf)
     - authors: Rod Thompson (supervisor: Thompson), Peter van Oosterom (supervisor: van Oosterom), Barbara Cemellini (student), Marian de Vries (supervisor: de Vries)
     - title similarity 0.44; abstract similarity n/a; year +0  (source: GDMC)
  4. "Design, development and usability testing of an LADM compliant 3D Cadastral prototype system" — Land Use Policy, Elsevier, 98(104418), pp. 1-24, 2020 — [journal article](https://doi.org/10.1016/j.landusepol.2019.104418)
     - authors: Barbara Cemellini (student), Peter van Oosterom (supervisor: van Oosterom), Rod Thompson (supervisor: Thompson), Marian de Vries (supervisor: de Vries)
     - title similarity 0.36; abstract similarity n/a; year +2  (source: GDMC)
  5. "Visualization/dissemination of 3D Cadastre" — Proceedings of the FIG Congress 2018, Istanbul, pp. 30, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/TS05C_cemellini_rod_et_al_9591.pdf)
     - authors: Barbara Cemellini (student), Thompson Rod, Marian de Vries (supervisor: de Vries), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.70; abstract similarity n/a; year +0  (source: GDMC)
  6. "Developing an LADM Compliant Dissemination and Visualization System for 3D Spatial Units" — Research Repository (Delft University of Technology), 2020 — [conference paper](https://doi.org/10.4233/uuid:57b1dfb4-74c8-4393-b997-5ae6484ae913)
     - authors: Thompson, Rod, van Oosterom, Peter, Cemellini, Barbara (student), de Vries, Marian
     - title similarity 0.44; abstract similarity 0.31; year +2  (source: OpenAlex)
  7. "Chapter 2. Initial Registration of 3D Parcels" — DiVA (University of Gävle), 2018 — [book-chapter](https://openalex.org/W2982243049)
     - authors: Efi Dimopooulou, S. Karki, Miodrag Roić, José-Paulo Duarte de Almeida, Charisse Griffith-Charles, R. J. Thompson (supervisor: Thompson), Ying Shen, Jesper M. Paasch, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.45; abstract similarity 0.12; year +0  (source: OpenAlex)
  8. "FIG publication Best Practices 3D Cadastres" — ?, 2018 — [journal article](https://openalex.org/W2890372006)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Diego Alfonso Erba, Ali Aien, Don Grant, Mohsen Kalantari, S. Karki, Davood Shojaei, R. J. Thompson (supervisor: Thompson), Gerhard Muggenhuber, Gerhard Navratil, Neeraj Dixit, Ammar Rashid Kashram, Andréa Flávia Tenório Carneiro, Francois Brochu, Louis-André Desbiens, Paul Egesborg, Marc Gervais, J. Pouliot, Francis Roy, Renzhong Guo, Ning Zhang, Shen Ying, Andres Hernández Bolaños Croatia Miodrag Roic, Elikkos Elia, Karel Janečka, Lars Bodum, Esben Munk Sørensen, Christian Thellufsen, Jani Hokkanen, Arvo Kokkonen, Tarja Myllymäki, Claire Galpin, Hervé Halbout, Markus Seifert, Efi Dimopoulou, Gyula Iván, Andras Osskó, Tarun Ghawana, Pradeep Khandelwal, Trias Aditya, S. Subaryono, Yerach Doytsher, Joseph Forrai, Gili Kirschner, Yoav Tal, Diego Navarra, Bruno Razza, Enrico Rispoli, Fausto Savoldi, Natalya Khairudinova, David Siriba, Gjorgji Gjorgjiev, Teng Chee Hua, Alias Abdul Rahman, Babu Ram Acharya, Benedict van Dam, C. Lemmen, H.D. Ploeger, Martijn Rijsdijk, Jantien Stoter, Thomas Dabiri, Lars Elsrud, Olav Jenssen, Lars Lobben, Tor Valstad, Jarosław Bydłosz, Marcin Karabin, José Paulo Elvas Duarte de Almeida, João Paulo Fonseca Hespanha de Oliveira, Mateus Magarotto, Sergey Sapelnikov, Natalia Vandysheva, Rajica Mihajlovic, Nenad Višnjevac, Victor Khoo, Kean Huat Soon, Young-Ho Lee, Amalia Velasco, Peter Ekbäck, Jesper M. Paasch, Jenny Paulsson, Helena Aström Boss, Robert Balanche, Laurent Niggeler, Charisse Griffith-Charles, Cemal Bıyık, Osman Demir, Fatih Döner, Gareth Robson, Carsten Rönsdorf, Bod Ader, David Cowen, Carl Reed, Alex Smith
     - title similarity 0.51; abstract similarity n/a; year +0  (source: OpenAlex)
- **Antria Christodoulou (2018)** — An image-based method for the pairwise registration of mobile laser scanning poi
  1. "Image-based Method for the Pairwise Registration of Mobile Laser Scanning Point Clouds" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLII-4/93/2018/)
     - authors: Antria Christodoulou (student), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 1.00; abstract similarity 0.79; year +0  (source: GDMC)
- **Xander den Duijn (2018)** — A 3D data modeling approach for integrated management of below and above ground 
  1. "MODELLING BELOW- AND ABOVE-GROUND UTILITY NETWORK FEATURES WITH THE CITYGML UTILITY NETWORK ADE: EXPERIENCES FROM ROTTERDAM" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2018 — [journal article](https://doi.org/10.5194/isprs-annals-iv-4-w7-43-2018)
     - authors: X. den Duijn (student), G. Agugiaro, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.51; abstract similarity 0.76; year +0  (source: Crossref)
  2. "3D Approach for Representing Uncertainties of Underground Utility Data" — Computing in Civil Engineering 2017, 2017 — [conference paper](https://doi.org/10.1061/9780784480823.044)
     - authors: L. L. olde Scholtenhuis, S. Zlatanova (supervisor: Zlatanova), X. den Duijn (student)
     - title similarity 0.49; abstract similarity n/a; year -1  (source: Crossref)
- **Balázs Dukai (2018)** — Exploring the automatic Level of Detail inference for the validation of building
  1. "3dfier: automatic reconstruction of 3D city models" — Journal of Open Source Software, 2021 — [journal article](https://doi.org/10.21105/joss.02866)
     - authors: Hugo Ledoux, Filip Biljecki (supervisor: Biljecki), Balázs Dukai (student), Kavisha Kumar, Ravi Peters, Jantien Stoter, Tom Commandeur
     - title similarity 0.52; abstract similarity n/a; year +3  (source: Crossref)
  2. "QUALITY ASSESSMENT OF A NATIONWIDE DATA SET CONTAINING AUTOMATICALLY RECONSTRUCTED 3D BUILDING MODELS" — The International Archives of the Photogrammetry, Remote Sensing and S, 2021 — [journal article](https://doi.org/10.5194/isprs-archives-xlvi-4-w4-2021-17-2021)
     - authors: B. Dukai (student), R. Peters, S. Vitalis, J. van Liempt, J. Stoter
     - title similarity 0.40; abstract similarity 0.31; year +3  (source: Crossref)
  3. "Automated 3D Reconstruction of LoD2 and LoD1 Models for All 10 Million Buildings of the Netherlands" — Photogrammetric Engineering &amp; Remote Sensing, 2022 — [journal article](https://doi.org/10.14358/pers.21-00032r2)
     - authors: Ravi Peters, Balázs Dukai (student), Stelios Vitalis, Jordi van Liempt, Jantien Stoter
     - title similarity 0.37; abstract similarity 0.26; year +4  (source: Crossref)
- **IJsbrand Groeneveld (2018)** — Generalisation of Hydrography Networks for a Vario-scale Basemap
  1. "Evaluation of the dual half-edge data structure for implementation of a vario-scale model" — Chapter in: The International Archives of the Photogrammetry, Remote S, 2024 — [conference paper](https://isprs-archives.copernicus.org/articles/XLVIII-4-W11-2024/25/2024/)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (supervisor: Meijers), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.46; abstract similarity 0.23; year +6  (source: GDMC)
  2. "Towards a scale dependent framework for creating vario-scale maps" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-4-425-2018)
     - authors: Martijn Meijers (supervisor: Meijers), Peter van Oosterom (supervisor: van Oosterom), Radan &Scaron;uba, Dongliang Peng
     - title similarity 0.48; abstract similarity n/a; year +0  (source: GDMC)
- **Tom Hemmes (2018)** — Classification of large scale outdoor point clouds using convolutional neural ne
  1. "Classification of Mobile Laser Scanning Point Clouds of Urban Scenes Exploiting Cylindrical Neighbourhoods" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-2-1225-2018)
     - authors: Mingxue Zheng, Mathias Lemmens (supervisor: Lemmens), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.58; abstract similarity n/a; year +0  (source: GDMC)
  2. "Classification of Mobile Laser Scanning Point Clouds from Height Features" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2017 — [conference paper](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLII-2-W7/321/2017/)
     - authors: Mingxue Zheng, Mathias Lemmens (supervisor: Lemmens), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.59; abstract similarity n/a; year -1  (source: GDMC)
- **Lydia Kotoula (2018)** — The Smart Point Cloud framework to detect pipelines using raw point cloud genera
  1. "Utilizing a Discrete Global Grid System for Handling Point Clouds with Varying Locations, Times, and Levels of Detail" — Cartographica, University of Toronto Press, 51(1), pp. 4-15, 2019 — [journal article](https://doi.org/10.3138/cart.54.1.2018-0009)
     - authors: Neeraj Sirdeshmukh, Edward Verbree (supervisor: Verbree), Peter van Oosterom, Stella Psomadaki, Martin Kodde
     - title similarity 0.24; abstract similarity 0.46; year +1  (source: GDMC)
- **Weiran Li (2018)** — Detection of subsurface meltwater in East Antarctica using SAR Interferometry
  1. "The potential of InSAR for assessing meltwater lake dynamics on Antarctic ice shelves" — ?, 2021 — [posted-content](https://doi.org/10.5194/tc-2021-169)
     - authors: Weiran Li (student), Stef Lhermitte (supervisor: Lhermitte), Paco López-Dekker
     - title similarity 0.48; abstract similarity 0.29; year +3  (source: Crossref)
  2. "The potential of synthetic aperture radar interferometry for assessing meltwater lake dynamics on Antarctic ice shelves" — The Cryosphere, 2021 — [journal article](https://doi.org/10.5194/tc-15-5309-2021)
     - authors: Weiran Li (student), Stef Lhermitte (supervisor: Lhermitte), Paco López-Dekker
     - title similarity 0.36; abstract similarity 0.27; year +3  (source: Crossref)
  3. "Ship detection in a large scene SAR image using image uniformity description factor" — 2017 SAR in Big Data Era: Models, Methods and Applications (BIGSARDATA, 2017 — [conference paper](https://doi.org/10.1109/bigsardata.2017.8124933)
     - authors: Weike Li (student), Bin Zou, Lamei Zhang
     - title similarity 0.40; abstract similarity n/a; year -1  (source: Crossref)
- **Neeraj Sirdeshmukh (2018)** — Utilizing a Discrete Global Grid System For Handling Point Clouds With Varying L
  1. "Utilizing a Discrete Global Grid System for Handling Point Clouds with Varying Locations, Times, and Levels of Detail" — Cartographica, University of Toronto Press, 51(1), pp. 4-15, 2019 — [journal article](https://doi.org/10.3138/cart.54.1.2018-0009)
     - authors: Neeraj Sirdeshmukh (student), Edward Verbree (supervisor: Verbree), Peter van Oosterom (supervisor: van Oosterom), Stella Psomadaki, Martin Kodde
     - title similarity 1.00; abstract similarity 0.77; year +1  (source: GDMC)
  2. "Organizing and visualizing point clouds with continuous levels of detail" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 194, , 2022 — [journal article](https://doi.org/10.1016/j.isprsjprs.2022.10.004)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Haicheng Liu, Rod Thompson, Martijn Meijers, Edward Verbree (supervisor: Verbree)
     - title similarity 0.60; abstract similarity 0.39; year +4  (source: GDMC)
- **Martijn Vermeer (2018)** — Large-scale efficient extraction of 3D roof segments from aerial stereo imagery
  1. "A quick-scan method to assess photovoltaic rooftop potential based on aerial imagery and LiDAR" — Solar Energy, 2020 — [journal article](https://doi.org/10.1016/j.solener.2020.07.035)
     - authors: Tim N.C. de Vries, Joris Bronkhorst, Martijn Vermeer (student), Jaap C.B. Donker, Sven A. Briels, Hesan Ziar, Miro Zeman, Olindo Isabella
     - title similarity 0.39; abstract similarity n/a; year +2  (source: Crossref)
  2. "Terrain-Informed Self-Supervised Learning: Enhancing Building Footprint Extraction From LiDAR Data With Limited Annotations" — IEEE Transactions on Geoscience and Remote Sensing, 2024 — [journal article](https://doi.org/10.1109/tgrs.2024.3391391)
     - authors: Anuja Vats, David Völgyes, Martijn Vermeer (student), Marius Pedersen, Kiran Raja, Daniele S. M. Fantin, Jacob Alexander Hay
     - title similarity 0.36; abstract similarity n/a; year +6  (source: Crossref)
- **Anastasia Anastasiadou (2019)** — A probabilistic analysis of results of co-registration of aerial and mobile lase
  1. "Image-based Method for the Pairwise Registration of Mobile Laser Scanning Point Clouds" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLII-4/93/2018/)
     - authors: Antria Christodoulou, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.60; abstract similarity n/a; year -1  (source: GDMC)
- **Niek Bebelaar (2019)** — Correction Model for Particulate Matter Measurements with a Low-Cost Sensor Netw
  1. "Monitoring urban environmental phenomena through a wireless distributed sensor network" — Smart and Sustainable Built Environment, Emerald, 7(1), pp. 68-79, 2018 — [journal article](https://doi.org/10.1108/sasbe-10-2017-0046)
     - authors: Niek Bebelaar (student), Robin Christian Braggaar, Catharina Marianne Kleijwegt, Roeland Willem Erik Meulmeester, Gina Michailidou, Nebras Salheb, Stefan van der Spek, Noortje Vaissier, Edward Verbree
     - title similarity 0.36; abstract similarity 0.48; year -1  (source: GDMC)
- **Fanny Bot (2019)** — A graph-matching approach to indoor localization: Using a mobile device and a re
  1. "A graph-matching approach to indoor localization using a mobile device and a reference BIM" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2019 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-2-w13-761-2019)
     - authors: Fanny Bot (student), Pirouz Nourian (supervisor: Nourian), Edward Verbree (supervisor: Verbree)
     - title similarity 1.00; abstract similarity 0.82; year +0  (source: GDMC)
- **Francisco Gabriel Garcia Gonzalez (2019)** — An interactive design tool for urban planning using the size of the living space
  1. "AN INTERACTIVE DESIGN TOOL FOR URBAN PLANNING USING THE SIZE OF THE LIVING SPACE AS UNIT OF MEASUREMENT" — The International Archives of the Photogrammetry, Remote Sensing and S, 2019 — [journal article](https://doi.org/10.5194/isprs-archives-xlii-4-w15-3-2019)
     - authors: F. G. García González (student), G. Agugiaro (supervisor: Agugiaro), R. Cavallo
     - title similarity 1.00; abstract similarity 0.87; year +0  (source: Crossref)
- **Meylin Herrera Herrera (2019)** — Landslide Detection using Random Forest Classifier
  1. "Multi-Regional landslide detection using combined unsupervised and supervised machine learning" — Geomatics, Natural Hazards and Risk, 2021 — [journal article](https://doi.org/10.1080/19475705.2021.1912196)
     - authors: Faraz S. Tehrani, Giorgio Santinelli, Meylin Herrera Herrera (student)
     - title similarity 0.47; abstract similarity n/a; year +2  (source: Crossref)
- **Cathelijne Kleijwegt (2019)** — Establishing an object identification method based on the description of the nei
  1. "Monitoring urban environmental phenomena through a wireless distributed sensor network" — Smart and Sustainable Built Environment, Emerald, 7(1), pp. 68-79, 2018 — [journal article](https://doi.org/10.1108/sasbe-10-2017-0046)
     - authors: Niek Bebelaar, Robin Christian Braggaar, Catharina Marianne Kleijwegt (student), Roeland Willem Erik Meulmeester, Gina Michailidou, Nebras Salheb, Stefan van der Spek, Noortje Vaissier, Edward Verbree
     - title similarity 0.36; abstract similarity n/a; year -1  (source: GDMC)
- **Roeland Willem Erik Meulmeester (2019)** — BIM Legal: Proposal for defining legal spaces for apartment rights in the Dutch 
  1. "BIM Models as input for 3D Land Administration Systems for Apartment Registration" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:5e240a06-5fdf-4354-9e6d-09c675f1cd8b)
     - authors: Marjan Broekhuizen, Eftychia Kalogianni, Peter van Oosterom (supervisor: van Oosterom), Broekhuizen, Marjan, Kalogianni, Eftychia, van Oosterom, Peter
     - title similarity 0.44; abstract similarity 0.56; year +2  (source: GDMC)
  2. "Mapping private, common, and exclusive common spaces in buildings from BIM/IFC to LADM. A case study from Saudi Arabia" — Land Use Policy, Elsevier, 104(105355), pp. 1-25, 2021 — [journal article](https://doi.org/10.1016/j.landusepol.2021.105355)
     - authors: Abdullah Alattas, Eftychia Kalogianni, Thamer Alzahrani, Sisi Zlatanova, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.31; abstract similarity 0.51; year +2  (source: GDMC)
- **Pablo Ruben (2019)** — 3D City Models in the Context of Urban Mining
  1. "3D CITY MODELS FOR URBAN MINING: POINT CLOUD BASED SEMANTIC ENRICHMENT FOR SPECTRAL VARIATION IDENTIFICATION IN HYPERSPECTRAL IMAGERY" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2020 — [journal article](https://doi.org/10.5194/isprs-annals-v-4-2020-223-2020)
     - authors: P. A. Ruben (student), R. Sileryte (supervisor: Šileryte), G. Agugiaro (supervisor: Agugiaro)
     - title similarity 0.32; abstract similarity 0.54; year +1  (source: Crossref)
- **Melika Sajadian (2019)** — Spatial and Temporal Analysis of Road Deformation based on Remote Sensing and Su
  1. "Predicting land deformation by integrating InSAR data and cone penetration testing through machine learning techniques" — Proceedings of the International Association of Hydrological Sciences,, 2020 — [journal article](https://doi.org/10.5194/piahs-382-525-2020)
     - authors: Melika Sajadian (student), Ana Teixeira, Faraz S. Tehrani, Mathias Lemmens (supervisor: Lemmens)
     - title similarity 0.39; abstract similarity n/a; year +1  (source: GDMC)
- **Jippe van der Maaden (2019)** — Vario-scale visualization of the AHN2 point cloud
  1. "Organizing and visualizing point clouds with continuous levels of detail" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 194, , 2022 — [journal article](https://doi.org/10.1016/j.isprsjprs.2022.10.004)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Haicheng Liu, Rod Thompson, Martijn Meijers (supervisor: Meijers), Edward Verbree
     - title similarity 0.44; abstract similarity 0.52; year +3  (source: GDMC)
  2. "Mathematical morphology directly applied to point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 168, , 2020 — [journal article](https://doi.org/10.1016/j.isprsjprs.2020.08.011)
     - authors: Jes&uacute;s Balado, Peter van Oosterom (supervisor: van Oosterom), Luc&iacute;a D&iacute;az-Vilari&ntilde;o, Martijn Meijers (supervisor: Meijers), Lucía Díaz-Vilariño
     - title similarity 0.44; abstract similarity 0.47; year +1  (source: GDMC)
  3. "Visualization of Point Cloud Models in Mobile Augmented Reality using continuous Level of Detail Method" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2020 — [conference paper](https://doi.org/10.5194/isprs-archives-xliv-4-w1-2020-167-2020)
     - authors: Liyao Zhang, Peter van Oosterom (supervisor: van Oosterom), Haicheng Liu
     - title similarity 0.38; abstract similarity 0.49; year +1  (source: GDMC)
  4. "Utilizing a Discrete Global Grid System for Handling Point Clouds with Varying Locations, Times, and Levels of Detail" — Cartographica, University of Toronto Press, 51(1), pp. 4-15, 2019 — [journal article](https://doi.org/10.3138/cart.54.1.2018-0009)
     - authors: Neeraj Sirdeshmukh, Edward Verbree, Peter van Oosterom (supervisor: van Oosterom), Stella Psomadaki, Martin Kodde
     - title similarity 0.29; abstract similarity 0.50; year +0  (source: GDMC)
- **Qu Wang (2019)** — 3D breakline extraction from point clouds with the medial axis transform
  1. "Semantic segmentation of point clouds with the 3D medial axis transform" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-33-2025)
     - authors: Giulia Ceccarelli, Weixiao Gao, Ravi Peters (supervisor: Peters)
     - title similarity 0.78; abstract similarity 0.16; year +6  (source: Crossref)
  2. "Building outline extraction from ALS point clouds using medial axis transform descriptors" — Pattern Recognition, 2020 — [journal article](https://doi.org/10.1016/j.patcog.2020.107447)
     - authors: Elyta Widyaningrum, Ravi Y. Peters (supervisor: Peters), Roderik C. Lindenbergh
     - title similarity 0.71; abstract similarity n/a; year +1  (source: Crossref)
- **Teng Wu (2019)** — Visibility analysis in a point cloud based on the medial axis transform
  1. "Semantic segmentation of point clouds with the 3D medial axis transform" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-33-2025)
     - authors: Giulia Ceccarelli, Weixiao Gao, Ravi Peters (supervisor: Peters)
     - title similarity 0.64; abstract similarity 0.34; year +6  (source: Crossref)
  2. "Building outline extraction from ALS point clouds using medial axis transform descriptors" — Pattern Recognition, 2020 — [journal article](https://doi.org/10.1016/j.patcog.2020.107447)
     - authors: Elyta Widyaningrum, Ravi Y. Peters (supervisor: Peters), Roderik C. Lindenbergh
     - title similarity 0.59; abstract similarity n/a; year +1  (source: Crossref)
- **Dimitris Xenakis (2019)** — Placement optimization of Positioning Nodes: Maximizing the distinction of Indoo
  1. "Placement optimization of positioning nodes: Maximizing the distinction of indoor zones" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2019 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-2-w13-909-2019)
     - authors: Dimitris Xenakis (student), Martijn Meijers (supervisor: Meijers), Edward Verbree (supervisor: Verbree)
     - title similarity 1.00; abstract similarity 0.84; year +0  (source: GDMC)
- **Giulia Ceccarelli (2020)** — Semantic segmentation of point clouds with the 3D medial axis transform
  1. "Semantic segmentation of point clouds with the 3D medial axis transform" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-33-2025)
     - authors: Giulia Ceccarelli (student), Weixiao Gao (supervisor: Gao), Ravi Peters (supervisor: Peters)
     - title similarity 1.00; abstract similarity 0.51; year +5  (source: Crossref)
  2. "Building outline extraction from ALS point clouds using medial axis transform descriptors" — Pattern Recognition, 2020 — [journal article](https://doi.org/10.1016/j.patcog.2020.107447)
     - authors: Elyta Widyaningrum, Ravi Y. Peters (supervisor: Peters), Roderik C. Lindenbergh
     - title similarity 0.56; abstract similarity n/a; year +0  (source: Crossref)
- **Chirag Garg (2020)** — Indoor 3D reconstruction from a single image
  1. "Crop Yield Prediction of Indian Districts Using Deep Learning" — 2021 Sixth International Conference on Image Information Processing (I, 2021 — [conference paper](https://doi.org/10.1109/iciip53038.2021.9702573)
     - authors: Parjanya Prashant, Kaustubh Ponkshe, Chirag Garg (student), Ishan Pendse, Prathamesh Muley
     - title similarity 0.42; abstract similarity n/a; year +1  (source: Crossref)
  2. "3D Construction and Realignment of Object for Interaction in Metaverse Space" — 2025 International Conference on Modeling, Simulation &amp;amp; Intell, 2025 — [conference paper](https://doi.org/10.1109/mosicom67153.2025.11398327)
     - authors: Chirag Garg (student), Manali Arora
     - title similarity 0.44; abstract similarity n/a; year +5  (source: Crossref)
  3. "3D Reconstruction and Understanding of Indoor Scene Based on Single Image" — 2020 International Conference on Virtual Reality and Visualization (IC, 2020 — [conference paper](https://doi.org/10.1109/icvrv51359.2020.00072)
     - authors: Junxiao Xue, Yuchun Tu, Dai Sun
     - title similarity 0.67; abstract similarity n/a; year +0  (source: Crossref)
  4. "3D Reconstruction of Single Indoor Image Based on Relational Network" — 2024 IEEE 4th International Conference on Power, Electronics and Compu, 2024 — [conference paper](https://doi.org/10.1109/icpeca60615.2024.10471020)
     - authors: Jingjing Shang, Yi Zheng, Minghan Yang
     - title similarity 0.67; abstract similarity n/a; year +4  (source: Crossref)
- **Jinglan Li (2020)** — Manage 4D historical AIS data by space filling curve
  1. "PointSCNet: Point Cloud Structure and Correlation Learning Based on Space-Filling Curve-Guided Sampling" — Symmetry, 2021 — [journal article](https://doi.org/10.3390/sym14010008)
     - authors: Xingye Chen, Yiqi Wu, Wenjie Xu, Jin Li (student), Huaiyi Dong
     - title similarity 0.41; abstract similarity 0.13; year +1  (source: Crossref)
- **Konstantinos Mastorakis (2020)** — An integrative workflow for 3D city model versioning
  1. "A DATA STRUCTURE TO INCORPORATE VERSIONING IN 3D CITY MODELS" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2019 — [journal article](https://doi.org/10.5194/isprs-annals-iv-4-w8-123-2019)
     - authors: S. Vitalis (supervisor: Vitalis), A. Labetski, K. Arroyo Ohori, H. Ledoux (supervisor: Ledoux), J. Stoter
     - title similarity 0.38; abstract similarity 0.47; year -1  (source: Crossref)
- **Laurens Oostwegel (2020)** — Indoor positioning using augmented reality
  1. "Explaining building exposure using urban morphology and AI" — ?, 2026 — [posted-content](https://doi.org/10.5194/egusphere-egu26-10682)
     - authors: Laurens Jozef Nicolaas Oostwegel (student), Danijel Schorlemmer, Doren Çalliku, Tara Evaz Zadeh, Lars Lingner, Pablo de la Mora, Wenyu Nie, Kasra Rafiezadeh Shahi, Chengzhi Rao, Philippe Guéguen
     - title similarity 0.36; abstract similarity 0.10; year +6  (source: Crossref)
  2. "Simplifying Mapping for Building Exposure using OpenStreetMap Tools" — ?, 2026 — [posted-content](https://doi.org/10.5194/egusphere-egu26-21319)
     - authors: Doren Calliku, Danijel Schorlemmer, Laurens J.N. Oostwegel (student), Pablo de la Mora Lobaton, Chengzhi Rao, Tara Evaz Zadeh, Lars Lingner
     - title similarity 0.39; abstract similarity 0.07; year +6  (source: Crossref)
  3. "Indoor Mapping and Positioning using Augmented Reality" — 2019 7th International Conference on Future Internet of Things and Clo, 2019 — [conference paper](https://doi.org/10.1109/ficloud.2019.00056)
     - authors: Ibrahim Alper Koc, Tacha Serif, Sezer Goren, George Ghinea
     - title similarity 0.88; abstract similarity n/a; year -1  (source: Crossref)
- **Willem van Opstal (2020)** — Automatic isobath generalisation for navigational charts
  1. "Rule-based isobath generalisation using the Triangle Region Graph: uniting soundings, isobaths and constraints through a navigational surface" — Proceedings of 23rd ICA Workshop on Generalisation and Multiple Repres, 2020 — [conference paper](https://www.gdmc.nl/publications/2020/ICAgen2020_paper_11.pdf)
     - authors: Willem van Opstal (student), Martijn Meijers (supervisor: Meijers), Ravi Peters
     - title similarity 0.43; abstract similarity n/a; year +0  (source: GDMC)
- **Yifang Zhao (2020)** — Outer surface extraction for complex 3D building models
  1. "Efficient extraction of chitin-glucan complex from Shiitake mushroom with deep eutectic solvent" — Journal of Environmental Chemical Engineering, 2025 — [journal article](https://doi.org/10.1016/j.jece.2025.117835)
     - authors: Xianwen Hu, Peiyu Zhao, Youcun Zhu, Yifang Zhao (student), Lei Dai
     - title similarity 0.37; abstract similarity n/a; year +5  (source: Crossref)
- **Xiaoai Li (2021)** — CityREST: CityJSON in a database + RESTful access
  1. "CITYJSON + WEB = NINJA" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2020 — [journal article](https://doi.org/10.5194/isprs-annals-vi-4-w1-2020-167-2020)
     - authors: S. Vitalis, A. Labetski, F. Boersma, F. Dahle, X. Li (student), K. Arroyo Ohori, H. Ledoux (supervisor: Ledoux), J. Stoter
     - title similarity 0.39; abstract similarity 0.43; year -1  (source: Crossref)
  2. "DSRP: A Database for Stress Reduction Using Physiological Signals" — IEEE Access, 2024 — [journal article](https://doi.org/10.1109/access.2024.3454090)
     - authors: Zhengping Li, Weizhi Ma, Junshuai Zhang, Lijun Wang, Yuwen Hao, Xiaoxue Li (student)
     - title similarity 0.40; abstract similarity n/a; year +3  (source: Crossref)
  3. "ScenarioSA: A Dyadic Conversational Database for Interactive Sentiment Analysis" — IEEE Access, 2020 — [journal article](https://doi.org/10.1109/access.2020.2994147)
     - authors: Yazhou Zhang, Zhipeng Zhao, Panpan Wang, Xiang Li (student), Lu Rong, Dawei Song
     - title similarity 0.44; abstract similarity n/a; year -1  (source: Crossref)
- **Ioannis Dardavesis (2022)** — Indoor localisation and location tracking in semi-public buildings based on LiDA
  1. "Indoor localisation and location tracking in indoor facilities based on LiDAR point clouds and images of the ceilings" — Proceedings of the 26th AGILE Conference on Geographic Information Sci, 2023 — [conference paper](https://doi.org/10.5194/agile-giss-4-4-2023)
     - authors: Ioannis Dardavesis (student), Edward Verbree (supervisor: Verbree), Azarakhsh Rafiee
     - title similarity 0.88; abstract similarity 0.78; year +1  (source: GDMC)
- **Michiel de Jong (2022)** — Using voxelised spaces for the generation and visualisation of dynamic evacuatio
  1. "Building Rhythms: Reopening the Workspace with Indoor Localisation" — Chapter in: LBS 2021: Proceedings of the 16th International Conference, 2021 — [conference paper](https://doi.org/10.34726/1741)
     - authors: Guilherme Spinoza Andreo, Ioannis Dardavesis, Michiel de Jong (student), Pratyush Kumar, Maundri Prihanggo, Georgios Triantafyllou, Niels van der Vaart, Edward Verbree, Zhenyu Liu, Runnan Fu, Linjun Wang, Yuzhen Jin, Theodoros Papakostas, Xenia Una Mainelli, Robert Voûte (supervisor: Voûte)
     - title similarity 0.37; abstract similarity n/a; year -1  (source: GDMC)
- **Yuzhen Jin (2022)** — Dynamic energy simulations based on the 3D BAG 2.0
  1. "Parametric Study on Wind Energy Harvesting of Extraneously Induced Excitation Flutter-Driven Triboelectric Nanogenerator" — ?, 2024 — [posted-content](https://doi.org/10.2139/ssrn.4889179)
     - authors: Yadong Zhang, Yuzhen Jin (student), Jingyu Cui
     - title similarity 0.35; abstract similarity n/a; year +2  (source: Crossref)
  2. "Design and development of a student information management platform based on support vector machines and data mining" — International Journal of Information and Communication Technology, 2026 — [journal article](https://doi.org/10.1504/ijict.2026.155942)
     - authors: Yuzhen Jin (student)
     - title similarity 0.38; abstract similarity n/a; year +4  (source: Crossref)
  3. "Design and development of a student information management platform based on support vector machines and data mining" — International Journal of Information and Communication Technology, 2026 — [journal article](https://doi.org/10.1504/ijict.2026.10080360)
     - authors: Yuzhen Jin (student)
     - title similarity 0.38; abstract similarity n/a; year +4  (source: Crossref)
- **Zhenyu Liu (2022)** — Dynamic Objects Detection and Removal in Mobile Laser Scanning Data
  1. "Data frame aware optimized Octomap-based dynamic object detection and removal in Mobile Laser Scanning data" — Alexandria Engineering Journal, 74, pp. 327-344, 2023 — [journal article](https://www.sciencedirect.com/science/article/pii/S1110016823003770)
     - authors: Zhenyu Liu (student), Peter van Oosterom (supervisor: van Oosterom), Jesús Balado, Arjen Swart, Bart Beers
     - title similarity 0.76; abstract similarity 0.84; year +1  (source: GDMC)
  2. "Detection and reconstruction of static vehicle-related ground occlusions in point clouds from mobile laser scanning" — Automation in Construction, Elsevier BV, 141, pp. 104461, 2022 — [journal article](https://www.sciencedirect.com/science/article/pii/S092658052200334X)
     - authors: Zhenyu Liu (student), Peter van Oosterom (supervisor: van Oosterom), Jesús Balado, Arjen Swart, Bart Beers
     - title similarity 0.49; abstract similarity 0.31; year +0  (source: GDMC)
- **Rohit Ramlakhan (2022)** — Modelling the legal spaces of 3D underground objects in a 3D LAS
  1. "Modelling the legal spaces of 3D underground objects in 3D land administration systems" — Land Use Policy, Elsevier BV, 127, pp. 106537, 2023 — [journal article](https://www.sciencedirect.com/science/article/pii/S0264837723000030)
     - authors: Rohit Ramlakhan (student), Eftychia Kalogianni (supervisor: Kalogianni), Peter van Oosterom (supervisor: van Oosterom), Behnam Atazadeh
     - title similarity 0.82; abstract similarity 0.70; year +1  (source: GDMC)
  2. "Modelling 3D underground legal spaces in 3D Land Administration Systems" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:4a499efb-f348-456b-9965-65c47519337a)
     - authors: Rohit Ramlakhan (student), Eftychia Kalogianni (supervisor: Kalogianni), Peter van Oosterom (supervisor: van Oosterom), Ramlakhan, Rohit (student), Kalogianni, Eftychia, van Oosterom , Peter
     - title similarity 0.56; abstract similarity 0.70; year -1  (source: GDMC)
  3. "BIM/IFC as input for registering apartment rights in a 3D Land Administration Systems – A prototype webservice" — Land Use Policy, Elsevier, 148(107368), pp. 14, 2025 — [journal article](https://doi.org/10.1016/j.landusepol.2024.107368)
     - authors: Marjan Broekhuizen, Eftychia Kalogianni (supervisor: Kalogianni), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.32; abstract similarity 0.51; year +3  (source: GDMC)
  4. "BIM Models as input for 3D Land Administration Systems for Apartment Registration" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:5e240a06-5fdf-4354-9e6d-09c675f1cd8b)
     - authors: Marjan Broekhuizen, Eftychia Kalogianni (supervisor: Kalogianni), Peter van Oosterom (supervisor: van Oosterom), Broekhuizen, Marjan, Kalogianni, Eftychia, van Oosterom, Peter
     - title similarity 0.23; abstract similarity 0.58; year -1  (source: GDMC)
- **Georgios Triantafyllou (2022)** — Isovist Fingerprinting as new way of Indoor Localisation
  1. "Indoor localisation through Isovist fingerprinting from point clouds and floor plans" — Journal of Location Based Services, 2024 — [journal article](https://doi.org/10.1080/17489725.2024.2320642)
     - authors: Georgios Triantafyllou (student), Edward Verbree (supervisor: Verbree), Azarakhsh Rafiee
     - title similarity 0.50; abstract similarity 0.65; year +2  (source: OpenAlex)
  2. "Building Rhythms: Reopening the Workspace with Indoor Localisation" — Chapter in: LBS 2021: Proceedings of the 16th International Conference, 2021 — [conference paper](https://doi.org/10.34726/1741)
     - authors: Guilherme Spinoza Andreo, Ioannis Dardavesis, Michiel de Jong, Pratyush Kumar, Maundri Prihanggo, Georgios Triantafyllou (student), Niels van der Vaart, Edward Verbree (supervisor: Verbree), Zhenyu Liu, Runnan Fu, Linjun Wang, Yuzhen Jin, Theodoros Papakostas, Xenia Una Mainelli, Robert Voûte
     - title similarity 0.58; abstract similarity n/a; year -1  (source: GDMC)
  3. "Indoor localisation through Isovist fingerprinting from point clouds and floor plans" — Journal of Location Based Services, Taylor & Francis, (2320642), pp. 2, 2024 — [journal article](https://www.tandfonline.com/doi/full/10.1080/17489725.2024.2320642)
     - authors: Georgios Triantafyllou (student), Edward Verbree (supervisor: Verbree), Azarakhsh Rafiee, Simon Pena Pereira, Stef Lhermitte
     - title similarity 0.50; abstract similarity n/a; year +2  (source: GDMC)
- **Jasper van der Vaart (2022)** — Automatic building feature detection and reconstruction in IFC models
  1. "Defining LoDs to support BIM-based 3D building abstractions in GIS" — The International Archives of the Photogrammetry, Remote Sensing and S, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-55-2026)
     - authors: Jasper van der Vaart (student), Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter, Siham El Yamani
     - title similarity 0.43; abstract similarity 0.11; year +4  (source: Crossref)
- **Ondrej Veselý (2022)** — Building massing generation using GAN trained on Dutch 3D city models
  1. "Generating 3D Building Volumes for a Given Urban Context using Pix2Pix GAN" — eCAADe proceedings, 2022 — [conference paper](https://doi.org/10.52842/conf.ecaade.2022.2.287)
     - authors: Raffaele Di Carlo, Divyae Mittal, Ondrej Vesely (student)
     - title similarity 0.41; abstract similarity n/a; year +0  (source: Crossref)
- **Carolin Bachert (2023)** — Mapping the Energy ADE to CityGML 3.0
  1. "Mapping the CityGML Energy ADE to CityGML 3.0 Using a Model-Driven Approach" — ISPRS International Journal of Geo-Information, 2024 — [journal article](https://doi.org/10.3390/ijgi13040121)
     - authors: Carolin Bachert (student), Camilo León-Sánchez, Tatjana Kutzner, Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.65; abstract similarity 0.69; year +1  (source: Crossref)
- **Chrysanthi Papadimitriou (2023)** — All in? Identifying and tackling private sector’s barriers to data sharing: A Pe
  1. "European Energy Regulatory, Socioeconomic, and Organizational Aspects: An Analysis of Barriers Related to Data-Driven Services across Electricity Sectors" — Energies, 2022 — [journal article](https://doi.org/10.3390/en15062197)
     - authors: Kyriaki Psara, Christina Papadimitriou (student), Marily Efstratiadi, Sotiris Tsakanikas, Panos Papadopoulos, Paul Tobin
     - title similarity 0.39; abstract similarity 0.36; year -1  (source: Crossref)
- **Simon Pena Pereira (2023)** — Automated rooftop solar panel detection through Convolutional Neural Networks
  1. "Indoor localisation through Isovist fingerprinting from point clouds and floor plans" — Journal of Location Based Services, Taylor & Francis, (2320642), pp. 2, 2024 — [journal article](https://www.tandfonline.com/doi/full/10.1080/17489725.2024.2320642)
     - authors: Georgios Triantafyllou, Edward Verbree, Azarakhsh Rafiee (supervisor: Rafiee), Simon Pena Pereira (student), Stef Lhermitte (supervisor: Lhermitte)
     - title similarity 0.39; abstract similarity n/a; year +1  (source: GDMC)
- **Adele Therias (2023)** — Integrating radar and multi-spectral data to detect cocoa crops: a deep learning
  1. "Integrating Radar and Multi-Spectral Data to Detect Cocoa Crops: A Deep Learning Approach" — ?, 2024 — [posted-content](https://doi.org/10.2139/ssrn.4920905)
     - authors: Adele Therias (student), Azarakhsh Rafiee (supervisor: Rafiee), Stef Lhermitte, Philip van der Lugt, Roderik Lindenbergh
     - title similarity 1.00; abstract similarity 0.94; year +1  (source: Crossref)
  2. "Integrating radar and multi-spectral data to detect cocoa crops: A deep learning approach" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2025 — [journal article](https://doi.org/10.1016/j.rsase.2025.101652)
     - authors: Adele Therias (student), Azarakhsh Rafiee (supervisor: Rafiee), Stef Lhermitte, Philip van der Lugt, Roderik Lindenbergh
     - title similarity 1.00; abstract similarity n/a; year +2  (source: GDMC)
  3. "Integrating Radar and Multi-Spectral Data to Detect Cocoa Crops: A Deep Learning Approach" — ?, 2024 — [posted-content](https://doi.org/10.2139/ssrn.4975854)
     - authors: Adele Therias (student), Azarakhsh Rafiee (supervisor: Rafiee), Stef Lhermitte, Philip van der Lugt, Roderik Lindenbergh
     - title similarity 1.00; abstract similarity n/a; year +1  (source: Crossref)
- **Yitong Xia (2023)** — A data-driven approach to add openings to 3D BAG building models
  1. "Enriching LoD2 Building Models with Façade Openings Using Oblique Imagery" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-225-2025)
     - authors: Yitong Xia (student), Weixiao Gao, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.39; abstract similarity 0.56; year +2  (source: Crossref)
- **Simay Batum (2024)** — Spatial Plan Registration and Compliance Checks in Estonia, based on LADM Part 5
  1. "Spatial plan registration and compliance checks in Estonia, based on LADM part 5: spatial plan information" — Survey Review, Informa UK Limited, pp. 1–31, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2547462)
     - authors: Simay Batum (student), Eftychia Kalogianni (supervisor: Kalogianni), Marjan Broekhuizen (supervisor: Broekhuizen), Christopher Raitviir, Kermo M&auml;gi, Peter Van Oosterom (supervisor: van Oosterom), Kermo Mägi
     - title similarity 1.00; abstract similarity 0.63; year +1  (source: GDMC)
  2. "Leveraging BIM/IFC for the Registration of Spatial Plans and Compliance Checks and Permitting in Estonia based on LADM Part 5 - Spatial Plan Information" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_J.pdf)
     - authors: Simay Batum (student), Eftychia Kalogianni (supervisor: Kalogianni), Marjan Broekhuizen (supervisor: Broekhuizen), Christopher Raitviir, Kermo Mägi, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.74; abstract similarity n/a; year +0  (source: GDMC)
- **Yuduan Cai (2024)** — SplitSFC: A database solution for massive point cloud data management
  1. "cjdb: A Simple, Fast, and Lean Database Solution for the CityGML Data Model" — Lecture Notes in Geoinformation and Cartography, 2024 — [book-chapter](https://doi.org/10.1007/978-3-031-43699-4_47)
     - authors: Leon Powałka, Chris Poon, Yitong Xia, Siebren Meines, Lan Yan, Yuduan Cai (student), Gina Stavropoulou, Balázs Dukai, Hugo Ledoux
     - title similarity 0.54; abstract similarity n/a; year +0  (source: Crossref)
- **Mengying Chen (2024)** — Formalizing land indicators for SDGs: Implementation and evaluation using intern
  1. "Formalizing land indicators for SDGs: Implementation and evaluation using international standards" — Proceedings of the FIG Working Week 20225, Brisbane, Australia, pp. 16, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/LADM_SDGindicators.pdf)
     - authors: Mengying Chen (student), Peter van Oosterom (supervisor: van Oosterom), Eftychia Kalogianni (supervisor: Kalogianni)
     - title similarity 1.00; abstract similarity n/a; year +1  (source: GDMC)
  2. "Bridging Sustainable Development Goals and Land Administration: The Role of the ISO 19152 Land Administration Domain Model in SDG Indicator Formalization" — Land, MDPI AG, 13(491), pp. 27, 2024 — [journal article](https://doi.org/10.3390/land13040491)
     - authors: Mengying Chen (student), Peter Van Oosterom (supervisor: van Oosterom), Eftychia Kalogianni (supervisor: Kalogianni), Paula Dijkstra, Christiaan Lemmen
     - title similarity 0.25; abstract similarity 0.43; year +0  (source: GDMC)
  3. "Monitoring Indicators of International Guidance Documents and Frameworks through LADM" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_R.pdf)
     - authors: Abdullah Kara, Mengying Chen (student), Peter van Oosterom (supervisor: van Oosterom), Christiaan Lemmen, Kara, Abdullah, Chen, Mengying (student), van Oosterom, Peter J.M., Lemmen, C.H.J.; id_orcid 0000-0003-1514-8385
     - title similarity 0.44; abstract similarity 0.51; year +0  (source: GDMC)
  4. "Analyzing and formalising land indicators of LGAF, GLII and SDGs through LADM" — Survey Review, Taylor and Francis, pp. 21, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2544400)
     - authors: Mengying Chen (student), Abdullah Kara, Peter van Oosterom (supervisor: van Oosterom), Regina Orvañanos Murguía, John Gitau, Christiaan Lemmen
     - title similarity 0.40; abstract similarity 0.42; year +1  (source: GDMC)
- **Irina Gheorghiu (2024)** — Analysis of the visibility of GPS satellites in the urban environment using poin
  1. "An Approach to Map Visibility in the Built Environment From Airborne LiDAR Point Clouds" — IEEE Access, 2021 — [journal article](https://doi.org/10.1109/access.2021.3066649)
     - authors: Guan-Ting Zhang, Edward Verbree (supervisor: Verbree), Xiao-Jun Wang
     - title similarity 0.56; abstract similarity 0.19; year -3  (source: OpenAlex)
- **Tessel Elisabeth Kaal (2024)** — Optimizing Energy Balance in Multi-Energy Microgrids -- Enhancing Grid Efficienc
  1. "Deep Reinforcement Learning-Graph Neural Networks-Dynamic Clustering triplet for Adaptive Multi Energy Microgrid optimization" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-g-2025-427-2025)
     - authors: Tessel Kaal (student), Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.30; abstract similarity 0.57; year +1  (source: Crossref)
- **Maria Luisa Tarozzo Kawasaki (2024)** — Common Ground: Bridging Subsurface Information Models and Climate Adaptation Des
  1. "Integrating subsurface data into urban planning for climate adaptation using land administration domain model part 5" — Survey Review, Taylor and Francis, pp. 17, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2539606)
     - authors: Maria Luisa Tarozzo Kawasaki (student), Laura Thomas, Ulf Hackauf (supervisor: Hackauf), Rob van der Krogt (supervisor: van der Krogt), Wilfred Visser (supervisor: Visser), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.46; abstract similarity 0.57; year +1  (source: GDMC)
  2. "Bringing Subsurface Information Models and Climate Adaptation Design into LADM part 5 Spatial Plan Information" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_G.pdf)
     - authors: Maria Luisa Tarozzo Kawasaki (student), Rob van der Krogt (supervisor: van der Krogt), Wilfred Visser (supervisor: Visser), Ulf Hackauf (supervisor: Hackauf), Alexander Wandl (supervisor: Wandl), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.71; abstract similarity n/a; year +0  (source: GDMC)
  3. "Climate resilient spatial plans: Revised LADM climate adaptation profile" — Proceedings of the 13th International FIG Workshop on Land Administrat, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/3DLA2025_paper_ZA_89.pdf)
     - authors: Maria Luisa Tarozzo Kawasaki (student), Rob van der Krogt (supervisor: van der Krogt), Wilfred Visser (supervisor: Visser), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.43; abstract similarity n/a; year +1  (source: GDMC)
- **Gabriela Koster (2024)** — Implementing a Dutch building energy simulation tool: Energy model testing for R
  1. "Solar potential mapping to address energy poverty in a data poor region: A case study in Plovdiv, Bulgaria" — ?, 2023 — [posted-content](https://doi.org/10.5194/egusphere-egu23-13628)
     - authors: Wilfried van Sark, Gabriela Koster (student), Britta Ricker
     - title similarity 0.36; abstract similarity 0.26; year -1  (source: Crossref)
- **Sharath Chandra Madanu (2024)** — A Confidence-aware Deep Learning Framework for Refining Laser-scanned Point Clou
  1. "RefineNet: a Confidence-aware Deep Online Learning Framework to Refine Real-world Point Cloud Semantic Segmentation" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-3-2026-179-2026)
     - authors: Sharath Chandra Madanu (student), Shenglan Du (supervisor: Du), Jantien Stoter (supervisor: Stoter), Daan van der Heide (supervisor: van der Heide)
     - title similarity 0.71; abstract similarity 0.62; year +2  (source: Crossref)
- **Dimitris Mantas (2024)** — CNN-based roofing material segmentation using aerial imagery and LiDAR data fusi
  1. "RoofSense: A Multimodal Semantic Segmentation Dataset for Roofing Material Classification" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-153-2025)
     - authors: Dimitris Mantas (student), Weixiao Gao, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.36; abstract similarity 0.40; year +1  (source: Crossref)
- **Ping Mao (2024)** — A digital twin based on Land Administration
  1. "A digital twin based on Land Administration" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_N.pdf)
     - authors: Ping Mao (student), Peter van Oosterom (supervisor: van Oosterom), Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 1.00; abstract similarity n/a; year +0  (source: GDMC)
  2. "The Land Administration Domain Model" — Land Use Policy, 2015 — [journal article](https://doi.org/10.1016/j.landusepol.2015.01.014)
     - authors: Christiaan Lemmen, Peter van Oosterom (supervisor: van Oosterom), Rohan Bennett
     - title similarity 0.58; abstract similarity 0.25; year -9  (source: OpenAlex)
  3. "Remote Sensing for Land Administration" — Remote Sensing, 2020 — [journal article](https://doi.org/10.3390/rs12152497)
     - authors: Rohan Bennett, Peter van Oosterom (supervisor: van Oosterom), Christiaan Lemmen, Mila Koeva
     - title similarity 0.62; abstract similarity 0.18; year -4  (source: OpenAlex)
- **Pam Sterkman (2024)** — Exploring the potential of explorative point clouds in floodplain maintenance
  1. "Comparison of cloud-to-cloud distance calculation methods for change detection in spatio-temporal point clouds" — ?, 2024 — [conference paper](https://doi.org/10.5194/egusphere-egu24-8191)
     - authors: Vitali Diaz, Peter van Oosterom, Martijn Meijers, Edward Verbree (supervisor: Verbree), Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.31; abstract similarity 0.54; year +0  (source: OpenAlex)
- **Bing-Shiuan Tsai (2024)** — 3DCityDB-Tools plug-in for QGIS: Adding server-side support to 3DCityDB v.5.0
  1. "Introducing server-side support for 3DCityDB 5.0 to the 3DCityDB-Tools plug-in for QGIS" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-193-2025)
     - authors: Bing-Shiuan Tsai (student), Giorgio Agugiaro (supervisor: Agugiaro), Camilo Leon-Sanchez, Claus Nagel (supervisor: Nagel), Zhihang Yao (supervisor: Yao)
     - title similarity 0.78; abstract similarity 0.53; year +1  (source: Crossref)
  2. "Introducing the 3DCityDB-Tools Plug-In for QGIS" — Lecture Notes in Geoinformation and Cartography, 2024 — [book-chapter](https://doi.org/10.1007/978-3-031-43699-4_48)
     - authors: Giorgio Agugiaro (supervisor: Agugiaro), Konstantinos Pantelios, Camilo León-Sánchez, Zhihang Yao (supervisor: Yao), Claus Nagel (supervisor: Nagel)
     - title similarity 0.51; abstract similarity n/a; year +0  (source: Crossref)
- **Marjolein van Aalst (2024)** — A standards-based portal for integrated Land Administration information - A case
  1. "A standards-based portal for integrated Land Administration information: A case study of the Netherlands" — Proceedings of the FIG Working Week 20225, Brisbane, Australia, pp. 18, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/IntegratedLADM_NL.pdf)
     - authors: Marjolein van Aalst (student), Peter van Oosterom (supervisor: van Oosterom), Lexi Rowland, Erwin Folmer, Hendrik Ploeger
     - title similarity 1.00; abstract similarity n/a; year +1  (source: GDMC)
  2. "The first five parts of LADM Edition II have been published as ISO standards now" — Proceedings of the 13th International FIG Workshop on Land Administrat, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/3DLA2025_paper_C_1.pdf)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Abdullah Kara, and Christiaan Lemmen, van Oosterom, Peter J.M., Kara, Abdullah, Lemmen, C.H.J.; id_orcid 0000-0003-1514-8385
     - title similarity 0.14; abstract similarity 0.49; year +1  (source: GDMC)
- **Citra Andinasari (2025)** — Point Cloud for 3D Land Administration System (LAS)
  1. "Point Clouds for 3D Land Administration: Integrating Floor Plans and Nationwide Airborne LiDAR (AHN)" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2025 — [conference paper](https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-9-2025)
     - authors: Citra Andinasari (student), Peter van Oosteroom, Edward Verbree (supervisor: Verbree)
     - title similarity 0.60; abstract similarity 0.71; year +0  (source: GDMC)
  2. "Point Cloud for 3D Land Administration System (LAS)" — Proceedings of the 13th International FIG Workshop on Land Administrat, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/3DLA2025_paper_S_39.pdf)
     - authors: Citra Andinasari (student), Peter van Oosteroma, Edward Verbree (supervisor: Verbree)
     - title similarity 1.00; abstract similarity n/a; year +0  (source: GDMC)
  3. "Remote Sensing for Land Administration" — Remote Sensing, 2020 — [journal article](https://doi.org/10.3390/rs12152497)
     - authors: Rohan Bennett, Peter van Oosterom (supervisor: van Oosterom), Christiaan Lemmen, Mila Koeva
     - title similarity 0.63; abstract similarity 0.23; year -5  (source: OpenAlex)
  4. "The Land Administration Domain Model" — Land Use Policy, 2015 — [journal article](https://doi.org/10.1016/j.landusepol.2015.01.014)
     - authors: Christiaan Lemmen, Peter van Oosterom (supervisor: van Oosterom), Rohan Bennett
     - title similarity 0.57; abstract similarity 0.22; year -10  (source: OpenAlex)
  5. "Modelling the legal spaces of 3D underground objects in 3D land administration systems" — Land Use Policy, 2023 — [journal article](https://doi.org/10.1016/j.landusepol.2023.106537)
     - authors: Rohit Ramlakhan, Eftychia Kalogianni, Peter van Oosterom (supervisor: van Oosterom), Behnam Atazadeh
     - title similarity 0.62; abstract similarity 0.15; year -2  (source: OpenAlex)
  6. "3D Land Administration for 3D Land Uses" — Land Use Policy, 2020 — [journal article](https://doi.org/10.1016/j.landusepol.2020.104665)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Rohan Bennett, Mila Koeva, Christiaan Lemmen
     - title similarity 0.61; abstract similarity 0.15; year -5  (source: OpenAlex)
- **Hidemichi Baba (2025)** — FlatCityBuf: A new cloud-optimised CityJSON format
  1. "FlatCityBuf: A new cloud-optimised CityJSON format" — The International Archives of the Photogrammetry, Remote Sensing and S, 2025 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-17-2025)
     - authors: Hidemichi Baba (student), Hugo Ledoux (supervisor: Ledoux), Ravi Peters (supervisor: Peters)
     - title similarity 1.00; abstract similarity 0.61; year +0  (source: Crossref)
- **Aswathy Chandran (2025)** — Proposal for the integration of a Building Material part: (ISO 19152-7) within t
  1. "Proposal for the integration of a Building Material part: (ISO 19152-7) within the Land Administration Domain Model" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_C.pdf)
     - authors: Aswathy Chandran (student), Peter van Oosterom (supervisor: van Oosterom), Wilko Quak (supervisor: Quak), Pablo van den Bosch, Frederique van Erven
     - title similarity 1.00; abstract similarity n/a; year -1  (source: GDMC)
  2. "Integrating subsurface data into urban planning for climate adaptation using land administration domain model part 5" — Survey Review, Taylor and Francis, pp. 17, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2539606)
     - authors: Maria Luisa Tarozzo Kawasaki, Laura Thomas, Ulf Hackauf, Rob van der Krogt, Wilfred Visser, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.59; abstract similarity 0.20; year +0  (source: GDMC)
  3. "The Foundation of Edition II of the Land Administration Domain Model" — University of Twente Research Information, 2021 — [conference paper](https://openalex.org/W3184511481)
     - authors: C. Lemmen, Abdullah Alattas, Agung Indrajit, Eftychia Kalogianni, Abdullah Kara, Peter Oukes, P.J.M. van Oosterom (supervisor: van Oosterom)
     - title similarity 0.65; abstract similarity 0.21; year -4  (source: OpenAlex)
  4. "Validity of Mixed 2D and 3D Cadastral Parcels in the Land Administration Domain Model" — Research Repository (Delft University of Technology), 2012 — [conference paper](https://openalex.org/W2162670506)
     - authors: Rodney James Thompson, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.60; abstract similarity 0.19; year -13  (source: OpenAlex)
  5. "Developing a spatial planning information package in ISO 19152 land administration domain model" — Land Use Policy, 2020 — [journal article](https://doi.org/10.1016/j.landusepol.2019.104111)
     - authors: Agung Indrajit, Bastiaan van Loenen, Hendrik Ploeger, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.60; abstract similarity n/a; year -5  (source: OpenAlex)
- **Hsin-Yu Cheng (2025)** — Roof Structure Extraction from Remote Sensing Images
  1. "Roof Structure Extraction from Remote Sensing Images" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xii-4-w1-2026-81-2026)
     - authors: Hsin-Yu Cheng (student), Weixiao Gao (supervisor: Gao), Liangliang Nan (supervisor: Nan)
     - title similarity 1.00; abstract similarity 0.50; year +1  (source: Crossref)
- **Haohua Gan (2025)** — Exploration of algorithms for extracting wireframe models from man-made urban li
  1. "Wireframe Extraction of Urban Linear Objects from Aerial Lidar Point Clouds" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xii-4-w1-2026-145-2026)
     - authors: Haohua Gan (student), Hugo Ledoux (supervisor: Ledoux), Weixiao Gao (supervisor: Gao)
     - title similarity 0.50; abstract similarity 0.50; year +1  (source: Crossref)
- **Xueheng Li (2025)** — 3D Visualization and Dissemination of Property Valuation Information Based on LA
  1. "Visualisation and dissemination of 3D valuation units and groups – An LADM valuation information compliant prototype" — Land Use Policy, 2023 — [journal article](https://doi.org/10.1016/j.landusepol.2023.106829)
     - authors: Abdullah Kara (supervisor: Kara), Peter van Oosterom (supervisor: van Oosterom), Ruud Kathmann, Christiaan Lemmen
     - title similarity 0.67; abstract similarity n/a; year -2  (source: OpenAlex)
- **Adhisye Rahmawati (2025)** — Scenario-based energy simulation: Modelling tree planting strategy to reduce hea
  1. "Scenario-based energy simulation of tree planting strategies to reduce the heating and cooling demand of buildings under 2050 climate conditions" — The International Archives of the Photogrammetry, Remote Sensing and S, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlix-b4-2026-513-2026)
     - authors: Adhisye Rahmawati (student), Weixiao Gao (supervisor: Gao), Camilo León Sánchez, Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.89; abstract similarity 0.60; year +1  (source: Crossref)
- **Zhuoyue Wang (2025)** — Structuring Semantics in Smart Point Clouds Using an HBIM Ontology for Heritage 
  1. "Towards the architectural heritage information infrastructure: a UML-based information model linking HBIM, smart point clouds, and 3D Gaussian splatting" — Advanced Engineering Informatics, Elsevier BV, 76, pp. 16, 2026 — [journal article](https://doi.org/10.1016/j.aei.2026.105042)
     - authors: Yingwen Yu, Peter van Oosterom (supervisor: van Oosterom), Edward Verbree (supervisor: Verbree), Zhuoyue Wang (student), Uta Pottgiesser, Abeer Abu Raed, Yuyang Peng
     - title similarity 0.39; abstract similarity 0.30; year +1  (source: GDMC)
  2. "Towards a smart heritage information infrastructure: integrating multiple geometric representations and sharing semantics" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xii-4-w1-2026-325-2026)
     - authors: Yingwen Yu, Peter van Oosterom (supervisor: van Oosterom), Edward Verbree (supervisor: Verbree), Uta Pottgiesser, Yuyang Peng, Zhuoyue Wang (student)
     - title similarity 0.18; abstract similarity 0.46; year +1  (source: Crossref)
  3. "Smart point cloud–guided 3D gaussian splatting for urban modeling and data-driven analysis" — Sustainable Cities and Society, Elsevier BV, 149, pp. 107753, 2026 — [journal article](https://doi.org/10.1016/j.scs.2026.107753)
     - authors: Yingwen Yu, Zhuoyue Wang (student), Guanting Zhang, Peter van Oosterom (supervisor: van Oosterom), Edward Verbree (supervisor: Verbree), Steffen Nijhuis, Yuyang Peng
     - title similarity 0.38; abstract similarity 0.25; year +1  (source: GDMC)
  4. "Smart Point Cloud–Guided 3D Gaussian Splatting for Urban Modeling and Data-Driven Analysis" — SSRN Electronic Journal, 2026 — [preprint](https://doi.org/10.2139/ssrn.6094769)
     - authors: Yingwen Yu, Zhuoyue Wang (student), Guanting Zhang, Peter van Oosterom (supervisor: van Oosterom), Edward Verbree (supervisor: Verbree), Steffen NIJHUIS, Yuyang PENG
     - title similarity 0.38; abstract similarity n/a; year +1  (source: OpenAlex)
- **Xiaduo Zhao (2025)** — Structure guided roof heightmap completion
  1. "Structure-guided strategies for aptamer screening and optimization: Advances and perspectives" — TrAC Trends in Analytical Chemistry, 2026 — [journal article](https://doi.org/10.1016/j.trac.2026.118870)
     - authors: Lianhui Zhao, Ping Wang, Tianming Qu, Qinglong Ji, Xiaomei Zhao (student), Ying Chen
     - title similarity 0.43; abstract similarity n/a; year +1  (source: Crossref)
- **Jiaoyang Wu (2026)** — Detecting building element/material through ground-based thermal imagery using D
  1. "Enhancing Pandemic Prediction: A Deep Learning Approach Using Transformer Neural Networks and Multi-Source Data Fusion for Infectious Disease Forecasting" — ?, 2025 — [posted-content](https://doi.org/10.1101/2025.06.24.25330211)
     - authors: Jiande Wu (student), Shakhawat Tanim, MinJae Woo, Tanvir Ahammed, Lior Rennert
     - title similarity 0.35; abstract similarity 0.09; year -1  (source: Crossref)

## Possible (94 theses)

Weaker evidence; most of these are probably unrelated (a supervisor's other work, a namesake). Top candidates only.

- **Tirza Bont (2006)** — Geographic data integration for telecommunication purposes
  1. "Geo-Information Support in Management of Urban Disasters" — Open House International, 2006 — [journal article](https://doi.org/10.1108/ohi-01-2006-b0008)
     - authors: Sisi Zlatanova, Peter van Oosterom (supervisor: van Oosterom), Edward Verbree (supervisor: Verbree)
     - title similarity 0.43; abstract similarity 0.05; year +0  (source: OpenAlex)
  2. "A Standardized Land Administration Domain Model as Part of the (Spatial) Information Infrastructure" — ?, 2008 — [book-chapter](https://doi.org/10.1201/9781420070729-14)
     - authors: Arco Groothedde, Christiaan Lemmen, Paul van der Molen, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.36; abstract similarity 0.32; year +2  (source: OpenAlex)
  3. "A Generic Approach to Simplification of Geodata for Mobile Applications" — Proceedings of the 10th AGILE International Conference on Geographic I, 2007 — [conference paper](https://www.gdmc.nl/publications/2007/Simplification_Geodata_Mobile_Applications.pdf)
     - authors: Theodor Foerster, Jantien Stoter, Barend Köbben, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.35; abstract similarity 0.21; year +1  (source: GDMC)
  4. "Towards a National 3D Spatial Data Infrastructure: Case of The Netherlands" — Photogrammetrie - Fernerkundung - Geoinformation, Schweizerbart, 2011(, 2011 — [journal article](https://doi.org/10.1127/1432-8364/2011/0094)
     - authors: J. Stoter, G. Vosselman, J. Goos, S. Zlatanova, E. Verbree (supervisor: Verbree), R. Klooster, M. Reuvers
     - title similarity 0.38; abstract similarity 0.22; year +5  (source: GDMC)
  … and 78 more possible candidates; re-run with --limit/--surname to see them all.
- **Adamantios Kagkaras (2006)** — Laser scanning modelling of a Cessna citation
  1. "Combining modern techniques for urban 3D modelling First impressions of an architectural modelling project" — ?, 2007 — [journal article](https://openalex.org/W2185462091)
     - authors: Georgeta Pop, Alexander Bucksch (supervisor: Bucksch)
     - title similarity 0.36; abstract similarity 0.26; year +1  (source: OpenAlex)
  2. "Combining modern techniques for urban 3D modelling" — ?, 2007 — [conference paper](https://doi.org/10.1109/igarss.2007.4423239)
     - authors: Georgeta Pop (Manea), Alexander Bucksch (supervisor: Bucksch)
     - title similarity 0.34; abstract similarity 0.26; year +1  (source: OpenAlex)
  3. "Reducing the error in terrestrial laser scanning by optimizing the measurement set-up" — Data Archiving and Networked Services (DANS), 2008 — [conference paper](https://openalex.org/W1538320763)
     - authors: Sylvie Dijkstra-Soudarissanane, Roderik Lindenbergh, Ben Gorte (supervisor: Gorte)
     - title similarity 0.38; abstract similarity 0.18; year +2  (source: OpenAlex)
  4. "PLANAR FEATURE EXTRACTION IN TERRESTRIAL LASER SCANS USING GRADIENT BASED RANGE IMAGE SEGMENTATION" — ?, 2007 — [journal article](https://openalex.org/W1493140170)
     - authors: Ben Gorte (supervisor: Gorte)
     - title similarity 0.42; abstract similarity 0.10; year +1  (source: OpenAlex)
  … and 20 more possible candidates; re-run with --limit/--surname to see them all.
- **Martin Kodde (2006)** — Glacier Surface Analysis. Airborne Laser Scanning for monitoring glaciers and cr
  1. "Reducing the error in terrestrial laser scanning by optimizing the measurement set-up" — Data Archiving and Networked Services (DANS), 2008 — [conference paper](https://openalex.org/W1538320763)
     - authors: Sylvie Dijkstra-Soudarissanane, Roderik Lindenbergh (supervisor: Lindenbergh), Ben Gorte (supervisor: Gorte)
     - title similarity 0.44; abstract similarity n/a; year +2  (source: OpenAlex)
  2. "Aeolian Beach Sand Transport Monitored by Terrestrial Laser Scanning" — The Photogrammetric Record, 2011 — [journal article](https://doi.org/10.1111/j.1477-9730.2011.00659.x)
     - authors: Roderik C. Lindenbergh (supervisor: Lindenbergh), Sylvie S. Soudarissanane, Sierd De Vries, Ben G. H. Gorte (supervisor: Gorte), Matthieu A. De Schipper
     - title similarity 0.34; abstract similarity n/a; year +5  (source: OpenAlex)
  3. "Extraction of building footprints from airborne laser scanning: Comparison and validation techniques" — 2007 Urban Remote Sensing Joint Event, 2007 — [conference paper](https://doi.org/10.1109/urs.2007.371854)
     - authors: Norbert Pfeifer (supervisor: Pfeifer), Martin Rutzinger, Franz Rottensteiner, Werner Muecke, Markus Hollaus
     - title similarity 0.46; abstract similarity n/a; year +1  (source: Crossref)
  4. "Object-Based Point Cloud Analysis of Full-Waveform Airborne Laser Scanning Data for Urban Vegetation Classification" — Sensors, 2008 — [journal article](https://doi.org/10.3390/s8084505)
     - authors: Martin Rutzinger, Bernhard Höfle, Markus Hollaus, Norbert Pfeifer (supervisor: Pfeifer)
     - title similarity 0.45; abstract similarity n/a; year +2  (source: Crossref)
  … and 9 more possible candidates; re-run with --limit/--surname to see them all.
- **Steven Alexander Sablerolle (2006)** — Automatic Registration of laser scanning data and colour images
  1. "STRUCTURAL MONITORING OF TUNNELS USING TERRESTRIAL LASER SCANNING" — Research Repository (Delft University of Technology), 2009 — [conference paper](https://openalex.org/W2137190534)
     - authors: Roderik Lindenbergh, Łukasz Uchański, Alexander Bucksch (supervisor: Bucksch), R. van Gosliga
     - title similarity 0.37; abstract similarity 0.28; year +3  (source: OpenAlex)
  2. "Localized Registration of Point Clouds of Botanic Trees" — IEEE Geoscience and Remote Sensing Letters, 2012 — [journal article](https://doi.org/10.1109/lgrs.2012.2216251)
     - authors: Alexander Bucksch (supervisor: Bucksch), Kourosh Khoshelham
     - title similarity 0.50; abstract similarity 0.22; year +6  (source: OpenAlex)
  3. "Revealing the skeleton from imperfect point clouds" — Research Repository (Delft University of Technology), 2011 — [dissertation](https://openalex.org/W1500469302)
     - authors: Alexander Bucksch (supervisor: Bucksch)
     - title similarity 0.30; abstract similarity 0.34; year +5  (source: OpenAlex)
  4. "Applications for point cloud skeletonizations in forestry and agriculture" — Research Repository (Delft University of Technology), 2009 — [conference paper](https://openalex.org/W1554064819)
     - authors: Alexander Bucksch (supervisor: Bucksch), Roderik Lindenbergh, Massimo Menenti
     - title similarity 0.40; abstract similarity 0.10; year +3  (source: OpenAlex)
  … and 6 more possible candidates; re-run with --limit/--surname to see them all.
- **Jane Margaret van Ree (2006)** — Determination of the precision and reliability parameters of terrestrial laser s
  1. "STRUCTURAL MONITORING OF TUNNELS USING TERRESTRIAL LASER SCANNING" — Research Repository (Delft University of Technology), 2009 — [conference paper](https://openalex.org/W2137190534)
     - authors: Roderik Lindenbergh (supervisor: Lindenbergh), Łukasz Uchański, Alexander Bucksch (supervisor: Bucksch), R. van Gosliga
     - title similarity 0.42; abstract similarity n/a; year +3  (source: OpenAlex)
  2. "Skeleton-based botanic tree diameter estimation from dense LiDAR data" — Proceedings of SPIE, the International Society for Optical Engineering, 2009 — [conference paper](https://doi.org/10.1117/12.825997)
     - authors: Alexander Bucksch (supervisor: Bucksch), Roderik Lindenbergh (supervisor: Lindenbergh), Massimo Menenti, Muhammad Z. Rahman
     - title similarity 0.35; abstract similarity n/a; year +3  (source: OpenAlex)
  3. "Applications for point cloud skeletonizations in forestry and agriculture" — Research Repository (Delft University of Technology), 2009 — [conference paper](https://openalex.org/W1554064819)
     - authors: Alexander Bucksch (supervisor: Bucksch), Roderik Lindenbergh (supervisor: Lindenbergh), Massimo Menenti
     - title similarity 0.31; abstract similarity n/a; year +3  (source: OpenAlex)
  4. "Automated detection of branch dimensions in woody skeletons of leafless fruit tree canopies" — Research Repository (Delft University of Technology), 2009 — [conference paper](https://openalex.org/W1588309802)
     - authors: Alexander Bucksch (supervisor: Bucksch), Stefan Fleck
     - title similarity 0.36; abstract similarity n/a; year +3  (source: OpenAlex)
  … and 2 more possible candidates; re-run with --limit/--surname to see them all.
- **Thanos Bantis (2008)** — Aerostat Photogrammetry for Large Scale Hydrological Modeling with Special Focus
  1. "4D cadastres: First analysis of Legal, organizational, and technical impact - With a case study on utility networks" — Land Use Policy, 27(4), pp. 1068-1081, 2010 — [journal article](https://doi.org/10.1016/j.landusepol.2010.02.003)
     - authors: Fatih Döner, Rod Thompson, Jantien Stoter, Christiaan Lemmen, Hendrik Ploeger, Peter van Oosterom, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.37; abstract similarity n/a; year +2  (source: GDMC)
  2. "A SWOT Analysis on the Implementation of Building Information Models within the Geospatial Environment" — Chapter in: Urban and Regional Data Management, UDMS 2009 Annual (Krek, 2009 — [conference paper](https://doi.org/10.1201/9780203869352.ch2)
     - authors: Ü. Işıkdağ, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.36; abstract similarity n/a; year +1  (source: GDMC)
  3. "A Conceptual Framework for 3D Visualisation to Support Urban Disaster Management" — Proceedings of the Joint Symposium of ICA WG on CEWaCM and JBGIS Gi4DM, 2009 — [conference paper](https://www.gdmc.nl/publications/2009/3D_Visualization_Urban_Disaster_Management.pdf)
     - authors: S. Kemec, S. Duzgun, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.35; abstract similarity n/a; year +1  (source: GDMC)
  4. "Exploring ontology potential in emergency management" — Proceedings of the Gi4DM Conference - Geomatics for Disaster Managemen, 2010 — [conference paper](https://www.gdmc.nl/publications/2010/Ontology_potential_emergency_management.pdf)
     - authors: Zhengjie Fan, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.33; abstract similarity n/a; year +2  (source: GDMC)
  … and 15 more possible candidates; re-run with --limit/--surname to see them all.
- **Tom Wortel (2009)** — Automating quantity surveying in road construction using UAV Videogrammetry
  1. "Vibration measurement of a model wind turbine using high speed photogrammetry" — Proceedings of SPIE, the International Society for Optical Engineering, 2011 — [conference paper](https://doi.org/10.1117/12.889440)
     - authors: Dinesh Kalpoe, Kourosh Khoshelham (supervisor: Khoshelham), Ben Gorte (supervisor: Gorte)
     - title similarity 0.33; abstract similarity 0.37; year +2  (source: OpenAlex)
  2. "Roof plane extraction in gridded digital surface models" — Research Repository (Delft University of Technology), 2009 — [conference paper](https://openalex.org/W1493451398)
     - authors: Ben Gorte (supervisor: Gorte)
     - title similarity 0.33; abstract similarity 0.07; year +0  (source: OpenAlex)
  3. "Evaluating MERIS-Based Aquatic Vegetation Mapping in Lake Victoria" — Remote Sensing, 2014 — [journal article](https://doi.org/10.3390/rs6087762)
     - authors: Elijah Cheruiyot, Collins Mito, Massimo Menenti, Ben Gorte (supervisor: Gorte), Roderik Koenders, Nadia Akdim
     - title similarity 0.38; abstract similarity 0.03; year +5  (source: OpenAlex)
  4. "Modelling and observation of heat losses from buildings : The impact of geometric detail on 3D heat flux modelling" — Data Archiving and Networked Services (DANS), 2013 — [conference paper](https://openalex.org/W2156116826)
     - authors: D. Lee, Peter Pietrzyk, Serge Donkers, V Liem, J. van Oostveen, Sina Montazeri, R. Boeters, J. Colin, Pierre Kastendeuch, Françoise Nerry, Massimo Menenti, Ben Gorte (supervisor: Gorte), E. Verbree
     - title similarity 0.31; abstract similarity 0.06; year +4  (source: OpenAlex)
  … and 4 more possible candidates; re-run with --limit/--surname to see them all.
- **Effrosyni Boufidou (2011)** — Towards understanding the DOQ Priorat terroirs: A multivariate GIS analysis
  1. "Measure the climate, model the city" — ISPRS Archives Volume XXXVIII-4/C21, 28th Urban Data Management Sympos, 2011 — [conference paper](https://doi.org/10.5194/isprsarchives-xxxviii-4-c21-59-2011)
     - authors: E. Boufidou (student), T.J.F. Commandeur, S.B. Nedkov, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.30; abstract similarity n/a; year +0  (source: GDMC)
  2. "Sensor services for buildings: a framework and opportunities" — Proceedings Gi4DM 2011, Antalya (O. Altan, R. Backhous, P. Boccardo, D, 2011 — [conference paper](https://www.gdmc.nl/publications/2011/Sensor_services_buildings.pdf)
     - authors: Ü. Işıkdağ, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.38; abstract similarity n/a; year +0  (source: GDMC)
  3. "A data model for route planning in the case of forest fires" — Computers & Geosciences, 68, pp. 1-10, 2014 — [journal article](https://doi.org/10.1016/j.cageo.2014.03.013)
     - authors: Zhiyong Wang, Sisi Zlatanova (supervisor: Zlatanova), Aitor Moreno, Peter van Oosterom, Carlos Toro
     - title similarity 0.37; abstract similarity n/a; year +3  (source: GDMC)
  4. "Detecting shadow for direct radiation using CityGML models for photovoltaic potentiality analysis" — Chapter in: UDMS Annual 2013 (C. Ellul, S. Zlatanova, M. Rumor, R. Lau, 2013 — [conference paper](https://doi.org/10.1201/b14914-23)
     - authors: N. Alam, V. Coors, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.36; abstract similarity n/a; year +2  (source: GDMC)
  … and 15 more possible candidates; re-run with --limit/--surname to see them all.
- **Lidia van Halderen (2011)** — Visual ego-motion estimation from unmanned deep sea vehicles
  1. "Evaluation of Sentinel-2 Bands over the Spectrum" — ESASP, 2012 — [journal article](https://openalex.org/W3008908672)
     - authors: S. E. Hosseini Aria, Ben Gorte (supervisor: Gorte), Massimo Menenti
     - title similarity 0.41; abstract similarity n/a; year +1  (source: OpenAlex)
  2. "Evaluating MERIS-Based Aquatic Vegetation Mapping in Lake Victoria" — Remote Sensing, 2014 — [journal article](https://doi.org/10.3390/rs6087762)
     - authors: Elijah Cheruiyot, Collins Mito, Massimo Menenti, Ben Gorte (supervisor: Gorte), Roderik Koenders, Nadia Akdim
     - title similarity 0.38; abstract similarity n/a; year +3  (source: OpenAlex)
  3. "Modeling and observation of heat losses from buildings: The impact of geometric detail on 3D heat flux modeling" — Proceedings EARSeL Conference (Rosa Lasaponara, ed.), Italy, pp. 20, 2013 — [conference paper](https://www.gdmc.nl/publications/2013/Geometric_detail_3D_heat_flux_modeling.pdf)
     - authors: Danbi Lee, Peter Pietrzyk, Sjors Donkers, Vera Liem, Jelte van Oostveen, Sina Montazeri, Roeland Boeters, Jerome Colin, Pierre Kastendeuch, Massimo Menenti, Ben Gorte (supervisor: Gorte), Edward Verbree
     - title similarity 0.34; abstract similarity n/a; year +2  (source: GDMC)
  4. "Modelling and observation of heat losses from buildings : The impact of geometric detail on 3D heat flux modelling" — Data Archiving and Networked Services (DANS), 2013 — [conference paper](https://openalex.org/W2156116826)
     - authors: D. Lee, Peter Pietrzyk, Serge Donkers, V Liem, J. van Oostveen, Sina Montazeri, R. Boeters, J. Colin, Pierre Kastendeuch, Françoise Nerry, Massimo Menenti, Ben Gorte (supervisor: Gorte), E. Verbree
     - title similarity 0.34; abstract similarity n/a; year +2  (source: OpenAlex)
  … and 2 more possible candidates; re-run with --limit/--surname to see them all.
- **Stijn Verlaar (2011)** — Evaluation of close range photogrammetric support for Pavescan
  1. "Aeolian Beach Sand Transport Monitored by Terrestrial Laser Scanning" — The Photogrammetric Record, 2011 — [journal article](https://doi.org/10.1111/j.1477-9730.2011.00659.x)
     - authors: Roderik C. Lindenbergh (supervisor: Lindenbergh), Sylvie S. Soudarissanane, Sierd De Vries, Ben G. H. Gorte (supervisor: Gorte), Matthieu A. De Schipper
     - title similarity 0.35; abstract similarity 0.05; year +0  (source: OpenAlex)
  2. "Vibration measurement of a model wind turbine using high speed photogrammetry" — Proceedings of SPIE, the International Society for Optical Engineering, 2011 — [conference paper](https://doi.org/10.1117/12.889440)
     - authors: Dinesh Kalpoe, Kourosh Khoshelham, Ben Gorte (supervisor: Gorte)
     - title similarity 0.43; abstract similarity 0.14; year +0  (source: OpenAlex)
  3. "Modelling and observation of heat losses from buildings : The impact of geometric detail on 3D heat flux modelling" — Data Archiving and Networked Services (DANS), 2013 — [conference paper](https://openalex.org/W2156116826)
     - authors: D. Lee, Peter Pietrzyk, Serge Donkers, V Liem, J. van Oostveen, Sina Montazeri, R. Boeters, J. Colin, Pierre Kastendeuch, Françoise Nerry, Massimo Menenti, Ben Gorte (supervisor: Gorte), E. Verbree
     - title similarity 0.44; abstract similarity 0.11; year +2  (source: OpenAlex)
  4. "Evaluation of Sentinel-2 Bands over the Spectrum" — ESASP, 2012 — [journal article](https://openalex.org/W3008908672)
     - authors: S. E. Hosseini Aria, Ben Gorte (supervisor: Gorte), Massimo Menenti
     - title similarity 0.46; abstract similarity n/a; year +1  (source: OpenAlex)
  … and 4 more possible candidates; re-run with --limit/--surname to see them all.
- **Daniel Xu (2011)** — Design and Implementation of Constraints for 3D Spatial Database - Using Climate
  1. "A Methodology for Modelling of 3D Spatial Constraints" — Chapter in: Advances in 3D Geoinformation (Alias Abdul-Rahman, ed.), p, 2016 — [conference paper](https://doi.org/10.1007/978-3-319-25691-7_6)
     - authors: Daniel Xu (student), Peter van Oosterom (supervisor: van Oosterom), Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.25; abstract similarity n/a; year +5  (source: GDMC)
  2. "A methodology for modelling of 3D spatial constraints" — Joint International Geoinformation Conference 2015, Kuala Lumpur, pp. , 2015 — [conference paper](https://www.gdmc.nl/publications/2015/Modelling_3D_spatial_constraints.pdf)
     - authors: Daniel Xu (student), Peter van Oosterom (supervisor: van Oosterom), Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.25; abstract similarity n/a; year +4  (source: GDMC)
  3. "An Approach to develop 3D Geo-DBMS Topological Operators by re-using existing 2D Operators" — Chapter in: ISPRS Annals Volume II-2/W1, Proceedings of the ISPRS 8th , 2013 — [conference paper](https://doi.org/10.5194/isprsannals-ii-2-w1-291-2013)
     - authors: D. Xu (student), S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.27; abstract similarity n/a; year +2  (source: GDMC)
  4. "Solutions for 4D cadastre - with a case study on utility networks" — International Journal of Geographical Information Science, 25(7), pp. , 2011 — [journal article](https://doi.org/10.1080/13658816.2010.520272)
     - authors: Fatih Döner, Rod Thompson, Jantien Stoter, Christiaan Lemmen, Hendrik Ploeger, Peter van Oosterom (supervisor: van Oosterom), Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.36; abstract similarity 0.07; year +0  (source: GDMC)
  … and 55 more possible candidates; re-run with --limit/--surname to see them all.
- **Bas Altena (2012)** — Filling the white gap on the map
  1. "Modeling Top of Atmosphere Radiance over Heterogeneous Non-Lambertian Rugged Terrain" — Remote Sensing, 2015 — [journal article](https://doi.org/10.3390/rs70608019)
     - authors: Alijafar Mousivand, Wout Verhoef, Massimo Menenti (supervisor: Menenti), Ben Gorte (supervisor: Gorte)
     - title similarity 0.32; abstract similarity 0.12; year +3  (source: OpenAlex)
  2. "Evaluating MERIS-Based Aquatic Vegetation Mapping in Lake Victoria" — Remote Sensing, 2014 — [journal article](https://doi.org/10.3390/rs6087762)
     - authors: Elijah Cheruiyot, Collins Mito, Massimo Menenti (supervisor: Menenti), Ben Gorte (supervisor: Gorte), Roderik Koenders, Nadia Akdim
     - title similarity 0.33; abstract similarity 0.10; year +2  (source: OpenAlex)
- **Prajnaparamita Bhattacharya (2012)** — Quality assessment and object matching of OpenStreetMap in combination with the 
  1. "Transportation mode-based segmentation and classification of movement trajectories" — International Journal of Geographical Information Science, 27(2), pp. , 2013 — [journal article](https://doi.org/10.1080/13658816.2012.692791)
     - authors: Filip Biljecki, Hugo Ledoux (supervisor: Ledoux), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.34; abstract similarity 0.16; year +1  (source: GDMC)
  2. "Airborne LiDAR Data Filtering Based on Geodesic Transformations of Mathematical Morphology" — Remote Sensing, MDPI AG, 9(11), pp. 1104, 2017 — [journal article](http://www.mdpi.com/2072-4292/9/11/1104)
     - authors: Yong Li, Bin Yong, Peter van Oosterom (supervisor: van Oosterom), Mathias Lemmens (supervisor: Lemmens), Huayi Wu, Liliang Ren, Mingxue Zheng, Jiajun Zhou
     - title similarity 0.33; abstract similarity 0.10; year +5  (source: GDMC)
  3. "Comparing the vario-scale approach with a discrete multi-representation based approach for automated generalisation of topographic data" — Proceedings of the 15th Workshop of the ICA Commission on Generalisati, 2012 — [conference paper](https://www.gdmc.nl/publications/2012/vario-scale_approach_versus_multi-representation_approach.pdf)
     - authors: Martijn Meijers, Jantien Stoter, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.31; abstract similarity 0.22; year +0  (source: GDMC)
  4. "Model driven architecture engineered land administration in conformance with international standards - illustrated with the Hellenic Cadastre" — Open Geospatial Data, Software and Standards, 1(3), 2016 — [journal article](https://doi.org/10.1186/s40965-016-0002-3)
     - authors: Styliani Psomadaki, Efi Dimopoulou, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.37; abstract similarity 0.16; year +4  (source: GDMC)
  … and 35 more possible candidates; re-run with --limit/--surname to see them all.
- **Tom Commandeur (2012)** — Footprint decomposition combined with point cloud segmentation for producing val
  1. "Generation and Dissemination of a National Virtual 3D City and Landscape Model for the Netherlands" — Photogrammetric Engineering & Remote Sensing, 79(2), pp. 147-158, 2013 — [journal article](http://digital.ipcprintservices.com/publication/?i=144145&p=41)
     - authors: Sander Oude Elberink, Jantien Stoter, Hugo Ledoux (supervisor: Ledoux), Tom Commandeur (student)
     - title similarity 0.28; abstract similarity n/a; year +1  (source: GDMC)
  2. "Managing large multidimensional hydrologic datasets: A case study comparing NetCDF and SciDB" — Journal of Hydroinformatics, IWA Publishing, 20(5), pp. 1058-1070, 2018 — [journal article](https://doi.org/10.2166/hydro.2018.136)
     - authors: Haicheng Liu, Peter van Oosterom (supervisor: van Oosterom), Theo Tijssen, Tom Commandeur (student), Wen Wang
     - title similarity 0.21; abstract similarity 0.07; year +6  (source: GDMC)
  3. "Transportation mode-based segmentation and classification of movement trajectories" — International Journal of Geographical Information Science, 27(2), pp. , 2013 — [journal article](https://doi.org/10.1080/13658816.2012.692791)
     - authors: Filip Biljecki, Hugo Ledoux (supervisor: Ledoux), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.40; abstract similarity 0.15; year +1  (source: GDMC)
  4. "Automatic generation of medium-detailed 3D models of buildings based on CAD data" — CGI'15, 32nd annual Conference, Strasbourg, pp. 2, 2015 (abstract)., 2015 — [conference paper](https://www.gdmc.nl/publications/2015/Automatic_generation_medium-detailed_3D_models.pdf)
     - authors: Bernardino Dominguez-Martin, Peter van Oosterom (supervisor: van Oosterom), Francisco Feito-Higueruela, Angel Luis Garcia-Fernandez, Carlos Javier Ogayar-Anguita, Francisco R. Feito, A. García, Carlos J. Ogáyar
     - title similarity 0.36; abstract similarity 0.36; year +3  (source: GDMC)
  … and 80 more possible candidates; re-run with --limit/--surname to see them all.
- **Martine Wijga-Hoefsloot (2012)** — Point Clouds in a Database
  1. "Introduction UDMS 2013" — Chapter in: UDMS Annual 2013 (C. Ellul, S. Zlatanova, M. Rumor, R. Lau, 2013 — [conference paper](https://doi.org/10.1201/b14914-2)
     - authors: C. Ellul, S. Zlatanova (supervisor: Zlatanova), M. Rumor, R. Laurini
     - title similarity 0.38; abstract similarity n/a; year +1  (source: GDMC)
  2. "Indoor Space Subdivision for Indoor Navigation" — Chapter in: Proceedings of the 6th ACM SIGSPATIAL International Worksh, 2014 — [conference paper](https://doi.org/10.1145/2676528.2676529)
     - authors: Marija Krūminaitė, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.35; abstract similarity n/a; year +2  (source: GDMC)
  3. "From point clouds to 3D Isovists in indoor environments" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-4-149-2018)
     - authors: Lucía Díaz-Vilariño, Luis Miguel González-Desantos, Edward Verbree, Gina Michailidou, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.46; abstract similarity n/a; year +6  (source: GDMC)
  4. "Generating Navigation Models from Existing Building Data" — ISPRS Archives Volume XL-4/W4, ISPRS Acquisition and Modelling of Indo, 2013 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-4-w4-19-2013)
     - authors: L. Liu, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.33; abstract similarity n/a; year +1  (source: GDMC)
  … and 4 more possible candidates; re-run with --limit/--surname to see them all.
- **Hoe-Ming Wong (2012)** — Registration of range images using geometric features
  1. "Modeling and observation of heat losses from buildings: The impact of geometric detail on 3D heat flux modeling" — Proceedings EARSeL Conference (Rosa Lasaponara, ed.), Italy, pp. 20, 2013 — [conference paper](https://www.gdmc.nl/publications/2013/Geometric_detail_3D_heat_flux_modeling.pdf)
     - authors: Danbi Lee, Peter Pietrzyk, Sjors Donkers, Vera Liem, Jelte van Oostveen, Sina Montazeri, Roeland Boeters, Jerome Colin, Pierre Kastendeuch, Massimo Menenti (supervisor: Menenti), Ben Gorte (supervisor: Gorte), Edward Verbree
     - title similarity 0.41; abstract similarity n/a; year +1  (source: GDMC)
  2. "Modelling and observation of heat losses from buildings : The impact of geometric detail on 3D heat flux modelling" — Data Archiving and Networked Services (DANS), 2013 — [conference paper](https://openalex.org/W2156116826)
     - authors: D. Lee, Peter Pietrzyk, Serge Donkers, V Liem, J. van Oostveen, Sina Montazeri, R. Boeters, J. Colin, Pierre Kastendeuch, Françoise Nerry, Massimo Menenti (supervisor: Menenti), Ben Gorte (supervisor: Gorte), E. Verbree
     - title similarity 0.41; abstract similarity n/a; year +1  (source: OpenAlex)
  3. "Evaluation of Sentinel-2 Bands over the Spectrum" — ESASP, 2012 — [journal article](https://openalex.org/W3008908672)
     - authors: S. E. Hosseini Aria, Ben Gorte (supervisor: Gorte), Massimo Menenti (supervisor: Menenti)
     - title similarity 0.39; abstract similarity n/a; year +0  (source: OpenAlex)
  4. "Breast Height Diameter Estimation From High-Density Airborne LiDAR Data" — IEEE Geoscience and Remote Sensing Letters, 2013 — [journal article](https://doi.org/10.1109/lgrs.2013.2285471)
     - authors: Alexander Bucksch (supervisor: Bucksch), Roderik Lindenbergh, Muhammad Zulkarnain Abd Rahman, Massimo Menenti (supervisor: Menenti)
     - title similarity 0.37; abstract similarity n/a; year +1  (source: OpenAlex)
  … and 17 more possible candidates; re-run with --limit/--surname to see them all.
- **Eva van der Laan (2014)** — Radio propagation aided indoor localization
  1. "Track-id: Activity Determination based on Wi-Fi Monitoring" — Proceedings of the 13th International Conference on Location Based Ser, 2016 — [conference paper](https://www.gdmc.nl/publications/2016/Track-id_Activity_Determination_Wi-Fi_Monitoring.pdf)
     - authors: S.C. van der Spek (supervisor: van der Spek), E. Verbree, C.W. Quak (supervisor: Quak), IJ.D.G. Groeneveld, R. Sulzer, E. Theocharous, M.S. Tryfona, O.T. Willems, Y. Xu
     - title similarity 0.34; abstract similarity n/a; year +2  (source: GDMC)
  2. "A graph-matching approach to indoor localization using a mobile device and a reference BIM" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2019 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-2-w13-761-2019)
     - authors: Fanny Bot, Pirouz Nourian (supervisor: Nourian), Edward Verbree
     - title similarity 0.47; abstract similarity n/a; year +5  (source: GDMC)
  3. "Towards a high level of semantic harmonisation in the geospatial domain" — Computers, Environment and Urban Systems, 62(March), pp. 233-242, 2017 — [journal article](https://doi.org/10.1016/j.compenvurbsys.2016.12.002)
     - authors: Linda van den Brink, Paul Janssen, Wilko Quak (supervisor: Quak), Jantien Stoter
     - title similarity 0.38; abstract similarity n/a; year +3  (source: GDMC)
  4. "Installed base registration of decentralised solar panels with applications in crisis management" — ISPRS Archives Volume XL-3/W3, ISPRS Geospatial Week 2015 (S. Zlatanov, 2015 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-3-w3-219-2015)
     - authors: R. Aarsen, M. Janssen, M. Ramkisoen, F. Biljecki, C.W. Quak (supervisor: Quak), E. Verbree
     - title similarity 0.32; abstract similarity n/a; year +1  (source: GDMC)
  … and 1 more possible candidates; re-run with --limit/--surname to see them all.
- **Rosann Aarsen (2015)** — Using sensor-data collected by a meet rollator for deriving outdoor accessibilit
  1. "Installed base registration of decentralised solar panels with applications in crisis management" — ISPRS Archives Volume XL-3/W3, ISPRS Geospatial Week 2015 (S. Zlatanov, 2015 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-3-w3-219-2015)
     - authors: R. Aarsen (student), M. Janssen, M. Ramkisoen, F. Biljecki, C.W. Quak, E. Verbree (supervisor: Verbree)
     - title similarity 0.28; abstract similarity n/a; year +0  (source: GDMC)
  2. "Utilizing a Discrete Global Grid System for Handling Point Clouds with Varying Locations, Times, and Levels of Detail" — Cartographica, University of Toronto Press, 51(1), pp. 4-15, 2019 — [journal article](https://doi.org/10.3138/cart.54.1.2018-0009)
     - authors: Neeraj Sirdeshmukh, Edward Verbree (supervisor: Verbree), Peter van Oosterom, Stella Psomadaki, Martin Kodde
     - title similarity 0.35; abstract similarity 0.08; year +4  (source: GDMC)
  3. "Using a linear octree to identify empty space in indoor point clouds for 3D pathfinding" — Proceedings of the 19th AGILE International Conference on Geographic I, 2016 — [conference paper](https://www.gdmc.nl/publications/2016/Linear_octree_identify_empty_space_indoor_point_clouds.pdf)
     - authors: Tom Broersen, Florian W. Fichtner, Erik J. Heeres, Ivo de Liefde, Olivier B.P.M. Rodenberg, Edward Verbree (supervisor: Verbree), Robert Vo&ucirc;te
     - title similarity 0.37; abstract similarity n/a; year +1  (source: GDMC)
  4. "Utilizing 3D Building and 3D Cadastre Geometries for Better Valuation of Existing Real Estate" — Proceedings of the FIG Working Week 2015, Sofia, pp. 18, 2015 — [conference paper](https://www.gdmc.nl/publications/2015/Utilizing_3D_Building_3D_Cadastre_Geometries.pdf)
     - authors: Ümit Işıkdağ, Mike Horhammer, Sisi Zlatanova (supervisor: Zlatanova), Ruud Kathmann, Peter van Oosterom
     - title similarity 0.35; abstract similarity n/a; year +0  (source: GDMC)
  … and 11 more possible candidates; re-run with --limit/--surname to see them all.
- **Godelief Abhilakh Missier (2015)** — Towards a Web application for viewing Spatial Linked Open Data of Rotterdam
  1. "Visualization/dissemination of 3D Cadastre" — Proceedings of the FIG Congress 2018, Istanbul, pp. 30, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/TS05C_cemellini_rod_et_al_9591.pdf)
     - authors: Barbara Cemellini, Thompson Rod, Marian de Vries (supervisor: de Vries), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.41; abstract similarity n/a; year +3  (source: GDMC)
  2. "Implementation of the spatial plan information package for improving ease of doing business in Indonesian cities" — Land Use Policy, Elsevier, 105(105338), pp. 1-17, 2021 — [journal article](https://doi.org/10.1016/j.landusepol.2021.105338)
     - authors: Agung Indrajit, Bastiaan van Loenen (supervisor: van Loenen), Suprajaka, Virgo Eresta Jaya, Hendrik Ploeger, Christiaan Lemmen, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.36; abstract similarity 0.13; year +6  (source: GDMC)
  3. "Multi-Domain Master Spatial Information Management for Open SDI in Indonesian Smart Cities" — Proceedings of the 20th AGILE Conference on Geographic Information Sci, 2017 — [conference paper](https://www.gdmc.nl/publications/2017/SpatialInformationManagementOpenSDIIndonesia.pdf)
     - authors: Agung Indrajit, Bastiaan van Loenen (supervisor: van Loenen), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.35; abstract similarity n/a; year +2  (source: GDMC)
  4. "Designing Open Spatial Information Infrastructure To Support 3D Urban Planning In Jakarta Smart City" — Proceedings of the 6th International Workshop on 3D Cadastres (Peter v, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/3DCadWorkshop2018_18.pdf)
     - authors: Agung Indrajit, Hendrik Ploeger, Bastian van Loenen (supervisor: van Loenen), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.34; abstract similarity n/a; year +3  (source: GDMC)
  … and 82 more possible candidates; re-run with --limit/--surname to see them all.
- **Carl Chen (2015)** — Edge-aware simplification of roof and facade point clouds into a uniformly dense
  1. "From point clouds to 3D Isovists in indoor environments" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-4-149-2018)
     - authors: Lucía Díaz-Vilariño, Luis Miguel González-Desantos, Edward Verbree, Gina Michailidou, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.38; abstract similarity n/a; year +3  (source: GDMC)
  2. "Strategies to evaluate the visibility along an indoor path in a point cloud representation" — Chapter in: ISPRS Annals Volume IV-2/W4, ISPRS Geospatial Week 2017, I, 2017 — [conference paper](https://www.isprs-ann-photogramm-remote-sens-spatial-inf-sci.net/IV-2-W4/311/2017/)
     - authors: N. Grasso, E. Verbree, S. Zlatanova (supervisor: Zlatanova), M. Piras
     - title similarity 0.36; abstract similarity n/a; year +2  (source: GDMC)
  3. "An Approach for Indoor Wayfinding replicating main Principles of an outdoor Navigation System for Cyclists" — ISPRS Archives Volume XL-4/W5, Indoor-Outdoor Seamless Modelling, Mapp, 2015 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-4-w5-29-2015)
     - authors: A. Makri, S. Zlatanova (supervisor: Zlatanova), E. Verbree
     - title similarity 0.34; abstract similarity n/a; year +0  (source: GDMC)
  4. "Real time localisation of assets in hospitals using QUUPA indoor positioning technology" — Chapter in: ISPRS Annals Volume IV-4/W1, First International Conferenc, 2016 — [conference paper](https://doi.org/10.5194/isprs-annals-iv-4-w1-105-2016)
     - authors: M.F.S. van der Ham, S. Zlatanova (supervisor: Zlatanova), E. Verbree, R. Vo&ucirc;te
     - title similarity 0.34; abstract similarity n/a; year +1  (source: GDMC)
  … and 3 more possible candidates; re-run with --limit/--surname to see them all.
- **Damien Mulder (2015)** — Automatic repair of geometrically invalid 3D City Building models using a voxel-
  1. "Construction of 3D Volumetric Objects for a 3D Cadastral System" — Transactions In GIS, 19(5), pp. 758-779, 2015 — [journal article](https://doi.org/10.1111/tgis.12129)
     - authors: Shen Ying, Renzhong Guo, Lin Li, Peter Van Oosterom, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.32; abstract similarity n/a; year +0  (source: GDMC)
  2. "A graph-matching approach to indoor localization using a mobile device and a reference BIM" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2019 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-2-w13-761-2019)
     - authors: Fanny Bot, Pirouz Nourian (supervisor: Nourian), Edward Verbree
     - title similarity 0.36; abstract similarity n/a; year +4  (source: GDMC)
- **Myron Ramkisoen (2015)** — Solid CAD Geometries in a Spatial DBMS - An Application in the Petrochemical Ind
  1. "Installed base registration of decentralised solar panels with applications in crisis management" — ISPRS Archives Volume XL-3/W3, ISPRS Geospatial Week 2015 (S. Zlatanov, 2015 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-3-w3-219-2015)
     - authors: R. Aarsen, M. Janssen, M. Ramkisoen (student), F. Biljecki, C.W. Quak, E. Verbree
     - title similarity 0.33; abstract similarity n/a; year +0  (source: GDMC)
- **Hester Willems (2015)** — The localisation of freight wagons on marshalling yards
  1. "Track-id: Activity Determination based on Wi-Fi Monitoring" — Proceedings of the 13th International Conference on Location Based Ser, 2016 — [conference paper](https://www.gdmc.nl/publications/2016/Track-id_Activity_Determination_Wi-Fi_Monitoring.pdf)
     - authors: S.C. van der Spek (supervisor: van der Spek), E. Verbree (supervisor: Verbree), C.W. Quak (supervisor: Quak), IJ.D.G. Groeneveld, R. Sulzer, E. Theocharous, M.S. Tryfona, O.T. Willems, Y. Xu
     - title similarity 0.35; abstract similarity n/a; year +1  (source: GDMC)
  2. "Installed base registration of decentralised solar panels with applications in crisis management" — ISPRS Archives Volume XL-3/W3, ISPRS Geospatial Week 2015 (S. Zlatanov, 2015 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-3-w3-219-2015)
     - authors: R. Aarsen, M. Janssen, M. Ramkisoen, F. Biljecki, C.W. Quak (supervisor: Quak), E. Verbree (supervisor: Verbree)
     - title similarity 0.38; abstract similarity n/a; year +0  (source: GDMC)
  3. "Assessing people travel behavior using GPS and open data to validate neighbourhoods characteristics" — Proceedings of the 19th AGILE International Conference on Geographic I, 2016 — [conference paper](https://www.gdmc.nl/publications/2016/Assessing_people_travel_behavior_GPS_open_data.pdf)
     - authors: Matilde Oliveti, Stefan van der Spek (supervisor: van der Spek), Wilko Quak (supervisor: Quak)
     - title similarity 0.31; abstract similarity n/a; year +1  (source: GDMC)
  4. "Real time localisation of assets in hospitals using QUUPA indoor positioning technology" — Chapter in: ISPRS Annals Volume IV-4/W1, First International Conferenc, 2016 — [conference paper](https://doi.org/10.5194/isprs-annals-iv-4-w1-105-2016)
     - authors: M.F.S. van der Ham, S. Zlatanova, E. Verbree (supervisor: Verbree), R. Vo&ucirc;te
     - title similarity 0.42; abstract similarity n/a; year +1  (source: GDMC)
  … and 10 more possible candidates; re-run with --limit/--surname to see them all.
- **Dimitrios Zervakis (2015)** — Combining a Physics-based Model and Spatial Interpolation of Scarce Bed Topograp
  1. "Mathematical morphology directly applied to point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 168, , 2020 — [journal article](https://doi.org/10.1016/j.isprsjprs.2020.08.011)
     - authors: Jes&uacute;s Balado, Peter van Oosterom (supervisor: van Oosterom), Luc&iacute;a D&iacute;az-Vilari&ntilde;o, Martijn Meijers (supervisor: Meijers), Lucía Díaz-Vilariño
     - title similarity 0.34; abstract similarity 0.11; year +5  (source: GDMC)
  2. "Web-based dissemination of continuously generalized Space-Scale Cube data for smooth user interaction" — International Journal of Cartography, Informa UK Limited, 6(1), pp. 15, 2020 — [journal article](https://doi.org/10.1080/23729333.2019.1705144)
     - authors: Martijn Meijers (supervisor: Meijers), Peter van Oosterom (supervisor: van Oosterom), Mattijs Driel, Radan &Scaron;uba, Radan Šuba
     - title similarity 0.35; abstract similarity 0.08; year +5  (source: GDMC)
  3. "HistSFC: Optimization for nD massive spatial points querying" — International Journal of Database Management Systems (IJDMS), Academy , 2020 — [journal article](https://aircconline.com/abstract/ijdms/v12n3/12320ijdms02.html)
     - authors: Haicheng Liu, Peter van Oosterom (supervisor: van Oosterom), Martijn Meijers (supervisor: Meijers), Xuefeng Guan, Edward Verbree, Mike Horhammer
     - title similarity 0.34; abstract similarity 0.07; year +5  (source: GDMC)
  4. "Using a generic spatial access method for caching and efficient retrieval of vario-scale data in a server-client architecture" — Proceedings of the 20th AGILE Conference on Geographic Information Sci, 2017 — [conference paper](https://www.gdmc.nl/publications/2017/SpatialAccessMethodVarioScaleServer.pdf)
     - authors: Adrie Rovers, Martijn Meijers (supervisor: Meijers), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.37; abstract similarity n/a; year +2  (source: GDMC)
  … and 61 more possible candidates; re-run with --limit/--surname to see them all.
- **Ivo de Liefde (2016)** — Exploring the Use of the Semantic Web for discovering, retrieving and processing
  1. "Using a generic spatial access method for caching and efficient retrieval of vario-scale data in a server-client architecture" — Proceedings of the 20th AGILE Conference on Geographic Information Sci, 2017 — [conference paper](https://www.gdmc.nl/publications/2017/SpatialAccessMethodVarioScaleServer.pdf)
     - authors: Adrie Rovers, Martijn Meijers (supervisor: Meijers), Peter van Oosterom
     - title similarity 0.36; abstract similarity n/a; year +1  (source: GDMC)
  2. "Clustering and indexing historic vessel movement data with space filling curves" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-4-417-2018)
     - authors: Martijn Meijers (supervisor: Meijers), Peter van Oosterom
     - title similarity 0.33; abstract similarity n/a; year +2  (source: GDMC)
  3. "Web-based dissemination of continuously generalized Space-Scale Cube data for smooth user interaction" — International Journal of Cartography, Informa UK Limited, 6(1), pp. 15, 2020 — [journal article](https://doi.org/10.1080/23729333.2019.1705144)
     - authors: Martijn Meijers (supervisor: Meijers), Peter van Oosterom, Mattijs Driel, Radan &Scaron;uba
     - title similarity 0.37; abstract similarity n/a; year +4  (source: GDMC)
  4. "Developing an LADM Compliant Dissemination and Visualization System for 3D Spatial Units" — Proceedings of the 7th Land Administration Domain Model Workshop, Zagr, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/07-26_LADM_2018.pdf)
     - authors: Rod Thompson, Peter van Oosterom, Barbara Cemellini, Marian de Vries (supervisor: de Vries)
     - title similarity 0.31; abstract similarity n/a; year +2  (source: GDMC)
  … and 4 more possible candidates; re-run with --limit/--surname to see them all.
- **Irene de Vreede (2016)** — Managing Historic Automatic Identification System data by using a proper Databas
  1. "INTERLIS Language for Modelling Legal 3D Spaces and Physical 3D Objects by Including Formalized Implementable Constraints and Meaningful Code Lists" — ISPRS International Journal of Geo-Information, MDPI AG, 6(10), pp. 31, 2017 — [journal article](https://doi.org/10.3390/ijgi6100319)
     - authors: Eftychia Kalogianni, Efi Dimopoulou, Wilko Quak (supervisor: Quak), Michael Germann, Lorenz Jenni, Peter van Oosterom (supervisor: van Oosterom), Ruba Jaljolie, Sagi Dalyot
     - title similarity 0.31; abstract similarity 0.07; year +1  (source: GDMC)
  2. "Formalisation of code lists and their values – The case of ISO 19152 Land Administration Domain Model" — Proceedings of the 10th FIG Land Administration Domain Model Workshop , 2022 — [conference paper](https://www.gdmc.nl/publications/2022/LADM2022_paper_CodeListValues.pdf)
     - authors: Abdullah Kara, Alexandra Rowland, Peter van Oosterom (supervisor: van Oosterom), Erik Stubkjær, Volkan Çağdaş, Erwin Folmer, Christiaan Lemmen, Wilko Quak (supervisor: Quak), Laura Meggiolaro
     - title similarity 0.31; abstract similarity n/a; year +6  (source: GDMC)
  3. "Managing large multidimensional hydrologic datasets: A case study comparing NetCDF and SciDB" — Journal of Hydroinformatics, IWA Publishing, 20(5), pp. 1058-1070, 2018 — [journal article](https://doi.org/10.2166/hydro.2018.136)
     - authors: Haicheng Liu, Peter van Oosterom (supervisor: van Oosterom), Theo Tijssen, Tom Commandeur, Wen Wang
     - title similarity 0.38; abstract similarity 0.27; year +2  (source: GDMC)
  4. "Managing Large Multidimensional Array Hydrologic Datasets: A Case Study Comparing NetCDF and SciDB" — Procedia Engineering, 154, pp. 207-214, 2016 — [journal article](https://doi.org/10.1016/j.proeng.2016.07.449)
     - authors: Haicheng Liu, Peter van Oosterom (supervisor: van Oosterom), Chengfang Hu, Wen Wang
     - title similarity 0.36; abstract similarity 0.25; year +0  (source: GDMC)
  … and 52 more possible candidates; re-run with --limit/--surname to see them all.
- **Kees Jonker (2016)** — Automatic generation of raster-based height data for the Netherlands based on th
  1. "Automatic Building Outline Extraction from ALS Point Clouds by Ordered Points Aided Hough Transform" — Remote Sensing, 2019 — [journal article](https://doi.org/10.3390/rs11141727)
     - authors: Elyta Widyaningrum, Ben Gorte (supervisor: Gorte), Roderik Lindenbergh
     - title similarity 0.43; abstract similarity 0.23; year +3  (source: OpenAlex)
  2. "Automatic Shadow Detection in Urban Very-High-Resolution Images Using Existing 3D Models for Free Training" — Remote Sensing, 2019 — [journal article](https://doi.org/10.3390/rs11010072)
     - authors: Kaixuan Zhou, Roderik Lindenbergh, Ben Gorte (supervisor: Gorte)
     - title similarity 0.41; abstract similarity 0.10; year +3  (source: OpenAlex)
  3. "RASTERIZATION AND VOXELIZATION OF TWO- AND THREE-DIMENSIONAL SPACE PARTITIONINGS" — The international archives of the photogrammetry, remote sensing and, 2016 — [journal article](https://doi.org/10.5194/isprs-archives-xli-b4-283-2016)
     - authors: Ben Gorte (supervisor: Gorte), Sisi Zlatanova
     - title similarity 0.33; abstract similarity 0.08; year +0  (source: OpenAlex)
  4. "Unsupervised dimensionality reduction of hyperspectral images using representations of reflectance spectra" — International Journal of Remote Sensing, 2020 — [journal article](https://doi.org/10.1080/01431161.2020.1766146)
     - authors: S. Enayat Hosseini Aria, Massimo Menenti, Ben G. H. Gorte (supervisor: Gorte), Saeid Homayouni
     - title similarity 0.32; abstract similarity 0.11; year +4  (source: OpenAlex)
- **Matthijs Kastelijns (2016)** — Making sense of standards An evaluation and harmonisation of standards in the Se
  1. "Towards a high level of semantic harmonisation in the geospatial domain" — Computers, Environment and Urban Systems, 62(March), pp. 233-242, 2017 — [journal article](https://doi.org/10.1016/j.compenvurbsys.2016.12.002)
     - authors: Linda van den Brink, Paul Janssen, Wilko Quak (supervisor: Quak), Jantien Stoter
     - title similarity 0.46; abstract similarity n/a; year +1  (source: GDMC)
  2. "Track-id: Activity Determination based on Wi-Fi Monitoring" — Proceedings of the 13th International Conference on Location Based Ser, 2016 — [conference paper](https://www.gdmc.nl/publications/2016/Track-id_Activity_Determination_Wi-Fi_Monitoring.pdf)
     - authors: S.C. van der Spek, E. Verbree, C.W. Quak (supervisor: Quak), IJ.D.G. Groeneveld, R. Sulzer, E. Theocharous, M.S. Tryfona, O.T. Willems, Y. Xu
     - title similarity 0.37; abstract similarity n/a; year +0  (source: GDMC)
  3. "Developing a spatial planning information package in ISO 19152 land administration domain model" — Land Use Policy, Elsevier, 98(104111), pp. 1-12, 2020 — [journal article](https://doi.org/10.1016/j.landusepol.2019.104111)
     - authors: Agung Indrajit, Bastiaan van Loenen (supervisor: van Loenen), Hendrik Ploeger, Peter van Oosterom
     - title similarity 0.39; abstract similarity n/a; year +4  (source: GDMC)
  4. "Assessing people travel behavior using GPS and open data to validate neighbourhoods characteristics" — Proceedings of the 19th AGILE International Conference on Geographic I, 2016 — [conference paper](https://www.gdmc.nl/publications/2016/Assessing_people_travel_behavior_GPS_open_data.pdf)
     - authors: Matilde Oliveti, Stefan van der Spek, Wilko Quak (supervisor: Quak)
     - title similarity 0.35; abstract similarity n/a; year +0  (source: GDMC)
  … and 2 more possible candidates; re-run with --limit/--surname to see them all.
- **Marco Lam (2016)** — Creating the medial axis transform for billions of lidar points using a memory e
  1. "Robust approximation of the Medial Axis Transform of LiDAR point clouds as a tool for visualisation" — Computers &amp; Geosciences, 2016 — [journal article](https://doi.org/10.1016/j.cageo.2016.02.019)
     - authors: Ravi Peters (supervisor: Peters), Hugo Ledoux
     - title similarity 0.53; abstract similarity n/a; year +0  (source: Crossref)
  2. "Building outline extraction from ALS point clouds using medial axis transform descriptors" — Pattern Recognition, 2020 — [journal article](https://doi.org/10.1016/j.patcog.2020.107447)
     - authors: Elyta Widyaningrum, Ravi Y. Peters (supervisor: Peters), Roderik C. Lindenbergh
     - title similarity 0.34; abstract similarity n/a; year +4  (source: Crossref)
- **Tim Nagelkerke (2016)** — Navigation to a human in motion by using points of interest
  1. "Real time localisation of assets in hospitals using QUUPA indoor positioning technology" — Chapter in: ISPRS Annals Volume IV-4/W1, First International Conferenc, 2016 — [conference paper](https://doi.org/10.5194/isprs-annals-iv-4-w1-105-2016)
     - authors: M.F.S. van der Ham, S. Zlatanova (supervisor: Zlatanova), E. Verbree, R. Vo&ucirc;te
     - title similarity 0.37; abstract similarity n/a; year +0  (source: GDMC)
  2. "Supporting Indoor Navigation Using Access Rights to Spaces Based on Combined Use of IndoorGML and LADM Models" — ISPRS International Journal of Geo-Information, MDPI AG, 6(12), pp. 38, 2017 — [journal article](https://doi.org/10.3390/ijgi6120384)
     - authors: Abdullah Alattas, Sisi Zlatanova (supervisor: Zlatanova), Peter van Oosterom, Efstathia Chatzinikolaou, Christiaan Lemmen, Ki-Joune Li
     - title similarity 0.37; abstract similarity n/a; year +1  (source: GDMC)
  3. "Indoor navigation supported by the Industry Foundation Classes (IFC): A survey" — Automation in Construction, Elsevier, 121(103436), pp. 1-20, 2021 — [journal article](https://doi.org/10.1016/j.autcon.2020.103436)
     - authors: Liu Liu, Bofeng Li, Sisi Zlatanova (supervisor: Zlatanova), Peter van Oosterom
     - title similarity 0.40; abstract similarity n/a; year +5  (source: GDMC)
  4. "Indoor Routing on Logical Network Using Space Semantics" — ISPRS International Journal of Geo-Information, MDPI AG, 8(3), pp. 126, 2019 — [journal article](https://doi.org/10.3390/ijgi8030126)
     - authors: Liu Liu, Sisi Zlatanova (supervisor: Zlatanova), Bofeng Li, Peter van Oosterom, Jack Barton
     - title similarity 0.33; abstract similarity n/a; year +3  (source: GDMC)
  … and 4 more possible candidates; re-run with --limit/--surname to see them all.
- **Jade Haayen (2017)** — Towards interoperable standards for 1D time series data within the water sector
  1. "Working with Open BIM Standards to Source Legal Spaces for a 3D Cadastre" — ISPRS International Journal of Geo-Information, MDPI AG, 6(11), pp. 19, 2017 — [journal article](https://doi.org/10.3390/ijgi6110351)
     - authors: Jennifer Oldfield, Peter van Oosterom (supervisor: van Oosterom), Jakob Beetz, Thomas F. Krijnen
     - title similarity 0.41; abstract similarity 0.40; year +0  (source: GDMC)
  2. "Towards the Netherlands LADM Valuation Information Model Country Profile" — Proceedings of the FIG Working Week 2019, Hanoi, Vietnam, pp. 31, 2019 — [conference paper](http://www.fig.net/resources/proceedings/fig_proceedings/fig2019/papers/ts08i/TS08I_kara_kathmann_et_al_10066.pdf)
     - authors: Abdullah Kara, Ruud Kathmann, Peter van Oosterom (supervisor: van Oosterom), Christiaan Lemmen, Ümit Işıkdağ
     - title similarity 0.41; abstract similarity 0.27; year +2  (source: GDMC)
  3. "3D Land Administration: A Review and a Future Vision in the Context of the Spatial Development Lifecycle" — ISPRS International Journal of Geo-Information, MDPI AG, 9(2), pp. 25, 2020 — [journal article](https://doi.org/10.3390/ijgi9020107)
     - authors: Eftychia Kalogianni, Peter van Oosterom (supervisor: van Oosterom), Efi Dimopoulou, Christiaan Lemmen
     - title similarity 0.34; abstract similarity 0.24; year +3  (source: GDMC)
  4. "The Foundation of Edition II of the Land Administration Domain Model" — Proceedings of the FIG Working Week 2021, Online, pp. 17, 2021 — [conference paper](https://fig.net/resources/proceedings/fig_proceedings/fig2021/papers/ws_03.4/WS_03.4_abdullah_indrajit_et_al_11163.pdf)
     - authors: Christiaan Lemmen, Alattas Abdullah, Agung Indrajit, Kalogianni Eftychia, Abdullah Kara, Peter van Oosterom (supervisor: van Oosterom), Peter Oukes, Abdullah Alattas, Eftychia Kalogianni
     - title similarity 0.33; abstract similarity 0.28; year +4  (source: GDMC)
  … and 52 more possible candidates; re-run with --limit/--surname to see them all.
- **Dimitrios Kyritsis (2017)** — The identification of road modality and occupancy patterns by Wi-Fi monitoring s
  1. "Using the combined LADM-IndoorGML model to support building evacuation" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-4-11-2018)
     - authors: Abdullah Alattas, Peter van Oosterom, Sisi Zlatanova (supervisor: Zlatanova), Dick Hoeneveld, Edward Verbree (supervisor: Verbree)
     - title similarity 0.37; abstract similarity n/a; year +1  (source: GDMC)
  2. "HistSFC: Optimization for nD massive spatial points querying" — International Journal of Database Management Systems (IJDMS), Academy , 2020 — [journal article](https://aircconline.com/abstract/ijdms/v12n3/12320ijdms02.html)
     - authors: Haicheng Liu, Peter van Oosterom, Martijn Meijers, Xuefeng Guan, Edward Verbree (supervisor: Verbree), Mike Horhammer
     - title similarity 0.31; abstract similarity 0.06; year +3  (source: GDMC)
  3. "Placement optimization of positioning nodes: Maximizing the distinction of indoor zones" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2019 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-2-w13-909-2019)
     - authors: Dimitris Xenakis, Martijn Meijers, Edward Verbree (supervisor: Verbree)
     - title similarity 0.37; abstract similarity n/a; year +2  (source: GDMC)
  4. "Automatic detection and characterization of ground occlusions in urban point clouds from Mobile Laser Scanning data" — Chapter in: ISPRS Annals of Photogrammetry, Remote Sensing and Spatial, 2020 — [conference paper](https://doi.org/10.5194/isprs-annals-vi-4-w1-2020-13-2020)
     - authors: Jesús Balado Frías, Elena González, Edward Verbree (supervisor: Verbree), Lucía Díaz Vilariño, Henrique Lorenzo
     - title similarity 0.33; abstract similarity n/a; year +3  (source: GDMC)
  … and 8 more possible candidates; re-run with --limit/--surname to see them all.
- **Birgit Ligtvoet (2017)** — Crowdsensing as a tool for up-to-date road asset distress detection
  1. "Virtual sensors - Synthesizing dynamic crowdsensing data into information on static instances" — Adjunct Proceedings of the 14th International Conference on Location B, 2018 — [conference paper](https://www.research-collection.ethz.ch/handle/20.500.11850/225584)
     - authors: Birgit R. Ligtvoet (student), Edward Verbree (supervisor: Verbree), Ben G.H. Gorte, Ligtvoet, Birgit R., Verbree, Edward, Gorte, Ben G.H.
     - title similarity 0.34; abstract similarity 0.31; year +1  (source: GDMC)
  2. "Inferring roof semantics for more accurate solar potential assessment" — Chapter in: The International Archives of the Photogrammetry, Remote S, 2021 — [conference paper](https://doi.org/10.5194/isprs-archives-xlvi-4-w4-2021-33-2021)
     - authors: I. Apra, C. Bachert, C. C&aacute;ceres Tocora, &Ouml;. Tufan, O. Vesel&yacute;, E. Verbree (supervisor: Verbree)
     - title similarity 0.41; abstract similarity n/a; year +4  (source: GDMC)
  3. "Visualizing of the below-ground water network infrastructure" — Proceedings of the 26th AGILE Conference on Geographic Information Sci, 2023 — [conference paper](https://doi.org/10.5194/agile-giss-4-47-2023)
     - authors: Sibe van den Beukel, Edward Verbree (supervisor: Verbree), Peter van Oosterom
     - title similarity 0.39; abstract similarity 0.10; year +6  (source: GDMC)
  4. "Point Cloud Based Visibility Analysis: first experimental results" — Proceedings of the 20th AGILE Conference on Geographic Information Sci, 2017 — [conference paper](https://www.gdmc.nl/publications/2017/PointCloudBasedVisibilityAnalysis.pdf)
     - authors: Guanting Zhang, Peter van Oosterom, Edward Verbree (supervisor: Verbree)
     - title similarity 0.35; abstract similarity n/a; year +0  (source: GDMC)
  … and 8 more possible candidates; re-run with --limit/--surname to see them all.
- **Yueqian Xu (2017)** — Construction of a Responsive Web Service for Smooth Rendering of Large SSC Datas
  1. "Paralleling generalization operations to support smooth zooming: case study of merging area objects" — Proceedings of 23rd Workshop on Generalisation and Multiple Representa, 2020 — [conference paper](https://www.gdmc.nl/publications/2020/ICAgen2020_paper_5.pdf)
     - authors: Dongliang Peng, Martijn Meijers (supervisor: Meijers), Peter van Oosterom
     - title similarity 0.39; abstract similarity n/a; year +3  (source: GDMC)
  2. "Towards a relational database Space Filling Curve (SFC) interface specification for managing nD-PointClouds" — Geoinformationssysteme 2019, Beiträge zur 6. Münchner GI-Runde (Thomas, 2019 — [conference paper](https://www.gdmc.nl/publications/2019/DBMS-nD-PC-GI-Runde2019.pdf)
     - authors: Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Edward Verbree, Haicheng Liu, Theo Tijssen
     - title similarity 0.32; abstract similarity n/a; year +2  (source: GDMC)
  3. "An Optimized SFC Approach for nD Window Querying on Point Clouds" — Chapter in: ISPRS Annals of Photogrammetry, Remote Sensing and Spatial, 2020 — [conference paper](https://doi.org/10.5194/isprs-annals-vi-4-w1-2020-119-2020)
     - authors: Haicheng Liu, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Edward Verbree
     - title similarity 0.31; abstract similarity n/a; year +3  (source: GDMC)
  4. "Generalizing Simultaneously to Support Smooth Zooming: Case Study of Merging Area Objects" — Journal of Geovisualization and Spatial Analysis, Springer, 7(12), pp., 2023 — [journal article](https://doi.org/10.1007/s41651-022-00109-x)
     - authors: Dongliang Peng, Martijn Meijers (supervisor: Meijers), Peter van Oosterom
     - title similarity 0.34; abstract similarity n/a; year +6  (source: GDMC)
- **Rob Braggaar (2018)** — Wi-Fi network-based indoor localisation - The case of the TU Delft campus
  1. "Using a Dynamic Sensor Network to Obtain Spatiotemporal Data in an Urban Environment" — Adjunct Proceedings of the 14th International Conference on Location B, 2018 — [conference paper](https://www.research-collection.ethz.ch/handle/20.500.11850/225582)
     - authors: Lilia Angelova, Puck Flikweert, Panagiotis Karydakis, Daniël Kersbergen, Roos Teeuwen, Kotryna Valečkaitė, Edward Verbree (supervisor: Verbree), Martijn Meijers, Stefan van der Spek (supervisor: van der Spek), Angelova, Lilia, Flikweert, Puck, Karydakis, Panagiotis, Kersbergen, Daniël, Teeuwen, Roos, Valečkaitė, Kotryna, Verbree, Edward, Meijers, Martijn, van der Spek, Stefan
     - title similarity 0.31; abstract similarity 0.16; year +0  (source: GDMC)
  2. "Indoor localisation and location tracking in indoor facilities based on LiDAR point clouds and images of the ceilings" — Proceedings of the 26th AGILE Conference on Geographic Information Sci, 2023 — [conference paper](https://doi.org/10.5194/agile-giss-4-4-2023)
     - authors: Ioannis Dardavesis, Edward Verbree (supervisor: Verbree), Azarakhsh Rafiee
     - title similarity 0.39; abstract similarity 0.42; year +5  (source: GDMC)
  3. "Indoor localisation through Isovist fingerprinting from point clouds and floor plans" — Journal of Location Based Services, 2024 — [journal article](https://doi.org/10.1080/17489725.2024.2320642)
     - authors: Georgios Triantafyllou, Edward Verbree (supervisor: Verbree), Azarakhsh Rafiee
     - title similarity 0.42; abstract similarity 0.23; year +6  (source: OpenAlex)
  4. "Direct Use of Indoor Point Clouds for Path Planning and Navigation Exploration in Emergency Situations" — Chapter in: The International Archives of the Photogrammetry, Remote S, 2024 — [conference paper](https://isprs-archives.copernicus.org/articles/XLVIII-4-W11-2024/175/2024/)
     - authors: Algan Yasar, Robert Vo&ucirc;te, Edward Verbree (supervisor: Verbree), Robert Voûte
     - title similarity 0.39; abstract similarity 0.26; year +6  (source: GDMC)
  … and 14 more possible candidates; re-run with --limit/--surname to see them all.
- **Panagiotis Karydakis (2018)** — Simplification & visualization of BIM models through Hololens
  1. "Using a Dynamic Sensor Network to Obtain Spatiotemporal Data in an Urban Environment" — Adjunct Proceedings of the 14th International Conference on Location B, 2018 — [conference paper](https://www.research-collection.ethz.ch/handle/20.500.11850/225582)
     - authors: Lilia Angelova, Puck Flikweert, Panagiotis Karydakis (student), Daniël Kersbergen, Roos Teeuwen, Kotryna Valečkaitė, Edward Verbree, Martijn Meijers, Stefan van der Spek
     - title similarity 0.27; abstract similarity n/a; year +0  (source: GDMC)
- **Manuela Manolova (2018)** — Integration of 3D BIM Models in a Web GIS for Life Cycle Asset Management
  1. "Designing Open Spatial Information Infrastructure To Support 3D Urban Planning In Jakarta Smart City" — Proceedings of the 6th International Workshop on 3D Cadastres (Peter v, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/3DCadWorkshop2018_18.pdf)
     - authors: Agung Indrajit, Hendrik Ploeger (supervisor: Ploeger), Bastian van Loenen, Peter van Oosterom
     - title similarity 0.33; abstract similarity n/a; year +0  (source: GDMC)
  2. "Visualization/dissemination of 3D Cadastre" — Proceedings of the FIG Congress 2018, Istanbul, pp. 30, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/TS05C_cemellini_rod_et_al_9591.pdf)
     - authors: Barbara Cemellini, Thompson Rod, Marian de Vries (supervisor: de Vries), Peter van Oosterom
     - title similarity 0.31; abstract similarity n/a; year +0  (source: GDMC)
  3. "Implementation of the spatial plan information package for improving ease of doing business in Indonesian cities" — Land Use Policy, Elsevier, 105(105338), pp. 1-17, 2021 — [journal article](https://doi.org/10.1016/j.landusepol.2021.105338)
     - authors: Agung Indrajit, Bastiaan van Loenen, Suprajaka, Virgo Eresta Jaya, Hendrik Ploeger (supervisor: Ploeger), Christiaan Lemmen, Peter van Oosterom
     - title similarity 0.31; abstract similarity n/a; year +3  (source: GDMC)
  4. "3D Land Administration: current status (2022) and expectation for the near future (2026) – initial analysis" — Proceedings of the FIG Working Week 2023, Orlando, Florida, USA, pp. 1, 2023 — [conference paper](https://www.gdmc.nl/publications/2023/FIGWW2023_3D_LAS_Questionnaire.pdf)
     - authors: Eftychia Kalogianni, Peter van Oosterom, Christiaan Lemmen, Hendrik Ploeger (supervisor: Ploeger), Rodney Thompson, Sudarshan Karki, Anna Shnaidman, Alias Abdul Rahman
     - title similarity 0.33; abstract similarity n/a; year +5  (source: GDMC)
- **Giorgos Dimopoulos (2019)** — From static to dynamic visualization of the sea surface height on a web GIS appl
  1. "Video Map - visual stories of change" — 2019 (Abstract from AGU Fall Meeting 2019, San Francisco, United State, 2019 — [conference paper](https://agu.confex.com/agu/fm19/meetingapp.cgi/Paper/613860)
     - authors: Fedor Baart (supervisor: Baart), Gennadii Donchyts, Giorgos Dimopoulos (student), Juliette Cortesarevalo, P.J.M. van Oosterom (supervisor: van Oosterom), Martijn Meijers, George Dimopoulos
     - title similarity 0.27; abstract similarity n/a; year +0  (source: GDMC)
  2. "Video Map - Generating and visualizing video map tiles from EO data" — 2019 (Abstract from AGU Fall Meeting 2019, San Francisco, United State, 2019 — [conference paper](https://agu.confex.com/agu/fm19/meetingapp.cgi/Paper/617191)
     - authors: Gennadii Donchyts, Fedor Baart (supervisor: Baart), Giorgos Dimopoulos (student), Peter van Oosterom (supervisor: van Oosterom), Christine Rogers, Cindy van de Vries, Martijn Meijers, George Dimopoulos
     - title similarity 0.27; abstract similarity n/a; year +0  (source: GDMC)
  3. "The LADM Valuation Information Model and its application to the Turkey case" — Land Use Policy, Elsevier, 104(105307), pp. 1-15, 2021 — [journal article](https://doi.org/10.1016/j.landusepol.2021.105307)
     - authors: Abdullah Kara, Volkan Çağdaş, Umit Isikdag, Peter van Oosterom (supervisor: van Oosterom), Christiaan Lemmen, Erik Stubkjaer
     - title similarity 0.41; abstract similarity 0.17; year +2  (source: GDMC)
  4. "The Foundation of Edition II of the Land Administration Domain Model" — Proceedings of the FIG Working Week 2021, Online, pp. 17, 2021 — [conference paper](https://fig.net/resources/proceedings/fig_proceedings/fig2021/papers/ws_03.4/WS_03.4_abdullah_indrajit_et_al_11163.pdf)
     - authors: Christiaan Lemmen, Alattas Abdullah, Agung Indrajit, Kalogianni Eftychia, Abdullah Kara, Peter van Oosterom (supervisor: van Oosterom), Peter Oukes, Abdullah Alattas, Eftychia Kalogianni
     - title similarity 0.37; abstract similarity 0.19; year +2  (source: GDMC)
  … and 46 more possible candidates; re-run with --limit/--surname to see them all.
- **Pim Klaassen (2019)** — Using neural networks to model the behavior in vessel trajectories
  1. "Paralleling generalization operations to support smooth zooming: case study of merging area objects" — Proceedings of 23rd Workshop on Generalisation and Multiple Representa, 2020 — [conference paper](https://www.gdmc.nl/publications/2020/ICAgen2020_paper_5.pdf)
     - authors: Dongliang Peng, Martijn Meijers (supervisor: Meijers), Peter van Oosterom
     - title similarity 0.45; abstract similarity n/a; year +1  (source: GDMC)
  2. "Web-based dissemination of continuously generalized Space-Scale Cube data for smooth user interaction" — International Journal of Cartography, Informa UK Limited, 6(1), pp. 15, 2020 — [journal article](https://doi.org/10.1080/23729333.2019.1705144)
     - authors: Martijn Meijers (supervisor: Meijers), Peter van Oosterom, Mattijs Driel, Radan &Scaron;uba
     - title similarity 0.37; abstract similarity n/a; year +1  (source: GDMC)
  3. "A Comparative Study of Point Clouds Semantic Segmentation using three different Neural Networks on the Railway Station Dataset" — Chapter in: The International Archives of the Photogrammetry, Remote S, 2021 — [conference paper](https://doi.org/10.5194/isprs-archives-xliii-b3-2021-223-2021)
     - authors: Y. A. Lumban-Gaol, Z. Chen, M. Smit, X. Li, M. A. Erbaşu, E. Verbree, J. Balado, M. Meijers (supervisor: Meijers), N. van der Vaart
     - title similarity 0.36; abstract similarity n/a; year +2  (source: GDMC)
  4. "Generalizing Simultaneously to Support Smooth Zooming: Case Study of Merging Area Objects" — Journal of Geovisualization and Spatial Analysis, Springer, 7(12), pp., 2023 — [journal article](https://doi.org/10.1007/s41651-022-00109-x)
     - authors: Dongliang Peng, Martijn Meijers (supervisor: Meijers), Peter van Oosterom
     - title similarity 0.37; abstract similarity n/a; year +4  (source: GDMC)
  … and 3 more possible candidates; re-run with --limit/--surname to see them all.
- **Ioanna Micha (2019)** — Design and Evaluate the OGC Web Services Architecture of a Geohazard analysis to
  1. "Driving quality in delirium care through a patient-centered monitoring system in palliative care: Protocol for the two-staged exploratory sequential mixed methods MODEL-PC study" — Delirium, 2024 — [journal article](https://doi.org/10.56392/001c.94808)
     - authors: Nameer van Oosterom (supervisor: van Oosterom), Meera R. Agar, Grace Walpole, Penelope Casey, Paula Moffat, Keiron Bradley, Angus Cook, Claire Johnson, Richard Chye, Jacqueline Oehme, Maria Senatore, Claudia Virdun, Mark Pearson, Imogen Featherstone, Peter G. Lawlor, Shirley H. Bush, Barb Daveson, Sabina Clapham, Kimberley Campbell, Annmarie Hosie
     - title similarity 0.33; abstract similarity 0.16; year +5  (source: OpenAlex)
  2. "Evaluation of the dual half-edge data structure for implementation of a vario-scale model" — Chapter in: The International Archives of the Photogrammetry, Remote S, 2024 — [conference paper](https://isprs-archives.copernicus.org/articles/XLVIII-4-W11-2024/25/2024/)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.39; abstract similarity 0.10; year +5  (source: GDMC)
  3. "Design of the new structure and capabilities of LADM edition II including 3D aspects" — Land Use Policy, Elsevier BV, 137, pp. 107003, 2024 — [journal article](https://www.sciencedirect.com/science/article/pii/S0264837723004696)
     - authors: Abdullah Kara, Christiaan Lemmen, Peter van Oosterom (supervisor: van Oosterom), Eftychia Kalogianni, Abdullah Alattas, Agung Indrajit
     - title similarity 0.35; abstract similarity 0.12; year +5  (source: GDMC)
  4. "Registration of apartments and office spaces in 3D land administration – A case study in Croatia" — Land Use Policy, Elsevier, 142(107187), pp. 14, 2024 — [journal article](https://doi.org/10.1016/j.landusepol.2024.107187)
     - authors: Nikola Vučić, Sa&scaron;a Vrani&cacute;, Michael Sutherland, Peter van Oosterom (supervisor: van Oosterom), Saša Vranić
     - title similarity 0.32; abstract similarity 0.12; year +5  (source: GDMC)
  … and 23 more possible candidates; re-run with --limit/--surname to see them all.
- **Evangelos Theocharous (2019)** — How to solve spatial problems using linked-data: the case of planning a shopping
  1. "Integrating subsurface data into urban planning for climate adaptation using land administration domain model part 5" — Survey Review, Taylor and Francis, pp. 17, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2539606)
     - authors: Maria Luisa Tarozzo Kawasaki, Laura Thomas, Ulf Hackauf, Rob van der Krogt, Wilfred Visser, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.39; abstract similarity 0.30; year +6  (source: GDMC)
  2. "Detection and reconstruction of static vehicle-related ground occlusions in point clouds from mobile laser scanning" — Automation in Construction, Elsevier BV, 141, pp. 104461, 2022 — [journal article](https://www.sciencedirect.com/science/article/pii/S092658052200334X)
     - authors: Zhenyu Liu, Peter van Oosterom (supervisor: van Oosterom), Jesús Balado, Arjen Swart, Bart Beers
     - title similarity 0.30; abstract similarity 0.24; year +3  (source: GDMC)
  3. "Registration of apartments and office spaces in 3D land administration – A case study in Croatia" — Land Use Policy, Elsevier, 142(107187), pp. 14, 2024 — [journal article](https://doi.org/10.1016/j.landusepol.2024.107187)
     - authors: Nikola Vučić, Sa&scaron;a Vrani&cacute;, Michael Sutherland, Peter van Oosterom (supervisor: van Oosterom), Saša Vranić
     - title similarity 0.31; abstract similarity 0.26; year +5  (source: GDMC)
  4. "Web-based dissemination of continuously generalized Space-Scale Cube data for smooth user interaction" — International Journal of Cartography, Informa UK Limited, 6(1), pp. 15, 2020 — [journal article](https://doi.org/10.1080/23729333.2019.1705144)
     - authors: Martijn Meijers, Peter van Oosterom (supervisor: van Oosterom), Mattijs Driel, Radan &Scaron;uba, Radan Šuba
     - title similarity 0.34; abstract similarity 0.19; year +1  (source: GDMC)
  … and 37 more possible candidates; re-run with --limit/--surname to see them all.
- **Yixin Xu (2019)** — Improving location accuracy of a crowdsourced weather station by using a point c
  1. "Bringing Subsurface Information Models and Climate Adaptation Design into LADM part 5 Spatial Plan Information" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_G.pdf)
     - authors: Maria Luisa Tarozzo Kawasaki, Rob van der Krogt, Wilfred Visser, Ulf Hackauf, Alexander Wandl (supervisor: Wandl), Peter van Oosterom
     - title similarity 0.36; abstract similarity n/a; year +5  (source: GDMC)
- **Mutian Deng (2020)** — Using Foreign Data Wrapper in PostgreSQL to Expose Point Clouds on File System
  1. "Mathematical morphology directly applied to point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 168, , 2020 — [journal article](https://doi.org/10.1016/j.isprsjprs.2020.08.011)
     - authors: Jes&uacute;s Balado, Peter van Oosterom (supervisor: van Oosterom), Luc&iacute;a D&iacute;az-Vilari&ntilde;o, Martijn Meijers (supervisor: Meijers), Lucía Díaz-Vilariño
     - title similarity 0.37; abstract similarity 0.36; year +0  (source: GDMC)
  2. "Organizing and visualizing point clouds with continuous levels of detail" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 194, , 2022 — [journal article](https://doi.org/10.1016/j.isprsjprs.2022.10.004)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Haicheng Liu, Rod Thompson, Martijn Meijers (supervisor: Meijers), Edward Verbree
     - title similarity 0.39; abstract similarity 0.30; year +2  (source: GDMC)
  3. "Point clouds and Hydroinformatics" — 2022 (Abstract from EGU General Assembly 2022, Vienna, Austria, 23–27 , 2022 — [conference paper](https://meetingorganizer.copernicus.org/EGU22/EGU22-12880.html)
     - authors: Vitali Diaz, Haicheng Liu, Peter van Oosterom (supervisor: van Oosterom), Martijn Meijers (supervisor: Meijers), Edward Verbree, Fedor Baart, Maarten Pronk, Thijs van Lankveld
     - title similarity 0.33; abstract similarity 0.32; year +2  (source: GDMC)
  4. "Comparison of cloud-to-cloud distance calculation methods for change detection in spatio-temporal point clouds" — ?, 2024 — [conference paper](https://doi.org/10.5194/egusphere-egu24-8191)
     - authors: Vitali Diaz, Peter van Oosterom (supervisor: van Oosterom), Martijn Meijers (supervisor: Meijers), Edward Verbree, Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.32; abstract similarity 0.32; year +4  (source: OpenAlex)
  … and 21 more possible candidates; re-run with --limit/--surname to see them all.
- **Charlotte Duynstee (2020)** — Data driven sustainable mobility analysis in the city of Amsterdam
  1. "Formalisation of code lists and their values – The case of ISO 19152 Land Administration Domain Model" — Proceedings of the 10th FIG Land Administration Domain Model Workshop , 2022 — [conference paper](https://www.gdmc.nl/publications/2022/LADM2022_paper_CodeListValues.pdf)
     - authors: Abdullah Kara, Alexandra Rowland, Peter van Oosterom, Erik Stubkjær, Volkan Çağdaş, Erwin Folmer, Christiaan Lemmen, Wilko Quak (supervisor: Quak), Laura Meggiolaro
     - title similarity 0.31; abstract similarity n/a; year +2  (source: GDMC)
- **Celine Jansen (2020)** — A change of view: Usable interface design propositions for geoportals
  1. "Development and Usability Testing of the Participatory Urban Plan Monitoring Prototype for Indonesian Smart Cities Based on Digital Triplets" — Proceedings of the FIG Working Week 2021, Online, pp. 27, 2021 — [conference paper](https://fig.net/resources/proceedings/fig_proceedings/fig2021/papers/ws_03.4/WS_03.4_indrajit_yusa_et_al_11023.pdf)
     - authors: Agung Indrajit, Muhammad Hasannudin Yusa, Bastiaan van Loenen (supervisor: van Loenen), Peter van Oosterom, Deni Suwardhi
     - title similarity 0.33; abstract similarity n/a; year +1  (source: GDMC)
- **Konrad Jarocki (2020)** — Parallel step assignment for continuous generalization constrained with target m
  1. "Paralleling generalization operations to support smooth zooming: case study of merging area objects" — Proceedings of 23rd Workshop on Generalisation and Multiple Representa, 2020 — [conference paper](https://www.gdmc.nl/publications/2020/ICAgen2020_paper_5.pdf)
     - authors: Dongliang Peng, Martijn Meijers (supervisor: Meijers), Peter van Oosterom
     - title similarity 0.48; abstract similarity n/a; year +0  (source: GDMC)
  2. "HistSFC: Optimization for nD massive spatial points querying" — International Journal of Database Management Systems (IJDMS), Academy , 2020 — [journal article](https://aircconline.com/abstract/ijdms/v12n3/12320ijdms02.html)
     - authors: Haicheng Liu, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Xuefeng Guan, Edward Verbree, Mike Horhammer
     - title similarity 0.40; abstract similarity n/a; year +0  (source: GDMC)
  3. "Web-based dissemination of continuously generalized Space-Scale Cube data for smooth user interaction" — International Journal of Cartography, Informa UK Limited, 6(1), pp. 15, 2020 — [journal article](https://doi.org/10.1080/23729333.2019.1705144)
     - authors: Martijn Meijers (supervisor: Meijers), Peter van Oosterom, Mattijs Driel, Radan &Scaron;uba
     - title similarity 0.40; abstract similarity n/a; year +0  (source: GDMC)
  4. "2D to 1D and 2D to 0D Geometry Generalization Based on the Straight Skeleton by the Dual-Half Edge Structure" — ISPRS Geospatial Week 2025 "Photogrammetry & Remote Sensing for a Bett, 2025 — [conference paper](https://doi.org/10.5194/isprs-archives-xlviii-g-2025-513-2025)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (supervisor: Meijers), Peter van Oosterom
     - title similarity 0.43; abstract similarity n/a; year +5  (source: GDMC)
  … and 9 more possible candidates; re-run with --limit/--surname to see them all.
- **Amber Mulder (2020)** — Semantic segmentation of RGB-Z aerial imagery using convolutional neural network
  1. "Semantic Segmentation of UAV Aerial Videos using Convolutional Neural Networks" — 2019 IEEE Second International Conference on Artificial Intelligence a, 2019 — [conference paper](https://doi.org/10.1109/aike.2019.00012)
     - authors: Girisha S., Manohara Pai M.M., Ujjwal Verma, Radhika M. Pai
     - title similarity 0.89; abstract similarity n/a; year -1  (source: Crossref)
  2. "Convolutional neural networks—Semantic segmentation" — Deep Learning, 2025 — [book-chapter](https://doi.org/10.1016/b978-0-443-43954-4.00003-2)
     - authors: Shuhao Wang, Gang Xu
     - title similarity 0.62; abstract similarity n/a; year +5  (source: Crossref)
- **Erik van der Wal (2020)** — Examining the influence of urban design on cyclist route choice in different wea
  1. "Cycling Speed and Weather: Roles of Cyclist Weather-Sensitivity, Spatial and Infrastructural Conditions" — ?, 2024 — [posted-content](https://doi.org/10.2139/ssrn.5052377)
     - authors: Hong Yan, Kees Maat (supervisor: Maat), Bert van Wee
     - title similarity 0.40; abstract similarity n/a; year +4  (source: Crossref)
  2. "Cycling speed and weather: Roles of cyclist weather-sensitivity, spatial and infrastructural conditions" — International Journal of Sustainable Transportation, 2026 — [journal article](https://doi.org/10.1080/15568318.2026.2718239)
     - authors: Hong Yan, Kees Maat (supervisor: Maat), Bert van Wee
     - title similarity 0.40; abstract similarity n/a; year +6  (source: Crossref)
- **Xin Wang (2020)** — Using CityGML EnergyADE Data in Honeybee
  1. "Online Personal Data Protection and Data Flows Under the RCEP: A Nostalgic New Start?" — Journal of World Trade, 2022 — [journal article](https://doi.org/10.54648/trad2022027)
     - authors: Xin Wang (student)
     - title similarity 0.30; abstract similarity 0.15; year +2  (source: Crossref)
  2. "Mapping the CityGML Energy ADE to CityGML 3.0 Using a Model-Driven Approach" — ISPRS International Journal of Geo-Information, 2024 — [journal article](https://doi.org/10.3390/ijgi13040121)
     - authors: Carolin Bachert, Camilo León-Sánchez, Tatjana Kutzner, Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.47; abstract similarity 0.42; year +4  (source: Crossref)
  3. "Editorial for Special Issue of Journal of Big Data Research on “Big Data Meets Knowledge Graphs”" — Big Data Research, 2021 — [journal article](https://doi.org/10.1016/j.bdr.2021.100215)
     - authors: Xin Wang (student), Diego Calvanese
     - title similarity 0.25; abstract similarity n/a; year +1  (source: Crossref)
  4. "Ponded Melt-Rich Zone at the Base of Lithospheric Plate in Central Mariana Revealed Using Ocean Bottom Seismometer Data" — ?, 2025 — [posted-content](https://doi.org/10.5194/egusphere-egu25-14179)
     - authors: Jiahui Zhang, Xin Wang (student)
     - title similarity 0.21; abstract similarity 0.06; year +5  (source: Crossref)
  … and 1 more possible candidates; re-run with --limit/--surname to see them all.
- **N.A. Nur An Nisa Milyana (2021)** — Designing User Experience (UX) to Support Public Participation in Spatial Planni
  1. "Implementation of the spatial plan information package for improving ease of doing business in Indonesian cities" — Land Use Policy, Elsevier, 105(105338), pp. 1-17, 2021 — [journal article](https://doi.org/10.1016/j.landusepol.2021.105338)
     - authors: Agung Indrajit, Bastiaan van Loenen (supervisor: van Loenen), Suprajaka, Virgo Eresta Jaya, Hendrik Ploeger (supervisor: Ploeger), Christiaan Lemmen, Peter van Oosterom
     - title similarity 0.40; abstract similarity n/a; year +0  (source: GDMC)
  2. "Development and Usability Testing of the Participatory Urban Plan Monitoring Prototype for Indonesian Smart Cities Based on Digital Triplets" — Proceedings of the FIG Working Week 2021, Online, pp. 27, 2021 — [conference paper](https://fig.net/resources/proceedings/fig_proceedings/fig2021/papers/ws_03.4/WS_03.4_indrajit_yusa_et_al_11023.pdf)
     - authors: Agung Indrajit, Muhammad Hasannudin Yusa, Bastiaan van Loenen (supervisor: van Loenen), Peter van Oosterom, Deni Suwardhi
     - title similarity 0.36; abstract similarity n/a; year +0  (source: GDMC)
  3. "A standards-based portal for integrated Land Administration information: A case study of the Netherlands" — Proceedings of the FIG Working Week 20225, Brisbane, Australia, pp. 18, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/IntegratedLADM_NL.pdf)
     - authors: Marjolein van Aalst, Peter van Oosterom, Lexi Rowland, Erwin Folmer, Hendrik Ploeger (supervisor: Ploeger)
     - title similarity 0.40; abstract similarity n/a; year +4  (source: GDMC)
- **Jialun Wu (2021)** — Automatic building permits checks by means of 3D city models
  1. "A tiered spatial validation workflow for geographic prediction models" — ?, 2026 — [posted-content](https://doi.org/10.2139/ssrn.7174563)
     - authors: Xueqian Jiang, Jialun Wu (student), Jiabei Liu
     - title similarity 0.23; abstract similarity 0.02; year +5  (source: Crossref)
  2. "A tiered spatial validation workflow for geographic prediction models" — MethodsX, 2026 — [journal article](https://doi.org/10.1016/j.mex.2026.104072)
     - authors: Xueqian Jiang, Jialun Wu (student), Jiabei Liu
     - title similarity 0.23; abstract similarity n/a; year +5  (source: Crossref)
  3. "IFC models for semi-automating common planning checks for building permits" — Automation in Construction, 2022 — [journal article](https://doi.org/10.1016/j.autcon.2021.104097)
     - authors: Francesca Noardo (supervisor: Noardo), Teng Wu, Ken Arroyo Ohori, Thomas Krijnen, Jantien Stoter
     - title similarity 0.42; abstract similarity n/a; year +1  (source: Crossref)
- **Camilo Caceres Tocora (2022)** — Automated Semantic Segmentation of Aerial Imagery using Synthetic Data
  1. "Synthetic Data for Semantic Segmentation in Underwater Imagery" — OCEANS 2022, Hampton Roads, 2022 — [conference paper](https://doi.org/10.1109/oceans47191.2022.9976962)
     - authors: Michael Pergeorelis, Maxim Bazik, Philip Saponaro, Joong Kim, Chandra Kambhamettu
     - title similarity 0.62; abstract similarity n/a; year +0  (source: Crossref)
- **Pratyush Kumar (2022)** — An OGC 3D tiling technique based user-interactive platform for digital twins in 
  1. "Innovative Ideas for Leveraging IoT in Conjunction with Digital Twins for Smart Cities and Urban Planning" — Digital Twins for Smart Cities and Urban Planning, 2025 — [book-chapter](https://doi.org/10.1201/9781003510338-9)
     - authors: V. Renukaradya, P.K. Kumar (student), M.S. Shreyas
     - title similarity 0.28; abstract similarity n/a; year +3  (source: Crossref)
  2. "City digital twins for urban resilience" — International Journal of Digital Earth, Taylor & Francis, 16(2), pp. 4, 2023 — [journal article](https://doi.org/10.1080/17538947.2023.2264827)
     - authors: Adele Therias, Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.35; abstract similarity n/a; year +1  (source: GDMC)
  3. "Automated District-Level Energy Demand Modeling Using EnergyPlus Empowered by Digital Twin Technology" — ISPRS Geospatial Week 2025 "Photogrammetry & Remote Sensing for a Bett, 2025 — [conference paper](https://doi.org/10.5194/isprs-annals-x-g-2025-397-2025)
     - authors: Amin Jalilzadeh, Azarakhsh Rafiee (supervisor: Rafiee), Stefan De Graaf, Thaleia Konstantinou, Peter van Oosterom
     - title similarity 0.34; abstract similarity n/a; year +3  (source: GDMC)
  4. "A High-Performance Game Engine-GIS-CFD System for Interactive Urban Wind Decision Support" — Proceedings AGILE: GIScience Series (Tartu, Estonia), pp. 8, 2026 — [conference paper](https://agile-giss.copernicus.org/articles/7/49/2026/)
     - authors: Xuanchen Zhou, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom
     - title similarity 0.34; abstract similarity n/a; year +4  (source: GDMC)
- **Xenia Una Mainelli (2022)** — Exploring Isovist Applications in Third-Person View Visualisations of Outdoor Sp
  1. "Comparison of cloud-to-cloud distance calculation methods for change detection in spatio-temporal point clouds" — ?, 2024 — [conference paper](https://doi.org/10.5194/egusphere-egu24-8191)
     - authors: Vitali Diaz, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Edward Verbree (supervisor: Verbree), Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.40; abstract similarity 0.21; year +2  (source: OpenAlex)
  2. "Organizing and visualizing point clouds with continuous levels of detail" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 194, , 2022 — [journal article](https://doi.org/10.1016/j.isprsjprs.2022.10.004)
     - authors: Peter van Oosterom, Haicheng Liu, Rod Thompson, Martijn Meijers (supervisor: Meijers), Edward Verbree (supervisor: Verbree)
     - title similarity 0.36; abstract similarity 0.23; year +0  (source: GDMC)
  3. "Comparison of point distance calculation methods in point clouds - Is the most complex always the most suitable?" — Proceedings of the 18th International 3DGeoInfo Conference 2023, Munic, 2023 — [conference paper](https://www.gdmc.nl/publications/2023/3DGeoInfo_ComparePC.pdf)
     - authors: Vitali Diaz, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Edward Verbree (supervisor: Verbree), Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.31; abstract similarity n/a; year +1  (source: GDMC)
  4. "Comparison of Cloud-to-Cloud Distance Calculation Methods - Is the Most Complex Always the Most Suitable?" — Chapter in: Recent Advances in 3D Geoinformation Science, Lecture Note, 2024 — [conference paper](https://doi.org/10.1007/978-3-031-43699-4_20)
     - authors: Vitali Diaz, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Edward Verbree (supervisor: Verbree), Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.31; abstract similarity n/a; year +2  (source: GDMC)
  … and 13 more possible candidates; re-run with --limit/--surname to see them all.
- **Mels Smit (2022)** — Deducing the Location of Glass Windows in 3D Indoor Environments
  1. "Exploiting big point clouds: Unveiling insights for sustainable development through change detection in the built environment" — Chapter in: Digitalisation of the Built Environment: 3rd 4TU-14UAS Res, 2024 — [conference paper](https://resolver.tudelft.nl/uuid:91725b0a-bfe6-4dd7-b6f2-b9c036c64122)
     - authors: Vitali Diaz, Peter Van Oosterom, Martijn Meijers (supervisor: Meijers), Edward Verbree (supervisor: Verbree), Nauman Ahmed, Thijs Van Lankveld
     - title similarity 0.35; abstract similarity n/a; year +2  (source: GDMC)
  2. "Comparison of point distance calculation methods in point clouds - Is the most complex always the most suitable?" — Proceedings of the 18th International 3DGeoInfo Conference 2023, Munic, 2023 — [conference paper](https://www.gdmc.nl/publications/2023/3DGeoInfo_ComparePC.pdf)
     - authors: Vitali Diaz, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Edward Verbree (supervisor: Verbree), Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.35; abstract similarity n/a; year +1  (source: GDMC)
  3. "Indoor localisation and location tracking in indoor facilities based on LiDAR point clouds and images of the ceilings" — Proceedings of the 26th AGILE Conference on Geographic Information Sci, 2023 — [conference paper](https://doi.org/10.5194/agile-giss-4-4-2023)
     - authors: Ioannis Dardavesis, Edward Verbree (supervisor: Verbree), Azarakhsh Rafiee
     - title similarity 0.36; abstract similarity 0.24; year +1  (source: GDMC)
  4. "Point Clouds for 3D Land Administration: Integrating Floor Plans and Nationwide Airborne LiDAR (AHN)" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2025 — [conference paper](https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-9-2025)
     - authors: Citra Andinasari, Peter van Oosteroom, Edward Verbree (supervisor: Verbree)
     - title similarity 0.35; abstract similarity 0.21; year +3  (source: GDMC)
  … and 12 more possible candidates; re-run with --limit/--surname to see them all.
- **Laurens van Rijssel (2022)** — Generating consistent triangular terrain elevation data for noise modelling
  1. "Automated noise modelling using a triangulated terrain model" — Geo-spatial Information Science, 2023 — [journal article](https://doi.org/10.1080/10095020.2023.2270520)
     - authors: Nadine Hobeika, Laurens van Rijssel (student), Maarit Prusti, Constantijn Dinklo, Denis Giannelli, Balázs Dukai (supervisor: Dukai), Arnaud Kok, Rob van Loon, René Nota, Jantien Stoter
     - title similarity 0.30; abstract similarity n/a; year +1  (source: Crossref)
- **Maximiliaan van Schendel (2022)** — Merging of Topometric Maps of Indoor Environments -- Extraction
  1. "Photorealistic Indoor Virtual Environments for Wayfinding: Exploring the Feasibility and Initial Evaluation of Gaussian Splatting in VR Simulation" — IOP Conference Series Earth and Environmental Science, 2026 — [conference paper](https://doi.org/10.1088/1755-1315/1647/1/012001)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter van Oosterom, Sisi Zlatanova, Yingwen Yu
     - title similarity 0.36; abstract similarity 0.11; year +4  (source: OpenAlex)
  2. "Exploring the Potential of Gaussian Splatting Environment for Indoor Wayfinding Simulation" — Proceedings AGILE 2025 workshop Geo xR (Dresden, Germany), pp. 6, 2025 — [conference paper](https://sites.google.com/view/geo-xr-workshop-agile205/home)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter Van Oosterom
     - title similarity 0.42; abstract similarity n/a; year +3  (source: GDMC)
  3. "Point Cloud for 3D Land Administration System (LAS)" — Proceedings of the 13th International FIG Workshop on Land Administrat, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/3DLA2025_paper_S_39.pdf)
     - authors: Citra Andinasari, Peter van Oosteroma, Edward Verbree (supervisor: Verbree)
     - title similarity 0.36; abstract similarity n/a; year +3  (source: GDMC)
  4. "Comparison of cloud-to-cloud distance calculation methods for change detection in spatio-temporal point clouds" — ?, 2024 — [conference paper](https://doi.org/10.5194/egusphere-egu24-8191)
     - authors: Vitali Diaz, Peter van Oosterom, Martijn Meijers, Edward Verbree (supervisor: Verbree), Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.32; abstract similarity 0.03; year +2  (source: OpenAlex)
  … and 2 more possible candidates; re-run with --limit/--surname to see them all.
- **Linjun Wang (2022)** — Detailed Facade Reconstruction for Mahattan-world Buildings
  1. "Detailed Complementary Consistency:Wave Function Tells Particle How to Hop, Particle Tells Wave Function How to Collapse" — ?, 2024 — [posted-content](https://doi.org/10.26434/chemrxiv-2024-0r04j-v2)
     - authors: Lei Huang, Zhecun Shi, Linjun Wang (student)
     - title similarity 0.32; abstract similarity 0.13; year +2  (source: Crossref)
  2. "Detailed Complementary Consistency:Wave Function Tells Particle How to Hop, Particle Tells Wave Function How to Collapse" — ?, 2024 — [posted-content](https://doi.org/10.26434/chemrxiv-2024-0r04j-v3)
     - authors: Lei Huang, Zhecun Shi, Linjun Wang (student)
     - title similarity 0.32; abstract similarity 0.13; year +2  (source: Crossref)
  3. "Detailed Complementary Consistency:Wave Function Tells Particle How to Hop, Particle Tells Wave Function How to Collapse" — ?, 2024 — [posted-content](https://doi.org/10.26434/chemrxiv-2024-0r04j)
     - authors: Lei Huang, Zhecun Shi, Linjun Wang (student)
     - title similarity 0.32; abstract similarity 0.13; year +2  (source: Crossref)
  4. "Detailed Complementary Consistency: Wave Function Tells Particle How to Hop, Particle Tells Wave Function How to Collapse" — The Journal of Physical Chemistry Letters, 2024 — [journal article](https://doi.org/10.1021/acs.jpclett.4c01313)
     - authors: Lei Huang, Zhecun Shi, Linjun Wang (student)
     - title similarity 0.32; abstract similarity n/a; year +2  (source: Crossref)
- **Ziyan Wu (2022)** — Estimating building height from ICESat-2 data: The case of the Netherlands
  1. "Reinforcement learning in building controls: A comparative study of algorithms considering model availability and policy representation" — Journal of Building Engineering, 2024 — [journal article](https://doi.org/10.1016/j.jobe.2024.109497)
     - authors: Ziyan Wu (student), Wenhao Zhang, Rui Tang, Huilong Wang, Ivan Korolija
     - title similarity 0.30; abstract similarity n/a; year +2  (source: Crossref)
  2. "Muflex: A Scalable, Physics-Based Platform for Multi-Building Flexibility Analysis and Coordination" — ?, 2025 — [posted-content](https://doi.org/10.2139/ssrn.5403344)
     - authors: Ziyan Wu (student), Ivan Korolija, Rui Tang
     - title similarity 0.27; abstract similarity n/a; year +3  (source: Crossref)
  3. "Muflex: A Scalable, Physics-Based Platform for Multi-Building Flexibility Analysis and Coordination" — ?, 2025 — [posted-content](https://doi.org/10.2139/ssrn.5401124)
     - authors: Ziyan Wu (student), Ivan Korolija, Rui Tang
     - title similarity 0.27; abstract similarity n/a; year +3  (source: Crossref)
  4. "Statement of Peer Review" — AAAI Workshop on Artificial Intelligence with Biased or Scarce Data (A, 2022 — [conference paper](https://doi.org/10.3390/cmsf2022003012)
     - authors: Kuan-Chuan Peng, Ziyan Wu (student)
     - title similarity 0.27; abstract similarity n/a; year +0  (source: Crossref)
  … and 1 more possible candidates; re-run with --limit/--surname to see them all.
- **Mihai-Alexandru Erbașu (2023)** — Improving the content of Vario-Scale Maps - An analysis into the generalization 
  1. "2D to 1D and 2D to 0D Geometry Generalization Based on the Straight Skeleton by the Dual-Half Edge Structure" — ISPRS Geospatial Week 2025 "Photogrammetry & Remote Sensing for a Bett, 2025 — [conference paper](https://doi.org/10.5194/isprs-archives-xlviii-g-2025-513-2025)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (supervisor: Meijers), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.39; abstract similarity 0.18; year +2  (source: GDMC)
  2. "Comparison of cloud-to-cloud distance calculation methods for change detection in spatio-temporal point clouds" — ?, 2024 — [conference paper](https://doi.org/10.5194/egusphere-egu24-8191)
     - authors: Vitali Diaz, Peter van Oosterom (supervisor: van Oosterom), Martijn Meijers (supervisor: Meijers), Edward Verbree, Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.30; abstract similarity 0.10; year +1  (source: OpenAlex)
  3. "Modelling the legal spaces of 3D underground objects in 3D land administration systems" — Land Use Policy, Elsevier BV, 127, pp. 106537, 2023 — [journal article](https://www.sciencedirect.com/science/article/pii/S0264837723000030)
     - authors: Rohit Ramlakhan, Eftychia Kalogianni, Peter van Oosterom (supervisor: van Oosterom), Behnam Atazadeh
     - title similarity 0.37; abstract similarity 0.14; year +0  (source: GDMC)
  4. "Identification and Visualization of Unscanned Areas Within a Building Based on the Building’s Outer Hull" — Proceedings AGILE: GIScience Series (Dresden, Germany), pp. 9, 2025 — [conference paper](https://agile-giss.copernicus.org/articles/6/28/2025/)
     - authors: Giorgios Iliopoulos, Robert Vo&ucirc;te, Peter van Oosterom (supervisor: van Oosterom), Robert Voûte
     - title similarity 0.35; abstract similarity 0.15; year +2  (source: GDMC)
  … and 27 more possible candidates; re-run with --limit/--surname to see them all.
- **Lisa Yvette Geers (2023)** — Localising objects with drones: A case study on the localisation of fisher boats
  1. "Generalizing Simultaneously to Support Smooth Zooming: Case Study of Merging Area Objects" — Journal of Geovisualization and Spatial Analysis, Springer, 7(12), pp., 2023 — [journal article](https://doi.org/10.1007/s41651-022-00109-x)
     - authors: Dongliang Peng, Martijn Meijers (supervisor: Meijers), Peter van Oosterom
     - title similarity 0.41; abstract similarity n/a; year +0  (source: GDMC)
  2. "A comprehensive review and framework on the applications of digital twins for energy transition at the district level" — Renewable and Sustainable Energy Reviews, Elsevier BV, 234, pp. 116872, 2026 — [journal article](https://doi.org/10.1016/j.rser.2026.116872)
     - authors: Amin Jalilzadeh, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom, Thaleia Konstantinou
     - title similarity 0.37; abstract similarity n/a; year +3  (source: GDMC)
  3. "2D to 1D and 2D to 0D Geometry Generalization Based on the Straight Skeleton by the Dual-Half Edge Structure" — ISPRS Geospatial Week 2025 "Photogrammetry & Remote Sensing for a Bett, 2025 — [conference paper](https://doi.org/10.5194/isprs-archives-xlviii-g-2025-513-2025)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (supervisor: Meijers), Peter van Oosterom
     - title similarity 0.36; abstract similarity n/a; year +2  (source: GDMC)
  4. "Indoor localisation through Isovist fingerprinting from point clouds and floor plans" — Journal of Location Based Services, Taylor & Francis, (2320642), pp. 2, 2024 — [journal article](https://www.tandfonline.com/doi/full/10.1080/17489725.2024.2320642)
     - authors: Georgios Triantafyllou, Edward Verbree, Azarakhsh Rafiee (supervisor: Rafiee), Simon Pena Pereira, Stef Lhermitte
     - title similarity 0.35; abstract similarity n/a; year +1  (source: GDMC)
  … and 6 more possible candidates; re-run with --limit/--surname to see them all.
- **Siebren Meines (2023)** — LuminaCity: a Real-Time Daylight Analysis Tool for Architectural and Urban Devel
  1. "Cloud-based application for indoor daylight performance analysis through BIM-GIS Integration" — Building and Environment, Elsevier BV, 293, pp. 114376, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2026.114376)
     - authors: Yangyu Liu, Eleonora Brembilla (supervisor: Brembilla), Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.36; abstract similarity n/a; year +3  (source: GDMC)
  2. "Integrating radar and multi-spectral data to detect cocoa crops: A deep learning approach" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2025 — [journal article](https://doi.org/10.1016/j.rsase.2025.101652)
     - authors: Adele Therias, Azarakhsh Rafiee (supervisor: Rafiee), Stef Lhermitte, Philip van der Lugt, Roderik Lindenbergh
     - title similarity 0.41; abstract similarity n/a; year +2  (source: GDMC)
  3. "City digital twins for urban resilience" — International Journal of Digital Earth, Taylor & Francis, 16(2), pp. 4, 2023 — [journal article](https://doi.org/10.1080/17538947.2023.2264827)
     - authors: Adele Therias, Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.37; abstract similarity n/a; year +0  (source: GDMC)
  4. "Automated District-Level Energy Demand Modeling Using EnergyPlus Empowered by Digital Twin Technology" — ISPRS Geospatial Week 2025 "Photogrammetry & Remote Sensing for a Bett, 2025 — [conference paper](https://doi.org/10.5194/isprs-annals-x-g-2025-397-2025)
     - authors: Amin Jalilzadeh, Azarakhsh Rafiee (supervisor: Rafiee), Stefan De Graaf, Thaleia Konstantinou, Peter van Oosterom
     - title similarity 0.37; abstract similarity n/a; year +2  (source: GDMC)
  … and 1 more possible candidates; re-run with --limit/--surname to see them all.
- **Eleni Theodoridou (2023)** — Implementation of OGC SensorThings API standard for the integration of dynamic s
  1. "Indoor localisation and location tracking in indoor facilities based on LiDAR point clouds and images of the ceilings" — Proceedings of the 26th AGILE Conference on Geographic Information Sci, 2023 — [conference paper](https://doi.org/10.5194/agile-giss-4-4-2023)
     - authors: Ioannis Dardavesis, Edward Verbree, Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.37; abstract similarity n/a; year +0  (source: GDMC)
  2. "Automated District-Level Energy Demand Modeling Using EnergyPlus Empowered by Digital Twin Technology" — ISPRS Geospatial Week 2025 "Photogrammetry & Remote Sensing for a Bett, 2025 — [conference paper](https://doi.org/10.5194/isprs-annals-x-g-2025-397-2025)
     - authors: Amin Jalilzadeh, Azarakhsh Rafiee (supervisor: Rafiee), Stefan De Graaf, Thaleia Konstantinou, Peter van Oosterom
     - title similarity 0.36; abstract similarity n/a; year +2  (source: GDMC)
  3. "Cloud-based application for indoor daylight performance analysis through BIM-GIS Integration" — Building and Environment, Elsevier BV, 293, pp. 114376, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2026.114376)
     - authors: Yangyu Liu, Eleonora Brembilla, Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.36; abstract similarity n/a; year +3  (source: GDMC)
  4. "An OGC SensorThings GIS Pipeline For Estimating Seismic Engineering Demand Parameters" — ISPRS - Annals of the Photogrammetry, Remote Sensing and Spatial Infor, 2025 — [conference paper](https://doi.org/10.5194/isprs-annals-x-g-2025-787-2025)
     - authors: Justin Schembri, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom
     - title similarity 0.34; abstract similarity n/a; year +2  (source: GDMC)
  … and 1 more possible candidates; re-run with --limit/--surname to see them all.
- **Fengyan Zhang (2023)** — Snap rounding polygons with a triangulation
  1. "The backward rounding error analysis of the quaternion Givens QR decomposition" — Numerical Algorithms, 2025 — [journal article](https://doi.org/10.1007/s11075-024-02002-8)
     - authors: Fengxia Zhang (student), Yuqing Zhang, Zhihan Zhou, Musheng Wei
     - title similarity 0.32; abstract similarity n/a; year +2  (source: Crossref)
- **Yingxin Feng (2024)** — 3D building model edit with generative AI
  1. "Building and Training Generative AI Models" — ?, 2026 — [book](https://doi.org/10.1007/979-8-8688-2332-9)
     - authors: Irena Cronin
     - title similarity 0.64; abstract similarity n/a; year +2  (source: Crossref)
- **Sicong Gong (2024)** — Towards Adaptive Trajectory Data Management: Modelling, Accessing, Distributing,
  1. "An nD-histogram technique for querying non-uniformly distributed point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 224, , 2025 — [journal article](https://doi.org/10.1016/j.isprsjprs.2025.03.014)
     - authors: Haicheng Liu, Zhiwei Li, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Chuqi Zhang
     - title similarity 0.38; abstract similarity n/a; year +1  (source: GDMC)
  2. "Exploiting big point clouds: Unveiling insights for sustainable development through change detection in the built environment" — Chapter in: Digitalisation of the Built Environment: 3rd 4TU-14UAS Res, 2024 — [conference paper](https://resolver.tudelft.nl/uuid:91725b0a-bfe6-4dd7-b6f2-b9c036c64122)
     - authors: Vitali Diaz, Peter Van Oosterom, Martijn Meijers (supervisor: Meijers), Edward Verbree, Nauman Ahmed, Thijs Van Lankveld
     - title similarity 0.31; abstract similarity n/a; year +0  (source: GDMC)
- **Stein Köbben (2024)** — Integrating 3D Functionality into a Web Application for Sharing Geo-information
  1. "Spatial plan registration and compliance checks in Estonia, based on LADM part 5: spatial plan information" — Survey Review, Informa UK Limited, pp. 1–31, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2547462)
     - authors: Simay Batum, Eftychia Kalogianni (supervisor: Kalogianni), Marjan Broekhuizen, Christopher Raitviir, Kermo M&auml;gi, Peter Van Oosterom
     - title similarity 0.39; abstract similarity n/a; year +1  (source: GDMC)
  2. "Leveraging BIM/IFC for the Registration of Spatial Plans and Compliance Checks and Permitting in Estonia based on LADM Part 5 - Spatial Plan Information" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_J.pdf)
     - authors: Simay Batum, Eftychia Kalogianni (supervisor: Kalogianni), Marjan Broekhuizen, Christopher Raitviir, Kermo Mägi, Peter van Oosterom
     - title similarity 0.36; abstract similarity n/a; year +0  (source: GDMC)
  3. "Developing a LADM Part 5 – Spatial Plan Information country profile for Greece" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_I.pdf)
     - authors: Maria Poulaki, Nikolaos Xagoraris, Eftychia Kalogianni (supervisor: Kalogianni), Charalampos Kyriakidis, Abdullah Kara, Efi Dimopoulou
     - title similarity 0.34; abstract similarity n/a; year +0  (source: GDMC)
  4. "Bridging Sustainable Development Goals and Land Administration: The Role of the ISO 19152 Land Administration Domain Model in SDG Indicator Formalization" — Land, MDPI AG, 13(491), pp. 27, 2024 — [journal article](https://doi.org/10.3390/land13040491)
     - authors: Mengying Chen, Peter Van Oosterom, Eftychia Kalogianni (supervisor: Kalogianni), Paula Dijkstra, Christiaan Lemmen
     - title similarity 0.32; abstract similarity n/a; year +0  (source: GDMC)
  … and 1 more possible candidates; re-run with --limit/--surname to see them all.
- **Sitong Li (2024)** — Enhancing 3D model for urban area with neural representations
  1. "Exploring the Architectural Art of Tang Dynasty Courtyards through Pottery Architectural Model: Spatial Layout, Architectural Features, and Cultural Connotations" — Journal of Civil and Transportation Engineering, 2025 — [journal article](https://doi.org/10.62517/jcte.202506209)
     - authors: Sitong Li (student), Lirong Zeng
     - title similarity 0.34; abstract similarity 0.15; year +1  (source: Crossref)
- **Georgios Konstantinos Nestoras (2024)** — Exploring the potential of 5G positioning via RSSI, comparing its efficacy with 
  1. "Photorealistic Indoor Virtual Environments for Wayfinding: Exploring the Feasibility and Initial Evaluation of Gaussian Splatting in VR Simulation" — IOP Conference Series Earth and Environmental Science, 2026 — [conference paper](https://doi.org/10.1088/1755-1315/1647/1/012001)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter van Oosterom, Sisi Zlatanova, Yingwen Yu
     - title similarity 0.38; abstract similarity 0.16; year +2  (source: OpenAlex)
  2. "Point Clouds for 3D Land Administration: Integrating Floor Plans and Nationwide Airborne LiDAR (AHN)" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2025 — [conference paper](https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-9-2025)
     - authors: Citra Andinasari, Peter van Oosteroom, Edward Verbree (supervisor: Verbree)
     - title similarity 0.34; abstract similarity 0.11; year +1  (source: GDMC)
  3. "Indoor localisation through Isovist fingerprinting from point clouds and floor plans" — Journal of Location Based Services, 2024 — [journal article](https://doi.org/10.1080/17489725.2024.2320642)
     - authors: Georgios Triantafyllou, Edward Verbree (supervisor: Verbree), Azarakhsh Rafiee
     - title similarity 0.31; abstract similarity 0.11; year +0  (source: OpenAlex)
  4. "Exploring the Potential of Gaussian Splatting Environment for Indoor Wayfinding Simulation" — Proceedings AGILE 2025 workshop Geo xR (Dresden, Germany), pp. 6, 2025 — [conference paper](https://sites.google.com/view/geo-xr-workshop-agile205/home)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter Van Oosterom
     - title similarity 0.36; abstract similarity n/a; year +1  (source: GDMC)
  … and 2 more possible candidates; re-run with --limit/--surname to see them all.
- **Qiwei Shen (2024)** — Plant Skeleton Extraction and Stem-leaf Segmentation
  1. "Tobacco stem and leaf segmentation and phenotypic parameter extraction based on the improved point cloud segmentation network PE-KPConv" — Smart Agricultural Technology, 2026 — [journal article](https://doi.org/10.1016/j.atech.2026.101927)
     - authors: Yunchong Bi, Junying Li, Hong Liang, Zhiyu Feng, Wenjie Tong, Dewang Nan (supervisor: Nan), Rui Liu
     - title similarity 0.31; abstract similarity n/a; year +2  (source: Crossref)
- **Marieke van Esch (2024)** — From thermal comfort to heat mitigation action - A reproducable QGIS plugin for 
  1. "From heatwaves to ‘healthwaves’: A spatial study on the impact of urban heat on cardiovascular and respiratory emergency calls in the city of Milan" — Sustainable Cities and Society, 2025 — [journal article](https://doi.org/10.1016/j.scs.2025.106181)
     - authors: Doruntina Zendeli, Nicola Colaninno, Daniela Maiullari, Marjolein van Esch (student), Arjan van Timmeren, Gianluca Marconi, Rodolfo Bonora, Eugenio Morello
     - title similarity 0.32; abstract similarity n/a; year +1  (source: Crossref)
  2. "From comparison to integration: A workflow evaluation of 3D Gaussian splatting and LiDAR point cloud for modern architectural heritage" — Automation in Construction, Elsevier BV, 180, pp. 106509, 2025 — [journal article](https://doi.org/10.1016/j.autcon.2025.106509)
     - authors: Yingwen Yu, Edward Verbree (supervisor: Verbree), Peter van Oosterom, Uta Pottgiesser, Yuyang Peng, Florent Poux
     - title similarity 0.38; abstract similarity 0.05; year +1  (source: GDMC)
  3. "Direct Use of Indoor Point Clouds for Path Planning and Navigation Exploration in Emergency Situations" — Chapter in: The International Archives of the Photogrammetry, Remote S, 2024 — [conference paper](https://isprs-archives.copernicus.org/articles/XLVIII-4-W11-2024/175/2024/)
     - authors: Algan Yasar, Robert Vo&ucirc;te, Edward Verbree (supervisor: Verbree), Robert Voûte
     - title similarity 0.32; abstract similarity 0.09; year +0  (source: GDMC)
  4. "Comparison of cloud-to-cloud distance calculation methods for change detection in spatio-temporal point clouds" — ?, 2024 — [conference paper](https://doi.org/10.5194/egusphere-egu24-8191)
     - authors: Vitali Diaz, Peter van Oosterom, Martijn Meijers, Edward Verbree (supervisor: Verbree), Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.35; abstract similarity 0.05; year +0  (source: OpenAlex)
  … and 3 more possible candidates; re-run with --limit/--surname to see them all.
- **Yue Yang (2024)** — Directly Serving 3D Tiles From A Geo-DBMS
  1. "Advancing LED efficiency through 3D-printed light extraction structures: from design to demonstration" — Optics Express, 2025 — [journal article](https://doi.org/10.1364/oe.572911)
     - authors: Yang Yue (student), Kevin Chen, Hongyang Zhu
     - title similarity 0.33; abstract similarity 0.03; year +1  (source: Crossref)
  2. "Revealing multi-scale spatial synergy of mega-city region from a human mobility perspective" — Geo-spatial Information Science, 2024 — [journal article](https://doi.org/10.1080/10095020.2024.2379060)
     - authors: Bichen Fang, Mingxiao Li, Zhengdong Huang, Yang Yue (student), Wei Tu, Renzhong Guo
     - title similarity 0.32; abstract similarity n/a; year +0  (source: Crossref)
  3. "An nD-histogram technique for querying non-uniformly distributed point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 224, , 2025 — [journal article](https://doi.org/10.1016/j.isprsjprs.2025.03.014)
     - authors: Haicheng Liu, Zhiwei Li, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Chuqi Zhang
     - title similarity 0.31; abstract similarity n/a; year +1  (source: GDMC)
- **Der Derian Auliyaa Bainus (2025)** — Harmonisation of Heterogeneous Point Cloud Using Road Marking as Benchmark
  1. "Evaluating Smartphone LiDAR for Road Infrastructure Mapping: Harmonisation of iPhone LiDAR Data with National Airborne LiDAR Datasets" — The International Archives of the Photogrammetry, Remote Sensing and S, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-l-4-w2-2026-229-2026)
     - authors: Daan H. van der Heide (supervisor: van der Heide), Tessa Eikelboom, Jantien E. Stoter (supervisor: Stoter)
     - title similarity 0.21; abstract similarity 0.38; year +1  (source: Crossref)
- **Vidushi Bhatt (2025)** — Geospatial Analytics from IoT ecosystem in Built spaces
  1. "A High-Performance Game Engine-GIS-CFD System for Interactive Urban Wind Decision Support" — Proceedings AGILE: GIScience Series (Tartu, Estonia), pp. 8, 2026 — [conference paper](https://agile-giss.copernicus.org/articles/7/49/2026/)
     - authors: Xuanchen Zhou, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom
     - title similarity 0.35; abstract similarity n/a; year +1  (source: GDMC)
  2. "Integrating radar and multi-spectral data to detect cocoa crops: A deep learning approach" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2025 — [journal article](https://doi.org/10.1016/j.rsase.2025.101652)
     - authors: Adele Therias, Azarakhsh Rafiee (supervisor: Rafiee), Stef Lhermitte, Philip van der Lugt, Roderik Lindenbergh
     - title similarity 0.34; abstract similarity n/a; year +0  (source: GDMC)
- **Lars Boertjes (2025)** — Selective image region focus for efficient 3D building reconstruction using SAM 
  1. "Urban Local Climate Zone Classification Through Deep Learning Using Spatio-temporal Thermal Imagery" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2026 — [journal article](https://doi.org/10.1016/j.rsase.2026.101889)
     - authors: Michaja van Capel, Azarakhsh Rafiee (supervisor: Rafiee), Roderik Lindenbergh
     - title similarity 0.43; abstract similarity n/a; year +1  (source: GDMC)
  2. "An OGC SensorThings GIS Pipeline For Estimating Seismic Engineering Demand Parameters" — ISPRS - Annals of the Photogrammetry, Remote Sensing and Spatial Infor, 2025 — [conference paper](https://doi.org/10.5194/isprs-annals-x-g-2025-787-2025)
     - authors: Justin Schembri, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom
     - title similarity 0.37; abstract similarity n/a; year +0  (source: GDMC)
  3. "A comprehensive review and framework on the applications of digital twins for energy transition at the district level" — Renewable and Sustainable Energy Reviews, Elsevier BV, 234, pp. 116872, 2026 — [journal article](https://doi.org/10.1016/j.rser.2026.116872)
     - authors: Amin Jalilzadeh, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom, Thaleia Konstantinou
     - title similarity 0.30; abstract similarity n/a; year +1  (source: GDMC)
- **Yan Gao (2025)** — Labeling Vario-scale Maps
  1. "Spectral analysis of carbon concentrations in sediments at a plot scale" — ?, 2026 — [posted-content](https://doi.org/10.2139/ssrn.7031278)
     - authors: Pingping Fan, Huacheng Chi, Yang Gao (student), Yan Liu
     - title similarity 0.31; abstract similarity 0.06; year +1  (source: Crossref)
  2. "FloorPlan2Nav: Semantic-Topological Navigation from Floor Plan Images as Prior Maps" — Proceedings of the International Symposium on Automation and Robotics , 2026 — [conference paper](https://doi.org/10.22260/isarc2026/0225)
     - authors: Yan GAO (student), Qian Zheng, Fuji Hu, Yiwei Weng
     - title similarity 0.32; abstract similarity n/a; year +1  (source: Crossref)
  3. "Non-recurrent rational maps with disconnected Julia set" — Nonlinearity, 2026 — [journal article](https://doi.org/10.1088/1361-6544/ae54f4)
     - authors: Yan Gao (student), Lele Xu, Luxian Yang
     - title similarity 0.26; abstract similarity 0.05; year +1  (source: Crossref)
  4. "Temporal-spatial evolution and formation mechanism of energy consumption carbon footprint at county scale in the Yellow River Basin" — Scientific Reports, 2025 — [journal article](https://doi.org/10.1038/s41598-025-86383-3)
     - authors: Liyan Zhang, Mei Song, Yan Gao (student)
     - title similarity 0.21; abstract similarity n/a; year +0  (source: Crossref)
  … and 3 more possible candidates; re-run with --limit/--surname to see them all.
- **Michele Giampaolo (2025)** — A Graph Neural Network-based Approach to Predict the Effects of Urban Climate on
  1. "Cloud-based application for indoor daylight performance analysis through BIM-GIS Integration" — Building and Environment, Elsevier BV, 293, pp. 114376, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2026.114376)
     - authors: Yangyu Liu, Eleonora Brembilla, Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.34; abstract similarity n/a; year +1  (source: GDMC)
  2. "The effect of urban density on compliance with indoor visual and non-visual daylight targets: A Dutch case study" — Sustainable Cities and Society, Elsevier, (106149), pp. 55, 2025 — [journal article](https://doi.org/10.1016/j.scs.2025.106149)
     - authors: Daniël Koster, Azarakhsh Rafiee (supervisor: Rafiee), Eleonora Brembilla
     - title similarity 0.34; abstract similarity n/a; year +0  (source: GDMC)
  3. "Urban Local Climate Zone Classification Through Deep Learning Using Spatio-temporal Thermal Imagery" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2026 — [journal article](https://doi.org/10.1016/j.rsase.2026.101889)
     - authors: Michaja van Capel, Azarakhsh Rafiee (supervisor: Rafiee), Roderik Lindenbergh
     - title similarity 0.32; abstract similarity n/a; year +1  (source: GDMC)
- **Xiaoluo Gong (2025)** — Dynamic Seamless Oblique Image Mosaics for Aerial Visualization
  1. "An nD-histogram technique for querying non-uniformly distributed point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 224, , 2025 — [journal article](https://doi.org/10.1016/j.isprsjprs.2025.03.014)
     - authors: Haicheng Liu, Zhiwei Li, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Chuqi Zhang
     - title similarity 0.33; abstract similarity n/a; year +0  (source: GDMC)
  2. "Exploring the Potential of Gaussian Splatting Environment for Indoor Wayfinding Simulation" — Proceedings AGILE 2025 workshop Geo xR (Dresden, Germany), pp. 6, 2025 — [conference paper](https://sites.google.com/view/geo-xr-workshop-agile205/home)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter Van Oosterom
     - title similarity 0.31; abstract similarity n/a; year +0  (source: GDMC)
- **Lars Huizer (2025)** — PHYSHADE-Net: Leveraging Geometric-Priors in Physics-Guided Neural Networks for 
  1. "3D Gaussian Splatting for Modern Architectural Heritage: Integrating UAV-Based Data Acquisition and Advanced Photorealistic 3D Techniques" — Proceedings AGILE: GIScience Series (Dresden, Germany), pp. 9, 2025 — [conference paper](https://agile-giss.copernicus.org/articles/6/51/2025/)
     - authors: Yingwen Yu, Edward Verbree (supervisor: Verbree), Peter van Oosterom, Uta Pottgiesser
     - title similarity 0.36; abstract similarity 0.06; year +0  (source: GDMC)
  2. "Photorealistic Indoor Virtual Environments for Wayfinding: Exploring the Feasibility and Initial Evaluation of Gaussian Splatting in VR Simulation" — IOP Conference Series Earth and Environmental Science, 2026 — [conference paper](https://doi.org/10.1088/1755-1315/1647/1/012001)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter van Oosterom, Sisi Zlatanova, Yingwen Yu
     - title similarity 0.34; abstract similarity 0.06; year +1  (source: OpenAlex)
  3. "Smart point cloud–guided 3D gaussian splatting for urban modeling and data-driven analysis" — Sustainable Cities and Society, Elsevier BV, 149, pp. 107753, 2026 — [journal article](https://doi.org/10.1016/j.scs.2026.107753)
     - authors: Yingwen Yu, Zhuoyue Wang, Guanting Zhang, Peter van Oosterom, Edward Verbree (supervisor: Verbree), Steffen Nijhuis, Yuyang Peng
     - title similarity 0.31; abstract similarity 0.08; year +1  (source: GDMC)
  4. "When to stop? A visual impact assessment framework for incremental urban and community expansion in rural heritage landscapes" — Sustainable Cities and Society, Elsevier BV, 143, pp. 107364, 2026 — [journal article](https://doi.org/10.1016/j.scs.2026.107364)
     - authors: Yuyang Peng, Steffen Nijhuis, Zhuoyue Wang, Yingwen Yu, Edward Verbree (supervisor: Verbree), Peter van Oosterom
     - title similarity 0.30; abstract similarity 0.05; year +1  (source: GDMC)
  … and 1 more possible candidates; re-run with --limit/--surname to see them all.
- **Walter Hugo Johannes Kahn (2025)** — Working Towards Oblique Aerial Adjustment through the Creation of Synthetic Test
  1. "LiDAR Point Cloud Virtual Reality Visual Evaluation Through Structural Similarity Index Measure and Edge Metric Similarity" — AGILE 2025 - 28th AGILE conference on Geographic Information Science (, 2025 — [conference paper](https://zenodo.org/doi/10.5281/zenodo.15324418)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter van Oosterom
     - title similarity 0.37; abstract similarity n/a; year +0  (source: GDMC)
  2. "Exploring the Potential of Gaussian Splatting Environment for Indoor Wayfinding Simulation" — Proceedings AGILE 2025 workshop Geo xR (Dresden, Germany), pp. 6, 2025 — [conference paper](https://sites.google.com/view/geo-xr-workshop-agile205/home)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter Van Oosterom
     - title similarity 0.35; abstract similarity n/a; year +0  (source: GDMC)
  3. "Hierarchical Polygon-to-Point Collapsing for Multi-Scale Representation Based on the Straight Skeleton" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2026 — [conference paper](https://doi.org/10.5194/isprs-annals-xi-4-2026-21-2026)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (supervisor: Meijers)
     - title similarity 0.34; abstract similarity n/a; year +1  (source: GDMC)
  4. "Point Cloud for 3D Land Administration System (LAS)" — Proceedings of the 13th International FIG Workshop on Land Administrat, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/3DLA2025_paper_S_39.pdf)
     - authors: Citra Andinasari, Peter van Oosteroma, Edward Verbree (supervisor: Verbree)
     - title similarity 0.32; abstract similarity n/a; year +0  (source: GDMC)
  … and 1 more possible candidates; re-run with --limit/--surname to see them all.
- **Javier Martinez (2025)** — Rock and soil classification using thermal and SAR data in deep learning models
  1. "Urban Local Climate Zone Classification Through Deep Learning Using Spatio-temporal Thermal Imagery" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2026 — [journal article](https://doi.org/10.1016/j.rsase.2026.101889)
     - authors: Michaja van Capel, Azarakhsh Rafiee (supervisor: Rafiee), Roderik Lindenbergh
     - title similarity 0.49; abstract similarity n/a; year +1  (source: GDMC)
  2. "Integrating radar and multi-spectral data to detect cocoa crops: A deep learning approach" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2025 — [journal article](https://doi.org/10.1016/j.rsase.2025.101652)
     - authors: Adele Therias, Azarakhsh Rafiee (supervisor: Rafiee), Stef Lhermitte, Philip van der Lugt, Roderik Lindenbergh
     - title similarity 0.41; abstract similarity n/a; year +0  (source: GDMC)
  3. "Automated District-Level Energy Demand Modeling Using EnergyPlus Empowered by Digital Twin Technology" — ISPRS Geospatial Week 2025 "Photogrammetry & Remote Sensing for a Bett, 2025 — [conference paper](https://doi.org/10.5194/isprs-annals-x-g-2025-397-2025)
     - authors: Amin Jalilzadeh, Azarakhsh Rafiee (supervisor: Rafiee), Stefan De Graaf, Thaleia Konstantinou, Peter van Oosterom
     - title similarity 0.31; abstract similarity n/a; year +0  (source: GDMC)
- **Michail Michalas (2025)** — Super-Resolution for Enhanced Aerial Imagery
  1. "Cloud-based application for indoor daylight performance analysis through BIM-GIS Integration" — Building and Environment, Elsevier BV, 293, pp. 114376, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2026.114376)
     - authors: Yangyu Liu, Eleonora Brembilla, Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.35; abstract similarity n/a; year +1  (source: GDMC)
  2. "A comprehensive review and framework on the applications of digital twins for energy transition at the district level" — Renewable and Sustainable Energy Reviews, Elsevier BV, 234, pp. 116872, 2026 — [journal article](https://doi.org/10.1016/j.rser.2026.116872)
     - authors: Amin Jalilzadeh, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom, Thaleia Konstantinou
     - title similarity 0.35; abstract similarity n/a; year +1  (source: GDMC)
  3. "Construction method for topological integration of multi-scale datasets supported by a primal-dual data structure" — Geo-spatial Information Science, Informa UK Limited, pp. 1–18, 2026 — [journal article](https://doi.org/10.1080/10095020.2026.2731849)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (supervisor: Meijers)
     - title similarity 0.32; abstract similarity n/a; year +1  (source: GDMC)
  4. "Urban Local Climate Zone Classification Through Deep Learning Using Spatio-temporal Thermal Imagery" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2026 — [journal article](https://doi.org/10.1016/j.rsase.2026.101889)
     - authors: Michaja van Capel, Azarakhsh Rafiee (supervisor: Rafiee), Roderik Lindenbergh
     - title similarity 0.32; abstract similarity n/a; year +1  (source: GDMC)
  … and 4 more possible candidates; re-run with --limit/--surname to see them all.
- **Dimitrios Mouzakidis (2025)** — LADM-based 3D system for Archaeological Site Information Registration
  1. "Towards the architectural heritage information infrastructure: a UML-based information model linking HBIM, smart point clouds, and 3D Gaussian splatting" — Advanced Engineering Informatics, Elsevier BV, 76, pp. 16, 2026 — [journal article](https://doi.org/10.1016/j.aei.2026.105042)
     - authors: Yingwen Yu, Peter van Oosterom (supervisor: van Oosterom), Edward Verbree, Zhuoyue Wang, Uta Pottgiesser, Abeer Abu Raed, Yuyang Peng
     - title similarity 0.38; abstract similarity 0.15; year +1  (source: GDMC)
  2. "BIM/IFC-LADM mapping framework for Sarawak country profile" — Survey Review, Taylor and Francis, pp. 12, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2532947)
     - authors: Ainn Zamzuri, Alias Abdul Rahman, Muhammad Imzan Hassan, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.31; abstract similarity 0.22; year +0  (source: GDMC)
  3. "An OGC SensorThings GIS Pipeline For Estimating Seismic Engineering Demand Parameters" — ISPRS - Annals of the Photogrammetry, Remote Sensing and Spatial Infor, 2025 — [conference paper](https://doi.org/10.5194/isprs-annals-x-g-2025-787-2025)
     - authors: Justin Schembri, Azarakhsh Rafiee, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.32; abstract similarity 0.11; year +0  (source: GDMC)
  4. "How digital technologies have been applied for architectural heritage risk management: A systemic literature review from 2014 to 2024" — npj Heritage Science, Springer Nature, 13, pp. 1-15, 2025 — [journal article](https://doi.org/10.1038/s40494-025-01558-5)
     - authors: Yingwen Yu, Abeer Abu Raed, Yuyang Peng, Uta Pottgiesser, Edward Verbree, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.32; abstract similarity 0.11; year +0  (source: GDMC)
  … and 9 more possible candidates; re-run with --limit/--surname to see them all.
- **Rafał Marek Tarczyński (2025)** — ST-SimNet: A Spatio-Temporal Graph Neural Network for Urban Freight Forecasting
  1. "Cloud-based application for indoor daylight performance analysis through BIM-GIS Integration" — Building and Environment, Elsevier BV, 293, pp. 114376, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2026.114376)
     - authors: Yangyu Liu, Eleonora Brembilla, Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.36; abstract similarity n/a; year +1  (source: GDMC)
  2. "An nD-histogram technique for querying non-uniformly distributed point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 224, , 2025 — [journal article](https://doi.org/10.1016/j.isprsjprs.2025.03.014)
     - authors: Haicheng Liu, Zhiwei Li, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Chuqi Zhang
     - title similarity 0.34; abstract similarity n/a; year +0  (source: GDMC)
  3. "Urban Local Climate Zone Classification Through Deep Learning Using Spatio-temporal Thermal Imagery" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2026 — [journal article](https://doi.org/10.1016/j.rsase.2026.101889)
     - authors: Michaja van Capel, Azarakhsh Rafiee (supervisor: Rafiee), Roderik Lindenbergh
     - title similarity 0.32; abstract similarity n/a; year +1  (source: GDMC)
  4. "Construction method for topological integration of multi-scale datasets supported by a primal-dual data structure" — Geo-spatial Information Science, Informa UK Limited, pp. 1–18, 2026 — [journal article](https://doi.org/10.1080/10095020.2026.2731849)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (supervisor: Meijers)
     - title similarity 0.30; abstract similarity n/a; year +1  (source: GDMC)
- **Victoria Tsalapati (2025)** — Assessing The Impact of Tree 3D Representations on Urban Daylight Simulation Bas
  1. "Cloud-based application for indoor daylight performance analysis through BIM-GIS Integration" — Building and Environment, Elsevier BV, 293, pp. 114376, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2026.114376)
     - authors: Yangyu Liu, Eleonora Brembilla (supervisor: Brembilla), Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.31; abstract similarity n/a; year +1  (source: GDMC)
  2. "A comprehensive review and framework on the applications of digital twins for energy transition at the district level" — Renewable and Sustainable Energy Reviews, Elsevier BV, 234, pp. 116872, 2026 — [journal article](https://doi.org/10.1016/j.rser.2026.116872)
     - authors: Amin Jalilzadeh, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom, Thaleia Konstantinou
     - title similarity 0.33; abstract similarity n/a; year +1  (source: GDMC)
  3. "An OGC SensorThings GIS Pipeline For Estimating Seismic Engineering Demand Parameters" — ISPRS - Annals of the Photogrammetry, Remote Sensing and Spatial Infor, 2025 — [conference paper](https://doi.org/10.5194/isprs-annals-x-g-2025-787-2025)
     - authors: Justin Schembri, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom
     - title similarity 0.32; abstract similarity n/a; year +0  (source: GDMC)
  4. "Urban Local Climate Zone Classification Through Deep Learning Using Spatio-temporal Thermal Imagery" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2026 — [journal article](https://doi.org/10.1016/j.rsase.2026.101889)
     - authors: Michaja van Capel, Azarakhsh Rafiee (supervisor: Rafiee), Roderik Lindenbergh
     - title similarity 0.31; abstract similarity n/a; year +1  (source: GDMC)
- **Eirini Chrysovalantou Tsipa (2025)** — Usability of the vario-scale approach in interactive and dynamic mapping
  1. "A High-Performance Game Engine-GIS-CFD System for Interactive Urban Wind Decision Support" — Proceedings AGILE: GIScience Series (Tartu, Estonia), pp. 8, 2026 — [conference paper](https://agile-giss.copernicus.org/articles/7/49/2026/)
     - authors: Xuanchen Zhou, Azarakhsh Rafiee, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.39; abstract similarity 0.10; year +1  (source: GDMC)
  2. "Mapping the Edge: A Novel Approach to Georeferencing Historical Map Series" — e-Perimetron, 20(1), pp. 12-24, 2025 — [journal article](http://www.e-perimetron.org/Vol_20_1/Meijers_et_al.pdf)
     - authors: Martijn Meijers (supervisor: Meijers), Jules Schoonman
     - title similarity 0.42; abstract similarity n/a; year +0  (source: GDMC)
  3. "3D Gaussian Splatting for Modern Architectural Heritage: Integrating UAV-Based Data Acquisition and Advanced Photorealistic 3D Techniques" — Proceedings AGILE: GIScience Series (Dresden, Germany), pp. 9, 2025 — [conference paper](https://agile-giss.copernicus.org/articles/6/51/2025/)
     - authors: Yingwen Yu, Edward Verbree, Peter van Oosterom (supervisor: van Oosterom), Uta Pottgiesser
     - title similarity 0.33; abstract similarity 0.07; year +0  (source: GDMC)
  4. "Land administration domain model and 3D land administration" — Survey Review, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2561263)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Abdullah Kara, Eftychia Kalogianni
     - title similarity 0.39; abstract similarity 0.00; year +0  (source: OpenAlex)
  … and 5 more possible candidates; re-run with --limit/--surname to see them all.
- **Marieke van Arnhem (2025)** — Detecting Structural Building Changes from Bitemporal Point Cloud Datasets with 
  1. "Towards the architectural heritage information infrastructure: a UML-based information model linking HBIM, smart point clouds, and 3D Gaussian splatting" — Advanced Engineering Informatics, Elsevier BV, 76, pp. 16, 2026 — [journal article](https://doi.org/10.1016/j.aei.2026.105042)
     - authors: Yingwen Yu, Peter van Oosterom (supervisor: van Oosterom), Edward Verbree (supervisor: Verbree), Zhuoyue Wang, Uta Pottgiesser, Abeer Abu Raed, Yuyang Peng
     - title similarity 0.36; abstract similarity 0.09; year +1  (source: GDMC)
  2. "3D Gaussian Splatting for Modern Architectural Heritage: Integrating UAV-Based Data Acquisition and Advanced Photorealistic 3D Techniques" — Proceedings AGILE: GIScience Series (Dresden, Germany), pp. 9, 2025 — [conference paper](https://agile-giss.copernicus.org/articles/6/51/2025/)
     - authors: Yingwen Yu, Edward Verbree (supervisor: Verbree), Peter van Oosterom (supervisor: van Oosterom), Uta Pottgiesser
     - title similarity 0.31; abstract similarity 0.10; year +0  (source: GDMC)
  3. "Reframing the “H” in HBIM: from systematic review to UML-based conceptual modeling" — Frontiers of Architectural Research, Higher Education Press and KeAi/E, 2026 — [journal article](https://doi.org/10.1016/j.foar.2026.02.007)
     - authors: Yingwen Yu, Zhuoyue Wang, Peter van Oosterom (supervisor: van Oosterom), Uta Pottgiesser, Edward Verbree (supervisor: Verbree), Yuyang Peng
     - title similarity 0.32; abstract similarity 0.10; year +1  (source: GDMC)
  4. "LiDAR Point Cloud Virtual Reality Visual Evaluation Through Structural Similarity Index Measure and Edge Metric Similarity" — AGILE 2025 - 28th AGILE conference on Geographic Information Science (, 2025 — [conference paper](https://zenodo.org/doi/10.5281/zenodo.15324418)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.36; abstract similarity n/a; year +0  (source: GDMC)
  … and 5 more possible candidates; re-run with --limit/--surname to see them all.
- **Qiaorui Yang (2025)** — Integrating Spatial Knowledge Graphs and Graph Neural Networks for Clustering an
  1. "Integrating radar and multi-spectral data to detect cocoa crops: A deep learning approach" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2025 — [journal article](https://doi.org/10.1016/j.rsase.2025.101652)
     - authors: Adele Therias, Azarakhsh Rafiee (supervisor: Rafiee), Stef Lhermitte, Philip van der Lugt, Roderik Lindenbergh
     - title similarity 0.32; abstract similarity n/a; year +0  (source: GDMC)
  2. "An OGC SensorThings GIS Pipeline For Estimating Seismic Engineering Demand Parameters" — ISPRS - Annals of the Photogrammetry, Remote Sensing and Spatial Infor, 2025 — [conference paper](https://doi.org/10.5194/isprs-annals-x-g-2025-787-2025)
     - authors: Justin Schembri, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom
     - title similarity 0.30; abstract similarity n/a; year +0  (source: GDMC)
- **Carlo Cordes (2026)** — Spatio-temporal Transformers for Wildfire Risk Prediction
  1. "Cloud-based application for indoor daylight performance analysis through BIM-GIS Integration" — Building and Environment, Elsevier BV, 293, pp. 114376, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2026.114376)
     - authors: Yangyu Liu, Eleonora Brembilla, Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.39; abstract similarity n/a; year +0  (source: GDMC)
  2. "A High-Performance Game Engine-GIS-CFD System for Interactive Urban Wind Decision Support" — Proceedings AGILE: GIScience Series (Tartu, Estonia), pp. 8, 2026 — [conference paper](https://agile-giss.copernicus.org/articles/7/49/2026/)
     - authors: Xuanchen Zhou, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom
     - title similarity 0.31; abstract similarity n/a; year +0  (source: GDMC)
- **Giorgos Iliopoulos (2026)** — (Semi-)automatic modeling of indoor building 3D models for daylight simulation w
  1. "Semi-automated indoor geometry reconstruction for daylight simulation" — Building and Environment, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2025.114045)
     - authors: Nima Forouzandeh, Jin Huang, Liangliang Nan, Eleonora Brembilla (supervisor: Brembilla), Jantien Stoter
     - title similarity 0.54; abstract similarity n/a; year +0  (source: Crossref)
  2. "Cloud-based application for indoor daylight performance analysis through BIM-GIS Integration" — Building and Environment, Elsevier BV, 293, pp. 114376, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2026.114376)
     - authors: Yangyu Liu, Eleonora Brembilla (supervisor: Brembilla), Azarakhsh Rafiee
     - title similarity 0.35; abstract similarity n/a; year +0  (source: GDMC)
- **Yair Roorda (2026)** — Now you see me, now you don't: Direct LiDAR-Based Intervisibility Modeling with 
  1. "Smart point cloud–guided 3D gaussian splatting for urban modeling and data-driven analysis" — Sustainable Cities and Society, Elsevier BV, 149, pp. 107753, 2026 — [journal article](https://doi.org/10.1016/j.scs.2026.107753)
     - authors: Yingwen Yu, Zhuoyue Wang, Guanting Zhang, Peter van Oosterom (supervisor: van Oosterom), Edward Verbree, Steffen Nijhuis, Yuyang Peng
     - title similarity 0.32; abstract similarity 0.22; year +0  (source: GDMC)
  2. "Photorealistic Indoor Virtual Environments for Wayfinding: Exploring the Feasibility and Initial Evaluation of Gaussian Splatting in VR Simulation" — IOP Conference Series Earth and Environmental Science, 2026 — [conference paper](https://doi.org/10.1088/1755-1315/1647/1/012001)
     - authors: Adibah Nurul Yunisya, Edward Verbree, Peter van Oosterom (supervisor: van Oosterom), Sisi Zlatanova, Yingwen Yu
     - title similarity 0.40; abstract similarity 0.06; year +0  (source: OpenAlex)
  3. "Towards the architectural heritage information infrastructure: a UML-based information model linking HBIM, smart point clouds, and 3D Gaussian splatting" — Advanced Engineering Informatics, Elsevier BV, 76, pp. 16, 2026 — [journal article](https://doi.org/10.1016/j.aei.2026.105042)
     - authors: Yingwen Yu, Peter van Oosterom (supervisor: van Oosterom), Edward Verbree, Zhuoyue Wang, Uta Pottgiesser, Abeer Abu Raed, Yuyang Peng
     - title similarity 0.35; abstract similarity 0.09; year +0  (source: GDMC)
  4. "DELFT-UBEM: An automated database-driven pipeline for district-scale building energy modeling, demonstrated on Dutch district retrofit" — SSRN Electronic Journal, 2026 — [preprint](https://doi.org/10.2139/ssrn.6730719)
     - authors: Amin Jalilzadeh, Azarakhsh Rafiee, Thaleia Konstantinou, Stefan de Graaf, Henk Scholten, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.35; abstract similarity n/a; year +0  (source: OpenAlex)
  … and 1 more possible candidates; re-run with --limit/--surname to see them all.
- **Mingjie Teo (2026)** — IndoorGML-Constrained Navigation Across Multiple 3D Gaussian Splatting Scenes fo
  1. "Smart point cloud–guided 3D gaussian splatting for urban modeling and data-driven analysis" — Sustainable Cities and Society, Elsevier BV, 149, pp. 107753, 2026 — [journal article](https://doi.org/10.1016/j.scs.2026.107753)
     - authors: Yingwen Yu, Zhuoyue Wang, Guanting Zhang, Peter van Oosterom, Edward Verbree (supervisor: Verbree), Steffen Nijhuis, Yuyang Peng
     - title similarity 0.44; abstract similarity 0.19; year +0  (source: GDMC)
  2. "Photorealistic Indoor Virtual Environments for Wayfinding: Exploring the Feasibility and Initial Evaluation of Gaussian Splatting in VR Simulation" — IOP Conference Series Earth and Environmental Science, 2026 — [conference paper](https://doi.org/10.1088/1755-1315/1647/1/012001)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter van Oosterom, Sisi Zlatanova, Yingwen Yu
     - title similarity 0.44; abstract similarity 0.11; year +0  (source: OpenAlex)
  3. "Smart Point Cloud–Guided 3D Gaussian Splatting for Urban Modeling and Data-Driven Analysis" — SSRN Electronic Journal, 2026 — [preprint](https://doi.org/10.2139/ssrn.6094769)
     - authors: Yingwen Yu, Zhuoyue Wang, Guanting Zhang, Peter van Oosterom, Edward Verbree (supervisor: Verbree), Steffen NIJHUIS, Yuyang PENG
     - title similarity 0.44; abstract similarity n/a; year +0  (source: OpenAlex)
  4. "Towards the architectural heritage information infrastructure: a UML-based information model linking HBIM, smart point clouds, and 3D Gaussian splatting" — Advanced Engineering Informatics, Elsevier BV, 76, pp. 16, 2026 — [journal article](https://doi.org/10.1016/j.aei.2026.105042)
     - authors: Yingwen Yu, Peter van Oosterom, Edward Verbree (supervisor: Verbree), Zhuoyue Wang, Uta Pottgiesser, Abeer Abu Raed, Yuyang Peng
     - title similarity 0.33; abstract similarity 0.11; year +0  (source: GDMC)
  … and 2 more possible candidates; re-run with --limit/--surname to see them all.
- **Lars van Blokland (2026)** — Air temperature estimation through thermal satellite imagery using uncertainty-i
  1. "Urban Local Climate Zone Classification Through Deep Learning Using Spatio-temporal Thermal Imagery" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2026 — [journal article](https://doi.org/10.1016/j.rsase.2026.101889)
     - authors: Michaja van Capel, Azarakhsh Rafiee (supervisor: Rafiee), Roderik Lindenbergh (supervisor: Lindenbergh)
     - title similarity 0.38; abstract similarity n/a; year +0  (source: GDMC)
  2. "Cloud-based application for indoor daylight performance analysis through BIM-GIS Integration" — Building and Environment, Elsevier BV, 293, pp. 114376, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2026.114376)
     - authors: Yangyu Liu, Eleonora Brembilla, Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.31; abstract similarity n/a; year +0  (source: GDMC)
- **Sue Wang (2026)** — From IFC BIM to Semantically Enriched 2.5D Indoor Navigation Graphs for Congesti
  1. "Hierarchical Polygon-to-Point Collapsing for Multi-Scale Representation Based on the Straight Skeleton" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2026 — [conference paper](https://doi.org/10.5194/isprs-annals-xi-4-2026-21-2026)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (supervisor: Meijers)
     - title similarity 0.33; abstract similarity n/a; year +0  (source: GDMC)

## No candidates (90)

Oudman (2006), Duijnmayer (2009), Briels (2010), de Koning (2010), Possel (2010), Koudijs (2012), Rammos (2012), Heeres (2016), ten Kate (2017), Tryfona (2017), Griffioen (2018), Ortega-Córdova (2018), Arapakis (2019), Boersma (2019), Oldenburg (2019), Tzounakos (2019), Alexandridis (2020), de Groot (2020), Kaniouras (2020), Lánský (2020), Moscholaki (2020), Staring (2020), van Liempt (2020), Wiersma (2020), Alhoz (2021), Chatzidiakos (2021), de Jong (2021), de Jongh (2021), Hobeika (2021), Kenesei (2021), Papageorgiou (2021), Stevers (2021), van Heerden (2021), Apra (2022), Feenstra (2022), Fratzeskou (2022), Fu (2022), Hurkmans (2022), Langhorst (2022), Pantelios (2022), Papakostas (2022), Pavlidou (2022), Prihanggo (2022), Prusti (2022), van der Horst (2022), Dobson (2023), Dong (2023), Mbwanda (2023), Meschin (2023), Panagiotidou (2023), Powalka (2023), Visser (2023), Yan (2023), Brouwer (2024), Dechamps (2024), Dinklo (2024), Hengelmolen (2024), Kan (2024), Keurentjes (2024), Monté (2024), Poon (2024), Post (2024), Rao (2024), Spit (2024), Wei (2024), Zhang (2024)

No candidates found for 24 theses from 2025–2026 either, but those rarely have papers yet: Alting (2025), Chontos (2025), de Niet (2025), Manden (2025), Monahan (2025), Tew (2025), Aalders (2026), Auer (2026), Beeren (2026), Bi (2026), Brakelé (2026), Bry (2026), den Hartog (2026), Félix Aires (2026), Hu (2026), Hutama (2026), Joh (2026), Jonker (2026), Pille (2026), Rotteveel (2026), Schlosser (2026), Singh (2026), Vanderheeren (2026), Ye (2026)

## Calibration

Of the 18 entries that already link a paper and can be checked automatically, the search surfaced 17 as a candidate (the rest had a title too far from the thesis's, or were not in the sources for this run); 4 more have a paper link this script cannot verify automatically:

- surfaced — Xu (2024): record title (best similarity 1.00) — title 0.67, abstract n/a, student co-author: yes, supervisors among authors: 0/0
- surfaced — Roy (2022): doi 10.1080/13658816.2022.2160454 — title 0.65, abstract n/a, student co-author: yes, supervisors among authors: 1/1
- surfaced — Tufan (2022): doi 10.5194/isprs-archives-xlviii-4-w4-2022-169-2022 — title 1.00, abstract 0.86, student co-author: no, supervisors among authors: 0/1
- surfaced — Chen (2021): doi 10.1016/j.isprsjprs.2022.09.017 — title 0.72, abstract n/a, student co-author: yes, supervisors among authors: 2/2
- **missed** — Doan (2021): doi 10.5194/isprs-annals-v-4-2021-169-2021 (not among the candidates)
- surfaced — Giannelli (2021): doi 10.5194/isprs-annals-v-4-2022-275-2022 — title 0.47, abstract 0.28, student co-author: yes, supervisors among authors: 1/1
- surfaced — Lumban Gaol (2021): doi 10.1080/01490419.2022.2091696 — title 0.36, abstract n/a, student co-author: no, supervisors among authors: 1/1
- surfaced — Morlighem (2021): doi 10.1007/s44212-022-00011-3 — title 0.55, abstract 0.60, student co-author: yes, supervisors among authors: 1/1
- not automatically checkable — Dahle (2020): non-DOI, non-record link
- not automatically checkable — Zhang (2020): non-DOI, non-record link
- surfaced — Bouzas (2019): doi 10.1016/j.isprsjprs.2020.07.010 — title 0.80, abstract n/a, student co-author: yes, supervisors among authors: 1/1
- surfaced — Du (2019): doi 10.3390/rs11182074 — title 0.71, abstract 0.81, student co-author: yes, supervisors among authors: 2/2
- not automatically checkable — Flikweert (2019): non-DOI, non-record link
- not automatically checkable — Salheb (2019): non-DOI, non-record link
- surfaced — Wang (2018): doi 10.1080/19401493.2020.1729862 — title 0.47, abstract n/a, student co-author: yes, supervisors among authors: 4/4
- surfaced — Broersen (2016): doi 10.1016/j.cageo.2017.06.003 — title 0.73, abstract n/a, student co-author: yes, supervisors among authors: 2/2
- surfaced — Rook (2016): doi 10.5194/isprs-annals-iv-2-w1-23-2016 — title 0.68, abstract 0.49, student co-author: yes, supervisors among authors: 2/2
- surfaced — van der Ham (2015): doi 10.5194/isprs-annals-iv-4-w1-105-2016 — title 0.98, abstract 0.64, student co-author: yes, supervisors among authors: 2/2
- surfaced — van Winden (2014): doi 10.1111/tgis.12186 — title 0.50, abstract 0.62, student co-author: yes, supervisors among authors: 2/2
- surfaced — Boeters (2013): doi 10.1080/13658816.2015.1072201 — title 0.58, abstract n/a, student co-author: yes, supervisors among authors: 2/3
- surfaced — Donkers (2013): doi 10.1111/tgis.12162 — title 0.50, abstract 0.58, student co-author: yes, supervisors among authors: 3/3
- surfaced — Biljecki (2010): record title (best similarity 1.00) — title 1.00, abstract n/a, student co-author: yes, supervisors among authors: 2/2
