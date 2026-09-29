# Paper cross-check (2026-09-29)

The archive holds 314 theses, 38 of which already link a paper. The other 273 were compared against the GDMC publication list (838 scientific/conference papers), Crossref (searched per thesis on title and student author) and OpenAlex works of their supervisors and students, scoring candidates on co-authorship, title similarity and abstract similarity.

Accepted papers go into the entry's `paper:` field in _data/geotheses.yml (optionally `paper_label:`), several at once as a `papers:` list of {url, label} entries; rejected candidates go into scripts/verified_papers.yml with `verdict: not related`, and a thesis to skip entirely with `verdict: no papers`.

## Likely (76 theses)

Strong signals: the thesis's student as co-author (preferably first author) plus a clear title or abstract overlap.

- **Doğan Altundağ (2009)** — De-noising terrestrial laser scanning data for roughness characterization of roc
  1. "Influence of range measurement noise on roughness characterization of rock surfaces using terrestrial laser scanning" — International Journal of Rock Mechanics and Mining Sciences, 2011 — [journal article](https://doi.org/10.1016/j.ijrmms.2011.09.007)
     - authors: Kourosh Khoshelham (supervisor: Khoshelham), Dogan Altundag (student), Dominique Ngan-Tillard (supervisor: Ngan-Tillard), Massimo Menenti (supervisor: Menenti)
     - title similarity 0.54; abstract similarity n/a; year +2  (source: OpenAlex)
  2. "WAVELET DE-NOISING OF TERRESTRIAL LASER SCANNER DATA FOR THE CHARACTERIZATION OF ROCK SURFACE ROUGHNESS" — Data Archiving and Networked Services (DANS), 2010 — [conference paper](https://openalex.org/W2095901660)
     - authors: Kourosh Khoshelham (supervisor: Khoshelham), Dogan Altundag (student)
     - title similarity 0.82; abstract similarity 0.53; year +1  (source: OpenAlex)
  3. "Influence of laser scanner range measurement noise on the quantification of rock surface roughness : abstract." — University of Twente Research Information, 2010 — [conference paper](https://openalex.org/W1638838387)
     - authors: Kourosh Khoshelham (supervisor: Khoshelham), Dogan Altundag (student)
     - title similarity 0.45; abstract similarity n/a; year +1  (source: OpenAlex)
- **Mohamed Saleh (2011)** — Sediment classification using Sub-bottom profiler
  1. "Seabed sub-bottom sediment classification using parametric sub-bottom profiler" — NRIAG Journal of Astronomy and Geophysics, 2016 — [journal article](https://doi.org/10.1016/j.nrjag.2016.01.004)
     - authors: Mohamed Saleh (student; first author), Mostafa Rabah
     - title similarity 0.78; abstract similarity n/a; year +5  (source: Crossref)
  2. "Supply Chain Performance Measurement Approaches: Review and Classification" — The Journal of Organizational Management Studies, 2012 — [journal article](https://doi.org/10.5171/2012.872753)
     - authors: Nedaa Agami, Mohamed Saleh (student), Mohamed Rasmy
     - title similarity 0.36; abstract similarity n/a; year +1  (source: Crossref)
- **Bas van Goor (2011)** — Change detection and deformation analysis using Terrestrial Laser Scanning
  1. "Eolian sand transport monitored by terrestrial laser scanning" — Research Repository (Delft University of Technology), 2010 — [conference paper](https://openalex.org/W1540833395)
     - authors: Roderik Lindenbergh (supervisor: Lindenbergh), Sylvie Dijkstra-Soudarissanane, Sierd de Vries, M.A.J.P. Coquet, Matthieu A. de Schipper, Karolina Hejbudzka, K. Duijnmayer, B. Van Goor (student), Ariel Cohen
     - title similarity 0.58; abstract similarity 0.14; year -1  (source: OpenAlex)
- **Tom Commandeur (2012)** — Footprint decomposition combined with point cloud segmentation for producing val
  1. "Automated reconstruction of 3D input data for noise simulation" — Computers Environment and Urban Systems, 2019 — [journal article](https://doi.org/10.1016/j.compenvurbsys.2019.101424)
     - authors: Jantien Stoter, Ravi Peters, Tom Commandeur (student), Balázs Dukai, Kavisha Kumar, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.39; abstract similarity n/a; year +7  (source: OpenAlex)
- **Haicheng Liu (2014)** — Comparing NetCDF and a multidimensional array database on managing and querying 
  1. "Managing large multidimensional hydrologic datasets: A case study comparing NetCDF and SciDB" — Journal of Hydroinformatics, IWA Publishing, 20(5), pp. 1058-1070, 2018 — [journal article](https://doi.org/10.2166/hydro.2018.136)
     - authors: Haicheng Liu (student; first author), Peter van Oosterom (supervisor: van Oosterom), Theo Tijssen (supervisor: Tijssen), Tom Commandeur (supervisor: Commandeur), Wen Wang
     - title similarity 0.77; abstract similarity 0.66; year +4  (source: GDMC)
  2. "Managing Large Multidimensional Array Hydrologic Datasets: A Case Study Comparing NetCDF and SciDB" — Procedia Engineering, 154, pp. 207-214, 2016 — [journal article](https://doi.org/10.1016/j.proeng.2016.07.449)
     - authors: Haicheng Liu (student; first author), Peter van Oosterom (supervisor: van Oosterom), Chengfang Hu, Wen Wang
     - title similarity 0.85; abstract similarity 0.83; year +2  (source: GDMC)
  3. "The design and application of histogram trees for querying massive LiDAR point clouds" — Proceedings of 5th China LiDAR Conference, Xiamen, China, pp. 1-8, 201, 2019 — [conference paper](https://www.gdmc.nl/publications/2019/Design_Application_Histogram_Trees_Massive_LiDAR_Point_Clouds.pdf)
     - authors: Haicheng Liu (student; first author), Xuefeng Guan, Martijn Meijers, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.37; abstract similarity n/a; year +5  (source: GDMC)
  4. "Comparing NetCDF and SciDB on managing and querying 5D hydrologic dataset" — IOP Conference Series: Earth and Environmental Science, 2016 — [journal article](https://doi.org/10.1088/1755-1315/46/1/012031)
     - authors: Haicheng Liu (student; first author), Xiao Xiao
     - title similarity 0.69; abstract similarity n/a; year +2  (source: Crossref)
  5. "Towards a relational database Space Filling Curve (SFC) interface specification for managing nD-PointClouds" — Geoinformationssysteme 2019, Beiträge zur 6. Münchner GI-Runde (Thomas, 2019 — [conference paper](https://www.gdmc.nl/publications/2019/DBMS-nD-PC-GI-Runde2019.pdf)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Martijn Meijers, Edward Verbree, Haicheng Liu (student), Theo Tijssen (supervisor: Tijssen)
     - title similarity 0.37; abstract similarity n/a; year +5  (source: GDMC)
- **Elise Tierie (2014)** — Visualisation conformity of three dimensional IMGeo for emergency response
  1. "Trauma-Related Clinical Practice Variation in Dutch Emergency Departments" — Healthcare, 2023 — [journal article](https://doi.org/10.3390/healthcare11050748)
     - authors: Elise L. Tierie (student; first author), Dennis G. Barten, Laura M. Esteve Cuevas, Rebekka Veugelers, Menno I. Gaakeer
     - title similarity 0.35; abstract similarity 0.06; year +9  (source: Crossref)
- **Weilin Xu (2014)** — Spatial model-aided indoor tracking
  1. "LEVERAGING SPATIAL MODEL TO IMPROVE INDOOR TRACKING" — The International Archives of the Photogrammetry, Remote Sensing and S, 2015 — [journal article](https://doi.org/10.5194/isprsarchives-xl-4-w5-75-2015)
     - authors: L. Liu (supervisor: Liu), W. Xu (student), W. Penard, S. Zlatanova
     - title similarity 0.74; abstract similarity 0.33; year +1  (source: Crossref)
  2. "A 3D Model Based Indoor Navigation System for Hubei Provincial Museum" — ISPRS Archives Volume XL-4/W4, ISPRS Acquisition and Modelling of Indo, 2013 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-4-w4-51-2013)
     - authors: W. Xu (student; first author), M. Kruminaite, B. Onrust, H. Liu (supervisor: Liu), Q. Xiong, S. Zlatanova
     - title similarity 0.42; abstract similarity n/a; year -1  (source: GDMC)
  3. "A pedestrian tracking algorithm using grid-based indoor model" — Automation in Construction, 2018 — [journal article](https://doi.org/10.1016/j.autcon.2018.03.031)
     - authors: Weilin Xu (student; first author), Liu Liu (supervisor: Liu), Sisi Zlatanova, Wouter Penard, Qing Xiong
     - title similarity 0.38; abstract similarity n/a; year +4  (source: Crossref)
- **Milo Janssen (2015)** — 3D Intersection operations for voxel data represented as surfaces in GIS
  1. "Installed base registration of decentralised solar panels with applications in crisis management" — ISPRS Archives Volume XL-3/W3, ISPRS Geospatial Week 2015 (S. Zlatanov, 2015 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-3-w3-219-2015)
     - authors: R. Aarsen, M. Janssen (student), M. Ramkisoen, F. Biljecki, C.W. Quak, E. Verbree
     - title similarity 0.39; abstract similarity n/a; year +0  (source: GDMC)
- **Antigoni Makri (2015)** — Indoor Signposting and Wayfinding through an Adaptation of the Dutch cyclist Jun
  1. "An Approach for Indoor Wayfinding replicating main Principles of an outdoor Navigation System for Cyclists" — ISPRS Archives Volume XL-4/W5, Indoor-Outdoor Seamless Modelling, Mapp, 2015 — [conference paper](https://doi.org/10.5194/isprsarchives-xl-4-w5-29-2015)
     - authors: A. Makri (student; first author), S. Zlatanova, E. Verbree (supervisor: Verbree)
     - title similarity 0.40; abstract similarity 0.58; year +0  (source: GDMC)
  2. "Indoor Signposting and Wayfinding through an Adaptation of the Dutch Cyclist Junction Network System" — Proceedings of the 11th International Symposium on Location-Based Serv, 2014 — [conference paper](https://www.gdmc.nl/publications/2014/Indoor_Signposting_and_Wayfinding.pdf)
     - authors: Antigoni Makri (student; first author), Edward Verbree (supervisor: Verbree)
     - title similarity 1.00; abstract similarity n/a; year -1  (source: GDMC)
- **Benny Onrust (2015)** — Automatic generation of plant distributions for existing and future natural envi
  1. "Ecologically Sound Procedural Generation of Natural Environments" — International Journal of Computer Games Technology, 2017 — [journal article](https://doi.org/10.1155/2017/7057141)
     - authors: Benny Onrust (student; first author), Rafael Bidarra, Robert Rooseboom, Johan van de Koppel
     - title similarity 0.45; abstract similarity 0.35; year +2  (source: Crossref)
  2. "Procedural generation and interactive web visualization of natural environments" — Proceedings of the 20th International Conference on 3D Web Technology, 2015 — [conference paper](https://doi.org/10.1145/2775292.2775306)
     - authors: Benny Onrust (student; first author), Rafael Bidarra, Robert Rooseboom, Johan van de Koppel
     - title similarity 0.50; abstract similarity n/a; year +0  (source: Crossref)
- **Haoxiang Wu (2015)** — Integration of 2D architectural floor plans into Indoor OpenStreetMap for recons
  1. "Extrusion-to-Masoning: Robotic 3D Concrete Printing of Concrete Shells As Building Floor System" — CAADRIA proceedings, 2023 — [conference paper](https://doi.org/10.52842/conf.caadria.2023.2.139)
     - authors: Hao Wu (student; first author), Sijia Gu, Xiaofan Gao, Jiaxiang Luo, Philip F. Yuan*
     - title similarity 0.37; abstract similarity n/a; year +8  (source: Crossref)
- **Kaixuan Zhou (2015)** — Exploring Regularities for Improving Quality of Facade Reconstruction from Point
  1. "EXPLORING REGULARITIES FOR IMPROVING FAÇADE RECONSTRUCTION FROM POINT CLOUDS" — The International Archives of the Photogrammetry, Remote Sensing and S, 2016 — [journal article](https://doi.org/10.5194/isprs-archives-xli-b5-749-2016)
     - authors: K. Zhou (student; first author), B. Gorte (supervisor: Gorte), S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.93; abstract similarity 0.61; year +1  (source: Crossref)
- **Florian W. Fichtner (2016)** — Semantic enrichment of a point cloud based on an octree for multi-storey pathfin
  1. "Semantic enrichment of octree structured point clouds for multi‐story 3D pathfinding" — Transactions in GIS, 2018 — [journal article](https://doi.org/10.1111/tgis.12308)
     - authors: Florian W. Fichtner (student; first author), Abdoulaye A. Diakité (supervisor: Diakite), Sisi Zlatanova (supervisor: Zlatanova), Robert Voûte
     - title similarity 0.76; abstract similarity 0.59; year +2  (source: OpenAlex)
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
     - authors: Eftychia Kalogianni (student; first author), Efi Dimopoulou, Wilko Quak (supervisor: Quak), Michael Germann, Lorenz Jenni, Peter van Oosterom (supervisor: van Oosterom), Ruba Jaljolie, Sagi Dalyot
     - title similarity 0.45; abstract similarity 0.48; year +1  (source: GDMC)
  2. "Refining the survey model of the LADM ISO 19152–2: Land registration" — Land Use Policy, Elsevier BV, 141, pp. 107125, 2024 — [journal article](https://www.sciencedirect.com/science/article/pii/S0264837724000772)
     - authors: Eftychia Kalogianni (student; first author), Efi Dimopoulou, Hans-Christoph Gruler, Erik Stubkjær, Javier Morales, Christiaan Lemmen, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.37; abstract similarity 0.40; year +8  (source: GDMC)
  3. "Refining the Legal Land Administration-related Aspects in LADM" — Proceedings of the 10th FIG Land Administration Domain Model Workshop , 2022 — [conference paper](https://www.gdmc.nl/publications/2022/LADM2022_paper_LegalRefinement.pdf)
     - authors: Eftychia Kalogianni (student; first author), Abdullah Kara, Anthony Beck, Jesper M. Paasch, Jaap Zevenbergen, Efi Dimopoulou, Dimitrios Kitsakis, Peter van Oosterom (supervisor: van Oosterom), Christiaan Lemmen
     - title similarity 0.50; abstract similarity n/a; year +6  (source: GDMC)
  4. "Investigating 3D spatial unit’s as basis for refined 3D spatial profiles in the context of LADM revision" — Proceedings of the 6th International Workshop on 3D Cadastres (Peter v, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/3DCadWorkshop2018_10.pdf)
     - authors: Eftychia Kalogianni (student; first author), Efi Dimopoulou, Rod Thompson, Christiaan Lemmen, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.37; abstract similarity n/a; year +2  (source: GDMC)
  5. "Modelling the legal spaces of 3D underground objects in 3D land administration systems" — Land Use Policy, Elsevier BV, 127, pp. 106537, 2023 — [journal article](https://www.sciencedirect.com/science/article/pii/S0264837723000030)
     - authors: Rohit Ramlakhan, Eftychia Kalogianni (student), Peter van Oosterom (supervisor: van Oosterom), Behnam Atazadeh
     - title similarity 0.56; abstract similarity 0.36; year +7  (source: GDMC)
  6. "Modelling 3D legal spaces of Public Law Restrictions within the context of LADM revision" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:a116493a-2cb6-4781-b2c4-3f2c94611ad8)
     - authors: Dimitrios Kitsakis, Eftychia Kalogianni (student), Efi Dimopoulou, Jaap Zevenbergen, Peter van Oosterom (supervisor: van Oosterom), Kitsakis, Dimitrios, Kalogianni, Eftychia (student), Dimopoulou, Efi, Zevenbergen, Jaap, van Oosterom, Peter
     - title similarity 0.43; abstract similarity 0.33; year +5  (source: GDMC)
  7. "Modelling 3D underground legal spaces in 3D Land Administration Systems" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:4a499efb-f348-456b-9965-65c47519337a)
     - authors: Rohit Ramlakhan, Eftychia Kalogianni (student), Peter van Oosterom (supervisor: van Oosterom), Ramlakhan, Rohit, Kalogianni, Eftychia (student), van Oosterom , Peter
     - title similarity 0.43; abstract similarity 0.33; year +5  (source: GDMC)
  8. "The Foundation of Edition II of the Land Administration Domain Model" — Proceedings of the FIG Working Week 2021, Online, pp. 17, 2021 — [conference paper](https://fig.net/resources/proceedings/fig_proceedings/fig2021/papers/ws_03.4/WS_03.4_abdullah_indrajit_et_al_11163.pdf)
     - authors: Christiaan Lemmen, Alattas Abdullah, Agung Indrajit, Kalogianni Eftychia (student), Abdullah Kara, Peter van Oosterom (supervisor: van Oosterom), Peter Oukes, Abdullah Alattas, Eftychia Kalogianni (student)
     - title similarity 0.51; abstract similarity 0.25; year +5  (source: GDMC)
  9. "BIM Models as input for 3D Land Administration Systems for Apartment Registration" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:5e240a06-5fdf-4354-9e6d-09c675f1cd8b)
     - authors: Marjan Broekhuizen, Eftychia Kalogianni (student), Peter van Oosterom (supervisor: van Oosterom), Broekhuizen, Marjan, Kalogianni, Eftychia (student), van Oosterom, Peter
     - title similarity 0.40; abstract similarity 0.33; year +5  (source: GDMC)
  10. "Bridging Sustainable Development Goals and Land Administration: The Role of the ISO 19152 Land Administration Domain Model in SDG Indicator Formalization" — Land, MDPI AG, 13(491), pp. 27, 2024 — [journal article](https://doi.org/10.3390/land13040491)
     - authors: Mengying Chen, Peter Van Oosterom (supervisor: van Oosterom), Eftychia Kalogianni (student), Paula Dijkstra, Christiaan Lemmen
     - title similarity 0.48; abstract similarity 0.17; year +8  (source: GDMC)
  … and 9 more likely candidates; re-run with --limit/--surname to see them all.
- **Martijn Koopman (2016)** — 3D Path-finding in a voxelized model of an indoor environment
  1. "Universal path planning for an indoor drone" — Automation in Construction, 2018 — [journal article](https://doi.org/10.1016/j.autcon.2018.07.025)
     - authors: Fangyu Li, Sisi Zlatanova (supervisor: Zlatanova), Martijn Koopman (student), Xueying Bai, Abdoulaye Diakité
     - title similarity 0.48; abstract similarity n/a; year +2  (source: OpenAlex)
- **Olivier Rodenberg (2016)** — The effect of A* pathfinding characteristics on the path length and performance 
  1. "Indoor A* Pathfinding through an Octree Representation of a Point Cloud" — Chapter in: ISPRS Annals Volume IV-2/W1, 11th 3D Geoinfo Conference (E, 2016 — [conference paper](https://doi.org/10.5194/isprs-annals-iv-2-w1-249-2016)
     - authors: O. Rodenberg (student; first author), E. Verbree (supervisor: Verbree), S. Zlatanova (supervisor: Zlatanova), O. B. P. M. Rodenberg (student)
     - title similarity 0.60; abstract similarity 0.65; year +0  (source: GDMC)
  2. "Using a linear octree to identify empty space in indoor point clouds for 3D pathfinding" — Proceedings of the 19th AGILE International Conference on Geographic I, 2016 — [conference paper](https://www.gdmc.nl/publications/2016/Linear_octree_identify_empty_space_indoor_point_clouds.pdf)
     - authors: Tom Broersen, Florian W. Fichtner, Erik J. Heeres, Ivo de Liefde, Olivier B.P.M. Rodenberg (student), Edward Verbree (supervisor: Verbree), Robert Vo&ucirc;te
     - title similarity 0.36; abstract similarity n/a; year +0  (source: GDMC)
- **Adrie Rovers (2016)** — Exploring the use of a generic spatial access method for caching and efficient r
  1. "Using a generic spatial access method for caching and efficient retrieval of vario-scale data in a server-client architecture" — Proceedings of the 20th AGILE Conference on Geographic Information Sci, 2017 — [conference paper](https://www.gdmc.nl/publications/2017/SpatialAccessMethodVarioScaleServer.pdf)
     - authors: Adrie Rovers (student; first author), Martijn Meijers (supervisor: Meijers), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.88; abstract similarity n/a; year +1  (source: GDMC)
- **Yuxuan Kang (2017)** — Straightening and simplifying a multi-view stereo mesh of a city
  1. "A2B: Identifying movement patterns from largescale Wi-Fi based location data" — Proceedings of the 13th International Conference on Location Based Ser, 2016 — [conference paper](https://www.gdmc.nl/publications/2016/A2B_Identifying_movement_patterns_largescale_Wi-Fi.pdf)
     - authors: S.C. van der Spek, E. Verbree, M. Bon, X.A. den Duijn, B. Dukai, S.J. Griffioen, Y. Kang (student), M. Vermeer
     - title similarity 0.39; abstract similarity n/a; year -1  (source: GDMC)
- **Stella Psomadaki (2017)** — Using a Space Filling Curve for the Management of Dynamic Point Cloud Data in a 
  1. "Using a Space Filling Curve Approach for the Management of Dynamic Point Clouds" — Chapter in: ISPRS Annals Volume IV-2/W1, 11th 3D Geoinfo Conference (E, 2016 — [conference paper](https://doi.org/10.5194/isprs-annals-iv-2-w1-107-2016)
     - authors: Stella Psomadaki (student; first author), Peter van Oosterom (supervisor: van Oosterom), Theo Tijssen (supervisor: Tijssen), Fedor Baart, S. Psomadaki (student)
     - title similarity 0.81; abstract similarity 0.68; year -1  (source: GDMC)
  2. "Utilizing a Discrete Global Grid System for Handling Point Clouds with Varying Locations, Times, and Levels of Detail" — Cartographica, University of Toronto Press, 51(1), pp. 4-15, 2019 — [journal article](https://doi.org/10.3138/cart.54.1.2018-0009)
     - authors: Neeraj Sirdeshmukh, Edward Verbree, Peter van Oosterom (supervisor: van Oosterom), Stella Psomadaki (student), Martin Kodde
     - title similarity 0.40; abstract similarity 0.47; year +2  (source: GDMC)
- **Pieter Soffers (2017)** — Designing an integrated future data model for survey data and cadastral mapping
  1. "The new, LADM inspired, data model of the Dutch cadastral map" — Land Use Policy, 2022 — [journal article](https://doi.org/10.1016/j.landusepol.2022.106074)
     - authors: Eric Hagemans, Eva-Maria Unger, Pieter Soffers (student), Tom Wortel, Christiaan Lemmen
     - title similarity 0.53; abstract similarity n/a; year +5  (source: Crossref)
- **Bart Staats (2017)** — Identification of walkable space in a voxel model, derived from a point cloud an
  1. "AUTOMATIC GENERATION OF INDOOR NAVIGABLE SPACE USING A POINT CLOUD AND ITS SCANNER TRAJECTORY" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2017 — [journal article](https://doi.org/10.5194/isprs-annals-iv-2-w4-393-2017)
     - authors: B. R. Staats (student; first author), A. A. Diakité, R. L. Voûte, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.59; abstract similarity 0.61; year +0  (source: Crossref)
  2. "Detection of doors in a voxel model, derived from a point cloud and its scanner trajectory, to improve the segmentation of the walkable space" — International Journal of Urban Sciences, 2018 — [journal article](https://doi.org/10.1080/12265934.2018.1553685)
     - authors: B. R. Staats (student; first author), A. A. Diakité, R. L. Voûte, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.61; abstract similarity n/a; year +1  (source: Crossref)
  3. "AUTOMATIC EXTRACTION OF A NAVIGATION GRAPH INTENDED FOR INDOORGML FROM AN INDOOR POINT CLOUD" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2019 — [journal article](https://doi.org/10.5194/isprs-annals-iv-2-w5-271-2019)
     - authors: P. Flikweert, R. Peters, L. Díaz-Vilariño, R. Voûte, B. Staats (student)
     - title similarity 0.43; abstract similarity 0.51; year +2  (source: Crossref)
- **Barbara Cemellini (2018)** — Web-based visualization of 3D cadastre
  1. "Usability testing of a web-based 3D Cadastral visualization system" — Proceedings of the 6th International Workshop on 3D Cadastres (Peter v, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/3DCadWorkshop2018_29.pdf)
     - authors: Barbara Cemellini (student; first author), Rod Thompson (supervisor: Thompson), Peter van Oosterom (supervisor: van Oosterom), Marian de Vries (supervisor: de Vries)
     - title similarity 0.53; abstract similarity n/a; year +0  (source: GDMC)
  2. "Design, development and usability testing of an LADM compliant 3D Cadastral prototype system" — Land Use Policy, Elsevier, 98(104418), pp. 1-24, 2020 — [journal article](https://doi.org/10.1016/j.landusepol.2019.104418)
     - authors: Barbara Cemellini (student; first author), Peter van Oosterom (supervisor: van Oosterom), Rod Thompson (supervisor: Thompson), Marian de Vries (supervisor: de Vries)
     - title similarity 0.36; abstract similarity n/a; year +2  (source: GDMC)
  3. "Visualization/dissemination of 3D Cadastre" — Proceedings of the FIG Congress 2018, Istanbul, pp. 30, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/TS05C_cemellini_rod_et_al_9591.pdf)
     - authors: Barbara Cemellini (student; first author), Thompson Rod, Marian de Vries (supervisor: de Vries), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.70; abstract similarity n/a; year +0  (source: GDMC)
  4. "Results of the Public Usability Testing of a Web-Based 3D Cadastral Visualization System" — Proceedings of the FIG Working Week 2019, Hanoi, Vietnam, pp. 15, 2019 — [conference paper](http://www.fig.net/resources/proceedings/fig_proceedings/fig2019/papers/ts06c/TS06C_van_oosterom_de_vries_et_al_10082.pdf)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Marian de Vries (supervisor: de Vries), Barbara Cemellini (student), Rod Thompson (supervisor: Thompson)
     - title similarity 0.44; abstract similarity n/a; year +1  (source: GDMC)
  5. "Developing an LADM Compliant Dissemination and Visualization System for 3D Spatial Units" — Proceedings of the 7th Land Administration Domain Model Workshop, Zagr, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/07-26_LADM_2018.pdf)
     - authors: Rod Thompson (supervisor: Thompson), Peter van Oosterom (supervisor: van Oosterom), Barbara Cemellini (student), Marian de Vries (supervisor: de Vries)
     - title similarity 0.44; abstract similarity n/a; year +0  (source: GDMC)
  6. "Developing an LADM Compliant Dissemination and Visualization System for 3D Spatial Units" — Research Repository (Delft University of Technology), 2020 — [conference paper](https://doi.org/10.4233/uuid:57b1dfb4-74c8-4393-b997-5ae6484ae913)
     - authors: Thompson, Rod, van Oosterom, Peter, Cemellini, Barbara (student), de Vries, Marian
     - title similarity 0.44; abstract similarity 0.31; year +2  (source: OpenAlex)
- **Antria Christodoulou (2018)** — An image-based method for the pairwise registration of mobile laser scanning poi
  1. "Image-based Method for the Pairwise Registration of Mobile Laser Scanning Point Clouds" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLII-4/93/2018/)
     - authors: Antria Christodoulou (student; first author), Peter van Oosterom (supervisor: van Oosterom), A. Christodoulou (student)
     - title similarity 1.00; abstract similarity 0.79; year +0  (source: GDMC)
- **Xander den Duijn (2018)** — A 3D data modeling approach for integrated management of below and above ground 
  1. "MODELLING BELOW- AND ABOVE-GROUND UTILITY NETWORK FEATURES WITH THE CITYGML UTILITY NETWORK ADE: EXPERIENCES FROM ROTTERDAM" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2018 — [journal article](https://doi.org/10.5194/isprs-annals-iv-4-w7-43-2018)
     - authors: X. den Duijn (student; first author), G. Agugiaro, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.51; abstract similarity 0.76; year +0  (source: Crossref)
  2. "3D Approach for Representing Uncertainties of Underground Utility Data" — Computing in Civil Engineering 2017, 2017 — [conference paper](https://doi.org/10.1061/9780784480823.044)
     - authors: L. L. olde Scholtenhuis, S. Zlatanova (supervisor: Zlatanova), X. den Duijn (student)
     - title similarity 0.49; abstract similarity n/a; year -1  (source: Crossref)
- **Balázs Dukai (2018)** — Exploring the automatic Level of Detail inference for the validation of building
  1. "3dfier: automatic reconstruction of 3D city models" — The Journal of Open Source Software, 2021 — [journal article](https://doi.org/10.21105/joss.02866)
     - authors: Hugo Ledoux, Filip Biljecki (supervisor: Biljecki), Balázs Dukai (student), Kavisha Kumar, Ravi Peters, Jantien Stoter, Tom Commandeur
     - title similarity 0.52; abstract similarity 0.21; year +3  (source: OpenAlex)
  2. "QUALITY ASSESSMENT OF A NATIONWIDE DATA SET CONTAINING AUTOMATICALLY RECONSTRUCTED 3D BUILDING MODELS" — The International Archives of the Photogrammetry, Remote Sensing and S, 2021 — [journal article](https://doi.org/10.5194/isprs-archives-xlvi-4-w4-2021-17-2021)
     - authors: B. Dukai (student; first author), R. Peters, S. Vitalis, J. van Liempt, J. Stoter
     - title similarity 0.40; abstract similarity 0.31; year +3  (source: Crossref)
  3. "Automated 3D Reconstruction of LoD2 and LoD1 Models for All 10 Million Buildings of the Netherlands" — Photogrammetric Engineering &amp; Remote Sensing, 2022 — [journal article](https://doi.org/10.14358/pers.21-00032r2)
     - authors: Ravi Peters, Balázs Dukai (student), Stelios Vitalis, Jordi van Liempt, Jantien Stoter
     - title similarity 0.37; abstract similarity 0.26; year +4  (source: Crossref)
- **Weiran Li (2018)** — Detection of subsurface meltwater in East Antarctica using SAR Interferometry
  1. "The potential of InSAR for assessing meltwater lake dynamics on Antarctic ice shelves" — ?, 2021 — [posted-content](https://doi.org/10.5194/tc-2021-169)
     - authors: Weiran Li (student; first author), Stef Lhermitte (supervisor: Lhermitte), Paco López-Dekker
     - title similarity 0.48; abstract similarity 0.29; year +3  (source: Crossref)
  2. "The potential of synthetic aperture radar interferometry for assessing meltwater lake dynamics on Antarctic ice shelves" — The Cryosphere, 2021 — [journal article](https://doi.org/10.5194/tc-15-5309-2021)
     - authors: Weiran Li (student; first author), Stef Lhermitte (supervisor: Lhermitte), Paco López-Dekker
     - title similarity 0.36; abstract similarity 0.27; year +3  (source: Crossref)
  3. "Ship detection in a large scene SAR image using image uniformity description factor" — 2017 SAR in Big Data Era: Models, Methods and Applications (BIGSARDATA, 2017 — [conference paper](https://doi.org/10.1109/bigsardata.2017.8124933)
     - authors: Weike Li (student; first author), Bin Zou, Lamei Zhang
     - title similarity 0.40; abstract similarity n/a; year -1  (source: Crossref)
- **Neeraj Sirdeshmukh (2018)** — Utilizing a Discrete Global Grid System For Handling Point Clouds With Varying L
  1. "Utilizing a Discrete Global Grid System for Handling Point Clouds with Varying Locations, Times, and Levels of Detail" — Cartographica, University of Toronto Press, 51(1), pp. 4-15, 2019 — [journal article](https://doi.org/10.3138/cart.54.1.2018-0009)
     - authors: Neeraj Sirdeshmukh (student; first author), Edward Verbree (supervisor: Verbree), Peter van Oosterom (supervisor: van Oosterom), Stella Psomadaki, Martin Kodde
     - title similarity 1.00; abstract similarity 0.77; year +1  (source: GDMC)
- **Martijn Vermeer (2018)** — Large-scale efficient extraction of 3D roof segments from aerial stereo imagery
  1. "A quick-scan method to assess photovoltaic rooftop potential based on aerial imagery and LiDAR" — Solar Energy, 2020 — [journal article](https://doi.org/10.1016/j.solener.2020.07.035)
     - authors: Tim N.C. de Vries, Joris Bronkhorst, Martijn Vermeer (student), Jaap C.B. Donker, Sven A. Briels, Hesan Ziar, Miro Zeman, Olindo Isabella
     - title similarity 0.39; abstract similarity n/a; year +2  (source: Crossref)
  2. "Terrain-Informed Self-Supervised Learning: Enhancing Building Footprint Extraction From LiDAR Data With Limited Annotations" — IEEE Transactions on Geoscience and Remote Sensing, 2024 — [journal article](https://doi.org/10.1109/tgrs.2024.3391391)
     - authors: Anuja Vats, David Völgyes, Martijn Vermeer (student), Marius Pedersen, Kiran Raja, Daniele S. M. Fantin, Jacob Alexander Hay
     - title similarity 0.36; abstract similarity n/a; year +6  (source: Crossref)
- **Niek Bebelaar (2019)** — Correction Model for Particulate Matter Measurements with a Low-Cost Sensor Netw
  1. "Monitoring urban environmental phenomena through a wireless distributed sensor network" — Smart and Sustainable Built Environment, Emerald, 7(1), pp. 68-79, 2018 — [journal article](https://doi.org/10.1108/sasbe-10-2017-0046)
     - authors: Niek Bebelaar (student; first author), Robin Christian Braggaar, Catharina Marianne Kleijwegt, Roeland Willem Erik Meulmeester, Gina Michailidou, Nebras Salheb, Stefan van der Spek, Noortje Vaissier, Edward Verbree
     - title similarity 0.36; abstract similarity 0.48; year -1  (source: GDMC)
- **Fanny Bot (2019)** — A graph-matching approach to indoor localization: Using a mobile device and a re
  1. "A graph-matching approach to indoor localization using a mobile device and a reference BIM" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2019 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-2-w13-761-2019)
     - authors: Fanny Bot (student; first author), Pirouz Nourian (supervisor: Nourian), Edward Verbree (supervisor: Verbree), F. J. Bot (student)
     - title similarity 1.00; abstract similarity 0.82; year +0  (source: GDMC)
- **Francisco Gabriel Garcia Gonzalez (2019)** — An interactive design tool for urban planning using the size of the living space
  1. "AN INTERACTIVE DESIGN TOOL FOR URBAN PLANNING USING THE SIZE OF THE LIVING SPACE AS UNIT OF MEASUREMENT" — The International Archives of the Photogrammetry, Remote Sensing and S, 2019 — [journal article](https://doi.org/10.5194/isprs-archives-xlii-4-w15-3-2019)
     - authors: F. G. García González (student; first author), G. Agugiaro (supervisor: Agugiaro), R. Cavallo
     - title similarity 1.00; abstract similarity 0.87; year +0  (source: Crossref)
  2. "The City of Tomorrow from… the Data of Today" — ISPRS International Journal of Geo-Information, 2020 — [journal article](https://doi.org/10.3390/ijgi9090554)
     - authors: Giorgio Agugiaro (supervisor: Agugiaro), Francisco González (student), Roberto Cavallo
     - title similarity 0.23; abstract similarity 0.58; year +1  (source: OpenAlex)
- **Meylin Herrera Herrera (2019)** — Landslide Detection using Random Forest Classifier
  1. "Multi-Regional landslide detection using combined unsupervised and supervised machine learning" — Geomatics, Natural Hazards and Risk, 2021 — [journal article](https://doi.org/10.1080/19475705.2021.1912196)
     - authors: Faraz S. Tehrani, Giorgio Santinelli, Meylin Herrera Herrera (student)
     - title similarity 0.47; abstract similarity n/a; year +2  (source: Crossref)
- **Cathelijne Kleijwegt (2019)** — Establishing an object identification method based on the description of the nei
  1. "Monitoring urban environmental phenomena through a wireless distributed sensor network" — Smart and Sustainable Built Environment, Emerald, 7(1), pp. 68-79, 2018 — [journal article](https://doi.org/10.1108/sasbe-10-2017-0046)
     - authors: Niek Bebelaar, Robin Christian Braggaar, Catharina Marianne Kleijwegt (student), Roeland Willem Erik Meulmeester, Gina Michailidou, Nebras Salheb, Stefan van der Spek, Noortje Vaissier, Edward Verbree
     - title similarity 0.36; abstract similarity n/a; year -1  (source: GDMC)
- **Pablo Ruben (2019)** — 3D City Models in the Context of Urban Mining
  1. "3D CITY MODELS FOR URBAN MINING: POINT CLOUD BASED SEMANTIC ENRICHMENT FOR SPECTRAL VARIATION IDENTIFICATION IN HYPERSPECTRAL IMAGERY" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2020 — [journal article](https://doi.org/10.5194/isprs-annals-v-4-2020-223-2020)
     - authors: P. A. Ruben (student; first author), R. Sileryte (supervisor: Šileryte), G. Agugiaro (supervisor: Agugiaro)
     - title similarity 0.32; abstract similarity 0.54; year +1  (source: Crossref)
- **Melika Sajadian (2019)** — Spatial and Temporal Analysis of Road Deformation based on Remote Sensing and Su
  1. "Predicting land deformation by integrating InSAR data and cone penetration testing through machine learning techniques" — Proceedings of the International Association of Hydrological Sciences,, 2020 — [journal article](https://doi.org/10.5194/piahs-382-525-2020)
     - authors: Melika Sajadian (student; first author), Ana Teixeira, Faraz S. Tehrani, Mathias Lemmens (supervisor: Lemmens)
     - title similarity 0.39; abstract similarity n/a; year +1  (source: GDMC)
- **Dimitris Xenakis (2019)** — Placement optimization of Positioning Nodes: Maximizing the distinction of Indoo
  1. "Placement optimization of positioning nodes: Maximizing the distinction of indoor zones" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2019 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-2-w13-909-2019)
     - authors: Dimitris Xenakis (student; first author), Martijn Meijers (supervisor: Meijers), Edward Verbree (supervisor: Verbree), D. Xenakis (student)
     - title similarity 1.00; abstract similarity 0.84; year +0  (source: GDMC)
- **Giulia Ceccarelli (2020)** — Semantic segmentation of point clouds with the 3D medial axis transform
  1. "Semantic segmentation of point clouds with the 3D medial axis transform" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-33-2025)
     - authors: Giulia Ceccarelli (student; first author), Weixiao Gao (supervisor: Gao), Ravi Peters (supervisor: Peters)
     - title similarity 1.00; abstract similarity 0.51; year +5  (source: OpenAlex)
- **Chirag Garg (2020)** — Indoor 3D reconstruction from a single image
  1. "3D Construction and Realignment of Object for Interaction in Metaverse Space" — 2025 International Conference on Modeling, Simulation &amp;amp; Intell, 2025 — [conference paper](https://doi.org/10.1109/mosicom67153.2025.11398327)
     - authors: Chirag Garg (student; first author), Manali Arora
     - title similarity 0.44; abstract similarity n/a; year +5  (source: Crossref)
  2. "Crop Yield Prediction of Indian Districts Using Deep Learning" — 2021 Sixth International Conference on Image Information Processing (I, 2021 — [conference paper](https://doi.org/10.1109/iciip53038.2021.9702573)
     - authors: Parjanya Prashant, Kaustubh Ponkshe, Chirag Garg (student), Ishan Pendse, Prathamesh Muley
     - title similarity 0.42; abstract similarity n/a; year +1  (source: Crossref)
- **Jinglan Li (2020)** — Manage 4D historical AIS data by space filling curve
  1. "PointSCNet: Point Cloud Structure and Correlation Learning Based on Space-Filling Curve-Guided Sampling" — Symmetry, 2021 — [journal article](https://doi.org/10.3390/sym14010008)
     - authors: Xingye Chen, Yiqi Wu, Wenjie Xu, Jin Li (student), Huaiyi Dong
     - title similarity 0.41; abstract similarity 0.13; year +1  (source: Crossref)
- **Laurens Oostwegel (2020)** — Indoor positioning using augmented reality
  1. "Explaining building exposure using urban morphology and AI" — ?, 2026 — [posted-content](https://doi.org/10.5194/egusphere-egu26-10682)
     - authors: Laurens Jozef Nicolaas Oostwegel (student; first author), Danijel Schorlemmer, Doren Çalliku, Tara Evaz Zadeh, Lars Lingner, Pablo de la Mora, Wenyu Nie, Kasra Rafiezadeh Shahi, Chengzhi Rao, Philippe Guéguen
     - title similarity 0.36; abstract similarity 0.10; year +6  (source: Crossref)
  2. "Simplifying Mapping for Building Exposure using OpenStreetMap Tools" — ?, 2026 — [posted-content](https://doi.org/10.5194/egusphere-egu26-21319)
     - authors: Doren Calliku, Danijel Schorlemmer, Laurens J.N. Oostwegel (student), Pablo de la Mora Lobaton, Chengzhi Rao, Tara Evaz Zadeh, Lars Lingner
     - title similarity 0.39; abstract similarity 0.07; year +6  (source: Crossref)
- **Willem van Opstal (2020)** — Automatic isobath generalisation for navigational charts
  1. "Rule-based isobath generalisation using the Triangle Region Graph: uniting soundings, isobaths and constraints through a navigational surface" — Proceedings of 23rd ICA Workshop on Generalisation and Multiple Repres, 2020 — [conference paper](https://www.gdmc.nl/publications/2020/ICAgen2020_paper_11.pdf)
     - authors: Willem van Opstal (student; first author), Martijn Meijers (supervisor: Meijers), Ravi Peters
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
     - authors: Ioannis Dardavesis (student; first author), Edward Verbree (supervisor: Verbree), Azarakhsh Rafiee
     - title similarity 0.88; abstract similarity 0.78; year +1  (source: GDMC)
- **Michiel de Jong (2022)** — Using voxelised spaces for the generation and visualisation of dynamic evacuatio
  1. "Building Rhythms: Reopening the Workspace with Indoor Localisation" — Chapter in: LBS 2021: Proceedings of the 16th International Conference, 2021 — [conference paper](https://doi.org/10.34726/1741)
     - authors: Guilherme Spinoza Andreo, Ioannis Dardavesis, Michiel de Jong (student), Pratyush Kumar, Maundri Prihanggo, Georgios Triantafyllou, Niels van der Vaart, Edward Verbree, Zhenyu Liu, Runnan Fu, Linjun Wang, Yuzhen Jin, Theodoros Papakostas, Xenia Una Mainelli, Robert Voûte (supervisor: Voûte)
     - title similarity 0.37; abstract similarity n/a; year -1  (source: GDMC)
- **Yuzhen Jin (2022)** — Dynamic energy simulations based on the 3D BAG 2.0
  1. "Design and development of a student information management platform based on support vector machines and data mining" — International Journal of Information and Communication Technology, 2026 — [journal article](https://doi.org/10.1504/ijict.2026.155942)
     - authors: Yuzhen Jin (student; first author)
     - title similarity 0.38; abstract similarity n/a; year +4  (source: Crossref)
  2. "Design and development of a student information management platform based on support vector machines and data mining" — International Journal of Information and Communication Technology, 2026 — [journal article](https://doi.org/10.1504/ijict.2026.10080360)
     - authors: Yuzhen Jin (student; first author)
     - title similarity 0.38; abstract similarity n/a; year +4  (source: Crossref)
  3. "Parametric Study on Wind Energy Harvesting of Extraneously Induced Excitation Flutter-Driven Triboelectric Nanogenerator" — ?, 2024 — [posted-content](https://doi.org/10.2139/ssrn.4889179)
     - authors: Yadong Zhang, Yuzhen Jin (student), Jingyu Cui
     - title similarity 0.35; abstract similarity n/a; year +2  (source: Crossref)
- **Zhenyu Liu (2022)** — Dynamic Objects Detection and Removal in Mobile Laser Scanning Data
  1. "Data frame aware optimized Octomap-based dynamic object detection and removal in Mobile Laser Scanning data" — Alexandria Engineering Journal, 74, pp. 327-344, 2023 — [journal article](https://www.sciencedirect.com/science/article/pii/S1110016823003770)
     - authors: Zhenyu Liu (student; first author), Peter van Oosterom (supervisor: van Oosterom), Jesús Balado, Arjen Swart, Bart Beers
     - title similarity 0.76; abstract similarity 0.84; year +1  (source: GDMC)
  2. "Detection and reconstruction of static vehicle-related ground occlusions in point clouds from mobile laser scanning" — Automation in Construction, Elsevier BV, 141, pp. 104461, 2022 — [journal article](https://www.sciencedirect.com/science/article/pii/S092658052200334X)
     - authors: Zhenyu Liu (student; first author), Peter van Oosterom (supervisor: van Oosterom), Jesús Balado, Arjen Swart, Bart Beers
     - title similarity 0.49; abstract similarity 0.31; year +0  (source: GDMC)
- **Rohit Ramlakhan (2022)** — Modelling the legal spaces of 3D underground objects in a 3D LAS
  1. "Modelling the legal spaces of 3D underground objects in 3D land administration systems" — Land Use Policy, Elsevier BV, 127, pp. 106537, 2023 — [journal article](https://www.sciencedirect.com/science/article/pii/S0264837723000030)
     - authors: Rohit Ramlakhan (student; first author), Eftychia Kalogianni (supervisor: Kalogianni), Peter van Oosterom (supervisor: van Oosterom), Behnam Atazadeh
     - title similarity 0.82; abstract similarity 0.70; year +1  (source: GDMC)
  2. "Modelling 3D underground legal spaces in 3D Land Administration Systems" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:4a499efb-f348-456b-9965-65c47519337a)
     - authors: Rohit Ramlakhan (student; first author), Eftychia Kalogianni (supervisor: Kalogianni), Peter van Oosterom (supervisor: van Oosterom), Ramlakhan, Rohit (student), Kalogianni, Eftychia, van Oosterom , Peter
     - title similarity 0.56; abstract similarity 0.70; year -1  (source: GDMC)
- **Georgios Triantafyllou (2022)** — Isovist Fingerprinting as new way of Indoor Localisation
  1. "Indoor localisation through Isovist fingerprinting from point clouds and floor plans" — Journal of Location Based Services, 2024 — [journal article](https://doi.org/10.1080/17489725.2024.2320642)
     - authors: Georgios Triantafyllou (student; first author), Edward Verbree (supervisor: Verbree), Azarakhsh Rafiee
     - title similarity 0.50; abstract similarity 0.65; year +2  (source: OpenAlex)
  2. "Indoor localisation through Isovist fingerprinting from point clouds and floor plans" — Journal of Location Based Services, Taylor & Francis, (2320642), pp. 2, 2024 — [journal article](https://www.tandfonline.com/doi/full/10.1080/17489725.2024.2320642)
     - authors: Georgios Triantafyllou (student; first author), Edward Verbree (supervisor: Verbree), Azarakhsh Rafiee, Simon Pena Pereira, Stef Lhermitte
     - title similarity 0.50; abstract similarity n/a; year +2  (source: GDMC)
  3. "Building Rhythms: Reopening the Workspace with Indoor Localisation" — Chapter in: LBS 2021: Proceedings of the 16th International Conference, 2021 — [conference paper](https://doi.org/10.34726/1741)
     - authors: Guilherme Spinoza Andreo, Ioannis Dardavesis, Michiel de Jong, Pratyush Kumar, Maundri Prihanggo, Georgios Triantafyllou (student), Niels van der Vaart, Edward Verbree (supervisor: Verbree), Zhenyu Liu, Runnan Fu, Linjun Wang, Yuzhen Jin, Theodoros Papakostas, Xenia Una Mainelli, Robert Voûte
     - title similarity 0.58; abstract similarity n/a; year -1  (source: GDMC)
- **Jasper van der Vaart (2022)** — Automatic building feature detection and reconstruction in IFC models
  1. "Defining LoDs to support BIM-based 3D building abstractions in GIS" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-55-2026)
     - authors: Jasper van der Vaart (student; first author), Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter, Siham El Yamani
     - title similarity 0.43; abstract similarity 0.11; year +4  (source: OpenAlex)
- **Ondrej Veselý (2022)** — Building massing generation using GAN trained on Dutch 3D city models
  1. "Generating 3D Building Volumes for a Given Urban Context using Pix2Pix GAN" — eCAADe proceedings, 2022 — [conference paper](https://doi.org/10.52842/conf.ecaade.2022.2.287)
     - authors: Raffaele Di Carlo, Divyae Mittal, Ondrej Vesely (student)
     - title similarity 0.41; abstract similarity n/a; year +0  (source: Crossref)
- **Carolin Bachert (2023)** — Mapping the Energy ADE to CityGML 3.0
  1. "Mapping the CityGML Energy ADE to CityGML 3.0 Using a Model-Driven Approach" — ISPRS International Journal of Geo-Information, 2024 — [journal article](https://doi.org/10.3390/ijgi13040121)
     - authors: Carolin Bachert (student; first author), Camilo León-Sánchez, Tatjana Kutzner, Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.65; abstract similarity 0.69; year +1  (source: OpenAlex)
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
     - authors: Adele Therias (student; first author), Azarakhsh Rafiee (supervisor: Rafiee), Stef Lhermitte, Philip van der Lugt, Roderik Lindenbergh
     - title similarity 1.00; abstract similarity 0.94; year +1  (source: Crossref)
  2. "Integrating radar and multi-spectral data to detect cocoa crops: A deep learning approach" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2025 — [journal article](https://doi.org/10.1016/j.rsase.2025.101652)
     - authors: Adele Therias (student; first author), Azarakhsh Rafiee (supervisor: Rafiee), Stef Lhermitte, Philip van der Lugt, Roderik Lindenbergh
     - title similarity 1.00; abstract similarity n/a; year +2  (source: GDMC)
  3. "Integrating Radar and Multi-Spectral Data to Detect Cocoa Crops: A Deep Learning Approach" — ?, 2024 — [posted-content](https://doi.org/10.2139/ssrn.4975854)
     - authors: Adele Therias (student; first author), Azarakhsh Rafiee (supervisor: Rafiee), Stef Lhermitte, Philip van der Lugt, Roderik Lindenbergh
     - title similarity 1.00; abstract similarity n/a; year +1  (source: Crossref)
- **Yitong Xia (2023)** — A data-driven approach to add openings to 3D BAG building models
  1. "Enriching LoD2 Building Models with Façade Openings Using Oblique Imagery" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-225-2025)
     - authors: Yitong Xia (student; first author), Weixiao Gao, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.39; abstract similarity 0.56; year +2  (source: OpenAlex)
- **Simay Batum (2024)** — Spatial Plan Registration and Compliance Checks in Estonia, based on LADM Part 5
  1. "Spatial plan registration and compliance checks in Estonia, based on LADM part 5: spatial plan information" — Survey Review, Informa UK Limited, pp. 1–31, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2547462)
     - authors: Simay Batum (student; first author), Eftychia Kalogianni (supervisor: Kalogianni), Marjan Broekhuizen (supervisor: Broekhuizen), Christopher Raitviir, Kermo M&auml;gi, Peter Van Oosterom (supervisor: van Oosterom), Kermo Mägi
     - title similarity 1.00; abstract similarity 0.63; year +1  (source: GDMC)
  2. "Leveraging BIM/IFC for the Registration of Spatial Plans and Compliance Checks and Permitting in Estonia based on LADM Part 5 - Spatial Plan Information" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_J.pdf)
     - authors: Simay Batum (student; first author), Eftychia Kalogianni (supervisor: Kalogianni), Marjan Broekhuizen (supervisor: Broekhuizen), Christopher Raitviir, Kermo Mägi, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.74; abstract similarity n/a; year +0  (source: GDMC)
- **Yuduan Cai (2024)** — SplitSFC: A database solution for massive point cloud data management
  1. "cjdb: A Simple, Fast, and Lean Database Solution for the CityGML Data Model" — Lecture Notes in Geoinformation and Cartography, 2024 — [book-chapter](https://doi.org/10.1007/978-3-031-43699-4_47)
     - authors: Leon Powałka, Chris Poon, Yitong Xia, Siebren Meines, Lan Yan, Yuduan Cai (student), Gina Stavropoulou, Balázs Dukai, Hugo Ledoux
     - title similarity 0.54; abstract similarity n/a; year +0  (source: Crossref)
- **Mengying Chen (2024)** — Formalizing land indicators for SDGs: Implementation and evaluation using intern
  1. "Formalizing land indicators for SDGs: Implementation and evaluation using international standards" — Proceedings of the FIG Working Week 20225, Brisbane, Australia, pp. 16, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/LADM_SDGindicators.pdf)
     - authors: Mengying Chen (student; first author), Peter van Oosterom (supervisor: van Oosterom), Eftychia Kalogianni (supervisor: Kalogianni)
     - title similarity 1.00; abstract similarity n/a; year +1  (source: GDMC)
  2. "Bridging Sustainable Development Goals and Land Administration: The Role of the ISO 19152 Land Administration Domain Model in SDG Indicator Formalization" — Land, MDPI AG, 13(491), pp. 27, 2024 — [journal article](https://doi.org/10.3390/land13040491)
     - authors: Mengying Chen (student; first author), Peter Van Oosterom (supervisor: van Oosterom), Eftychia Kalogianni (supervisor: Kalogianni), Paula Dijkstra, Christiaan Lemmen
     - title similarity 0.25; abstract similarity 0.43; year +0  (source: GDMC)
  3. "Analyzing and formalising land indicators of LGAF, GLII and SDGs through LADM" — Survey Review, Taylor and Francis, pp. 21, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2544400)
     - authors: Mengying Chen (student; first author), Abdullah Kara, Peter van Oosterom (supervisor: van Oosterom), Regina Orvañanos Murguía, John Gitau, Christiaan Lemmen
     - title similarity 0.40; abstract similarity 0.42; year +1  (source: GDMC)
  4. "Monitoring Indicators of International Guidance Documents and Frameworks through LADM" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_R.pdf)
     - authors: Abdullah Kara, Mengying Chen (student), Peter van Oosterom (supervisor: van Oosterom), Christiaan Lemmen, Kara, Abdullah, Chen, Mengying (student), van Oosterom, Peter J.M., Lemmen, C.H.J.; id_orcid 0000-0003-1514-8385
     - title similarity 0.44; abstract similarity 0.51; year +0  (source: GDMC)
- **Tessel Elisabeth Kaal (2024)** — Optimizing Energy Balance in Multi-Energy Microgrids -- Enhancing Grid Efficienc
  1. "Deep Reinforcement Learning-Graph Neural Networks-Dynamic Clustering triplet for Adaptive Multi Energy Microgrid optimization" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-g-2025-427-2025)
     - authors: Tessel Kaal (student; first author), Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.30; abstract similarity 0.57; year +1  (source: Crossref)
- **Maria Luisa Tarozzo Kawasaki (2024)** — Common Ground: Bridging Subsurface Information Models and Climate Adaptation Des
  1. "Integrating subsurface data into urban planning for climate adaptation using land administration domain model part 5" — Survey Review, Taylor and Francis, pp. 17, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2539606)
     - authors: Maria Luisa Tarozzo Kawasaki (student; first author), Laura Thomas, Ulf Hackauf (supervisor: Hackauf), Rob van der Krogt (supervisor: van der Krogt), Wilfred Visser (supervisor: Visser), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.46; abstract similarity 0.57; year +1  (source: GDMC)
  2. "Bringing Subsurface Information Models and Climate Adaptation Design into LADM part 5 Spatial Plan Information" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_G.pdf)
     - authors: Maria Luisa Tarozzo Kawasaki (student; first author), Rob van der Krogt (supervisor: van der Krogt), Wilfred Visser (supervisor: Visser), Ulf Hackauf (supervisor: Hackauf), Alexander Wandl (supervisor: Wandl), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.71; abstract similarity n/a; year +0  (source: GDMC)
  3. "Climate resilient spatial plans: Revised LADM climate adaptation profile" — Proceedings of the 13th International FIG Workshop on Land Administrat, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/3DLA2025_paper_ZA_89.pdf)
     - authors: Maria Luisa Tarozzo Kawasaki (student; first author), Rob van der Krogt (supervisor: van der Krogt), Wilfred Visser (supervisor: Visser), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.43; abstract similarity n/a; year +1  (source: GDMC)
- **Gabriela Koster (2024)** — Implementing a Dutch building energy simulation tool: Energy model testing for R
  1. "Solar potential mapping to address energy poverty in a data poor region: A case study in Plovdiv, Bulgaria" — ?, 2023 — [posted-content](https://doi.org/10.5194/egusphere-egu23-13628)
     - authors: Wilfried van Sark, Gabriela Koster (student), Britta Ricker
     - title similarity 0.36; abstract similarity 0.26; year -1  (source: Crossref)
- **Sharath Chandra Madanu (2024)** — A Confidence-aware Deep Learning Framework for Refining Laser-scanned Point Clou
  1. "RefineNet: a Confidence-aware Deep Online Learning Framework to Refine Real-world Point Cloud Semantic Segmentation" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-3-2026-179-2026)
     - authors: Sharath Chandra Madanu (student; first author), Shenglan Du (supervisor: Du), Jantien Stoter (supervisor: Stoter), Daan van der Heide (supervisor: van der Heide)
     - title similarity 0.71; abstract similarity 0.62; year +2  (source: OpenAlex)
- **Dimitris Mantas (2024)** — CNN-based roofing material segmentation using aerial imagery and LiDAR data fusi
  1. "RoofSense: A Multimodal Semantic Segmentation Dataset for Roofing Material Classification" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-153-2025)
     - authors: Dimitris Mantas (student; first author), Weixiao Gao, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.36; abstract similarity 0.40; year +1  (source: OpenAlex)
- **Ping Mao (2024)** — A digital twin based on Land Administration
  1. "A digital twin based on Land Administration" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_N.pdf)
     - authors: Ping Mao (student; first author), Peter van Oosterom (supervisor: van Oosterom), Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 1.00; abstract similarity n/a; year +0  (source: GDMC)
- **Bing-Shiuan Tsai (2024)** — 3DCityDB-Tools plug-in for QGIS: Adding server-side support to 3DCityDB v.5.0
  1. "Introducing server-side support for 3DCityDB 5.0 to the 3DCityDB-Tools plug-in for QGIS" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-193-2025)
     - authors: Bing-Shiuan Tsai (student; first author), Giorgio Agugiaro (supervisor: Agugiaro), Camilo Leon-Sanchez, Claus Nagel (supervisor: Nagel), Zhihang Yao (supervisor: Yao)
     - title similarity 0.78; abstract similarity 0.53; year +1  (source: OpenAlex)
- **Marjolein van Aalst (2024)** — A standards-based portal for integrated Land Administration information - A case
  1. "A standards-based portal for integrated Land Administration information: A case study of the Netherlands" — Proceedings of the FIG Working Week 20225, Brisbane, Australia, pp. 18, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/IntegratedLADM_NL.pdf)
     - authors: Marjolein van Aalst (student; first author), Peter van Oosterom (supervisor: van Oosterom), Lexi Rowland, Erwin Folmer, Hendrik Ploeger
     - title similarity 1.00; abstract similarity n/a; year +1  (source: GDMC)
- **Citra Andinasari (2025)** — Point Cloud for 3D Land Administration System (LAS)
  1. "Point Clouds for 3D Land Administration: Integrating Floor Plans and Nationwide Airborne LiDAR (AHN)" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2025 — [conference paper](https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-9-2025)
     - authors: Citra Andinasari (student; first author), Peter van Oosteroom, Edward Verbree (supervisor: Verbree)
     - title similarity 0.60; abstract similarity 0.71; year +0  (source: GDMC)
  2. "Point Cloud for 3D Land Administration System (LAS)" — Proceedings of the 13th International FIG Workshop on Land Administrat, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/3DLA2025_paper_S_39.pdf)
     - authors: Citra Andinasari (student; first author), Peter van Oosteroma, Edward Verbree (supervisor: Verbree)
     - title similarity 1.00; abstract similarity n/a; year +0  (source: GDMC)
- **Hidemichi Baba (2025)** — FlatCityBuf: A new cloud-optimised CityJSON format
  1. "FlatCityBuf: A new cloud-optimised CityJSON format" — The international archives of the photogrammetry, remote sensing and, 2025 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-17-2025)
     - authors: Hidemichi Baba (student; first author), Hugo Ledoux (supervisor: Ledoux), Ravi Peters (supervisor: Peters)
     - title similarity 1.00; abstract similarity 0.61; year +0  (source: OpenAlex)
- **Aswathy Chandran (2025)** — Proposal for the integration of a Building Material part: (ISO 19152-7) within t
  1. "Proposal for the integration of a Building Material part: (ISO 19152-7) within the Land Administration Domain Model" — Proceedings of the 12th International FIG Workshop on Land Administrat, 2024 — [conference paper](https://www.gdmc.nl/publications/2024/3DLA2024_paper_C.pdf)
     - authors: Aswathy Chandran (student; first author), Peter van Oosterom (supervisor: van Oosterom), Wilko Quak (supervisor: Quak), Pablo van den Bosch, Frederique van Erven
     - title similarity 1.00; abstract similarity n/a; year -1  (source: GDMC)
- **Hsin-Yu Cheng (2025)** — Roof Structure Extraction from Remote Sensing Images
  1. "Roof Structure Extraction from Remote Sensing Images" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xii-4-w1-2026-81-2026)
     - authors: Hsin-Yu Cheng (student; first author), Weixiao Gao (supervisor: Gao), Liangliang Nan (supervisor: Nan)
     - title similarity 1.00; abstract similarity 0.50; year +1  (source: Crossref)
- **Haohua Gan (2025)** — Exploration of algorithms for extracting wireframe models from man-made urban li
  1. "Wireframe Extraction of Urban Linear Objects from Aerial Lidar Point Clouds" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xii-4-w1-2026-145-2026)
     - authors: Haohua Gan (student; first author), Hugo Ledoux (supervisor: Ledoux), Weixiao Gao (supervisor: Gao)
     - title similarity 0.50; abstract similarity 0.50; year +1  (source: Crossref)
- **Adhisye Rahmawati (2025)** — Scenario-based energy simulation: Modelling tree planting strategy to reduce hea
  1. "Scenario-based energy simulation of tree planting strategies to reduce the heating and cooling demand of buildings under 2050 climate conditions" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlix-b4-2026-513-2026)
     - authors: Adhisye Rahmawati (student; first author), Weixiao Gao (supervisor: Gao), Camilo León Sánchez, Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.89; abstract similarity 0.60; year +1  (source: OpenAlex)
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
     - authors: Jiande Wu (student; first author), Shakhawat Tanim, MinJae Woo, Tanvir Ahammed, Lior Rennert
     - title similarity 0.35; abstract similarity 0.09; year -1  (source: Crossref)

## Possible (168 theses)

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
- **Erna Oudman (2006)** — The transformation of GPS into NAP heights
  1. "Using Satellite Constellations for Improved Determination of Earth's Time-Variable Gravity" — Journal of Spacecraft and Rockets, 2011 — [journal article](https://doi.org/10.2514/1.50926)
     - authors: Brian C. Gunter, Joao Encarnacao, Pavel Ditmar, Roland Klees (supervisor: Klees)
     - title similarity 0.35; abstract similarity 0.02; year +5  (source: OpenAlex)
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
  4. "Incidence angle influence on the quality of terrestrial laser scanning points" — Research Repository (Delft University of Technology), 2009 — [conference paper](https://openalex.org/W2099498711)
     - authors: Sylvie Dijkstra-Soudarissanane, Roderik Lindenbergh (supervisor: Lindenbergh), Massimo Menenti, P. J. G. Teunissen
     - title similarity 0.51; abstract similarity n/a; year +3  (source: OpenAlex)
  … and 15 more possible candidates; re-run with --limit/--surname to see them all.
- **Thanos Bantis (2008)** — Aerostat Photogrammetry for Large Scale Hydrological Modeling with Special Focus
  1. "HydroZIP: How Hydrological Knowledge can Be Used to Improve Compression of Hydrological Data" — Entropy, 2013 — [journal article](https://doi.org/10.3390/e15041289)
     - authors: Steven Weijs, Nick Van de Giesen (supervisor: van de Giesen), Marc Parlange
     - title similarity 0.32; abstract similarity 0.29; year +5  (source: OpenAlex)
  2. "Global hydrological model eWaterCycle" — ?, 2013 — [journal article](https://openalex.org/W635324389)
     - authors: Nick van de Giesen (supervisor: van de Giesen)
     - title similarity 0.40; abstract similarity 0.15; year +5  (source: OpenAlex)
  3. "Data consistency checks for building a 3D model: A case study of Technical University, Delft Campus, The Netherlands" — Research Repository (Delft University of Technology), 2010 — [journal article](https://openalex.org/W2100154710)
     - authors: Tarun Ghawana, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.37; abstract similarity 0.12; year +2  (source: OpenAlex)
  4. "A passive Distributed Temperature Sensing approach to large-scale soil moisture validation" — EGU General Assembly Conference Abstracts, 2009 — [conference paper](https://openalex.org/W1645997937)
     - authors: Susan Steele‐Dunne, Martine Rutten, D. Krzeminksa, Nick van de Giesen (supervisor: van de Giesen), Thom Bogaard, J. S. Selker, P. Sailhac
     - title similarity 0.35; abstract similarity 0.14; year +1  (source: OpenAlex)
  … and 72 more possible candidates; re-run with --limit/--surname to see them all.
- **Rikkert Wienia (2008)** — Use of global ionospheric maps for precise point positioning: Developing an opti
  1. "Use of Global and Regional Ionosphere Maps for Single-Frequency Precise Point Positioning" — International Association of Geodesy Symposia, 2009 — [book-chapter](https://doi.org/10.1007/978-3-540-85426-5_87)
     - authors: A.Q Le, C.C.J.M Tiberius, H van der Marel (supervisor: van der Marel), N Jakowski
     - title similarity 0.50; abstract similarity n/a; year +1  (source: Crossref)
  2. "Geometry-free undifferenced, single and double differenced analysis of single frequency GPS, EGNOS and GIOVE-A/B measurements" — GPS Solutions, 2009 — [journal article](https://doi.org/10.1007/s10291-009-0123-6)
     - authors: Peter F. de Bakker, Hans van der Marel (supervisor: van der Marel), Christian C. J. M. Tiberius
     - title similarity 0.36; abstract similarity 0.12; year +1  (source: OpenAlex)
  3. "High resolution spatio‐temporal water vapour mapping using GPS and MERIS observations" — International Journal of Remote Sensing, 2008 — [journal article](https://doi.org/10.1080/01431160701436825)
     - authors: Roderick Lindenbergh, Maxim Keshin, Hans van der Marel (supervisor: van der Marel), Ramon Hanssen
     - title similarity 0.30; abstract similarity 0.16; year +0  (source: OpenAlex)
  4. "TOWARDS SEQUENTIAL WATER VAPOR PREDICTIONS BASED ON TIME SERIES OF GPS AND MERIS OBSERVATIONS." — ?, 2013 — [conference paper](https://openalex.org/W2555849327)
     - authors: Roderik Lindenbergh, Hans Van Der Marel (supervisor: van der Marel), Maxim Keshin, Siebren De Haan
     - title similarity 0.31; abstract similarity 0.14; year +5  (source: OpenAlex)
  … and 5 more possible candidates; re-run with --limit/--surname to see them all.
- **Koen Duijnmayer (2009)** — Sediment characterization by geo-acoustic inversion of marine seismic data recei
  1. "Predicting Spatial Variability of Sediment Properties From Hydrographic Data for Geoacoustic Inversion" — IEEE Journal of Oceanic Engineering, 2010 — [journal article](https://doi.org/10.1109/joe.2010.2066711)
     - authors: Kerstin Siemes, Mirjam Snellen (supervisor: Snellen), Ali R. Amiri-Simkooei, Dick G. Simons (supervisor: Simons), Jean-Pierre Hermand
     - title similarity 0.37; abstract similarity n/a; year +1  (source: OpenAlex)
  2. "Hydroacoustic, infrasonic and seismic monitoring of the submarine eruptive activity and sub-aerial plume generation at South Sarigan, May 2010" — Journal of Volcanology and Geothermal Research, 2013 — [journal article](https://doi.org/10.1016/j.jvolgeores.2013.03.006)
     - authors: David N. Green, Läslo G. Evers, David Fee, Robin S. Matoza, Mirjam Snellen (supervisor: Snellen), Pieter Smets, Dick Simons (supervisor: Simons)
     - title similarity 0.41; abstract similarity n/a; year +4  (source: OpenAlex)
  3. "The potential of inverting geo-technical and geo-acoustic sediment parameters from single-beam echo sounder returns" — Research Repository (Delft University of Technology), 2009 — [conference paper](https://openalex.org/W1499440041)
     - authors: Dick G. Simons (supervisor: Simons), Mirjam Snellen (supervisor: Snellen), Kerstin Siemes
     - title similarity 0.36; abstract similarity n/a; year +0  (source: OpenAlex)
  4. "Determining sediment composition of coarse riverbeds using multi-beam echo-sounder backscatter and bathymetric features" — Proceedings of meetings on acoustics, 2012 — [conference paper](https://doi.org/10.1121/1.4774371)
     - authors: Dimitrios Eleftherakis, M. Snellen (supervisor: Snellen), AliReza Amiri-Simkooei, Dick G. Simons (supervisor: Simons)
     - title similarity 0.36; abstract similarity n/a; year +3  (source: OpenAlex)
  … and 20 more possible candidates; re-run with --limit/--surname to see them all.
- **Tom Wortel (2009)** — Automating quantity surveying in road construction using UAV Videogrammetry
  1. "Vibration measurement of a model wind turbine using high speed photogrammetry" — Proceedings of SPIE, the International Society for Optical Engineering, 2011 — [conference paper](https://doi.org/10.1117/12.889440)
     - authors: Dinesh Kalpoe, Kourosh Khoshelham (supervisor: Khoshelham), Ben Gorte (supervisor: Gorte)
     - title similarity 0.33; abstract similarity 0.37; year +2  (source: OpenAlex)
  2. "Localized Registration of Point Clouds of Botanic Trees" — IEEE Geoscience and Remote Sensing Letters, 2012 — [journal article](https://doi.org/10.1109/lgrs.2012.2216251)
     - authors: Alexander Bucksch, Kourosh Khoshelham (supervisor: Khoshelham)
     - title similarity 0.35; abstract similarity 0.18; year +3  (source: OpenAlex)
  3. "Automatic Extraction of Railroad Centerlines from Mobile Laser Scanning Data" — Remote Sensing, 2015 — [journal article](https://doi.org/10.3390/rs70505565)
     - authors: Sander Elberink, Kourosh Khoshelham (supervisor: Khoshelham)
     - title similarity 0.39; abstract similarity 0.21; year +6  (source: OpenAlex)
  4. "Motion estimation from point-plane correspondences" — Figshare, 2015 — [journal article](https://doi.org/10.4225/49/55ac623414932)
     - authors: KOUROSH KHOSHELHAM (supervisor: Khoshelham)
     - title similarity 0.32; abstract similarity 0.25; year +6  (source: OpenAlex)
  … and 17 more possible candidates; re-run with --limit/--surname to see them all.
- **Sven Andreas Briels (2010)** — Infrasound source location
  1. "Infrasonic interferometry applied to synthetic and measured data" — Utrecht University Repository (Utrecht University), 2013 — [conference paper](https://openalex.org/W2990294733)
     - authors: Julius T. Fricke, L. G. Evers (supervisor: Evers), Elmer Ruigrok, Kees Wapenaar, Dick G. Simons (supervisor: Simons)
     - title similarity 0.37; abstract similarity 0.19; year +3  (source: OpenAlex)
  2. "Infrasonic interferometry of stratospherically refracted microbaroms—A numerical study" — The Journal of the Acoustical Society of America, 2013 — [journal article](https://doi.org/10.1121/1.4819117)
     - authors: Julius T. Fricke, Nihed El Allouche, Dick G. Simons (supervisor: Simons), Elmer N. Ruigrok, Kees Wapenaar, Läslo G. Evers (supervisor: Evers)
     - title similarity 0.33; abstract similarity 0.12; year +3  (source: OpenAlex)
  3. "Infrasound Interferometry for Active and Passive Sources: A Synthetic Example for Waves Refracted in the Stratosphere" — AGU Fall Meeting Abstracts, 2012 — [conference paper](https://openalex.org/W3082886122)
     - authors: Julius T. Fricke, Elmer Ruigrok, L. G. Evers (supervisor: Evers), Nihed El Allouche, Dick G. Simons (supervisor: Simons), Kees Wapenaar
     - title similarity 0.35; abstract similarity n/a; year +2  (source: OpenAlex)
  4. "Results of Infrasound Interferometry in Netherlands" — EGUGA, 2012 — [journal article](https://openalex.org/W3010819701)
     - authors: Julius T. Fricke, Elmer Ruigrok, L. G. Evers (supervisor: Evers), Dick G. Simons (supervisor: Simons), Kees Wapenaar
     - title similarity 0.31; abstract similarity n/a; year +2  (source: OpenAlex)
  … and 15 more possible candidates; re-run with --limit/--surname to see them all.
- **Effrosyni Boufidou (2011)** — Towards understanding the DOQ Priorat terroirs: A multivariate GIS analysis
  1. "Measure the climate, model the city" — ISPRS Archives Volume XXXVIII-4/C21, 28th Urban Data Management Sympos, 2011 — [conference paper](https://doi.org/10.5194/isprsarchives-xxxviii-4-c21-59-2011)
     - authors: E. Boufidou (student; first author), T.J.F. Commandeur, S.B. Nedkov, S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.30; abstract similarity n/a; year +0  (source: GDMC)
  2. "Understanding the influence of wind pumping on temperature profiles in the topsoil" — AGUFM, 2012 — [journal article](https://openalex.org/W3041954528)
     - authors: M. G. Rütten, Nick van de Giesen (supervisor: van de Giesen), Susan Steele‐Dunne
     - title similarity 0.46; abstract similarity n/a; year +1  (source: OpenAlex)
  3. "Towards 3D raster GIS: On developing a raster engine for spatial DBMS" — Research Repository (Delft University of Technology), 2016 — [conference paper](https://openalex.org/W2341630917)
     - authors: Sisi Zlatanova (supervisor: Zlatanova), Pirouz Nourian, Romulo Gonçalves, Anh-Vu Vo
     - title similarity 0.44; abstract similarity 0.05; year +5  (source: OpenAlex)
  4. "Investigation of Temperature Dynamics in Small and Shallow Reservoirs, Case Study: Lake Binaba, Upper East Region of Ghana" — Water, 2016 — [journal article](https://doi.org/10.3390/w8030084)
     - authors: Ali Abbasi, Frank Annor, Nick Van de Giesen (supervisor: van de Giesen)
     - title similarity 0.34; abstract similarity 0.15; year +5  (source: OpenAlex)
  … and 92 more possible candidates; re-run with --limit/--surname to see them all.
- **Lidia van Halderen (2011)** — Visual ego-motion estimation from unmanned deep sea vehicles
  1. "Evaluation of Sentinel-2 Bands over the Spectrum" — ESASP, 2012 — [journal article](https://openalex.org/W3008908672)
     - authors: S. E. Hosseini Aria, Ben Gorte (supervisor: Gorte), Massimo Menenti
     - title similarity 0.41; abstract similarity n/a; year +1  (source: OpenAlex)
  2. "Evaluating MERIS-Based Aquatic Vegetation Mapping in Lake Victoria" — Remote Sensing, 2014 — [journal article](https://doi.org/10.3390/rs6087762)
     - authors: Elijah Cheruiyot, Collins Mito, Massimo Menenti, Ben Gorte (supervisor: Gorte), Roderik Koenders, Nadia Akdim
     - title similarity 0.38; abstract similarity n/a; year +3  (source: OpenAlex)
  3. "Effects of Decontamination of the Oropharynx and Intestinal Tract on Antibiotic Resistance in ICUs" — JAMA, 2014 — [journal article](https://doi.org/10.1001/jama.2014.7247)
     - authors: Evelien A. N. Oostdijk, Jozef Kesecioglu, Marcus J. Schultz, Caroline E. Visser, Evert de Jonge, Einar H. R. van Essen, Alexandra T. Bernards, Ilse Purmer, Roland Brimicombe, Dennis Bergmans, Frank van Tiel, Frank H. Bosch, Ellen Mascini, Arjanne van Griethuysen, Alexander Bindels, Arjan Jansz, Fred (A.) L. van Steveninck, Wil C. van der Zwet, Jan Willem Fijen, Steven Thijsen, Remko de Jong (supervisor: de Jong), Joke Oudbier, Adrienne Raben, Eric van der Vorm, Mirelle Koeman, Philip Rothbarth, Annemieke Rijkeboer, Paul Gruteke, Helga Hart-Sweet, Paul Peerbooms, Lex J. Winsser, Anne-Marie W. van Elsacker-Niele, Kees Demmendaal, Afke Brandenburg, Anne Marie G.A. de Smet, Marc J. M. Bonten
     - title similarity 0.36; abstract similarity n/a; year +3  (source: OpenAlex)
  4. "Analysis of Characteristics of BDS Observable Combinations for Wide-Lane Integer Ambiguity Resolution" — Lecture notes in electrical engineering, 2014 — [book-chapter](https://doi.org/10.1007/978-3-642-54737-9_36)
     - authors: Guangxing Wang, Kees de Jong (supervisor: de Jong), Xiaotao Li, Qile Zhao, Jing Guo
     - title similarity 0.35; abstract similarity n/a; year +3  (source: OpenAlex)
  … and 19 more possible candidates; re-run with --limit/--surname to see them all.
- **Stijn Verlaar (2011)** — Evaluation of close range photogrammetric support for Pavescan
  1. "Aeolian Beach Sand Transport Monitored by Terrestrial Laser Scanning" — The Photogrammetric Record, 2011 — [journal article](https://doi.org/10.1111/j.1477-9730.2011.00659.x)
     - authors: Roderik C. Lindenbergh (supervisor: Lindenbergh), Sylvie S. Soudarissanane, Sierd De Vries, Ben G. H. Gorte (supervisor: Gorte), Matthieu A. De Schipper
     - title similarity 0.35; abstract similarity 0.05; year +0  (source: OpenAlex)
  2. "Evaluation of a LIDAR Land-Based Mobile Mapping System for Monitoring Sandy Coasts" — Remote Sensing, 2011 — [journal article](https://doi.org/10.3390/rs3071472)
     - authors: Maja Bitenc, Roderik Lindenbergh (supervisor: Lindenbergh), Kourosh Khoshelham, A. Pieter Van Waarden
     - title similarity 0.42; abstract similarity 0.24; year +0  (source: OpenAlex)
  3. "Automatic Estimation of Excavation Volume from Laser Mobile Mapping Data for Mountain Road Widening" — Remote Sensing, 2013 — [journal article](https://doi.org/10.3390/rs5094629)
     - authors: Jinhu Wang, Higinio González-Jorge, Roderik Lindenbergh (supervisor: Lindenbergh), Pedro Arias-Sánchez, Massimo Menenti
     - title similarity 0.35; abstract similarity 0.27; year +2  (source: OpenAlex)
  4. "Vibration measurement of a model wind turbine using high speed photogrammetry" — Proceedings of SPIE, the International Society for Optical Engineering, 2011 — [conference paper](https://doi.org/10.1117/12.889440)
     - authors: Dinesh Kalpoe, Kourosh Khoshelham, Ben Gorte (supervisor: Gorte)
     - title similarity 0.43; abstract similarity 0.14; year +0  (source: OpenAlex)
  … and 20 more possible candidates; re-run with --limit/--surname to see them all.
- **Daniel Xu (2011)** — Design and Implementation of Constraints for 3D Spatial Database - Using Climate
  1. "A Methodology for Modelling of 3D Spatial Constraints" — Chapter in: Advances in 3D Geoinformation (Alias Abdul-Rahman, ed.), p, 2016 — [conference paper](https://doi.org/10.1007/978-3-319-25691-7_6)
     - authors: Daniel Xu (student; first author), Peter van Oosterom (supervisor: van Oosterom), Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.25; abstract similarity n/a; year +5  (source: GDMC)
  2. "A methodology for modelling of 3D spatial constraints" — Joint International Geoinformation Conference 2015, Kuala Lumpur, pp. , 2015 — [conference paper](https://www.gdmc.nl/publications/2015/Modelling_3D_spatial_constraints.pdf)
     - authors: Daniel Xu (student; first author), Peter van Oosterom (supervisor: van Oosterom), Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.25; abstract similarity n/a; year +4  (source: GDMC)
  3. "An Approach to develop 3D Geo-DBMS Topological Operators by re-using existing 2D Operators" — Chapter in: ISPRS Annals Volume II-2/W1, Proceedings of the ISPRS 8th , 2013 — [conference paper](https://doi.org/10.5194/isprsannals-ii-2-w1-291-2013)
     - authors: D. Xu (student; first author), S. Zlatanova (supervisor: Zlatanova)
     - title similarity 0.27; abstract similarity n/a; year +2  (source: GDMC)
  4. "Solutions for 4D cadastre - with a case study on utility networks" — International Journal of Geographical Information Science, 25(7), pp. , 2011 — [journal article](https://doi.org/10.1080/13658816.2010.520272)
     - authors: Fatih Döner, Rod Thompson, Jantien Stoter, Christiaan Lemmen, Hendrik Ploeger, Peter van Oosterom (supervisor: van Oosterom), Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.36; abstract similarity 0.07; year +0  (source: GDMC)
  … and 71 more possible candidates; re-run with --limit/--surname to see them all.
- **Bas Altena (2012)** — Filling the white gap on the map
  1. "Modeling Top of Atmosphere Radiance over Heterogeneous Non-Lambertian Rugged Terrain" — Remote Sensing, 2015 — [journal article](https://doi.org/10.3390/rs70608019)
     - authors: Alijafar Mousivand, Wout Verhoef, Massimo Menenti (supervisor: Menenti), Ben Gorte (supervisor: Gorte)
     - title similarity 0.32; abstract similarity 0.12; year +3  (source: OpenAlex)
  2. "Evaluating MERIS-Based Aquatic Vegetation Mapping in Lake Victoria" — Remote Sensing, 2014 — [journal article](https://doi.org/10.3390/rs6087762)
     - authors: Elijah Cheruiyot, Collins Mito, Massimo Menenti (supervisor: Menenti), Ben Gorte (supervisor: Gorte), Roderik Koenders, Nadia Akdim
     - title similarity 0.33; abstract similarity 0.10; year +2  (source: OpenAlex)
  3. "Evaluating ICESat full waveforms over the part of Nyainqêntanglha Mountain range, the Tibetan Plateau" — ?, 2012 — [conference paper](https://doi.org/10.1109/igarss.2012.6350483)
     - authors: Junchao Shi, Massimo Menenti (supervisor: Menenti), Roderik Lindenbergh
     - title similarity 0.27; abstract similarity 0.36; year +0  (source: OpenAlex)
  4. "Parameterization of Surface Roughness Based on ICESat/GLAS Full Waveforms: A Case Study on the Tibetan Plateau" — Journal of Hydrometeorology, 2013 — [journal article](https://doi.org/10.1175/jhm-d-12-0130.1)
     - authors: Junchao Shi, Massimo Menenti (supervisor: Menenti), Roderik Lindenbergh
     - title similarity 0.20; abstract similarity 0.41; year +1  (source: OpenAlex)
  … and 9 more possible candidates; re-run with --limit/--surname to see them all.
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
  4. "On the Validation of Solids Represented with the International Standards for Geographic Information" — Computer-Aided Civil and Infrastructure Engineering, 2013 — [journal article](https://doi.org/10.1111/mice.12043)
     - authors: Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.34; abstract similarity 0.16; year +1  (source: OpenAlex)
  … and 45 more possible candidates; re-run with --limit/--surname to see them all.
- **Josafat Isaí Guerrero Iñiguez (2012)** — Three-dimensional reconstruction of underground utilities for real-time visualiz
  1. "3D Visualisation of Underground Pipelines: Best Strategy for 3D Scene Creation" — Chapter in: ISPRS Annals Volume II-2/W1, Proceedings of the ISPRS 8th , 2013 — [conference paper](https://doi.org/10.5194/isprsannals-ii-2-w1-139-2013)
     - authors: J. Guerrero. S. Zlatanova (supervisor: Zlatanova), M. Meijers (supervisor: Meijers)
     - title similarity 0.53; abstract similarity n/a; year +1  (source: GDMC)
  2. "A semantic data model for indoor navigation" — ?, 2012 — [conference paper](https://doi.org/10.1145/2442616.2442618)
     - authors: Liu Liu, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.37; abstract similarity 0.10; year +0  (source: OpenAlex)
  3. "Spatial subdivision of complex indoor environments for 3D indoor navigation" — International Journal of Geographical Information Systems, 2017 — [journal article](https://doi.org/10.1080/13658816.2017.1376066)
     - authors: Abdoulaye A. Diakité, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.41; abstract similarity 0.10; year +5  (source: OpenAlex)
  4. "NIBU: a new approach to representing and analyzing interior utility networks within 3D geo-information systems" — International Journal of Digital Earth, 5(1), pp. 22-42, 2012 — [journal article](https://doi.org/10.1080/17538947.2011.564661)
     - authors: Ihab Hamzi Hijazi, Manfred Ehlers, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.36; abstract similarity 0.09; year +0  (source: GDMC)
  … and 59 more possible candidates; re-run with --limit/--surname to see them all.
- **Marjolein Koudijs (2012)** — Using ICESat/GLAS laser altimetry for water level estimations in the Mekong Rive
  1. "Determining geometric links between glaciers and lakes on the Tibetan plateau" — ?, 2013 — [journal article](https://openalex.org/W283019617)
     - authors: V. Phan Hien, Roderik Lindenbergh (supervisor: Lindenbergh), Massimo Menenti (supervisor: Menenti)
     - title similarity 0.34; abstract similarity 0.23; year +1  (source: OpenAlex)
  2. "Parameterization of Surface Roughness Based on ICESat/GLAS Full Waveforms: A Case Study on the Tibetan Plateau" — Journal of Hydrometeorology, 2013 — [journal article](https://doi.org/10.1175/jhm-d-12-0130.1)
     - authors: Junchao Shi, Massimo Menenti (supervisor: Menenti), Roderik Lindenbergh (supervisor: Lindenbergh)
     - title similarity 0.33; abstract similarity 0.16; year +1  (source: OpenAlex)
  3. "Breast Height Diameter Estimation From High-Density Airborne LiDAR Data" — IEEE Geoscience and Remote Sensing Letters, 2013 — [journal article](https://doi.org/10.1109/lgrs.2013.2285471)
     - authors: Alexander Bucksch, Roderik Lindenbergh (supervisor: Lindenbergh), Muhammad Zulkarnain Abd Rahman, Massimo Menenti (supervisor: Menenti)
     - title similarity 0.35; abstract similarity 0.07; year +1  (source: OpenAlex)
  4. "Is the morphological characterization of valley networks on Earth portable to Mars" — ?, 2013 — [journal article](https://openalex.org/W2986461342)
     - authors: R. Koenders, Roderik Lindenbergh (supervisor: Lindenbergh), Massimo Menenti (supervisor: Menenti)
     - title similarity 0.36; abstract similarity n/a; year +1  (source: OpenAlex)
  … and 49 more possible candidates; re-run with --limit/--surname to see them all.
- **Simeon Nedkov (2012)** — Knowledge-based optimisation of three-dimensional city models for car navigation
  1. "Google maps for crowdsourced emergency routing" — ISPRS Archives Volume XXXIX-B4, XXII ISPRS Congress, Technical Commiss, 2012 — [conference paper](https://doi.org/10.5194/isprsarchives-xxxix-b4-477-2012)
     - authors: Simeon Nedkov (student; first author), Sisi Zlatanova
     - title similarity 0.25; abstract similarity n/a; year +0  (source: GDMC)
  2. "Using extrusion to generate higher-dimensional GIS datasets" — Chapter in: Proceedings of the 21st ACM SIGSPATIAL International Confe, 2013 — [conference paper](https://doi.org/10.1145/2525314.2525447)
     - authors: Ken Arroyo Ohori, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.43; abstract similarity 0.18; year +1  (source: GDMC)
  3. "Applications of 3D City Models: State of the Art Review" — ISPRS International Journal of Geo-Information, 2015 — [journal article](https://doi.org/10.3390/ijgi4042842)
     - authors: Filip Biljecki, Jantien Stoter, Hugo Ledoux (supervisor: Ledoux), Sisi Zlatanova, Arzu Çöltekin
     - title similarity 0.46; abstract similarity 0.15; year +3  (source: OpenAlex)
  4. "Generation and Dissemination of a National Virtual 3D City and Landscape Model for the Netherlands" — Photogrammetric Engineering & Remote Sensing, 79(2), pp. 147-158, 2013 — [journal article](http://digital.ipcprintservices.com/publication/?i=144145&p=41)
     - authors: Sander Oude Elberink, Jantien Stoter, Hugo Ledoux (supervisor: Ledoux), Tom Commandeur
     - title similarity 0.45; abstract similarity 0.16; year +1  (source: GDMC)
  … and 46 more possible candidates; re-run with --limit/--surname to see them all.
- **Penelope Rammos (2012)** — Automatic detection of benthos & birds
  1. "Automatic detection of snow avalanche debris in central Svalbard using C-band SAR data" — Polar Research, 2017 — [journal article](https://doi.org/10.1080/17518369.2017.1333236)
     - authors: Dieuwertje S. Wesselink, Eirik Malnes, Markus Eckerstorfer, Roderik C. Lindenbergh (supervisor: Lindenbergh)
     - title similarity 0.55; abstract similarity 0.12; year +5  (source: OpenAlex)
  2. "Sequential and Automatic Image-Sequence Registration of Road Areas Monitored from a Hovering Helicopter" — Sensors, 2014 — [journal article](https://doi.org/10.3390/s140916630)
     - authors: Fatemeh Nejadasl, Roderik Lindenbergh (supervisor: Lindenbergh)
     - title similarity 0.39; abstract similarity 0.21; year +2  (source: OpenAlex)
  3. "Active Shapes for Automatic 3D Modeling of Buildings" — Journal of Imaging, 2015 — [journal article](https://doi.org/10.3390/jimaging1010156)
     - authors: Beril Sirmacek, Roderik Lindenbergh (supervisor: Lindenbergh)
     - title similarity 0.47; abstract similarity 0.09; year +3  (source: OpenAlex)
  4. "Automatic Tree Breast Height Diameter Estimation from Laser Mobile Mapping Data in an Urban Context" — ?, 2015 — [journal article](https://openalex.org/W2766873232)
     - authors: Melissa Huerta, Roderik Lindenbergh (supervisor: Lindenbergh)
     - title similarity 0.38; abstract similarity 0.07; year +3  (source: OpenAlex)
  … and 17 more possible candidates; re-run with --limit/--surname to see them all.
- **Martine Wijga-Hoefsloot (2012)** — Point Clouds in a Database
  1. "Big Data Analytics In The Geo-Spatial Domain" — Zenodo (CERN European Organization for Nuclear Research), 2015 — [other](https://doi.org/10.5281/zenodo.1045064)
     - authors: Romulo Goncalves, Ivanova, Milena, Kersten, Martin, Scholten, Henk, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.27; abstract similarity 0.39; year +3  (source: OpenAlex)
  2. "3D Cadastres Best Practices, Chapter 4: 3D Spatial DBMS for 3D Cadastres" — Proceedings of the FIG Congress 2018, Istanbul, pp. 59, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/TS04C_janecka_karki_et_al_9657.pdf)
     - authors: Karel Janecka, Sudarshan Karki, Peter van Oosterom, Sisi Zlatanova (supervisor: Zlatanova), Mohsen Kalantari, Tarun Ghawana
     - title similarity 0.25; abstract similarity 0.49; year +6  (source: GDMC)
  3. "COMPARISON OF ZEB1 AND LEICA C10 INDOOR LASER SCANNING POINT CLOUDS" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2016 — [journal article](https://doi.org/10.5194/isprs-annals-iii-1-143-2016)
     - authors: Beril Sirmacek, Yueqian Shen, Roderik Lindenbergh, Sisi Zlatanova (supervisor: Zlatanova), Abdoulaye Diakite
     - title similarity 0.28; abstract similarity 0.36; year +4  (source: OpenAlex)
  4. "Semantic enrichment of octree structured point clouds for multi‐story 3D pathfinding" — Transactions in GIS, 2018 — [journal article](https://doi.org/10.1111/tgis.12308)
     - authors: Florian W. Fichtner, Abdoulaye A. Diakité, Sisi Zlatanova (supervisor: Zlatanova), Robert Voûte
     - title similarity 0.29; abstract similarity 0.36; year +6  (source: OpenAlex)
  … and 21 more possible candidates; re-run with --limit/--surname to see them all.
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
  … and 74 more possible candidates; re-run with --limit/--surname to see them all.
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
     - authors: R. Aarsen (student; first author), M. Janssen, M. Ramkisoen, F. Biljecki, C.W. Quak, E. Verbree (supervisor: Verbree)
     - title similarity 0.28; abstract similarity n/a; year +0  (source: GDMC)
  2. "Integration of Traffic Information into the Path Planning among Moving Obstacles" — ISPRS International Journal of Geo-Information, 2017 — [journal article](https://doi.org/10.3390/ijgi6030086)
     - authors: Zhiyong Wang, John Steenbruggen, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.40; abstract similarity 0.14; year +2  (source: OpenAlex)
  3. "3D Cadastres Best Practices, Chapter 3: 3D Cadastral Information Modelling" — Proceedings of the FIG Congress 2018, Istanbul, pp. 42, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/TS04C_van_oosterom_lemmen_et_al_9656.pdf)
     - authors: Peter van Oosterom, Chrit Lemmen, Rod Thompson, Karel Janecka, Sisi Zlatanova (supervisor: Zlatanova), Mohsen Kalantari
     - title similarity 0.33; abstract similarity 0.13; year +3  (source: GDMC)
  4. "An Approach for Indoor Path Computation among Obstacles that Considers User Dimension" — ISPRS International Journal of Geo-Information, 2015 — [journal article](https://doi.org/10.3390/ijgi4042821)
     - authors: Liu Liu, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.32; abstract similarity 0.13; year +0  (source: OpenAlex)
  … and 20 more possible candidates; re-run with --limit/--surname to see them all.
- **Godelief Abhilakh Missier (2015)** — Towards a Web application for viewing Spatial Linked Open Data of Rotterdam
  1. "Towards a User-Oriented Open Data Strategy" — Information technology and law series/Information technology & law ser, 2018 — [book-chapter](https://doi.org/10.1007/978-94-6265-261-3_3)
     - authors: Bastiaan van Loenen (supervisor: van Loenen)
     - title similarity 0.56; abstract similarity 0.43; year +3  (source: OpenAlex)
  2. "How to assess the success of the open data ecosystem?" — International Journal of Digital Earth, 2016 — [journal article](https://doi.org/10.1080/17538947.2016.1224938)
     - authors: Frederika Welle Donker, Bastiaan van Loenen (supervisor: van Loenen)
     - title similarity 0.37; abstract similarity 0.60; year +1  (source: OpenAlex)
  3. "Visualization/dissemination of 3D Cadastre" — Proceedings of the FIG Congress 2018, Istanbul, pp. 30, 2018 — [conference paper](https://www.gdmc.nl/publications/2018/TS05C_cemellini_rod_et_al_9591.pdf)
     - authors: Barbara Cemellini, Thompson Rod, Marian de Vries (supervisor: de Vries), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.41; abstract similarity n/a; year +3  (source: GDMC)
  4. "Sustainable Business Models for Public Sector Open Data Providers" — JeDEM - eJournal of eDemocracy and Open Government, 2016 — [journal article](https://doi.org/10.29379/jedem.v8i1.390)
     - authors: Frederika Welle Donker, Bastiaan Van Loenen (supervisor: van Loenen)
     - title similarity 0.40; abstract similarity 0.50; year +1  (source: OpenAlex)
  … and 93 more possible candidates; re-run with --limit/--surname to see them all.
- **Carl Chen (2015)** — Edge-aware simplification of roof and facade point clouds into a uniformly dense
  1. "COMPARISON OF ZEB1 AND LEICA C10 INDOOR LASER SCANNING POINT CLOUDS" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2016 — [journal article](https://doi.org/10.5194/isprs-annals-iii-1-143-2016)
     - authors: Beril Sirmacek, Yueqian Shen, Roderik Lindenbergh, Sisi Zlatanova (supervisor: Zlatanova), Abdoulaye Diakite
     - title similarity 0.37; abstract similarity 0.35; year +1  (source: OpenAlex)
  2. "Semantic enrichment of octree structured point clouds for multi‐story 3D pathfinding" — Transactions in GIS, 2018 — [journal article](https://doi.org/10.1111/tgis.12308)
     - authors: Florian W. Fichtner, Abdoulaye A. Diakité, Sisi Zlatanova (supervisor: Zlatanova), Robert Voûte
     - title similarity 0.32; abstract similarity 0.40; year +3  (source: OpenAlex)
  3. "Integration of Traffic Information into the Path Planning among Moving Obstacles" — ISPRS International Journal of Geo-Information, 2017 — [journal article](https://doi.org/10.3390/ijgi6030086)
     - authors: Zhiyong Wang, John Steenbruggen, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.45; abstract similarity 0.09; year +2  (source: OpenAlex)
  4. "Classification of Power Facility Point Clouds from Unmanned Aerial Vehicles Based on Adaboost and Topological Constraints" — Sensors, 2019 — [journal article](https://doi.org/10.3390/s19214717)
     - authors: Yuxuan Liu, Mitko Aleksandrov, Sisi Zlatanova (supervisor: Zlatanova), Junjun Zhang, Fan Mo, Xiaojian Chen
     - title similarity 0.35; abstract similarity 0.22; year +4  (source: OpenAlex)
  … and 35 more possible candidates; re-run with --limit/--surname to see them all.
- **Damien Mulder (2015)** — Automatic repair of geometrically invalid 3D City Building models using a voxel-
  1. "Automatic conversion of IFC datasets to geometrically and semantically correct CityGML LOD3 buildings" — Transactions in GIS, 2015 — [journal article](https://doi.org/10.1111/tgis.12162)
     - authors: Sjors Donkers, Hugo Ledoux (supervisor: Ledoux), Junqiao Zhao, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.48; abstract similarity 0.35; year +0  (source: OpenAlex)
  2. "Applications of 3D City Models: State of the Art Review" — ISPRS International Journal of Geo-Information, 2015 — [journal article](https://doi.org/10.3390/ijgi4042842)
     - authors: Filip Biljecki, Jantien Stoter (supervisor: Stoter), Hugo Ledoux (supervisor: Ledoux), Sisi Zlatanova, Arzu Çöltekin
     - title similarity 0.42; abstract similarity 0.35; year +0  (source: OpenAlex)
  3. "Modeling a 3D City Model and Its Levels of Detail as a True 4D Model" — ISPRS International Journal of Geo-Information, 2015 — [journal article](https://doi.org/10.3390/ijgi4031055)
     - authors: Ken Ohori, Hugo Ledoux (supervisor: Ledoux), Filip Biljecki, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.40; abstract similarity 0.35; year +0  (source: OpenAlex)
  4. "Population Estimation Using a 3D City Model: A Multi-Scale Country-Wide Study in the Netherlands" — PLoS ONE, 2016 — [journal article](https://doi.org/10.1371/journal.pone.0156808)
     - authors: Filip Biljecki, Ken Arroyo Ohori, Hugo Ledoux (supervisor: Ledoux), Ravi Peters, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.39; abstract similarity 0.33; year +1  (source: OpenAlex)
  … and 35 more possible candidates; re-run with --limit/--surname to see them all.
- **Maarten Pronk (2015)** — Storing massive TINs in a DBMS - A comparison and a prototype implementation of 
  1. "COMPARATIVE ANALYSIS OF DATA STRUCTURES FOR STORING MASSIVE TINS IN A DBMS" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2016 — [journal article](https://doi.org/10.5194/isprsarchives-xli-b2-123-2016)
     - authors: K. Kumar, H. Ledoux (supervisor: Ledoux), J. Stoter (supervisor: Stoter)
     - title similarity 0.34; abstract similarity 0.57; year +1  (source: Crossref)
  2. "Compactly representing massive terrain models as TINs in CityGML" — Transactions in GIS, 2018 — [journal article](https://doi.org/10.1111/tgis.12456)
     - authors: Kavisha Kumar, Hugo Ledoux (supervisor: Ledoux), Jantien Stoter (supervisor: Stoter)
     - title similarity 0.34; abstract similarity 0.41; year +3  (source: OpenAlex)
  3. "An evaluation and classification ofnD topological data structures for the representation of objects in a higher-dimensional GIS" — International Journal of Geographical Information Systems, 2015 — [journal article](https://doi.org/10.1080/13658816.2014.999683)
     - authors: Ken Arroyo Ohori, Hugo Ledoux (supervisor: Ledoux), Jantien Stoter (supervisor: Stoter)
     - title similarity 0.31; abstract similarity 0.25; year +0  (source: OpenAlex)
  4. "Registration of Multi-Level Property Rights in 3D in The Netherlands: Two Cases and Next Steps in Further Implementation" — ISPRS International Journal of Geo-Information, 2017 — [journal article](https://doi.org/10.3390/ijgi6060158)
     - authors: Jantien Stoter (supervisor: Stoter), Hendrik Ploeger, Ruben Roes, Els van der Riet, Filip Biljecki, Hugo Ledoux (supervisor: Ledoux), Dirco Kok, Sangmin Kim
     - title similarity 0.37; abstract similarity 0.10; year +2  (source: OpenAlex)
  … and 36 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Erik Heeres (2016)** — Exploring the 3D BAG: How to define it and to what extent can it automatically b
  1. "Generating 3D city models without elevation data" — Computers Environment and Urban Systems, 2017 — [journal article](https://doi.org/10.1016/j.compenvurbsys.2017.01.001)
     - authors: Filip Biljecki, Hugo Ledoux (supervisor: Ledoux), Jantien Stoter (supervisor: Stoter)
     - title similarity 0.41; abstract similarity n/a; year +1  (source: OpenAlex)
  2. "AdTree: Accurate, Detailed, and Automatic Modelling of Laser-Scanned Trees" — Remote Sensing, 2019 — [journal article](https://doi.org/10.3390/rs11182074)
     - authors: Shenglan Du, Roderik Lindenbergh, Hugo Ledoux (supervisor: Ledoux), Jantien Stoter (supervisor: Stoter), Liangliang Nan
     - title similarity 0.41; abstract similarity n/a; year +3  (source: OpenAlex)
  3. "AdTree: Accurate, Detailed, and Automatic Modelling of Laser-Scanned Trees" — Preprints.org, 2019 — [preprint](https://doi.org/10.20944/preprints201907.0058.v2)
     - authors: Shenglan Du, Roderik Lindenbergh, Hugo Ledoux (supervisor: Ledoux), Jantien Stoter (supervisor: Stoter), Liangliang Nan
     - title similarity 0.41; abstract similarity n/a; year +3  (source: OpenAlex)
  4. "Accurate, Detailed, and Automatic Modelling of Laser-Scanned Trees" — Preprints.org, 2019 — [preprint](https://doi.org/10.20944/preprints201907.0058.v1)
     - authors: Shenglan Du, Roderik Lindenbergh, Hugo Ledoux (supervisor: Ledoux), Jantien Stoter (supervisor: Stoter), Liangliang Nan
     - title similarity 0.38; abstract similarity n/a; year +3  (source: OpenAlex)
  … and 24 more possible candidates; re-run with --limit/--surname to see them all.
- **Kees Jonker (2016)** — Automatic generation of raster-based height data for the Netherlands based on th
  1. "Registration of Multi-Level Property Rights in 3D in The Netherlands: Two Cases and Next Steps in Further Implementation" — ISPRS International Journal of Geo-Information, 2017 — [journal article](https://doi.org/10.3390/ijgi6060158)
     - authors: Jantien Stoter (supervisor: Stoter), Hendrik Ploeger, Ruben Roes, Els van der Riet, Filip Biljecki, Hugo Ledoux (supervisor: Ledoux), Dirco Kok, Sangmin Kim
     - title similarity 0.46; abstract similarity 0.15; year +1  (source: OpenAlex)
  2. "Geo-BIM data integration: easier said than done?" — Data Archiving and Networked Services (DANS), 2018 — [journal article](https://openalex.org/W2921255631)
     - authors: Jantien Stoter (supervisor: Stoter), G.A.K. Arroyo Ohori, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.44; abstract similarity 0.14; year +2  (source: OpenAlex)
  3. "Integratie BIM- en GIS-data: Makkelijker gezegd dan gedaan?" — Data Archiving and Networked Services (DANS), 2018 — [journal article](https://openalex.org/W2905744637)
     - authors: Abdoulaye Diakité, Thomas Krijnen, Hugo Ledoux (supervisor: Ledoux), G.A.K. Arroyo Ohori, Friso Penninga, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.31; abstract similarity 0.25; year +2  (source: OpenAlex)
  4. "Processing BIM and GIS models in practice: experiences and recommendations from a GeoBIM project in the Netherlands" — Preprints.org, 2018 — [preprint](https://doi.org/10.20944/preprints201806.0488.v1)
     - authors: Ken Arroyo Ohori, Abdoulaye Diakité, Thomas Krijnen, Hugo Ledoux (supervisor: Ledoux), Jantien Stoter (supervisor: Stoter)
     - title similarity 0.38; abstract similarity 0.15; year +2  (source: OpenAlex)
  … and 29 more possible candidates; re-run with --limit/--surname to see them all.
- **Matthijs Kastelijns (2016)** — Making sense of standards An evaluation and harmonisation of standards in the Se
  1. "Towards Digital Innovation: Stakeholder Interactions in Agricultural Data Ecosystem in Croatia" — Interdisciplinary Description of Complex Systems, 2022 — [journal article](https://doi.org/10.7906/indecs.20.2.10)
     - authors: Larisa Hrustek, Martina Tomičić Furjan, Filip Varga, Alen Džidić, Bastiaan van Loenen (supervisor: van Loenen), Dragica Šalamon
     - title similarity 0.35; abstract similarity 0.24; year +6  (source: OpenAlex)
  2. "Towards a high level of semantic harmonisation in the geospatial domain" — Computers, Environment and Urban Systems, 62(March), pp. 233-242, 2017 — [journal article](https://doi.org/10.1016/j.compenvurbsys.2016.12.002)
     - authors: Linda van den Brink, Paul Janssen, Wilko Quak (supervisor: Quak), Jantien Stoter
     - title similarity 0.46; abstract similarity n/a; year +1  (source: GDMC)
  3. "Open Data as a Condition for Smart Application Development: Assessing Access to Hospitals in Croatian Cities" — Sustainability, 2022 — [journal article](https://doi.org/10.3390/su141912014)
     - authors: Sanja Seljan, Marina Viličić, Zvonimir Nevistić, Luka Dedić, Marina Grubišić, Iva Cibilić, Karlo Kević, Bastiaan van Loenen (supervisor: van Loenen), Frederika Welle Donker, Charalampos Alexopoulos
     - title similarity 0.35; abstract similarity 0.22; year +6  (source: OpenAlex)
  4. "Open National CORS Data Ecosystems: A Cross-Jurisdictional Comparison*" — Interdisciplinary Description of Complex Systems, 2022 — [journal article](https://doi.org/10.7906/indecs.20.2.2)
     - authors: Warakan Supinajaroen, Bastiaan van Loenen (supervisor: van Loenen), Willem Korthals Altes
     - title similarity 0.37; abstract similarity 0.18; year +6  (source: OpenAlex)
  … and 6 more possible candidates; re-run with --limit/--surname to see them all.
- **Marco Lam (2016)** — Creating the medial axis transform for billions of lidar points using a memory e
  1. "Population Estimation Using a 3D City Model: A Multi-Scale Country-Wide Study in the Netherlands" — PLoS ONE, 2016 — [journal article](https://doi.org/10.1371/journal.pone.0156808)
     - authors: Filip Biljecki, Ken Arroyo Ohori, Hugo Ledoux, Ravi Peters (supervisor: Peters), Jantien Stoter (supervisor: Stoter)
     - title similarity 0.36; abstract similarity 0.13; year +0  (source: OpenAlex)
  2. "City3D: Large-Scale Building Reconstruction from Airborne LiDAR Point Clouds" — Remote Sensing, 2022 — [journal article](https://doi.org/10.3390/rs14092254)
     - authors: Jin Huang, Jantien Stoter (supervisor: Stoter), Ravi Peters (supervisor: Peters), Liangliang Nan
     - title similarity 0.35; abstract similarity 0.17; year +6  (source: OpenAlex)
  3. "Automated 3D Reconstruction of LoD2 and LoD1 Models for All 10 Million Buildings of the Netherlands" — Photogrammetric Engineering & Remote Sensing, 2022 — [journal article](https://doi.org/10.14358/pers.21-00032r2)
     - authors: Ravi Peters (supervisor: Peters), Balázs Dukai, Stelios Vitalis, Jordi van Liempt, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.35; abstract similarity 0.15; year +6  (source: OpenAlex)
  4. "Incorporating Topological Representation in 3D City Models" — ISPRS International Journal of Geo-Information, 2019 — [journal article](https://doi.org/10.3390/ijgi8080347)
     - authors: Stelios Vitalis, Ken Arroyo Ohori, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.33; abstract similarity 0.22; year +3  (source: OpenAlex)
  … and 34 more possible candidates; re-run with --limit/--surname to see them all.
- **Tim Nagelkerke (2016)** — Navigation to a human in motion by using points of interest
  1. "A unified 3D space-based navigation model for seamless navigation in indoor and outdoor" — International Journal of Digital Earth, 2021 — [journal article](https://doi.org/10.1080/17538947.2021.1913522)
     - authors: Jinjin Yan, Sisi Zlatanova (supervisor: Zlatanova), Abdoulaye Diakité (supervisor: Diakite)
     - title similarity 0.37; abstract similarity 0.24; year +5  (source: OpenAlex)
  2. "COMPARISON OF ZEB1 AND LEICA C10 INDOOR LASER SCANNING POINT CLOUDS" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2016 — [journal article](https://doi.org/10.5194/isprs-annals-iii-1-143-2016)
     - authors: Beril Sirmacek, Yueqian Shen, Roderik Lindenbergh, Sisi Zlatanova (supervisor: Zlatanova), Abdoulaye Diakite (supervisor: Diakite)
     - title similarity 0.40; abstract similarity 0.17; year +0  (source: OpenAlex)
  3. "Semantic enrichment of octree structured point clouds for multi‐story 3D pathfinding" — Transactions in GIS, 2018 — [journal article](https://doi.org/10.1111/tgis.12308)
     - authors: Florian W. Fichtner, Abdoulaye A. Diakité (supervisor: Diakite), Sisi Zlatanova (supervisor: Zlatanova), Robert Voûte
     - title similarity 0.31; abstract similarity 0.25; year +2  (source: OpenAlex)
  4. "Navigation network derivation for QR code‐based indoor pedestrian path planning" — Transactions in GIS, 2022 — [journal article](https://doi.org/10.1111/tgis.12912)
     - authors: Jinjin Yan, Jinwoo (Brian) Lee, Sisi Zlatanova (supervisor: Zlatanova), Abdoulaye A. Diakité (supervisor: Diakite), Hyun Kim
     - title similarity 0.37; abstract similarity 0.15; year +6  (source: OpenAlex)
  … and 49 more possible candidates; re-run with --limit/--surname to see them all.
- **Jade Haayen (2017)** — Towards interoperable standards for 1D time series data within the water sector
  1. "Working with Open BIM Standards to Source Legal Spaces for a 3D Cadastre" — ISPRS International Journal of Geo-Information, MDPI AG, 6(11), pp. 19, 2017 — [journal article](https://doi.org/10.3390/ijgi6110351)
     - authors: Jennifer Oldfield, Peter van Oosterom (supervisor: van Oosterom), Jakob Beetz, Thomas F. Krijnen
     - title similarity 0.41; abstract similarity 0.40; year +0  (source: GDMC)
  2. "Towards Open and FAIR Hydrological Modelling with eWaterCycle" — ?, 2021 — [conference paper](https://doi.org/10.5194/egusphere-egu21-7797)
     - authors: Niels Drost, Jerom P.M. Aerts, Fakhereh Alidoost, Bouwe Andela, Jaro Camphuijsen, Nick van de Giesen (supervisor: van de Giesen), Rolf Hut, Eric Hutton, Peter Kalverla, Gijs van den Oord, Inti Pelupessy, Stef Smeets, Stefan Verhoeven, Ben van Werkhoven
     - title similarity 0.49; abstract similarity 0.26; year +4  (source: OpenAlex)
  3. "Towards the Netherlands LADM Valuation Information Model Country Profile" — Proceedings of the FIG Working Week 2019, Hanoi, Vietnam, pp. 31, 2019 — [conference paper](http://www.fig.net/resources/proceedings/fig_proceedings/fig2019/papers/ts08i/TS08I_kara_kathmann_et_al_10066.pdf)
     - authors: Abdullah Kara, Ruud Kathmann, Peter van Oosterom (supervisor: van Oosterom), Christiaan Lemmen, Ümit Işıkdağ
     - title similarity 0.41; abstract similarity 0.27; year +2  (source: GDMC)
  4. "Towards Reproducible Hydrological Modelling with eWaterCycle" — ?, 2021 — [preprint](https://doi.org/10.1002/essoar.10506345.1)
     - authors: Niels Drost, Jerom Aerts, Fakhereh Alidoost, Bouwe Andela, Jaro Camphuijsen, Yifat Dzigan, Nick Van De Giesen (supervisor: van de Giesen), Rolf Hut, Eric Hutton, Peter Kalverla, Maarten van Meersbergen, Gijs van den Oord, Inti Pelupessy, Stefan Verhoeven, Berend Weel, Ben van Werkhoven
     - title similarity 0.42; abstract similarity 0.26; year +4  (source: OpenAlex)
  … and 129 more possible candidates; re-run with --limit/--surname to see them all.
- **Dimitrios Kyritsis (2017)** — The identification of road modality and occupancy patterns by Wi-Fi monitoring s
  1. "Using the combined LADM-IndoorGML model to support building evacuation" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-4-11-2018)
     - authors: Abdullah Alattas, Peter van Oosterom, Sisi Zlatanova (supervisor: Zlatanova), Dick Hoeneveld, Edward Verbree (supervisor: Verbree)
     - title similarity 0.37; abstract similarity n/a; year +1  (source: GDMC)
  2. "A generic space definition framework to support seamless indoor/outdoor navigation systems" — Transactions in GIS, 2019 — [journal article](https://doi.org/10.1111/tgis.12574)
     - authors: Jinjin Yan, Abdoulaye A. Diakité, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.38; abstract similarity 0.15; year +2  (source: OpenAlex)
  3. "Integration of Traffic Information into the Path Planning among Moving Obstacles" — ISPRS International Journal of Geo-Information, 2017 — [journal article](https://doi.org/10.3390/ijgi6030086)
     - authors: Zhiyong Wang, John Steenbruggen, Sisi Zlatanova (supervisor: Zlatanova)
     - title similarity 0.37; abstract similarity 0.14; year +0  (source: OpenAlex)
  4. "Identification of physical and visual enclosure of landscape space units with the help of point clouds" — Spatial Cognition and Computation, 2020 — [journal article](https://doi.org/10.1080/13875868.2020.1767625)
     - authors: Yijing Wang, Yuning Cheng, Sisi Zlatanova (supervisor: Zlatanova), Elisa Palazzo
     - title similarity 0.39; abstract similarity 0.05; year +3  (source: OpenAlex)
  … and 20 more possible candidates; re-run with --limit/--surname to see them all.
- **Birgit Ligtvoet (2017)** — Crowdsensing as a tool for up-to-date road asset distress detection
  1. "Virtual sensors - Synthesizing dynamic crowdsensing data into information on static instances" — Adjunct Proceedings of the 14th International Conference on Location B, 2018 — [conference paper](https://www.research-collection.ethz.ch/handle/20.500.11850/225584)
     - authors: Birgit R. Ligtvoet (student; first author), Edward Verbree (supervisor: Verbree), Ben G.H. Gorte, Ligtvoet, Birgit R., Verbree, Edward, Gorte, Ben G.H.
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
- **Jan ten Kate (2017)** — Predicting noise nuisance from outdoor music events in the built environment
  1. "Linking Persistent Scatterers to the Built Environment Using Ray Tracing on Urban Models" — IEEE Transactions on Geoscience and Remote Sensing, 2019 — [journal article](https://doi.org/10.1109/tgrs.2019.2901904)
     - authors: Mengshi Yang, Paco Lopez-Dekker, Prabu Dheenathayalan, Filip Biljecki (supervisor: Biljecki), Mingsheng Liao, Ramon F. Hanssen
     - title similarity 0.42; abstract similarity 0.09; year +2  (source: OpenAlex)
  2. "Infrared thermography in the built environment: A multi-scale review" — Renewable and Sustainable Energy Reviews, 2022 — [journal article](https://doi.org/10.1016/j.rser.2022.112540)
     - authors: Miguel Martin, Adrian Chong, Filip Biljecki (supervisor: Biljecki), Clayton Miller
     - title similarity 0.48; abstract similarity 0.06; year +5  (source: OpenAlex)
  3. "Exploration of open data in Southeast Asia to generate 3D building models" — National University of Singapore, 2020 — [conference paper](https://openalex.org/W3178802936)
     - authors: Filip Biljecki (supervisor: Biljecki)
     - title similarity 0.38; abstract similarity 0.08; year +3  (source: OpenAlex)
  4. "Registration of Multi-Level Property Rights in 3D in The Netherlands: Two Cases and Next Steps in Further Implementation" — ISPRS International Journal of Geo-Information, 2017 — [journal article](https://doi.org/10.3390/ijgi6060158)
     - authors: Jantien Stoter, Hendrik Ploeger, Ruben Roes, Els van der Riet, Filip Biljecki (supervisor: Biljecki), Hugo Ledoux, Dirco Kok, Sangmin Kim
     - title similarity 0.36; abstract similarity 0.07; year +0  (source: OpenAlex)
  … and 18 more possible candidates; re-run with --limit/--surname to see them all.
- **Maya Tryfona (2017)** — Bidirectional enrichment of CityGML and Multi-View Stereo Mesh models
  1. "CityJSON: a compact and easy-to-use encoding of the CityGML data model" — Open Geospatial Data Software and Standards, 2019 — [journal article](https://doi.org/10.1186/s40965-019-0064-0)
     - authors: Hugo Ledoux (supervisor: Ledoux), Ken Arroyo Ohori, Kavisha Kumar, Balázs Dukai, Anna Labetski, Stelios Vitalis
     - title similarity 0.43; abstract similarity 0.40; year +2  (source: OpenAlex)
  2. "Reconstructing historical 3D city models" — Urban Informatics, 2022 — [journal article](https://doi.org/10.1007/s44212-022-00011-3)
     - authors: Camille Morlighem, Anna Labetski, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.40; abstract similarity 0.30; year +5  (source: OpenAlex)
  3. "3dfier: automatic reconstruction of 3D city models" — The Journal of Open Source Software, 2021 — [journal article](https://doi.org/10.21105/joss.02866)
     - authors: Hugo Ledoux (supervisor: Ledoux), Filip Biljecki, Balázs Dukai, Kavisha Kumar, Ravi Peters, Jantien Stoter, Tom Commandeur
     - title similarity 0.41; abstract similarity 0.28; year +4  (source: OpenAlex)
  4. "Compactly representing massive terrain models as TINs in CityGML" — Transactions in GIS, 2018 — [journal article](https://doi.org/10.1111/tgis.12456)
     - authors: Kavisha Kumar, Hugo Ledoux (supervisor: Ledoux), Jantien Stoter
     - title similarity 0.24; abstract similarity 0.36; year +1  (source: OpenAlex)
  … and 19 more possible candidates; re-run with --limit/--surname to see them all.
- **Oscar Willems (2017)** — Exploring a pure landmark-based approach for indoor localisation
  1. "Using the combined LADM-IndoorGML model to support building evacuation" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-4-11-2018)
     - authors: Abdullah Alattas, Peter van Oosterom, Sisi Zlatanova (supervisor: Zlatanova), Dick Hoeneveld, Edward Verbree (supervisor: Verbree)
     - title similarity 0.38; abstract similarity n/a; year +1  (source: GDMC)
  2. "LADM-IndoorGML for exploring user movements in evacuation exercise" — Land Use Policy, Elsevier, 98(104219), pp. 1-18, 2020 — [journal article](https://doi.org/10.1016/j.landusepol.2019.104219)
     - authors: Abdullah Alattas, Peter van Oosterom, Sisi Zlatanova (supervisor: Zlatanova), Dick Hoeneveld, Edward Verbree (supervisor: Verbree)
     - title similarity 0.37; abstract similarity n/a; year +3  (source: GDMC)
  3. "Strategies to evaluate the visibility along an indoor path in a point cloud representation" — Chapter in: ISPRS Annals Volume IV-2/W4, ISPRS Geospatial Week 2017, I, 2017 — [conference paper](https://www.isprs-ann-photogramm-remote-sens-spatial-inf-sci.net/IV-2-W4/311/2017/)
     - authors: N. Grasso, E. Verbree (supervisor: Verbree), S. Zlatanova (supervisor: Zlatanova), M. Piras
     - title similarity 0.32; abstract similarity n/a; year +0  (source: GDMC)
  4. "OGC IndoorGML: A Standard Approach for Indoor Maps" — Elsevier eBooks, 2018 — [book-chapter](https://doi.org/10.1016/b978-0-12-813189-3.00010-1)
     - authors: Ki-Joune Li, Giuseppe Conti, Evdokimos Konstantinidis, Sisi Zlatanova (supervisor: Zlatanova), Panagiotis Bamidis
     - title similarity 0.59; abstract similarity n/a; year +1  (source: OpenAlex)
  … and 48 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Simon Griffioen (2018)** — A voxel-based methodology to detect (clustered) outliers in aerial lidar point c
  1. "Building outline extraction from ALS point clouds using medial axis transform descriptors" — Pattern Recognition, 2020 — [journal article](https://doi.org/10.1016/j.patcog.2020.107447)
     - authors: Elyta Widyaningrum, Ravi Y. Peters (supervisor: Peters), Roderik C. Lindenbergh
     - title similarity 0.35; abstract similarity 0.28; year +2  (source: OpenAlex)
  2. "City3D: Large-Scale Building Reconstruction from Airborne LiDAR Point Clouds" — Remote Sensing, 2022 — [journal article](https://doi.org/10.3390/rs14092254)
     - authors: Jin Huang, Jantien Stoter, Ravi Peters (supervisor: Peters), Liangliang Nan
     - title similarity 0.39; abstract similarity 0.25; year +4  (source: OpenAlex)
  3. "Building-PCC: Building Point Cloud Completion Benchmarks" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-179-2024)
     - authors: Weixiao Gao, Ravi Peters (supervisor: Peters), Jantien Stoter
     - title similarity 0.30; abstract similarity 0.26; year +6  (source: OpenAlex)
  4. "A Model-based Architecture for Autonomic and Heterogeneous Cloud Systems" — ?, 2018 — [conference paper](https://doi.org/10.5220/0006773002010212)
     - authors: Hugo Bruneliere, Zakarea Al-Shara, Frederico Alvares, Jonathan Lejeune, Thomas Ledoux (supervisor: Ledoux)
     - title similarity 0.42; abstract similarity 0.00; year +0  (source: OpenAlex)
  … and 26 more possible candidates; re-run with --limit/--surname to see them all.
- **IJsbrand Groeneveld (2018)** — Generalisation of Hydrography Networks for a Vario-scale Basemap
  1. "Evaluation of the dual half-edge data structure for implementation of a vario-scale model" — Chapter in: The International Archives of the Photogrammetry, Remote S, 2024 — [conference paper](https://isprs-archives.copernicus.org/articles/XLVIII-4-W11-2024/25/2024/)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (supervisor: Meijers), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.46; abstract similarity 0.23; year +6  (source: GDMC)
  2. "Towards a scale dependent framework for creating vario-scale maps" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-4-425-2018)
     - authors: Martijn Meijers (supervisor: Meijers), Peter van Oosterom (supervisor: van Oosterom), Radan &Scaron;uba, Dongliang Peng
     - title similarity 0.48; abstract similarity n/a; year +0  (source: GDMC)
  3. "The design and application of histogram trees for querying massive LiDAR point clouds" — Proceedings of 5th China LiDAR Conference, Xiamen, China, pp. 1-8, 201, 2019 — [conference paper](https://www.gdmc.nl/publications/2019/Design_Application_Histogram_Trees_Massive_LiDAR_Point_Clouds.pdf)
     - authors: Haicheng Liu, Xuefeng Guan, Martijn Meijers (supervisor: Meijers), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.45; abstract similarity n/a; year +1  (source: GDMC)
  4. "Generalizing Simultaneously to Support Smooth Zooming: Case Study of Merging Area Objects" — Journal of Geovisualization and Spatial Analysis, Springer, 7(12), pp., 2023 — [journal article](https://doi.org/10.1007/s41651-022-00109-x)
     - authors: Dongliang Peng, Martijn Meijers (supervisor: Meijers), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.36; abstract similarity 0.10; year +5  (source: GDMC)
  … and 66 more possible candidates; re-run with --limit/--surname to see them all.
- **Tom Hemmes (2018)** — Classification of large scale outdoor point clouds using convolutional neural ne
  1. "Classification of Mobile Laser Scanning Point Clouds of Urban Scenes Exploiting Cylindrical Neighbourhoods" — Chapter in: ISPRS - International Archives of the Photogrammetry, Remo, 2018 — [conference paper](https://doi.org/10.5194/isprs-archives-xlii-2-1225-2018)
     - authors: Mingxue Zheng, Mathias Lemmens (supervisor: Lemmens), Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.58; abstract similarity n/a; year +0  (source: GDMC)
  2. "Utilizing a Discrete Global Grid System for Handling Point Clouds with Varying Locations, Times, and Levels of Detail" — Cartographica, University of Toronto Press, 51(1), pp. 4-15, 2019 — [journal article](https://doi.org/10.3138/cart.54.1.2018-0009)
     - authors: Neeraj Sirdeshmukh, Edward Verbree, Peter van Oosterom (supervisor: van Oosterom), Stella Psomadaki, Martin Kodde
     - title similarity 0.41; abstract similarity 0.41; year +1  (source: GDMC)
  3. "Organizing and visualizing point clouds with continuous levels of detail" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 194, , 2022 — [journal article](https://doi.org/10.1016/j.isprsjprs.2022.10.004)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Haicheng Liu, Rod Thompson, Martijn Meijers, Edward Verbree
     - title similarity 0.42; abstract similarity 0.43; year +4  (source: GDMC)
  4. "Mathematical morphology directly applied to point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 168, , 2020 — [journal article](https://doi.org/10.1016/j.isprsjprs.2020.08.011)
     - authors: Jes&uacute;s Balado, Peter van Oosterom (supervisor: van Oosterom), Luc&iacute;a D&iacute;az-Vilari&ntilde;o, Martijn Meijers, Lucía Díaz-Vilariño
     - title similarity 0.29; abstract similarity 0.50; year +2  (source: GDMC)
  … and 61 more possible candidates; re-run with --limit/--surname to see them all.
- **Panagiotis Karydakis (2018)** — Simplification & visualization of BIM models through Hololens
  1. "Using a Dynamic Sensor Network to Obtain Spatiotemporal Data in an Urban Environment" — Adjunct Proceedings of the 14th International Conference on Location B, 2018 — [conference paper](https://www.research-collection.ethz.ch/handle/20.500.11850/225582)
     - authors: Lilia Angelova, Puck Flikweert, Panagiotis Karydakis (student), Daniël Kersbergen, Roos Teeuwen, Kotryna Valečkaitė, Edward Verbree, Martijn Meijers, Stefan van der Spek
     - title similarity 0.27; abstract similarity n/a; year +0  (source: GDMC)
  2. "Investigating the automation of building permit checks through 3D GeoBIM information." — arXiv (Cornell University), 2020 — [preprint](https://openalex.org/W3101904176)
     - authors: Francesca Noardo, Teng Wu, Ken Arroyo Ohori (supervisor: Ohori), Thomas Krijnen, Jantien Stoter
     - title similarity 0.44; abstract similarity 0.31; year +2  (source: OpenAlex)
  3. "An Inspection of IFC Models from Practice" — Applied Sciences, 2021 — [journal article](https://doi.org/10.3390/app11052232)
     - authors: Francesca Noardo, Ken Arroyo Ohori (supervisor: Ohori), Thomas Krijnen, Jantien Stoter
     - title similarity 0.43; abstract similarity 0.32; year +3  (source: OpenAlex)
  4. "Incorporating Topological Representation in 3D City Models" — ISPRS International Journal of Geo-Information, 2019 — [journal article](https://doi.org/10.3390/ijgi8080347)
     - authors: Stelios Vitalis, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.36; abstract similarity 0.30; year +1  (source: OpenAlex)
  … and 7 more possible candidates; re-run with --limit/--surname to see them all.
- **Lydia Kotoula (2018)** — The Smart Point Cloud framework to detect pipelines using raw point cloud genera
  1. "Point clouds and Hydroinformatics" — 2022 (Abstract from EGU General Assembly 2022, Vienna, Austria, 23–27 , 2022 — [conference paper](https://meetingorganizer.copernicus.org/EGU22/EGU22-12880.html)
     - authors: Vitali Diaz, Haicheng Liu, Peter van Oosterom, Martijn Meijers, Edward Verbree (supervisor: Verbree), Fedor Baart, Maarten Pronk, Thijs van Lankveld
     - title similarity 0.35; abstract similarity 0.43; year +4  (source: GDMC)
  2. "Utilizing a Discrete Global Grid System for Handling Point Clouds with Varying Locations, Times, and Levels of Detail" — Cartographica, University of Toronto Press, 51(1), pp. 4-15, 2019 — [journal article](https://doi.org/10.3138/cart.54.1.2018-0009)
     - authors: Neeraj Sirdeshmukh, Edward Verbree (supervisor: Verbree), Peter van Oosterom, Stella Psomadaki, Martin Kodde
     - title similarity 0.24; abstract similarity 0.46; year +1  (source: GDMC)
  3. "Organizing and visualizing point clouds with continuous levels of detail" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 194, , 2022 — [journal article](https://doi.org/10.1016/j.isprsjprs.2022.10.004)
     - authors: Peter van Oosterom, Haicheng Liu, Rod Thompson, Martijn Meijers, Edward Verbree (supervisor: Verbree)
     - title similarity 0.24; abstract similarity 0.43; year +4  (source: GDMC)
  4. "Virtual sensors - Synthesizing dynamic crowdsensing data into information on static instances" — Adjunct Proceedings of the 14th International Conference on Location B, 2018 — [conference paper](https://www.research-collection.ethz.ch/handle/20.500.11850/225584)
     - authors: Birgit R. Ligtvoet, Edward Verbree (supervisor: Verbree), Ben G.H. Gorte, Ligtvoet, Birgit R., Verbree, Edward, Gorte, Ben G.H.
     - title similarity 0.39; abstract similarity 0.14; year +0  (source: GDMC)
  … and 11 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Lessie M. Ortega-Córdova (2018)** — Urban Vegetation Modeling 3D Levels of Detail
  1. "State of the Art in 3D City Modelling: Six Challenges Facing 3D Data as a Platform" — Research Repository (Delft University of Technology), 2020 — [journal article](https://openalex.org/W3133597296)
     - authors: Jantien Stoter (supervisor: Stoter), G.A.K. Arroyo Ohori, Balázs Dukai, Anna Labetski (supervisor: Labetski), K. Kavisha, Stelios Vitalis, Hugo Ledoux
     - title similarity 0.36; abstract similarity 0.20; year +2  (source: OpenAlex)
  2. "Incorporating Topological Representation in 3D City Models" — ISPRS International Journal of Geo-Information, 2019 — [journal article](https://doi.org/10.3390/ijgi8080347)
     - authors: Stelios Vitalis, Ken Arroyo Ohori, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.37; abstract similarity 0.28; year +1  (source: OpenAlex)
  3. "Incorporating Topological Representation in 3D City Models" — Preprints.org, 2019 — [preprint](https://doi.org/10.20944/preprints201905.0024.v1)
     - authors: Stelios Vitalis, Ken Arroyo Ohori, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.37; abstract similarity 0.28; year +1  (source: OpenAlex)
  4. "Investigating the automation of building permit checks through 3D GeoBIM information." — arXiv (Cornell University), 2020 — [preprint](https://openalex.org/W3101904176)
     - authors: Francesca Noardo, Teng Wu, Ken Arroyo Ohori, Thomas Krijnen, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.41; abstract similarity 0.24; year +2  (source: OpenAlex)
  … and 30 more possible candidates; re-run with --limit/--surname to see them all.
- **Anastasia Anastasiadou (2019)** — A probabilistic analysis of results of co-registration of aerial and mobile lase
  1. "Mathematical morphology directly applied to point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 168, , 2020 — [journal article](https://doi.org/10.1016/j.isprsjprs.2020.08.011)
     - authors: Jes&uacute;s Balado, Peter van Oosterom (supervisor: van Oosterom), Luc&iacute;a D&iacute;az-Vilari&ntilde;o, Martijn Meijers, Lucía Díaz-Vilariño
     - title similarity 0.30; abstract similarity 0.35; year +1  (source: GDMC)
  2. "Detection and reconstruction of static vehicle-related ground occlusions in point clouds from mobile laser scanning" — Automation in Construction, Elsevier BV, 141, pp. 104461, 2022 — [journal article](https://www.sciencedirect.com/science/article/pii/S092658052200334X)
     - authors: Zhenyu Liu, Peter van Oosterom (supervisor: van Oosterom), Jesús Balado, Arjen Swart, Bart Beers
     - title similarity 0.45; abstract similarity 0.16; year +3  (source: GDMC)
  3. "Comparison of cloud-to-cloud distance calculation methods for change detection in spatio-temporal point clouds" — ?, 2024 — [conference paper](https://doi.org/10.5194/egusphere-egu24-8191)
     - authors: Vitali Diaz, Peter van Oosterom (supervisor: van Oosterom), Martijn Meijers, Edward Verbree, Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.38; abstract similarity 0.24; year +5  (source: OpenAlex)
  4. "BIM Models as input for 3D Land Administration Systems for Apartment Registration" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:5e240a06-5fdf-4354-9e6d-09c675f1cd8b)
     - authors: Marjan Broekhuizen, Eftychia Kalogianni, Peter van Oosterom (supervisor: van Oosterom), Broekhuizen, Marjan, Kalogianni, Eftychia, van Oosterom, Peter
     - title similarity 0.34; abstract similarity 0.17; year +2  (source: GDMC)
  … and 65 more possible candidates; re-run with --limit/--surname to see them all.
- **Panagiotis Arapakis (2019)** — The use of digital models in microclimatic studies : First steps in coupling Cit
  1. "Enriching lower LoD 3D city models with semantic data computed by the voxelisation of BIM sources" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-297-2024)
     - authors: Jasper van der Vaart, Jantien Stoter, Giorgio Agugiaro (supervisor: Agugiaro), Ken Arroyo Ohori, Amir Hakim, Siham El Yamani
     - title similarity 0.27; abstract similarity 0.45; year +5  (source: OpenAlex)
  2. "Linking Semantic 3D City Models with Domain-Specific Simulation Tools for the Planning and Validation of Energy Applications at District Level" — Sustainability, 2021 — [journal article](https://doi.org/10.3390/su13168782)
     - authors: Edmund Widl, Giorgio Agugiaro (supervisor: Agugiaro), Jan Peters-Anders
     - title similarity 0.19; abstract similarity 0.46; year +2  (source: OpenAlex)
  3. "Lessons learnt from the integration of open data and semantic 3D city models for urban building energy modelling in the Netherlands" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w7-2025-89-2025)
     - authors: Camilo León-Sánchez, Giorgio Agugiaro (supervisor: Agugiaro), Jantien Stoter
     - title similarity 0.31; abstract similarity 0.42; year +6  (source: OpenAlex)
  4. "Semantic 3D city models as support for urban flood resilience: experiences from Rotterdam" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w4-2024-5-2024)
     - authors: Lara Andriessen, Giorgio Agugiaro (supervisor: Agugiaro), Aloys Borgers, Pieter Pauwels
     - title similarity 0.31; abstract similarity 0.32; year +5  (source: OpenAlex)
  … and 5 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Roeland Willem Erik Meulmeester (2019)** — BIM Legal: Proposal for defining legal spaces for apartment rights in the Dutch 
  1. "BIM Models as input for 3D Land Administration Systems for Apartment Registration" — Proceedings of the 7th International Workshop on 3D Cadastres (Eftychi, 2021 — [conference paper](https://doi.org/10.4233/uuid:5e240a06-5fdf-4354-9e6d-09c675f1cd8b)
     - authors: Marjan Broekhuizen, Eftychia Kalogianni, Peter van Oosterom (supervisor: van Oosterom), Broekhuizen, Marjan, Kalogianni, Eftychia, van Oosterom, Peter
     - title similarity 0.44; abstract similarity 0.56; year +2  (source: GDMC)
  2. "Mapping private, common, and exclusive common spaces in buildings from BIM/IFC to LADM. A case study from Saudi Arabia" — Land Use Policy, Elsevier, 104(105355), pp. 1-25, 2021 — [journal article](https://doi.org/10.1016/j.landusepol.2021.105355)
     - authors: Abdullah Alattas, Eftychia Kalogianni, Thamer Alzahrani, Sisi Zlatanova, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.31; abstract similarity 0.51; year +2  (source: GDMC)
  3. "BIM/IFC as input for registering apartment rights in a 3D Land Administration Systems – A prototype webservice" — Land Use Policy, Elsevier, 148(107368), pp. 14, 2025 — [journal article](https://doi.org/10.1016/j.landusepol.2024.107368)
     - authors: Marjan Broekhuizen, Eftychia Kalogianni, Peter van Oosterom (supervisor: van Oosterom)
     - title similarity 0.44; abstract similarity 0.48; year +6  (source: GDMC)
  4. "How to exploit BIM/IFC for 3D registration of ownership rights in multi-storey buildings: an evidence from Turkey" — Geocarto International, Taylor & Francis, pp. 1-30, 2022 — [journal article](https://doi.org/10.1080/10106049.2022.2142960)
     - authors: Dogus Guler, Peter van Oosterom (supervisor: van Oosterom), Tahsin Yomralioglu
     - title similarity 0.37; abstract similarity 0.41; year +3  (source: GDMC)
  … and 37 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Davey Oldenburg (2019)** — Reverse Household Waste Flow Mapping
  1. "Reference study of IFC software support: The GeoBIM benchmark 2019—Part I" — Transactions in GIS, 2021 — [journal article](https://doi.org/10.1111/tgis.12709)
     - authors: Francesca Noardo, Thomas Krijnen, Ken Arroyo Ohori, Filip Biljecki, Claire Ellul, Lars Harrie, Helen Eriksson, Lorenzo Polia, Nebras Salheb, Helga Tauscher, Jordi van Liempt, Hendrik Goerne, Dean Hintz, Tim Kaiser, Cristina Leoni, Artur Warchol, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.39; abstract similarity 0.03; year +2  (source: OpenAlex)
  2. "Reference study of CityGML software support: The GeoBIM benchmark 2019—Part II" — Transactions in GIS, 2020 — [journal article](https://doi.org/10.1111/tgis.12710)
     - authors: Francesca Noardo, Ken Arroyo Ohori, Filip Biljecki, Claire Ellul, Lars Harrie, Thomas Krijnen, Helen Eriksson, Jordi van Liempt, Maria Pla, Antonio Ruiz, Dean Hintz, Nina Krueger, Cristina Leoni, Leire Leoz, Diana Moraru, Stelios Vitalis, Philipp Willkomm, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.37; abstract similarity 0.03; year +1  (source: OpenAlex)
  3. "A benchmark approach and dataset for large-scale lane mapping from MLS point clouds" — International Journal of Applied Earth Observation and Geoinformation, 2024 — [journal article](https://doi.org/10.1016/j.jag.2024.104139)
     - authors: Xiaoxin Mi, Zhen Dong, Zhipeng Cao, Bisheng Yang, Chao Zheng, Jantien Stoter (supervisor: Stoter), Liangliang Nan
     - title similarity 0.33; abstract similarity 0.07; year +5  (source: OpenAlex)
  4. "Ἰουδαίαν in Acts 2:9: Reverse Engineering Textual Emendations" — Open Theology, 2020 — [journal article](https://doi.org/10.1515/opth-2020-0113)
     - authors: Vincent van Altena, Jan Krans, Henk Bakker, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.32; abstract similarity 0.03; year +1  (source: OpenAlex)
  … and 2 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Nikolaos Tzounakos (2019)** — Robust interior-exterior classification for 3d models
  1. "HRBF-Fusion: Accurate 3D Reconstruction from RGB-D Data Using On-the-fly Implicits" — ACM Transactions on Graphics, 2022 — [journal article](https://doi.org/10.1145/3516521)
     - authors: Yabin Xu, Liangliang Nan (supervisor: Nan), Laishui Zhou, Jun Wang
     - title similarity 0.42; abstract similarity 0.15; year +3  (source: OpenAlex)
  2. "City3D: Large-Scale Building Reconstruction from Airborne LiDAR Point Clouds" — Remote Sensing, 2022 — [journal article](https://doi.org/10.3390/rs14092254)
     - authors: Jin Huang, Jantien Stoter, Ravi Peters, Liangliang Nan (supervisor: Nan)
     - title similarity 0.30; abstract similarity 0.22; year +3  (source: OpenAlex)
  3. "An End-to-End Geometric Deficiencies Elimination Algorithm for 3D Meshes" — ?, 2020 — [conference paper](https://doi.org/10.1109/yac51587.2020.9337658)
     - authors: Bingtao Ma, Hongsen Liu, Liangliang Nan (supervisor: Nan), Xu Tang, Huijie Fan, Yang Cong
     - title similarity 0.39; abstract similarity 0.13; year +1  (source: OpenAlex)
  4. "Enriching Point Clouds with Implicit Representations for 3D Classification and Segmentation" — Remote Sensing, 2022 — [journal article](https://doi.org/10.3390/rs15010061)
     - authors: Zexin Yang, Qin Ye, Jantien Stoter, Liangliang Nan (supervisor: Nan)
     - title similarity 0.41; abstract similarity 0.08; year +3  (source: OpenAlex)
  … and 27 more possible candidates; re-run with --limit/--surname to see them all.
- **Jippe van der Maaden (2019)** — Vario-scale visualization of the AHN2 point cloud
  1. "Organizing and visualizing point clouds with continuous levels of detail" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 194, , 2022 — [journal article](https://doi.org/10.1016/j.isprsjprs.2022.10.004)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Haicheng Liu, Rod Thompson, Martijn Meijers (supervisor: Meijers), Edward Verbree
     - title similarity 0.44; abstract similarity 0.52; year +3  (source: GDMC)
  2. "Mathematical morphology directly applied to point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 168, , 2020 — [journal article](https://doi.org/10.1016/j.isprsjprs.2020.08.011)
     - authors: Jes&uacute;s Balado, Peter van Oosterom (supervisor: van Oosterom), Luc&iacute;a D&iacute;az-Vilari&ntilde;o, Martijn Meijers (supervisor: Meijers), Lucía Díaz-Vilariño
     - title similarity 0.44; abstract similarity 0.47; year +1  (source: GDMC)
  3. "Comparison of cloud-to-cloud distance calculation methods for change detection in spatio-temporal point clouds" — ?, 2024 — [conference paper](https://doi.org/10.5194/egusphere-egu24-8191)
     - authors: Vitali Diaz, Peter van Oosterom (supervisor: van Oosterom), Martijn Meijers (supervisor: Meijers), Edward Verbree, Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.42; abstract similarity 0.44; year +5  (source: OpenAlex)
  4. "Point clouds and Hydroinformatics" — 2022 (Abstract from EGU General Assembly 2022, Vienna, Austria, 23–27 , 2022 — [conference paper](https://meetingorganizer.copernicus.org/EGU22/EGU22-12880.html)
     - authors: Vitali Diaz, Haicheng Liu, Peter van Oosterom (supervisor: van Oosterom), Martijn Meijers (supervisor: Meijers), Edward Verbree, Fedor Baart, Maarten Pronk, Thijs van Lankveld
     - title similarity 0.29; abstract similarity 0.40; year +3  (source: GDMC)
  … and 71 more possible candidates; re-run with --limit/--surname to see them all.
- **Qu Wang (2019)** — 3D breakline extraction from point clouds with the medial axis transform
  1. "Building outline extraction from ALS point clouds using medial axis transform descriptors" — Pattern Recognition, 2020 — [journal article](https://doi.org/10.1016/j.patcog.2020.107447)
     - authors: Elyta Widyaningrum, Ravi Y. Peters (supervisor: Peters), Roderik C. Lindenbergh
     - title similarity 0.71; abstract similarity 0.26; year +1  (source: OpenAlex)
  2. "Semantic segmentation of point clouds with the 3D medial axis transform" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-33-2025)
     - authors: Giulia Ceccarelli, Weixiao Gao, Ravi Peters (supervisor: Peters)
     - title similarity 0.78; abstract similarity 0.16; year +6  (source: OpenAlex)
  3. "City3D: Large-Scale Building Reconstruction from Airborne LiDAR Point Clouds" — Remote Sensing, 2022 — [journal article](https://doi.org/10.3390/rs14092254)
     - authors: Jin Huang, Jantien Stoter, Ravi Peters (supervisor: Peters), Liangliang Nan
     - title similarity 0.44; abstract similarity 0.16; year +3  (source: OpenAlex)
  4. "Building-PCC: Building Point Cloud Completion Benchmarks" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-179-2024)
     - authors: Weixiao Gao, Ravi Peters (supervisor: Peters), Jantien Stoter
     - title similarity 0.31; abstract similarity 0.18; year +5  (source: OpenAlex)
  … and 37 more possible candidates; re-run with --limit/--surname to see them all.
- **Teng Wu (2019)** — Visibility analysis in a point cloud based on the medial axis transform
  1. "Building outline extraction from ALS point clouds using medial axis transform descriptors" — Pattern Recognition, 2020 — [journal article](https://doi.org/10.1016/j.patcog.2020.107447)
     - authors: Elyta Widyaningrum, Ravi Y. Peters (supervisor: Peters), Roderik C. Lindenbergh
     - title similarity 0.59; abstract similarity 0.40; year +1  (source: OpenAlex)
  2. "Semantic segmentation of point clouds with the 3D medial axis transform" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-33-2025)
     - authors: Giulia Ceccarelli, Weixiao Gao, Ravi Peters (supervisor: Peters)
     - title similarity 0.64; abstract similarity 0.34; year +6  (source: OpenAlex)
  3. "Building-PCC: Building Point Cloud Completion Benchmarks" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-179-2024)
     - authors: Weixiao Gao, Ravi Peters (supervisor: Peters), Jantien Stoter
     - title similarity 0.40; abstract similarity 0.34; year +5  (source: OpenAlex)
  4. "City3D: Large-Scale Building Reconstruction from Airborne LiDAR Point Clouds" — Remote Sensing, 2022 — [journal article](https://doi.org/10.3390/rs14092254)
     - authors: Jin Huang, Jantien Stoter, Ravi Peters (supervisor: Peters), Liangliang Nan
     - title similarity 0.33; abstract similarity 0.36; year +3  (source: OpenAlex)
  … and 12 more possible candidates; re-run with --limit/--surname to see them all.
- **Yixin Xu (2019)** — Improving location accuracy of a crowdsourced weather station by using a point c
  1. "Incorporating Topological Representation in 3D City Models" — ISPRS International Journal of Geo-Information, 2019 — [journal article](https://doi.org/10.3390/ijgi8080347)
     - authors: Stelios Vitalis, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.32; abstract similarity 0.14; year +0  (source: OpenAlex)
  2. "Incorporating Topological Representation in 3D City Models" — Preprints.org, 2019 — [preprint](https://doi.org/10.20944/preprints201905.0024.v1)
     - authors: Stelios Vitalis, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.32; abstract similarity 0.14; year +0  (source: OpenAlex)
  3. "Tools for BIM-GIS Integration (IFC Georeferencing and Conversions): Results from the GeoBIM Benchmark 2019" — ISPRS International Journal of Geo-Information, 2020 — [journal article](https://doi.org/10.3390/ijgi9090502)
     - authors: Francesca Noardo, Lars Harrie, Ken Arroyo Ohori (supervisor: Ohori), Filip Biljecki, Claire Ellul, Thomas Krijnen, Helen Eriksson, Dogus Guler, Dean Hintz, Mojgan Jadidi, Maria Pla, Santi Sanchez, Ville-Pekka Soini, Rudi Stouffs, Jernej Tekavec, Jantien Stoter
     - title similarity 0.31; abstract similarity 0.08; year +1  (source: OpenAlex)
  4. "Tools for BIM-GIS Integration (IFC Georeferencing and Conversions): Results from the GeoBIM Benchmark 2019" — Preprints.org, 2020 — [preprint](https://doi.org/10.20944/preprints202007.0243.v1)
     - authors: Francesca Noardo, Lars Harrie, Ken Arroyo Ohori (supervisor: Ohori), Filip Biljecki, Claire Ellul, Helen Eriksson, Dogus Guler, Dean Hintz, Mojgan A. Jadidi, Maria Pla, Santi Sanchez, Rudi Stouffs, Jernej Tekavec, Jantien Stoter
     - title similarity 0.31; abstract similarity 0.08; year +1  (source: OpenAlex)
  … and 3 more possible candidates; re-run with --limit/--surname to see them all.
- **Vasileios Alexandridis (2020)** — Automatic detection of waterbeds in shallow muddy water bodies in the Netherland
  1. "Automated 3D Reconstruction of LoD2 and LoD1 Models for All 10 Million Buildings of the Netherlands" — Photogrammetric Engineering & Remote Sensing, 2022 — [journal article](https://doi.org/10.14358/pers.21-00032r2)
     - authors: Ravi Peters (supervisor: Peters), Balázs Dukai, Stelios Vitalis, Jordi van Liempt, Jantien Stoter
     - title similarity 0.49; abstract similarity 0.16; year +2  (source: OpenAlex)
  2. "Building outline extraction from ALS point clouds using medial axis transform descriptors" — Pattern Recognition, 2020 — [journal article](https://doi.org/10.1016/j.patcog.2020.107447)
     - authors: Elyta Widyaningrum, Ravi Y. Peters (supervisor: Peters), Roderik C. Lindenbergh
     - title similarity 0.33; abstract similarity 0.18; year +0  (source: OpenAlex)
  3. "3dfier: automatic reconstruction of 3D city models" — The Journal of Open Source Software, 2021 — [journal article](https://doi.org/10.21105/joss.02866)
     - authors: Hugo Ledoux, Filip Biljecki, Balázs Dukai, Kavisha Kumar, Ravi Peters (supervisor: Peters), Jantien Stoter, Tom Commandeur
     - title similarity 0.38; abstract similarity 0.09; year +1  (source: OpenAlex)
  4. "Kinetic coefficient for ice–water interface from simulated non-equilibrium relaxation at coexistence" — The Journal of Chemical Physics, 2022 — [journal article](https://doi.org/10.1063/5.0124848)
     - authors: Ravi Kumar Reddy Addula, Baron Peters (supervisor: Peters)
     - title similarity 0.31; abstract similarity 0.15; year +2  (source: OpenAlex)
  … and 26 more possible candidates; re-run with --limit/--surname to see them all.
- **Rob de Groot (2020)** — Automatic construction of 3D tree models in multiple levels of detail from airbo
  1. "3dfier: automatic reconstruction of 3D city models" — The Journal of Open Source Software, 2021 — [journal article](https://doi.org/10.21105/joss.02866)
     - authors: Hugo Ledoux (supervisor: Ledoux), Filip Biljecki, Balázs Dukai, Kavisha Kumar, Ravi Peters, Jantien Stoter, Tom Commandeur
     - title similarity 0.52; abstract similarity 0.29; year +1  (source: OpenAlex)
  2. "Towards automatic reconstruction of 3D city models tailored for urban flow simulations" — Frontiers in Built Environment, 2022 — [journal article](https://doi.org/10.3389/fbuil.2022.899332)
     - authors: Ivan Pađen, Clara García-Sánchez, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.57; abstract similarity 0.17; year +2  (source: OpenAlex)
  3. "State of the Art in 3D City Modelling: Six Challenges Facing 3D Data as a Platform" — Research Repository (Delft University of Technology), 2020 — [journal article](https://openalex.org/W3133597296)
     - authors: Jantien Stoter, G.A.K. Arroyo Ohori, Balázs Dukai, Anna Labetski, K. Kavisha, Stelios Vitalis, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.41; abstract similarity 0.25; year +0  (source: OpenAlex)
  4. "Reconstructing compact building models from point clouds using deep implicit fields" — ISPRS Journal of Photogrammetry and Remote Sensing, 2022 — [journal article](https://doi.org/10.1016/j.isprsjprs.2022.09.017)
     - authors: Zhaiyu Chen, Hugo Ledoux (supervisor: Ledoux), Seyran Khademi, Liangliang Nan
     - title similarity 0.37; abstract similarity 0.22; year +2  (source: OpenAlex)
  … and 14 more possible candidates; re-run with --limit/--surname to see them all.
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
  1. "Towards value-creating and sustainable open data ecosystems: A comparative case study and a research agenda" — JeDEM - eJournal of eDemocracy and Open Government, 2021 — [journal article](https://doi.org/10.29379/jedem.v13i2.644)
     - authors: Bastiaan Van Loenen (supervisor: van Loenen), Anneke Zuiderwijk, Glenn Vancauwenberghe, Francisco J. Lopez-Pellicer, Ingrid Mulder, Charalampos Alexopoulos, Rikke Magnussen, Mubashrah Saddiqa, Melanie Dulong de Rosnay, Joep Crompvoets, Andrea Polini, Barbara Re, Cesar Casiano Flores
     - title similarity 0.33; abstract similarity 0.20; year +1  (source: OpenAlex)
  2. "Editorial: Trends and Prospects of Opening Data in Problem Driven Societies" — Interdisciplinary Description of Complex Systems, 2022 — [editorial](https://doi.org/10.7906/indecs.20.2.e.1)
     - authors: Bastiaan van Loenen (supervisor: van Loenen), Dragica Šalamon
     - title similarity 0.34; abstract similarity 0.14; year +2  (source: OpenAlex)
  3. "A fourth way to the digital transformation: The data republic as a fair data ecosystem" — Data & Policy, 2023 — [journal article](https://doi.org/10.1017/dap.2023.18)
     - authors: Stefano Calzati, Bastiaan van Loenen (supervisor: van Loenen)
     - title similarity 0.32; abstract similarity 0.12; year +3  (source: OpenAlex)
  4. "Towards a Common Definition of Open Data Intermediaries" — Digital Government Research and Practice, 2023 — [journal article](https://doi.org/10.1145/3585537)
     - authors: Ashraf Shaharudin, Bastiaan van Loenen (supervisor: van Loenen), Marijn Janssen
     - title similarity 0.32; abstract similarity 0.10; year +3  (source: OpenAlex)
  … and 8 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Pantelis Kaniouras (2020)** — Road detection from remote sensing imagery
  1. "ComNet: Combinational Neural Network for Object Detection in UAV-Borne Thermal Images" — IEEE Transactions on Geoscience and Remote Sensing, 2020 — [journal article](https://doi.org/10.1109/tgrs.2020.3029945)
     - authors: Minglei Li, Xingke Zhao, Liangliang Nan (supervisor: Nan)
     - title similarity 0.33; abstract similarity 0.27; year +0  (source: OpenAlex)
  2. "DDL-MVS: Depth Discontinuity Learning for Multi-View Stereo Networks" — Remote Sensing, 2023 — [journal article](https://doi.org/10.3390/rs15122970)
     - authors: Nail Ibrahimli, Hugo Ledoux, Julian F. P. Kooij, Liangliang Nan (supervisor: Nan)
     - title similarity 0.34; abstract similarity 0.19; year +3  (source: OpenAlex)
  3. "Reconstructing compact building models from point clouds using deep implicit fields" — ISPRS Journal of Photogrammetry and Remote Sensing, 2022 — [journal article](https://doi.org/10.1016/j.isprsjprs.2022.09.017)
     - authors: Zhaiyu Chen, Hugo Ledoux, Seyran Khademi, Liangliang Nan (supervisor: Nan)
     - title similarity 0.40; abstract similarity 0.11; year +2  (source: OpenAlex)
  4. "PathNet: Path-Selective Point Cloud Denoising" — IEEE Transactions on Pattern Analysis and Machine Intelligence, 2024 — [journal article](https://doi.org/10.1109/tpami.2024.3355988)
     - authors: Zeyong Wei, Honghua Chen, Liangliang Nan (supervisor: Nan), Jun Wang, Jing Qin
     - title similarity 0.42; abstract similarity 0.12; year +4  (source: OpenAlex)
  … and 53 more possible candidates; re-run with --limit/--surname to see them all.
- **Imke Lánský (2020)** — Height inference for all USA building footprints in the absence of height data
  1. "Inferring the number of floors for residential buildings" — International Journal of Geographical Information Systems, 2022 — [journal article](https://doi.org/10.1080/13658816.2022.2160454)
     - authors: Ellie Roy, Maarten Pronk, Giorgio Agugiaro, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.38; abstract similarity 0.49; year +2  (source: OpenAlex)
  2. "Reconstructing compact building models from point clouds using deep implicit fields" — ISPRS Journal of Photogrammetry and Remote Sensing, 2022 — [journal article](https://doi.org/10.1016/j.isprsjprs.2022.09.017)
     - authors: Zhaiyu Chen, Hugo Ledoux (supervisor: Ledoux), Seyran Khademi, Liangliang Nan
     - title similarity 0.39; abstract similarity 0.32; year +2  (source: OpenAlex)
  3. "Structure-aware Building Mesh Polygonization" — ISPRS Journal of Photogrammetry and Remote Sensing, 2020 — [journal article](https://doi.org/10.1016/j.isprsjprs.2020.07.010)
     - authors: Vasileios Bouzas, Hugo Ledoux (supervisor: Ledoux), Liangliang Nan
     - title similarity 0.32; abstract similarity 0.24; year +0  (source: OpenAlex)
  4. "Filling holes in LoD2 building models" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-171-2024)
     - authors: Weixiao Gao, Ravi Peters, Hugo Ledoux (supervisor: Ledoux), Jantien Stoter
     - title similarity 0.33; abstract similarity 0.26; year +4  (source: OpenAlex)
  … and 8 more possible candidates; re-run with --limit/--surname to see them all.
- **Konstantinos Mastorakis (2020)** — An integrative workflow for 3D city model versioning
  1. "State of the Art in 3D City Modelling: Six Challenges Facing 3D Data as a Platform" — Research Repository (Delft University of Technology), 2020 — [journal article](https://openalex.org/W3133597296)
     - authors: Jantien Stoter, G.A.K. Arroyo Ohori, Balázs Dukai, Anna Labetski, K. Kavisha, Stelios Vitalis (supervisor: Vitalis), Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.31; abstract similarity 0.26; year +0  (source: OpenAlex)
  2. "From road centrelines to carriageways—A reconstruction algorithm" — PLoS ONE, 2022 — [journal article](https://doi.org/10.1371/journal.pone.0262801)
     - authors: Stelios Vitalis (supervisor: Vitalis), Anna Labetski, Hugo Ledoux (supervisor: Ledoux), Jantien Stoter
     - title similarity 0.31; abstract similarity 0.05; year +2  (source: OpenAlex)
  3. "APPLYING VERSIONING TO MULTI-LOD 3D CITY MODELS" — The International Archives of the Photogrammetry, Remote Sensing and S, 2022 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-4-w4-2022-177-2022)
     - authors: S. Vitalis (supervisor: Vitalis), K. Arroyo Ohori, J. Stoter
     - title similarity 0.49; abstract similarity 0.21; year +2  (source: Crossref)
  4. "3dfier: automatic reconstruction of 3D city models" — The Journal of Open Source Software, 2021 — [journal article](https://doi.org/10.21105/joss.02866)
     - authors: Hugo Ledoux (supervisor: Ledoux), Filip Biljecki, Balázs Dukai, Kavisha Kumar, Ravi Peters, Jantien Stoter, Tom Commandeur
     - title similarity 0.48; abstract similarity 0.21; year +1  (source: OpenAlex)
  … and 19 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Jordi van Liempt (2020)** — CityJSON: does (file) size matter?
  1. "Streaming CityJSON datasets" — The international archives of the photogrammetry, remote sensing and, 2024 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-4-w11-2024-57-2024)
     - authors: Hugo Ledoux (supervisor: Ledoux), Gina Stavropoulou, Balázs Dukai (supervisor: Dukai)
     - title similarity 0.47; abstract similarity 0.27; year +4  (source: OpenAlex)
  2. "State of the Art in 3D City Modelling: Six Challenges Facing 3D Data as a Platform" — Research Repository (Delft University of Technology), 2020 — [journal article](https://openalex.org/W3133597296)
     - authors: Jantien Stoter, G.A.K. Arroyo Ohori, Balázs Dukai (supervisor: Dukai), Anna Labetski, K. Kavisha, Stelios Vitalis, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.30; abstract similarity 0.14; year +0  (source: OpenAlex)
  3. "FlatCityBuf: A new cloud-optimised CityJSON format" — The international archives of the photogrammetry, remote sensing and, 2025 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-17-2025)
     - authors: Hidemichi Baba, Hugo Ledoux (supervisor: Ledoux), Ravi Peters
     - title similarity 0.35; abstract similarity 0.37; year +5  (source: OpenAlex)
  4. "A Harmonized Data Model for Noise Simulation in the EU" — ISPRS International Journal of Geo-Information, 2020 — [journal article](https://doi.org/10.3390/ijgi9020121)
     - authors: Kavisha Kumar, Hugo Ledoux (supervisor: Ledoux), Richard Schmidt, Theo Verheij, Jantien Stoter
     - title similarity 0.39; abstract similarity 0.15; year +0  (source: OpenAlex)
  … and 2 more possible candidates; re-run with --limit/--surname to see them all.
- **Xin Wang (2020)** — Using CityGML EnergyADE Data in Honeybee
  1. "Online Personal Data Protection and Data Flows Under the RCEP: A Nostalgic New Start?" — Journal of World Trade, 2022 — [journal article](https://doi.org/10.54648/trad2022027)
     - authors: Xin Wang (student; first author)
     - title similarity 0.30; abstract similarity 0.15; year +2  (source: Crossref)
  2. "Editorial for Special Issue of Journal of Big Data Research on “Big Data Meets Knowledge Graphs”" — Big Data Research, 2021 — [journal article](https://doi.org/10.1016/j.bdr.2021.100215)
     - authors: Xin Wang (student; first author), Diego Calvanese
     - title similarity 0.25; abstract similarity n/a; year +1  (source: Crossref)
  3. "Urban road BC emissions of LDGVs: Machine learning models using OBD/PEMS data" — Chemosphere, 2024 — [journal article](https://doi.org/10.1016/j.chemosphere.2024.143348)
     - authors: Xin Wang (student; first author), Zhaowen Qiu, Zhen Liu
     - title similarity 0.20; abstract similarity n/a; year +4  (source: Crossref)
  4. "Mapping the CityGML Energy ADE to CityGML 3.0 Using a Model-Driven Approach" — ISPRS International Journal of Geo-Information, 2024 — [journal article](https://doi.org/10.3390/ijgi13040121)
     - authors: Carolin Bachert, Camilo León-Sánchez, Tatjana Kutzner, Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.47; abstract similarity 0.42; year +4  (source: OpenAlex)
  … and 16 more possible candidates; re-run with --limit/--surname to see them all.
- **Gabriella Wiersma (2020)** — Towards the linking of geospatial government data: A study on the semantic harmo
  1. "Lessons learnt from the integration of open data and semantic 3D city models for urban building energy modelling in the Netherlands" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w7-2025-89-2025)
     - authors: Camilo León-Sánchez, Giorgio Agugiaro, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.38; abstract similarity 0.43; year +5  (source: OpenAlex)
  2. "Aligning heterogenous topographical data to derive multiscale content for the Dutch nationwide Spatial Data Infrastructure" — Research Repository (Delft University of Technology), 2020 — [conference paper](https://openalex.org/W3131563100)
     - authors: Jantien Stoter (supervisor: Stoter), Daniël te Winkel, V.P. van Altena
     - title similarity 0.29; abstract similarity 0.38; year +0  (source: OpenAlex)
  3. "Automated 3D Reconstruction of LoD2 and LoD1 Models for All 10 Million Buildings of the Netherlands" — Photogrammetric Engineering & Remote Sensing, 2022 — [journal article](https://doi.org/10.14358/pers.21-00032r2)
     - authors: Ravi Peters, Balázs Dukai, Stelios Vitalis, Jordi van Liempt, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.21; abstract similarity 0.43; year +2  (source: OpenAlex)
  4. "Enriching lower LoD 3D city models with semantic data computed by the voxelisation of BIM sources" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-297-2024)
     - authors: Jasper van der Vaart, Jantien Stoter (supervisor: Stoter), Giorgio Agugiaro, Ken Arroyo Ohori, Amir Hakim, Siham El Yamani
     - title similarity 0.37; abstract similarity 0.31; year +4  (source: OpenAlex)
  … and 19 more possible candidates; re-run with --limit/--surname to see them all.
- **Charalampos Chatzidiakos (2021)** — Safety-driven road width estimations from vector data
  1. "Towards Extending CityGML for Property Valuation: Property Valuation ADE" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-127-2024)
     - authors: Siham El Yamani, Rafika Hajji, Roland Billen, Ken Arroyo Ohori (supervisor: Ohori), Jasper van der Vaart, Amir Hakim, Jantien Stoter
     - title similarity 0.35; abstract similarity 0.09; year +3  (source: OpenAlex)
  2. "Enriching lower LoD 3D city models with semantic data computed by the voxelisation of BIM sources" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-297-2024)
     - authors: Jasper van der Vaart, Jantien Stoter, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Amir Hakim, Siham El Yamani
     - title similarity 0.31; abstract similarity 0.12; year +3  (source: OpenAlex)
  3. "An Inspection of IFC Models from Practice" — Applied Sciences, 2021 — [journal article](https://doi.org/10.3390/app11052232)
     - authors: Francesca Noardo, Ken Arroyo Ohori (supervisor: Ohori), Thomas Krijnen, Jantien Stoter
     - title similarity 0.32; abstract similarity 0.10; year +0  (source: OpenAlex)
  4. "Multi-disciplinary Use of Three-Dimensional Geospatial Information" — Structural integrity, 2021 — [book-chapter](https://doi.org/10.1007/978-3-030-82430-3_12)
     - authors: Thomas Krijnen, Francesca Noardo, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.38; abstract similarity n/a; year +0  (source: OpenAlex)
  … and 4 more possible candidates; re-run with --limit/--surname to see them all.
- **Maarten de Jong (2021)** — Simplification of massive TINs with the streaming geometries paradigm
  1. "The Hessigheim 3D (H3D) benchmark on semantic segmentation of high-resolution 3D point clouds and textured meshes from UAV LiDAR and Multi-View-Stereo" — ISPRS Open Journal of Photogrammetry and Remote Sensing, 2021 — [journal article](https://doi.org/10.1016/j.ophoto.2021.100001)
     - authors: Michael Kölle, Dominik Laupheimer, Stefan Schmohl, Norbert Haala, Franz Rottensteiner, Jan Dirk Wegner, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.33; abstract similarity 0.28; year +0  (source: OpenAlex)
  2. "DDL-MVS: Depth Discontinuity Learning for Multi-View Stereo Networks" — Remote Sensing, 2023 — [journal article](https://doi.org/10.3390/rs15122970)
     - authors: Nail Ibrahimli, Hugo Ledoux (supervisor: Ledoux), Julian F. P. Kooij, Liangliang Nan
     - title similarity 0.35; abstract similarity 0.21; year +2  (source: OpenAlex)
  3. "Semantic segmentation of point clouds with the 3D medial axis transform" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-33-2025)
     - authors: Giulia Ceccarelli, Weixiao Gao, Ravi Peters (supervisor: Peters)
     - title similarity 0.43; abstract similarity 0.14; year +4  (source: OpenAlex)
  4. "A review of machine learning techniques for identifying weeds in corn" — Smart Agricultural Technology, 2022 — [journal article](https://doi.org/10.1016/j.atech.2022.100102)
     - authors: Akhil Venkataraju, Dharanidharan Arumugam, Calvin Stepan, Ravi Kiran, Thomas Peters (supervisor: Peters)
     - title similarity 0.33; abstract similarity 0.13; year +1  (source: OpenAlex)
  … and 31 more possible candidates; re-run with --limit/--surname to see them all.
- **Kristof Kenesei (2021)** — Constructing a digital 3D road network for The Netherlands
  1. "Automated 3D Reconstruction of LoD2 and LoD1 Models for All 10 Million Buildings of the Netherlands" — Photogrammetric Engineering & Remote Sensing, 2022 — [journal article](https://doi.org/10.14358/pers.21-00032r2)
     - authors: Ravi Peters (supervisor: Peters), Balázs Dukai, Stelios Vitalis, Jordi van Liempt, Jantien Stoter
     - title similarity 0.52; abstract similarity 0.18; year +1  (source: OpenAlex)
  2. "3dfier: automatic reconstruction of 3D city models" — The Journal of Open Source Software, 2021 — [journal article](https://doi.org/10.21105/joss.02866)
     - authors: Hugo Ledoux, Filip Biljecki, Balázs Dukai, Kavisha Kumar, Ravi Peters (supervisor: Peters), Jantien Stoter, Tom Commandeur
     - title similarity 0.34; abstract similarity 0.21; year +0  (source: OpenAlex)
  3. "City3D: Large-Scale Building Reconstruction from Airborne LiDAR Point Clouds" — Remote Sensing, 2022 — [journal article](https://doi.org/10.3390/rs14092254)
     - authors: Jin Huang, Jantien Stoter, Ravi Peters (supervisor: Peters), Liangliang Nan
     - title similarity 0.34; abstract similarity 0.19; year +1  (source: OpenAlex)
  4. "A review of machine learning techniques for identifying weeds in corn" — Smart Agricultural Technology, 2022 — [journal article](https://doi.org/10.1016/j.atech.2022.100102)
     - authors: Akhil Venkataraju, Dharanidharan Arumugam, Calvin Stepan, Ravi Kiran, Thomas Peters (supervisor: Peters)
     - title similarity 0.31; abstract similarity 0.20; year +1  (source: OpenAlex)
  … and 16 more possible candidates; re-run with --limit/--surname to see them all.
- **N.A. Nur An Nisa Milyana (2021)** — Designing User Experience (UX) to Support Public Participation in Spatial Planni
  1. "Implementation of the spatial plan information package for improving ease of doing business in Indonesian cities" — Land Use Policy, Elsevier, 105(105338), pp. 1-17, 2021 — [journal article](https://doi.org/10.1016/j.landusepol.2021.105338)
     - authors: Agung Indrajit, Bastiaan van Loenen (supervisor: van Loenen), Suprajaka, Virgo Eresta Jaya, Hendrik Ploeger (supervisor: Ploeger), Christiaan Lemmen, Peter van Oosterom
     - title similarity 0.40; abstract similarity 0.10; year +0  (source: GDMC)
  2. "Active teaching and learning in GI sciences: lessons learned from the BSc. Course Open Urban Data Governance" — AGILE GIScience Series, 2023 — [journal article](https://doi.org/10.5194/agile-giss-4-14-2023)
     - authors: Bastiaan van Loenen (supervisor: van Loenen), Hendrik Ploeger (supervisor: Ploeger), Noor van Everdingen, Kristian Cuervo, Jessica Monahan, Julia Pille, Carmel Verhaeghe
     - title similarity 0.31; abstract similarity 0.06; year +2  (source: OpenAlex)
  3. "4D Musrenbang: Designing User Experience (UX) to Support Public Participation in Spatial Planning for Indonesia" — Research Repository (Delft University of Technology), 2021 — [conference paper](https://doi.org/10.4233/uuid:b00ca7b9-a480-4752-b12b-f7337b62e262)
     - authors: Milyana, Nur An Nisa, van Loenen, Bastiaan, Korthals Altes, Willem, Ploeger, Hendrik
     - title similarity 0.87; abstract similarity 0.50; year +0  (source: OpenAlex)
  4. "Towards value-creating and sustainable open data ecosystems: A comparative case study and a research agenda" — JeDEM - eJournal of eDemocracy and Open Government, 2021 — [journal article](https://doi.org/10.29379/jedem.v13i2.644)
     - authors: Bastiaan Van Loenen (supervisor: van Loenen), Anneke Zuiderwijk, Glenn Vancauwenberghe, Francisco J. Lopez-Pellicer, Ingrid Mulder, Charalampos Alexopoulos, Rikke Magnussen, Mubashrah Saddiqa, Melanie Dulong de Rosnay, Joep Crompvoets, Andrea Polini, Barbara Re, Cesar Casiano Flores
     - title similarity 0.39; abstract similarity 0.08; year +0  (source: OpenAlex)
  … and 7 more possible candidates; re-run with --limit/--surname to see them all.
- **Manos Papageorgiou (2021)** — Semantic segmentation of the AHN dataset with the Random Forest Classifier
  1. "Semantic segmentation of point clouds with the 3D medial axis transform" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-33-2025)
     - authors: Giulia Ceccarelli, Weixiao Gao, Ravi Peters (supervisor: Peters)
     - title similarity 0.61; abstract similarity 0.28; year +4  (source: OpenAlex)
  2. "City3D: Large-Scale Building Reconstruction from Airborne LiDAR Point Clouds" — Remote Sensing, 2022 — [journal article](https://doi.org/10.3390/rs14092254)
     - authors: Jin Huang, Jantien Stoter, Ravi Peters (supervisor: Peters), Liangliang Nan
     - title similarity 0.29; abstract similarity 0.44; year +1  (source: OpenAlex)
  3. "3dfier: automatic reconstruction of 3D city models" — The Journal of Open Source Software, 2021 — [journal article](https://doi.org/10.21105/joss.02866)
     - authors: Hugo Ledoux, Filip Biljecki, Balázs Dukai, Kavisha Kumar, Ravi Peters (supervisor: Peters), Jantien Stoter, Tom Commandeur
     - title similarity 0.36; abstract similarity 0.30; year +0  (source: OpenAlex)
  4. "Building-PCC: Building Point Cloud Completion Benchmarks" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-179-2024)
     - authors: Weixiao Gao, Ravi Peters (supervisor: Peters), Jantien Stoter
     - title similarity 0.19; abstract similarity 0.43; year +3  (source: OpenAlex)
  … and 28 more possible candidates; re-run with --limit/--surname to see them all.
- **Anna Vera Stevers (2021)** — The effects of beach house configurations on dune-ward sediment transport
  1. "Towards Automated BIM and BEM Model Generation using a B-Rep-based Method with Topological Map" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-2024-287-2024)
     - authors: Oscar Roman, Gabriele Mazzacca, Elisa Mariarosaria Farella, Fabio Remondino, Maarten Bassier, Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.37; abstract similarity 0.11; year +3  (source: OpenAlex)
  2. "Data-Driven Energy Simulations To Evaluate Positive Energy District Potential In Rotterdam" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w7-2025-25-2025)
     - authors: Weixiao Gao, Giorgio Agugiaro (supervisor: Agugiaro), Camilo León-Sánchez
     - title similarity 0.35; abstract similarity 0.13; year +4  (source: OpenAlex)
  3. "IFC and QGIS integration for the Integrated Water Service Management" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-4-2026-13-2026)
     - authors: Michele Berlato, Giorgio Agugiaro (supervisor: Agugiaro), Ken Arroyo Ohori, Carlo Zanchetta
     - title similarity 0.36; abstract similarity 0.12; year +5  (source: OpenAlex)
  4. "Scan-to-EDTs: Automated Generation of Energy Digital Twins from 3D Point Clouds" — Buildings, 2025 — [journal article](https://doi.org/10.3390/buildings15224060)
     - authors: Oscar Roman, Maarten Bassier, Giorgio Agugiaro (supervisor: Agugiaro), Ken Arroyo Ohori, Elisa Mariarosaria Farella, Fabio Remondino
     - title similarity 0.33; abstract similarity 0.12; year +4  (source: OpenAlex)
  … and 4 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Irène Apra (2022)** — Semantic segmentation of roof superstructures
  1. "Enriching lower LoD 3D city models with semantic data computed by the voxelisation of BIM sources" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-297-2024)
     - authors: Jasper van der Vaart, Jantien Stoter, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Amir Hakim, Siham El Yamani
     - title similarity 0.34; abstract similarity 0.26; year +2  (source: OpenAlex)
  2. "Towards Extending CityGML for Property Valuation: Property Valuation ADE" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-127-2024)
     - authors: Siham El Yamani, Rafika Hajji, Roland Billen, Ken Arroyo Ohori (supervisor: Ohori), Jasper van der Vaart, Amir Hakim, Jantien Stoter
     - title similarity 0.42; abstract similarity 0.17; year +2  (source: OpenAlex)
  3. "Scan-to-EDTs: Automated Generation of Energy Digital Twins from 3D Point Clouds" — Buildings, 2025 — [journal article](https://doi.org/10.3390/buildings15224060)
     - authors: Oscar Roman, Maarten Bassier, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Elisa Mariarosaria Farella, Fabio Remondino
     - title similarity 0.37; abstract similarity 0.12; year +3  (source: OpenAlex)
  4. "IFC and QGIS integration for the Integrated Water Service Management" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-4-2026-13-2026)
     - authors: Michele Berlato, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Carlo Zanchetta
     - title similarity 0.32; abstract similarity 0.21; year +4  (source: OpenAlex)
  … and 4 more possible candidates; re-run with --limit/--surname to see them all.
- **Camilo Caceres Tocora (2022)** — Automated Semantic Segmentation of Aerial Imagery using Synthetic Data
  1. "RefineNet: a Confidence-aware Deep Online Learning Framework to Refine Real-world Point Cloud Semantic Segmentation" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-3-2026-179-2026)
     - authors: Sharath Chandra Madanu, Shenglan Du (supervisor: Du), Jantien Stoter, Daan van der Heide
     - title similarity 0.32; abstract similarity 0.40; year +4  (source: OpenAlex)
  2. "Push-the-Boundary: Boundary-aware Feature Propagation for Semantic Segmentation of 3D Point Clouds" — ?, 2022 — [conference paper](https://doi.org/10.1109/3dv57658.2022.00025)
     - authors: Shenglan Du (supervisor: Du), Nail Ibrahimli, Jantien Stoter, Julian Kooij, Liangliang Nan
     - title similarity 0.41; abstract similarity 0.17; year +0  (source: OpenAlex)
  3. "SATree: Structure-aware tree instance segmentation from 3D LiDAR point clouds" — Urban forestry & urban greening, 2026 — [journal article](https://doi.org/10.1016/j.ufug.2026.129414)
     - authors: Shenglan Du (supervisor: Du), Jantien Stoter, Julian F.P. Kooij, Liangliang Nan
     - title similarity 0.44; abstract similarity 0.15; year +4  (source: OpenAlex)
  4. "Structure- and Semantics-Aware Mesh Simplification for Generating Lightweight 3D Building Models" — Remote Sensing, 2026 — [journal article](https://doi.org/10.3390/rs18060914)
     - authors: Dong Chen, Chenwei Zhu, Shenglan Du (supervisor: Du), Yuliang Wang, Zhen Cao, Mingming Sui, Yiyang Kong, Shengjie Feng, Jiju Peethambaran, Liqiang Zhang
     - title similarity 0.37; abstract similarity 0.22; year +4  (source: OpenAlex)
  … and 30 more possible candidates; re-run with --limit/--surname to see them all.
- **Jos Feenstra (2022)** — Geofront: directly accessible GIS tools using a web-based visual programming lan
  1. "IFC and QGIS integration for the Integrated Water Service Management" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-4-2026-13-2026)
     - authors: Michele Berlato, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Carlo Zanchetta
     - title similarity 0.30; abstract similarity 0.14; year +4  (source: OpenAlex)
  2. "Defining LoDs to support BIM-based 3D building abstractions in GIS" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-55-2026)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter, Siham El Yamani
     - title similarity 0.34; abstract similarity 0.09; year +4  (source: OpenAlex)
  3. "Extracting Coastal Water Depths from Multi-Temporal Sentinel-2 Images Using Convolutional Neural Networks" — Marine Geodesy, 2022 — [journal article](https://doi.org/10.1080/01490419.2022.2091696)
     - authors: Yustisi Lumban-Gaol, Ken Arroyo Ohori (supervisor: Ohori), Ravi Peters
     - title similarity 0.32; abstract similarity 0.06; year +0  (source: OpenAlex)
- **Robin Hurkmans (2022)** — Efficient Solar Potential Estimation of 3D Buildings: 3D BAG as use case
  1. "Inferring the number of floors for residential buildings" — International Journal of Geographical Information Systems, 2022 — [journal article](https://doi.org/10.1080/13658816.2022.2160454)
     - authors: Ellie Roy, Maarten Pronk, Giorgio Agugiaro, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.35; abstract similarity 0.38; year +0  (source: OpenAlex)
  2. "Reconstructing compact building models from point clouds using deep implicit fields" — ISPRS Journal of Photogrammetry and Remote Sensing, 2022 — [journal article](https://doi.org/10.1016/j.isprsjprs.2022.09.017)
     - authors: Zhaiyu Chen, Hugo Ledoux (supervisor: Ledoux), Seyran Khademi, Liangliang Nan
     - title similarity 0.38; abstract similarity 0.30; year +0  (source: OpenAlex)
  3. "Filling holes in LoD2 building models" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-171-2024)
     - authors: Weixiao Gao, Ravi Peters, Hugo Ledoux (supervisor: Ledoux), Jantien Stoter
     - title similarity 0.43; abstract similarity 0.23; year +2  (source: OpenAlex)
  4. "Towards automatic reconstruction of 3D city models tailored for urban flow simulations" — Frontiers in Built Environment, 2022 — [journal article](https://doi.org/10.3389/fbuil.2022.899332)
     - authors: Ivan Pađen, Clara García-Sánchez, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.31; abstract similarity 0.17; year +0  (source: OpenAlex)
  … and 15 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Lars Langhorst (2022)** — Predicting sedimentation in Lake Alajuela
  1. "Extracting Coastal Water Depths from Multi-Temporal Sentinel-2 Images Using Convolutional Neural Networks" — Marine Geodesy, 2022 — [journal article](https://doi.org/10.1080/01490419.2022.2091696)
     - authors: Yustisi Lumban-Gaol, Ken Arroyo Ohori (supervisor: Ohori), Ravi Peters
     - title similarity 0.36; abstract similarity 0.18; year +0  (source: OpenAlex)
  2. "Enriching lower LoD 3D city models with semantic data computed by the voxelisation of BIM sources" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-297-2024)
     - authors: Jasper van der Vaart, Jantien Stoter, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Amir Hakim, Siham El Yamani
     - title similarity 0.30; abstract similarity 0.23; year +2  (source: OpenAlex)
  3. "IFC and QGIS integration for the Integrated Water Service Management" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-4-2026-13-2026)
     - authors: Michele Berlato, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Carlo Zanchetta
     - title similarity 0.35; abstract similarity 0.21; year +4  (source: OpenAlex)
  4. "Towards Extending CityGML for Property Valuation: Property Valuation ADE" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-127-2024)
     - authors: Siham El Yamani, Rafika Hajji, Roland Billen, Ken Arroyo Ohori (supervisor: Ohori), Jasper van der Vaart, Amir Hakim, Jantien Stoter
     - title similarity 0.36; abstract similarity 0.15; year +2  (source: OpenAlex)
  … and 4 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Kostantinos Pantelios (2022)** — Development of a QGIS plugin for the CityGML 3D City Database
  1. "Realidad aumentada para el fortalecimiento del pensamiento matemático geométrico espacial" — Panorama, 2024 — [journal article](https://doi.org/10.15765/cg8kkn05)
     - authors: Cristian Camilo Barragán Sánchez (supervisor: Sánchez), Julián Andrés Diaz León, Jorge Amado Renteria Vera
     - title similarity 0.32; abstract similarity 0.03; year +2  (source: OpenAlex)
  2. "Lineamientos para la formulación de los Programas de Gobierno 2023. Área Metropolitana de Bucaramanga" — Universidad Autonoma de Bucaramanga eBooks, 2023 — [book](https://doi.org/10.29375/9786289578706)
     - authors: María Juliana Acebedo Ordóñez, Juan Manuel Álvarez Cruz, Flor Manuelita Barrios Rodríguez, Yoana Bermúdez González, María Eugenia Bonilla Ovallos, Paul Cáceres Rojas, Geovanny Castro Aristizabal, Catalina Chacón, Camilo Alipios Cruz Merchán, Jhon Alexis Díaz Contreras, Yudy Adriana Gamboa Vesga, Valentina Gómez Castaño, Claudia Milena Hormiga Sánchez (supervisor: Sánchez), Ana María León Avellaneda, Andrea Catalina Martínez Lozada, Gustavo Mendoza López, Maryi Yurany Olarte Dueñas, Rafael Gustavo Ortiz Martínez, Ana Patricia Pabón Mantilla, Marcela Pabón Rozo, Miguel Jesús Pardo Uribe, Silvia Catalina Parra Jiménez, Laura Milena Parra Prada, Enrique Pedroza Orlando, Nadia Jimena Pérez Guevara, Juan José Rey Serrano, María Alejandra Rodríguez Duarte, Carolina Rubio Sguerra, María Alejandra Santos Barón, Luis Carlos Tiria Sandoval, Sergio Andrés Zabala Vargas, Eliana Zambrano Becerra
     - title similarity 0.32; abstract similarity 0.00; year +1  (source: OpenAlex)
  3. "Danza educativa, identidad corporal y autoestima en estudiantes escolares" — Revista Boliviana de Educación, 2026 — [journal article](https://doi.org/10.33996/rebe.v8i16.8)
     - authors: Raquel Arcenia Tenorio Sánchez (supervisor: Sánchez), Camilo Fernando León Reyes, Carolina Andrea Páez Merchan, Marjorie Geoconda Zamora Arana
     - title similarity 0.31; abstract similarity 0.00; year +4  (source: OpenAlex)
  4. "Inteligencia artificial como herramienta para la evaluación del desempeño motor en escolares" — Revista de Propuestas Educativas, 2026 — [journal article](https://doi.org/10.33996/propuestaseducativas.v8i18.1)
     - authors: Camilo Fernando León Reyes, Carolina Andrea Páez Merchan, Marjorie Geoconda Zamora Arana, Raquel Arcenia Tenorio Sánchez (supervisor: Sánchez)
     - title similarity 0.30; abstract similarity 0.00; year +4  (source: OpenAlex)
- **Androniki Pavlidou (2022)** — Integrated modeling of utility networks in the urban environment
  1. "Enriching lower LoD 3D city models with semantic data computed by the voxelisation of BIM sources" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-297-2024)
     - authors: Jasper van der Vaart, Jantien Stoter (supervisor: Stoter), Giorgio Agugiaro (supervisor: Agugiaro), Ken Arroyo Ohori, Amir Hakim, Siham El Yamani
     - title similarity 0.29; abstract similarity 0.36; year +2  (source: OpenAlex)
  2. "Lessons learnt from the integration of open data and semantic 3D city models for urban building energy modelling in the Netherlands" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w7-2025-89-2025)
     - authors: Camilo León-Sánchez, Giorgio Agugiaro (supervisor: Agugiaro), Jantien Stoter (supervisor: Stoter)
     - title similarity 0.36; abstract similarity 0.23; year +3  (source: OpenAlex)
  3. "Comparative Analysis of Geospatial Tools for Solar Simulation" — Transactions in GIS, 2025 — [journal article](https://doi.org/10.1111/tgis.13296)
     - authors: Camilo León‐Sánchez, Denis Giannelli, Giorgio Agugiaro (supervisor: Agugiaro), Jantien Stoter (supervisor: Stoter)
     - title similarity 0.36; abstract similarity 0.21; year +3  (source: OpenAlex)
  4. "High resolution solar potential computation in large scale urban areas by means of semantic 3D city models" — The international archives of the photogrammetry, remote sensing and, 2024 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-4-w11-2024-167-2024)
     - authors: Longxiang Xu, Camilo León-Sánchez, Giorgio Agugiaro (supervisor: Agugiaro), Jantien Stoter (supervisor: Stoter)
     - title similarity 0.33; abstract similarity 0.13; year +2  (source: OpenAlex)
  … and 24 more possible candidates; re-run with --limit/--surname to see them all.
- **Maarit Prusti (2022)** — How could BIM support the digital building permit process in the Netherlands?
  1. "Automated noise modelling using a triangulated terrain model" — Geo-spatial Information Science, 2023 — [journal article](https://doi.org/10.1080/10095020.2023.2270520)
     - authors: Nadine Hobeika, Laurens van Rijssel, Maarit Prusti (student), Constantijn Dinklo, Denis Giannelli, Balázs Dukai, Arnaud Kok, Rob van Loon, René Nota, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.34; abstract similarity 0.07; year +1  (source: OpenAlex)
  2. "A Methodology to Convert Highly Detailed BIM Models into 3D Geospatial Building Models at Different LoDs" — Preprints.org, 2025 — [preprint](https://doi.org/10.20944/preprints202509.2284.v1)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.40; abstract similarity 0.39; year +3  (source: OpenAlex)
  3. "A Methodology to Convert Highly Detailed BIM Models into 3D Geospatial Building Models at Different LoDs" — ISPRS International Journal of Geo-Information, 2025 — [journal article](https://doi.org/10.3390/ijgi14120465)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.40; abstract similarity 0.34; year +3  (source: OpenAlex)
  4. "Defining LoDs to support BIM-based 3D building abstractions in GIS" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-55-2026)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori, Jantien Stoter (supervisor: Stoter), Siham El Yamani
     - title similarity 0.43; abstract similarity 0.26; year +4  (source: OpenAlex)
  … and 21 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Noortje van der Horst (2022)** — Procedural Modelling of Tree Growth Using Multi-temporal Point Clouds
  1. "City3D: Large-Scale Building Reconstruction from Airborne LiDAR Point Clouds" — Remote Sensing, 2022 — [journal article](https://doi.org/10.3390/rs14092254)
     - authors: Jin Huang, Jantien Stoter (supervisor: Stoter), Ravi Peters, Liangliang Nan (supervisor: Nan)
     - title similarity 0.44; abstract similarity 0.24; year +0  (source: OpenAlex)
  2. "SATree: Structure-aware tree instance segmentation from 3D LiDAR point clouds" — Urban forestry & urban greening, 2026 — [journal article](https://doi.org/10.1016/j.ufug.2026.129414)
     - authors: Shenglan Du, Jantien Stoter (supervisor: Stoter), Julian F.P. Kooij, Liangliang Nan (supervisor: Nan)
     - title similarity 0.33; abstract similarity 0.37; year +4  (source: OpenAlex)
  3. "A benchmark approach and dataset for large-scale lane mapping from MLS point clouds" — International Journal of Applied Earth Observation and Geoinformation, 2024 — [journal article](https://doi.org/10.1016/j.jag.2024.104139)
     - authors: Xiaoxin Mi, Zhen Dong, Zhipeng Cao, Bisheng Yang, Chao Zheng, Jantien Stoter (supervisor: Stoter), Liangliang Nan (supervisor: Nan)
     - title similarity 0.43; abstract similarity 0.11; year +2  (source: OpenAlex)
  4. "Semi-automated indoor geometry reconstruction for daylight simulation" — Building and Environment, 2025 — [journal article](https://doi.org/10.1016/j.buildenv.2025.114045)
     - authors: Nima Forouzandeh, Jin Huang, Liangliang Nan (supervisor: Nan), Eleonora Brembilla, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.31; abstract similarity 0.16; year +3  (source: OpenAlex)
  … and 52 more possible candidates; re-run with --limit/--surname to see them all.
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
  … and 43 more possible candidates; re-run with --limit/--surname to see them all.
- **Ziyan Wu (2022)** — Estimating building height from ICESat-2 data: The case of the Netherlands
  1. "Reinforcement learning in building controls: A comparative study of algorithms considering model availability and policy representation" — Journal of Building Engineering, 2024 — [journal article](https://doi.org/10.1016/j.jobe.2024.109497)
     - authors: Ziyan Wu (student; first author), Wenhao Zhang, Rui Tang, Huilong Wang, Ivan Korolija
     - title similarity 0.30; abstract similarity n/a; year +2  (source: Crossref)
  2. "Muflex: A Scalable, Physics-Based Platform for Multi-Building Flexibility Analysis and Coordination" — ?, 2025 — [posted-content](https://doi.org/10.2139/ssrn.5403344)
     - authors: Ziyan Wu (student; first author), Ivan Korolija, Rui Tang
     - title similarity 0.27; abstract similarity n/a; year +3  (source: Crossref)
  3. "Muflex: A Scalable, Physics-Based Platform for Multi-Building Flexibility Analysis and Coordination" — ?, 2025 — [posted-content](https://doi.org/10.2139/ssrn.5401124)
     - authors: Ziyan Wu (student; first author), Ivan Korolija, Rui Tang
     - title similarity 0.27; abstract similarity n/a; year +3  (source: Crossref)
  4. "MuFlex: A scalable, physics-based platform for multi-building flexibility analysis and coordination" — Energy, 2026 — [journal article](https://doi.org/10.1016/j.energy.2026.140565)
     - authors: Ziyan Wu (student; first author), Ivan Korolija, Rui Tang
     - title similarity 0.27; abstract similarity n/a; year +4  (source: Crossref)
  … and 10 more possible candidates; re-run with --limit/--surname to see them all.
- **Daniël Dobson (2023)** — Floor count from street view imagery using learning-based façade parsing
  1. "Creating 3D city models of Mexican cities based on open data" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-3-2026)
     - authors: Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.34; abstract similarity 0.14; year +3  (source: OpenAlex)
  2. "A Methodology to Convert Highly Detailed BIM Models into 3D Geospatial Building Models at Different LoDs" — Preprints.org, 2025 — [preprint](https://doi.org/10.20944/preprints202509.2284.v1)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.36; abstract similarity 0.11; year +2  (source: OpenAlex)
  3. "A Methodology to Convert Highly Detailed BIM Models into 3D Geospatial Building Models at Different LoDs" — ISPRS International Journal of Geo-Information, 2025 — [journal article](https://doi.org/10.3390/ijgi14120465)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.36; abstract similarity 0.09; year +2  (source: OpenAlex)
  4. "Defining LoDs to support BIM-based 3D building abstractions in GIS" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-55-2026)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter, Siham El Yamani
     - title similarity 0.32; abstract similarity 0.09; year +3  (source: OpenAlex)
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
- **Tendai Mbwanda (2023)** — Further Development of a QGIS plugin for the CityGML 3D City Database
  1. "Introducing server-side support for 3DCityDB 5.0 to the 3DCityDB-Tools plug-in for QGIS" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-193-2025)
     - authors: Bing-Shiuan Tsai, Giorgio Agugiaro (supervisor: Agugiaro), Camilo Leon-Sanchez, Claus Nagel, Zhihang Yao
     - title similarity 0.31; abstract similarity 0.50; year +2  (source: OpenAlex)
  2. "Mapping the CityGML Energy ADE to CityGML 3.0 Using a Model-Driven Approach" — ISPRS International Journal of Geo-Information, 2024 — [journal article](https://doi.org/10.3390/ijgi13040121)
     - authors: Carolin Bachert, Camilo León-Sánchez, Tatjana Kutzner, Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.37; abstract similarity 0.41; year +1  (source: OpenAlex)
  3. "A proposal to update and enhance the CityGML Energy Application Domain Extension" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-1-2025)
     - authors: Giorgio Agugiaro (supervisor: Agugiaro), Rushikesh Padsala
     - title similarity 0.33; abstract similarity 0.35; year +2  (source: OpenAlex)
  4. "From point clouds to CityGML 3.0: An approach to multi-granular urban road modelling" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-201-2025)
     - authors: Elisavet Tsiranidou, Giorgio Agugiaro (supervisor: Agugiaro), Antonio Fernández, Lucía Díaz Vilariño
     - title similarity 0.35; abstract similarity 0.27; year +2  (source: OpenAlex)
  … and 7 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Leon Powalka (2023)** — Shape-guided artistic route finding
  1. "MuVieCAST: Multi-View Consistent Artistic Style Transfer" — ?, 2024 — [conference paper](https://doi.org/10.1109/3dv62453.2024.00090)
     - authors: Nail Ibrahimli, Julian F. P. Kooij, Liangliang Nan (supervisor: Nan)
     - title similarity 0.35; abstract similarity 0.09; year +1  (source: OpenAlex)
  2. "High-speed, self-powered, and position-sensitive photodetector based on ReS2/Si heterojunction" — Applied Physics Letters, 2025 — [journal article](https://doi.org/10.1063/5.0289301)
     - authors: Longyu Lyu, Haiyan Nan (supervisor: Nan), Yuan Gao, Jialing Jian, Zhengjin Weng, Chengxin Jiang, Haomin Wang, Liangliang Lin, Shaoqing Xiao, Xiaofeng Gu
     - title similarity 0.34; abstract similarity 0.05; year +2  (source: OpenAlex)
  3. "AdLeaf: Quantitative Leaf Reconstruction From TLS Point Clouds" — IEEE Transactions on Geoscience and Remote Sensing, 2025 — [journal article](https://doi.org/10.1109/tgrs.2025.3608325)
     - authors: Guangpeng Fan, Liangliang Xu, Jiani Guo, Ruoyoulan Wang, Haoran Zhao, Hao Lu, Feixiang Chen, Liangliang Nan (supervisor: Nan)
     - title similarity 0.35; abstract similarity 0.03; year +2  (source: OpenAlex)
  4. "NeuSEditor: From Multi-View Images to Text-Guided Neural Surface Edits" — ?, 2026 — [conference paper](https://doi.org/10.1109/3dv69130.2026.00135)
     - authors: Nail Ibrahimli, Julian F. P. Kooij, Liangliang Nan (supervisor: Nan)
     - title similarity 0.33; abstract similarity 0.05; year +3  (source: OpenAlex)
  … and 7 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Fabian Visser (2023)** — Neural Surface Reconstruction and Stylization
  1. "MuVieCAST: Multi-View Consistent Artistic Style Transfer" — ?, 2024 — [conference paper](https://doi.org/10.1109/3dv62453.2024.00090)
     - authors: Nail Ibrahimli (supervisor: Ibrahimli), Julian F. P. Kooij, Liangliang Nan (supervisor: Nan)
     - title similarity 0.40; abstract similarity 0.36; year +1  (source: OpenAlex)
  2. "NeuSEditor: From Multi-View Images to Text-Guided Neural Surface Edits" — ?, 2026 — [conference paper](https://doi.org/10.1109/3dv69130.2026.00135)
     - authors: Nail Ibrahimli (supervisor: Ibrahimli), Julian F. P. Kooij, Liangliang Nan (supervisor: Nan)
     - title similarity 0.30; abstract similarity 0.23; year +3  (source: OpenAlex)
  3. "Parametric Point Cloud Completion for Polygonal Surface Reconstruction" — ?, 2025 — [conference paper](https://doi.org/10.1109/cvpr52734.2025.01097)
     - authors: Zhaiyu Chen, Yuqing Wang, Liangliang Nan (supervisor: Nan), Xiao Xiang Zhu
     - title similarity 0.50; abstract similarity 0.10; year +2  (source: OpenAlex)
  4. "Fast Building Instance Proxy Reconstruction for Large Urban Scenes" — IEEE Transactions on Pattern Analysis and Machine Intelligence, 2024 — [journal article](https://doi.org/10.1109/tpami.2024.3388371)
     - authors: Jianwei Guo, Haobo Qin, Yinchang Zhou, Xin Chen, Liangliang Nan (supervisor: Nan), Hui Huang
     - title similarity 0.44; abstract similarity 0.13; year +1  (source: OpenAlex)
  … and 29 more possible candidates; re-run with --limit/--surname to see them all.
- **Lan Yan (2023)** — Extraction of Exterior Building Envelopes from Building Information Models
  1. "Scan-to-EDTs: Automated Generation of Energy Digital Twins from 3D Point Clouds" — Buildings, 2025 — [journal article](https://doi.org/10.3390/buildings15224060)
     - authors: Oscar Roman, Maarten Bassier, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Elisa Mariarosaria Farella, Fabio Remondino
     - title similarity 0.41; abstract similarity 0.31; year +2  (source: OpenAlex)
  2. "Defining LoDs to support BIM-based 3D building abstractions in GIS" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-55-2026)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter, Siham El Yamani
     - title similarity 0.25; abstract similarity 0.39; year +3  (source: OpenAlex)
  3. "Automatic 3D Building Model Generation for Energy Digital Twins" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-1-2026-447-2026)
     - authors: Oscar Roman, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Maarten Bassier, Elisa Mariarosaria Farella, Fabio Remondino
     - title similarity 0.41; abstract similarity 0.21; year +3  (source: OpenAlex)
  4. "Leveraging knowledge graphs and semantic web technologies for validating 3D city models" — International Journal of Geographical Information Systems, 2025 — [journal article](https://doi.org/10.1080/13658816.2025.2578723)
     - authors: Alper Tunga Akın, Ziya Usta, Jantien Stoter, Ken Arroyo Ohori (supervisor: Ohori), Çetin Cömert
     - title similarity 0.39; abstract similarity 0.08; year +2  (source: OpenAlex)
  … and 3 more possible candidates; re-run with --limit/--surname to see them all.
- **Fengyan Zhang (2023)** — Snap rounding polygons with a triangulation
  1. "The backward rounding error analysis of the quaternion Givens QR decomposition" — Numerical Algorithms, 2025 — [journal article](https://doi.org/10.1007/s11075-024-02002-8)
     - authors: Fengxia Zhang (student; first author), Yuqing Zhang, Zhihan Zhou, Musheng Wei
     - title similarity 0.32; abstract similarity n/a; year +2  (source: Crossref)
  2. "startinpy: A Python library for modelling and processing 2.5D triangulated terrains" — The Journal of Open Source Software, 2024 — [journal article](https://doi.org/10.21105/joss.07123)
     - authors: Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.39; abstract similarity 0.13; year +1  (source: OpenAlex)
  3. "Code supporting: DDL-MVS: Depth Discontinuity Learning for MVS Networks" — 4TU.ResearchData, 2026 — [software](https://doi.org/10.4121/a52925e4-21df-40ae-a030-6ff4d80086e7.v1)
     - authors: Ibrahimli, Nail, H. (Hugo) Ledoux (supervisor: Ledoux), Kooij, Julian, Nan, Liangliang
     - title similarity 0.37; abstract similarity 0.11; year +3  (source: OpenAlex)
  4. "Code supporting: DDL-MVS: Depth Discontinuity Learning for MVS Networks" — 4TU.ResearchData, 2026 — [software](https://doi.org/10.4121/a52925e4-21df-40ae-a030-6ff4d80086e7)
     - authors: Ibrahimli, Nail, H. (Hugo) Ledoux (supervisor: Ledoux), Kooij, Julian, Nan, Liangliang
     - title similarity 0.37; abstract similarity 0.11; year +3  (source: OpenAlex)
  … and 18 more possible candidates; re-run with --limit/--surname to see them all.
- **Gees Brouwer (2024)** — Automated data-driven generation of 3D coral reef models: Assessing and integrat
  1. "VeriFog: A Generic Model-based Approach for Verifying Fog Systems at Design Time" — ?, 2024 — [conference paper](https://doi.org/10.1145/3605098.3635973)
     - authors: Hiba Awad, Abdelghani Alidra, Hugo Bruneliere, Thomas Ledoux (supervisor: Ledoux), Etienne Leclercq, Jonathan Rivalan
     - title similarity 0.34; abstract similarity 0.16; year +0  (source: OpenAlex)
  2. "Automated Levee Detection in Digital Elevation Models" — ?, 2026 — [preprint](https://doi.org/10.31223/x57x8x)
     - authors: Maarten Pronk, Matthijs Gawehn, Marieke Eleveld, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.35; abstract similarity 0.15; year +2  (source: OpenAlex)
  3. "VeriFogOps: Automated Deployment Tool Selection and CI/CD Pipeline Generation for Verifying Fog Systems at Deployment Time" — ?, 2025 — [conference paper](https://doi.org/10.1145/3672608.3707854)
     - authors: Hiba Awad, Thomas Ledoux (supervisor: Ledoux), Hugo Bruneliere, Jonathan Rivalan
     - title similarity 0.38; abstract similarity 0.09; year +1  (source: OpenAlex)
  4. "startinpy: A Python library for modelling and processing 2.5D triangulated terrains" — The Journal of Open Source Software, 2024 — [journal article](https://doi.org/10.21105/joss.07123)
     - authors: Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.36; abstract similarity 0.05; year +0  (source: OpenAlex)
  … and 6 more possible candidates; re-run with --limit/--surname to see them all.
- **Louis Dechamps (2024)** — Spatial and semantic enrichment of utility networks data
  1. "Lessons learnt from the integration of open data and semantic 3D city models for urban building energy modelling in the Netherlands" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w7-2025-89-2025)
     - authors: Camilo León-Sánchez, Giorgio Agugiaro (supervisor: Agugiaro), Jantien Stoter
     - title similarity 0.31; abstract similarity 0.31; year +1  (source: OpenAlex)
  2. "Semantic 3D city models as support for urban flood resilience: experiences from Rotterdam" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w4-2024-5-2024)
     - authors: Lara Andriessen, Giorgio Agugiaro (supervisor: Agugiaro), Aloys Borgers, Pieter Pauwels
     - title similarity 0.32; abstract similarity 0.17; year +0  (source: OpenAlex)
  3. "High resolution solar potential computation in large scale urban areas by means of semantic 3D city models" — The international archives of the photogrammetry, remote sensing and, 2024 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-4-w11-2024-167-2024)
     - authors: Longxiang Xu, Camilo León-Sánchez, Giorgio Agugiaro (supervisor: Agugiaro), Jantien Stoter
     - title similarity 0.32; abstract similarity 0.09; year +0  (source: OpenAlex)
  4. "Shadowing Calculation on Urban Areas from Semantic 3D City Models" — Lecture notes in geoinformation and cartography, 2024 — [conference paper](https://doi.org/10.1007/978-3-031-43699-4_2)
     - authors: Longxiang Xu, Camilo León-Sánchez, Giorgio Agugiaro (supervisor: Agugiaro), Jantien Stoter
     - title similarity 0.38; abstract similarity n/a; year +0  (source: OpenAlex)
- **Yingxin Feng (2024)** — 3D building model edit with generative AI
  1. "Automatic 3D Building Model Generation for Energy Digital Twins" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-1-2026-447-2026)
     - authors: Oscar Roman, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Maarten Bassier, Elisa Mariarosaria Farella, Fabio Remondino
     - title similarity 0.58; abstract similarity 0.09; year +2  (source: OpenAlex)
  2. "Creating 3D city models of Mexican cities based on open data" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-3-2026)
     - authors: Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.35; abstract similarity 0.16; year +2  (source: OpenAlex)
  3. "A Methodology to Convert Highly Detailed BIM Models into 3D Geospatial Building Models at Different LoDs" — ISPRS International Journal of Geo-Information, 2025 — [journal article](https://doi.org/10.3390/ijgi14120465)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.32; abstract similarity 0.17; year +1  (source: OpenAlex)
  4. "A Methodology to Convert Highly Detailed BIM Models into 3D Geospatial Building Models at Different LoDs" — Preprints.org, 2025 — [preprint](https://doi.org/10.20944/preprints202509.2284.v1)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.32; abstract similarity 0.17; year +1  (source: OpenAlex)
  … and 7 more possible candidates; re-run with --limit/--surname to see them all.
- **Irina Gheorghiu (2024)** — Analysis of the visibility of GPS satellites in the urban environment using poin
  1. "Comparison of cloud-to-cloud distance calculation methods for change detection in spatio-temporal point clouds" — ?, 2024 — [conference paper](https://doi.org/10.5194/egusphere-egu24-8191)
     - authors: Vitali Diaz, Peter van Oosterom, Martijn Meijers, Edward Verbree (supervisor: Verbree), Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.34; abstract similarity 0.23; year +0  (source: OpenAlex)
  2. "Indoor localisation through Isovist fingerprinting from point clouds and floor plans" — Journal of Location Based Services, 2024 — [journal article](https://doi.org/10.1080/17489725.2024.2320642)
     - authors: Georgios Triantafyllou, Edward Verbree (supervisor: Verbree), Azarakhsh Rafiee
     - title similarity 0.40; abstract similarity 0.09; year +0  (source: OpenAlex)
  3. "Exploring the Potential of Gaussian Splatting Environment for Indoor Wayfinding Simulation" — Proceedings AGILE 2025 workshop Geo xR (Dresden, Germany), pp. 6, 2025 — [conference paper](https://sites.google.com/view/geo-xr-workshop-agile205/home)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter Van Oosterom
     - title similarity 0.44; abstract similarity n/a; year +1  (source: GDMC)
  4. "Photorealistic Indoor Virtual Environments for Wayfinding: Exploring the Feasibility and Initial Evaluation of Gaussian Splatting in VR Simulation" — IOP Conference Series Earth and Environmental Science, 2026 — [conference paper](https://doi.org/10.1088/1755-1315/1647/1/012001)
     - authors: Adibah Nurul Yunisya, Edward Verbree (supervisor: Verbree), Peter van Oosterom, Sisi Zlatanova, Yingwen Yu
     - title similarity 0.32; abstract similarity 0.10; year +2  (source: OpenAlex)
  … and 5 more possible candidates; re-run with --limit/--surname to see them all.
- **Sicong Gong (2024)** — Towards Adaptive Trajectory Data Management: Modelling, Accessing, Distributing,
  1. "An nD-histogram technique for querying non-uniformly distributed point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 224, , 2025 — [journal article](https://doi.org/10.1016/j.isprsjprs.2025.03.014)
     - authors: Haicheng Liu, Zhiwei Li, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Chuqi Zhang
     - title similarity 0.38; abstract similarity n/a; year +1  (source: GDMC)
  2. "Exploiting big point clouds: Unveiling insights for sustainable development through change detection in the built environment" — Chapter in: Digitalisation of the Built Environment: 3rd 4TU-14UAS Res, 2024 — [conference paper](https://resolver.tudelft.nl/uuid:91725b0a-bfe6-4dd7-b6f2-b9c036c64122)
     - authors: Vitali Diaz, Peter Van Oosterom, Martijn Meijers (supervisor: Meijers), Edward Verbree, Nauman Ahmed, Thijs Van Lankveld
     - title similarity 0.31; abstract similarity n/a; year +0  (source: GDMC)
- **Leo Kan (2024)** — Spatial Height Prediction of ICESat-2 Data using Random Forest Regression
  1. "startinpy: A Python library for modelling and processing 2.5D triangulated terrains" — The Journal of Open Source Software, 2024 — [journal article](https://doi.org/10.21105/joss.07123)
     - authors: Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.34; abstract similarity 0.24; year +0  (source: OpenAlex)
  2. "Assessing Vertical Accuracy and Spatial Coverage of ICESat-2 and GEDI Spaceborne Lidar for Creating Global Terrain Models" — Remote Sensing, 2024 — [journal article](https://doi.org/10.3390/rs16132259)
     - authors: Maarten Pronk, Marieke Eleveld, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.37; abstract similarity 0.16; year +0  (source: OpenAlex)
  3. "RoofSense: A Multimodal Semantic Segmentation Dataset for Roofing Material Classification" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-153-2025)
     - authors: Dimitris Mantas, Weixiao Gao, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.41; abstract similarity 0.11; year +1  (source: OpenAlex)
  4. "FlatCityBuf: A new cloud-optimised CityJSON format" — The international archives of the photogrammetry, remote sensing and, 2025 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-17-2025)
     - authors: Hidemichi Baba, Hugo Ledoux (supervisor: Ledoux), Ravi Peters
     - title similarity 0.30; abstract similarity 0.22; year +1  (source: OpenAlex)
  … and 6 more possible candidates; re-run with --limit/--surname to see them all.
- **Lisa Keurentjes (2024)** — An automatic geometry repair framework for semantic 3D city models: Develop a fr
  1. "Automatic high-detailed building reconstruction workflow for urban microscale simulations" — Building and Environment, 2024 — [journal article](https://doi.org/10.1016/j.buildenv.2024.111978)
     - authors: Ivan Pađen, Ravi Peters, Clara García-Sánchez, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.32; abstract similarity n/a; year +0  (source: OpenAlex)
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
     - authors: Sitong Li (student; first author), Lirong Zeng
     - title similarity 0.34; abstract similarity 0.15; year +1  (source: Crossref)
  2. "Enriching lower LoD 3D city models with semantic data computed by the voxelisation of BIM sources" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2024 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w5-2024-297-2024)
     - authors: Jasper van der Vaart, Jantien Stoter, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Amir Hakim, Siham El Yamani
     - title similarity 0.40; abstract similarity 0.39; year +0  (source: OpenAlex)
  3. "Enhancing Georeferencing of IFC Models through Surveyed Points Integration" — The international archives of the photogrammetry, remote sensing and, 2024 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-4-w11-2024-41-2024)
     - authors: Amir Hakim, Ken Arroyo Ohori (supervisor: Ohori), Jasper van der Vaart, Siham El Yamani, Jantien Stoter
     - title similarity 0.44; abstract similarity 0.32; year +0  (source: OpenAlex)
  4. "Creating 3D city models of Mexican cities based on open data" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-3-2026)
     - authors: Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.39; abstract similarity 0.32; year +2  (source: OpenAlex)
  … and 6 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Hoi-Kang (Chris) Poon (2024)** — Inferring the residential building type from 3DBAG
  1. "Scenario-based energy simulation of tree planting strategies to reduce the heating and cooling demand of buildings under 2050 climate conditions" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlix-b4-2026-513-2026)
     - authors: Adhisye Rahmawati, Weixiao Gao, Camilo León Sánchez (supervisor: Sánchez), Giorgio Agugiaro
     - title similarity 0.33; abstract similarity 0.19; year +2  (source: OpenAlex)
  2. "Changes in social norms during the early stages of the COVID-19 pandemic across 43 countries" — Nature Communications, 2024 — [journal article](https://doi.org/10.1038/s41467-024-44999-5)
     - authors: Giulia Andrighetto, Aron Szekely, Andrea Guido, Michele Gelfand, Jered Abernathy, Gizem Arikan, Zeynep Aycan, Shweta Bankar, Davide Barrera, Dana Basnight-Brown, Anabel Belaus, Elizaveta Berezina, Sheyla Blumen, Paweł Boski, Huyen Thi Thu Bui, Juan Camilo Cárdenas, Đorđe Čekrlija, Mícheál de Barra, Piyanjali de Zoysa, Angela Dorrough, Jan B. Engelmann, Hyun Euh, Susann Fiedler, Olivia Foster-Gimbel, Gonçalo Freitas, Marta Fülöp, Ragna B. Gardarsdottir, Colin Mathew Hugues D. Gill, Andreas Glöckner, Sylvie Graf, Ani Grigoryan, Katarzyna Growiec, Hirofumi Hashimoto, Tim Hopthrow, Martina Hřebíčková, Hirotaka Imada, Yoshio Kamijo, Hansika Kapoor, Yoshihisa Kashima, Narine Khachatryan, Natalia Kharchenko, Diana León, Lisa M. Leslie, Yang Li, Kadi Liik, Marco Tullio Liuzza, Angela T. Maitner, Pavan Mamidi, Michele McArdle, Imed Medhioub, Maria Luisa Mendes Teixeira, Sari Mentser, Francisco Morales, Jayanth Narayanan, Kohei Nitta, Ravit Nussinson, Nneoma G. Onyedire, Ike E. Onyishi, Evgeny Osin, Seniha Özden, Penny Panagiotopoulou, Oleksandr Pereverziev, Lorena R. Perez-Floriano, Anna-Maija Pirttilä-Backman, Marianna Pogosyan, Jana Raver, Cecilia Reyna, Ricardo Borges Rodrigues, Sara Romanò, Pedro P. Romero, Inari Sakki, Angel Sánchez (supervisor: Sánchez), Sara Sherbaji, Brent Simpson, Lorenzo Spadoni, Eftychia Stamkou, Giovanni A. Travaglino, Paul A. M. Van Lange, Fiona Fira Winata, Rizqy Amelia Zein, Qing-peng Zhang, Kimmo Eriksson
     - title similarity 0.33; abstract similarity 0.08; year +0  (source: OpenAlex)
  3. "Compendio Memorias de Investigación. 3er Encuentro Virtual de Investigadores de Posgrado" — ?, 2024 — [book](https://doi.org/10.26620/uniminuto/3028-4619.2024)
     - authors: Alena Proshakova, Romero Meza Alex J., Alexander Gordillo Gaitán, Andrea Estefanía Restrepo Rodríguez, Angélica Gallego Rivera, Anivar Chaves-Torres, Carlos Alberto Ramírez Noreña, Catalina Quintero-López, Diana Catalina Wilches Alarcón, Diana Macias Cobo, Diana Patricia de Castro Daza, Éder García Dussán, Edgar González Bohórquez, Edna María Restrepo Andrade, Fernando Martínez Abad, Fernando Vallejo Cabrera, Francisco Javier Blanchar Añez, Gloria Inés Figueroa Correa, Jasveidy Yuliany Becerra Ascanio, José de Jesús González Méndez, Lorena Carreón Calvillo, Luis Felipe Arturo, Luis García-Noguera, Luz Stella Ospina, Marby Lucero Gutiérrez Sánchez (supervisor: Sánchez), Marcela Rodríguez González, Miguel Ángel Vázquez León, Miralba Correa Restrepo, Natalia Son Vargas, Néstor Eduardo Figueroa Cardona, Paola Elizabeth Noguera, Raúl Jiménez, Ricardo Timarán Pereira, Sandra María Cardona Álzate, Valentín Redondo Blasco, Verónica Martínez Guzmán, Víctor Daniel GilVer, Yasmine Adriana Camelo Bergaño, Yeimy Carolina Saavedra Gómez, Yurany Vásquez Bermúdez
     - title similarity 0.35; abstract similarity 0.00; year +0  (source: OpenAlex)
  4. "Danza educativa, identidad corporal y autoestima en estudiantes escolares" — Revista Boliviana de Educación, 2026 — [journal article](https://doi.org/10.33996/rebe.v8i16.8)
     - authors: Raquel Arcenia Tenorio Sánchez (supervisor: Sánchez), Camilo Fernando León Reyes, Carolina Andrea Páez Merchan, Marjorie Geoconda Zamora Arana
     - title similarity 0.31; abstract similarity 0.00; year +2  (source: OpenAlex)
- **Oliver Post (2024)** — The City Stack: A morphology-based city analysis and generation framework
  1. "FlatCityBuf: A new cloud-optimised CityJSON format" — The international archives of the photogrammetry, remote sensing and, 2025 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-17-2025)
     - authors: Hidemichi Baba, Hugo Ledoux (supervisor: Ledoux), Ravi Peters
     - title similarity 0.42; abstract similarity 0.26; year +1  (source: OpenAlex)
  2. "VeriFog: A Generic Model-based Approach for Verifying Fog Systems at Design Time and Generating Deployment Configurations" — ACM SIGAPP Applied Computing Review, 2024 — [journal article](https://doi.org/10.1145/3699839.3699841)
     - authors: Hiba Awad, Abdelghani Alidra, Hugo Bruneliere, Thomas Ledoux (supervisor: Ledoux), Jonathan Rivalan
     - title similarity 0.41; abstract similarity 0.09; year +0  (source: OpenAlex)
  3. "RoofSense: A Multimodal Semantic Segmentation Dataset for Roofing Material Classification" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2025 — [journal article](https://doi.org/10.5194/isprs-annals-x-4-w6-2025-153-2025)
     - authors: Dimitris Mantas, Weixiao Gao, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.31; abstract similarity 0.18; year +1  (source: OpenAlex)
  4. "SUM Parts: Benchmarking Part-Level Semantic Segmentation of Urban Meshes" — ?, 2025 — [conference paper](https://doi.org/10.1109/cvpr52734.2025.02279)
     - authors: Weixiao Gao, Liangliang Nan, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.35; abstract similarity 0.11; year +1  (source: OpenAlex)
  … and 5 more possible candidates; re-run with --limit/--surname to see them all.
- **Qiwei Shen (2024)** — Plant Skeleton Extraction and Stem-leaf Segmentation
  1. "PathNet: Path-Selective Point Cloud Denoising" — IEEE Transactions on Pattern Analysis and Machine Intelligence, 2024 — [journal article](https://doi.org/10.1109/tpami.2024.3355988)
     - authors: Zeyong Wei, Honghua Chen, Liangliang Nan (supervisor: Nan), Jun Wang, Jing Qin
     - title similarity 0.42; abstract similarity 0.15; year +0  (source: OpenAlex)
  2. "PointCG: Self-Supervised Point Cloud Learning via Joint Completion and Generation" — IEEE Transactions on Visualization and Computer Graphics, 2025 — [journal article](https://doi.org/10.1109/tvcg.2025.3526257)
     - authors: Yun Liu, Peng Li, Xuefeng Yan, Liangliang Nan (supervisor: Nan), Bing Wang, Honghua Chen, Lina Gong, Wei Zhao, Mingqiang Wei
     - title similarity 0.31; abstract similarity 0.23; year +1  (source: OpenAlex)
  3. "Parametric Point Cloud Completion for Polygonal Surface Reconstruction" — ?, 2025 — [conference paper](https://doi.org/10.1109/cvpr52734.2025.01097)
     - authors: Zhaiyu Chen, Yuqing Wang, Liangliang Nan (supervisor: Nan), Xiao Xiang Zhu
     - title similarity 0.31; abstract similarity 0.20; year +1  (source: OpenAlex)
  4. "AdLeaf: Quantitative Leaf Reconstruction From TLS Point Clouds" — IEEE Transactions on Geoscience and Remote Sensing, 2025 — [journal article](https://doi.org/10.1109/tgrs.2025.3608325)
     - authors: Guangpeng Fan, Liangliang Xu, Jiani Guo, Ruoyoulan Wang, Haoran Zhao, Hao Lu, Feixiang Chen, Liangliang Nan (supervisor: Nan)
     - title similarity 0.38; abstract similarity 0.14; year +1  (source: OpenAlex)
  … and 28 more possible candidates; re-run with --limit/--surname to see them all.
- **Josephine Spit (2024)** — Evaluating Gender-Blindness and User Satisfaction in Dutch Campus Map Creation
  1. "The Data Republic: fostering a sustainable, inclusive and resilient digital transformation for the European Union" — Frontiers in Political Science, 2025 — [journal article](https://doi.org/10.3389/fpos.2025.1670152)
     - authors: Stefano Calzati (supervisor: Calzati), Bastiaan van Loenen (supervisor: van Loenen)
     - title similarity 0.34; abstract similarity 0.01; year +1  (source: OpenAlex)
  2. "Exploring the contributions of open data intermediaries for a sustainable open data ecosystem" — Data & Policy, 2024 — [journal article](https://doi.org/10.1017/dap.2024.63)
     - authors: Ashraf Shaharudin, Bastiaan van Loenen (supervisor: van Loenen), Marijn Janssen
     - title similarity 0.35; abstract similarity 0.05; year +0  (source: OpenAlex)
  3. "Business model archetypes of open data intermediaries: Empirical insights from practice" — Electronic Markets, 2026 — [journal article](https://doi.org/10.1007/s12525-026-00882-3)
     - authors: Ashraf Shaharudin, Bastiaan van Loenen (supervisor: van Loenen), Marijn Janssen
     - title similarity 0.31; abstract similarity 0.04; year +2  (source: OpenAlex)
- **Pam Sterkman (2024)** — Exploring the potential of explorative point clouds in floodplain maintenance
  1. "Comparison of cloud-to-cloud distance calculation methods for change detection in spatio-temporal point clouds" — ?, 2024 — [conference paper](https://doi.org/10.5194/egusphere-egu24-8191)
     - authors: Vitali Diaz, Peter van Oosterom, Martijn Meijers, Edward Verbree (supervisor: Verbree), Nauman Ahmed, Thijs van Lankveld
     - title similarity 0.31; abstract similarity 0.54; year +0  (source: OpenAlex)
  2. "Point Clouds for 3D Land Administration: Integrating Floor Plans and Nationwide Airborne LiDAR (AHN)" — ISPRS - International Archives of the Photogrammetry, Remote Sensing a, 2025 — [conference paper](https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-9-2025)
     - authors: Citra Andinasari, Peter van Oosteroom, Edward Verbree (supervisor: Verbree)
     - title similarity 0.36; abstract similarity 0.33; year +1  (source: GDMC)
  3. "Direct Use of Indoor Point Clouds for Path Planning and Navigation Exploration in Emergency Situations" — Chapter in: The International Archives of the Photogrammetry, Remote S, 2024 — [conference paper](https://isprs-archives.copernicus.org/articles/XLVIII-4-W11-2024/175/2024/)
     - authors: Algan Yasar, Robert Vo&ucirc;te, Edward Verbree (supervisor: Verbree), Robert Voûte
     - title similarity 0.36; abstract similarity 0.21; year +0  (source: GDMC)
  4. "Smart point cloud–guided 3D gaussian splatting for urban modeling and data-driven analysis" — Sustainable Cities and Society, Elsevier BV, 149, pp. 107753, 2026 — [journal article](https://doi.org/10.1016/j.scs.2026.107753)
     - authors: Yingwen Yu, Zhuoyue Wang, Guanting Zhang, Peter van Oosterom, Edward Verbree (supervisor: Verbree), Steffen Nijhuis, Yuyang Peng
     - title similarity 0.39; abstract similarity 0.15; year +2  (source: GDMC)
  … and 11 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Qiuxian Wei (2024)** — Multi-levels of detail terrain construction for navigation
  1. "Defining LoDs to support BIM-based 3D building abstractions in GIS" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-55-2026)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter, Siham El Yamani
     - title similarity 0.32; abstract similarity 0.27; year +2  (source: OpenAlex)
  2. "Automatic 3D Building Model Generation for Energy Digital Twins" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-1-2026-447-2026)
     - authors: Oscar Roman, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Maarten Bassier, Elisa Mariarosaria Farella, Fabio Remondino
     - title similarity 0.45; abstract similarity 0.09; year +2  (source: OpenAlex)
  3. "A Methodology to Convert Highly Detailed BIM Models into 3D Geospatial Building Models at Different LoDs" — ISPRS International Journal of Geo-Information, 2025 — [journal article](https://doi.org/10.3390/ijgi14120465)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.31; abstract similarity 0.21; year +1  (source: OpenAlex)
  4. "A Methodology to Convert Highly Detailed BIM Models into 3D Geospatial Building Models at Different LoDs" — Preprints.org, 2025 — [preprint](https://doi.org/10.20944/preprints202509.2284.v1)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.31; abstract similarity 0.21; year +1  (source: OpenAlex)
  … and 4 more possible candidates; re-run with --limit/--surname to see them all.
- **Yue Yang (2024)** — Directly Serving 3D Tiles From A Geo-DBMS
  1. "Advancing LED efficiency through 3D-printed light extraction structures: from design to demonstration" — Optics Express, 2025 — [journal article](https://doi.org/10.1364/oe.572911)
     - authors: Yang Yue (student; first author), Kevin Chen, Hongyang Zhu
     - title similarity 0.33; abstract similarity 0.03; year +1  (source: Crossref)
  2. "Revealing multi-scale spatial synergy of mega-city region from a human mobility perspective" — Geo-spatial Information Science, 2024 — [journal article](https://doi.org/10.1080/10095020.2024.2379060)
     - authors: Bichen Fang, Mingxiao Li, Zhengdong Huang, Yang Yue (student), Wei Tu, Renzhong Guo
     - title similarity 0.32; abstract similarity n/a; year +0  (source: Crossref)
  3. "An nD-histogram technique for querying non-uniformly distributed point cloud data" — ISPRS Journal of Photogrammetry and Remote Sensing, Elsevier BV, 224, , 2025 — [journal article](https://doi.org/10.1016/j.isprsjprs.2025.03.014)
     - authors: Haicheng Liu, Zhiwei Li, Peter van Oosterom, Martijn Meijers (supervisor: Meijers), Chuqi Zhang
     - title similarity 0.31; abstract similarity n/a; year +1  (source: GDMC)
- **Noah Alting (2025)** — From point clouds to porous crowns: A scalable approach for CFD-ready urban tree
  1. "Shady Politics: Mapping Inequalities in Urban Shade Distribution" — ?, 2025 — [conference paper](https://doi.org/10.5194/icuc12-793)
     - authors: Lukas Beuster, Titus Venverloo, Clara García-Sánchez, Fábio Duarte, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.37; abstract similarity 0.15; year +0  (source: OpenAlex)
- **Der Derian Auliyaa Bainus (2025)** — Harmonisation of Heterogeneous Point Cloud Using Road Marking as Benchmark
  1. "Evaluating Smartphone LiDAR for Road Infrastructure Mapping: Harmonisation of iPhone LiDAR Data with National Airborne LiDAR Datasets" — The International Archives of the Photogrammetry, Remote Sensing and S, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-l-4-w2-2026-229-2026)
     - authors: Daan H. van der Heide (supervisor: van der Heide), Tessa Eikelboom, Jantien E. Stoter (supervisor: Stoter)
     - title similarity 0.21; abstract similarity 0.38; year +1  (source: Crossref)
  2. "SATree: Structure-aware tree instance segmentation from 3D LiDAR point clouds" — Urban forestry & urban greening, 2026 — [journal article](https://doi.org/10.1016/j.ufug.2026.129414)
     - authors: Shenglan Du, Jantien Stoter (supervisor: Stoter), Julian F.P. Kooij, Liangliang Nan
     - title similarity 0.35; abstract similarity 0.12; year +1  (source: OpenAlex)
  3. "Navigating the shift towards sustainable digital building permits and building logbooks" — Open Research Europe, 2025 — [journal article](https://doi.org/10.12688/openreseurope.18553.2)
     - authors: Rita Lavikka, Judith Fauth, Mayte Toscano, Gonçal Costa, Thomas Beach, Pedro Meda Magalhães, Jantien Stoter (supervisor: Stoter), Stefanie Brigitte Deac Kaiser, Jeroen Werbrouck
     - title similarity 0.39; abstract similarity 0.05; year +0  (source: OpenAlex)
  4. "Navigating the shift towards sustainable digital building permits and building logbooks" — Open Research Europe, 2025 — [journal article](https://doi.org/10.12688/openreseurope.18553.1)
     - authors: Rita Lavikka, Judith Fauth, Mayte Toscano, Gonçal Costa, Thomas Beach, Pedro Meda Magalhães, Jantien Stoter (supervisor: Stoter), Stefanie Brigitte Deac Kaiser, Jeroen Werbrouck
     - title similarity 0.39; abstract similarity 0.04; year +0  (source: OpenAlex)
  … and 5 more possible candidates; re-run with --limit/--surname to see them all.
- **Vidushi Bhatt (2025)** — Geospatial Analytics from IoT ecosystem in Built spaces
  1. "A High-Performance Game Engine-GIS-CFD System for Interactive Urban Wind Decision Support" — Proceedings AGILE: GIScience Series (Tartu, Estonia), pp. 8, 2026 — [conference paper](https://agile-giss.copernicus.org/articles/7/49/2026/)
     - authors: Xuanchen Zhou, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom
     - title similarity 0.35; abstract similarity n/a; year +1  (source: GDMC)
  2. "Integrating radar and multi-spectral data to detect cocoa crops: A deep learning approach" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2025 — [journal article](https://doi.org/10.1016/j.rsase.2025.101652)
     - authors: Adele Therias, Azarakhsh Rafiee (supervisor: Rafiee), Stef Lhermitte, Philip van der Lugt, Roderik Lindenbergh
     - title similarity 0.34; abstract similarity n/a; year +0  (source: GDMC)
- **Lars Boertjes (2025)** — Selective image region focus for efficient 3D building reconstruction using SAM 
  1. "Defining LoDs to support BIM-based 3D building abstractions in GIS" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-55-2026)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter, Siham El Yamani
     - title similarity 0.34; abstract similarity 0.13; year +1  (source: OpenAlex)
  2. "Urban Local Climate Zone Classification Through Deep Learning Using Spatio-temporal Thermal Imagery" — Remote Sensing Applications: Society and Environment, Elsevier BV, pp., 2026 — [journal article](https://doi.org/10.1016/j.rsase.2026.101889)
     - authors: Michaja van Capel, Azarakhsh Rafiee (supervisor: Rafiee), Roderik Lindenbergh
     - title similarity 0.43; abstract similarity n/a; year +1  (source: GDMC)
  3. "An OGC SensorThings GIS Pipeline For Estimating Seismic Engineering Demand Parameters" — ISPRS - Annals of the Photogrammetry, Remote Sensing and Spatial Infor, 2025 — [conference paper](https://doi.org/10.5194/isprs-annals-x-g-2025-787-2025)
     - authors: Justin Schembri, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom
     - title similarity 0.37; abstract similarity n/a; year +0  (source: GDMC)
  4. "A comprehensive review and framework on the applications of digital twins for energy transition at the district level" — Renewable and Sustainable Energy Reviews, Elsevier BV, 234, pp. 116872, 2026 — [journal article](https://doi.org/10.1016/j.rser.2026.116872)
     - authors: Amin Jalilzadeh, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom, Thaleia Konstantinou
     - title similarity 0.30; abstract similarity n/a; year +1  (source: GDMC)
- **Lotte de Niet (2025)** — Reconstructing legal 3D apartment models from 2D division drawings
  1. "A Methodology to Convert Highly Detailed BIM Models into 3D Geospatial Building Models at Different LoDs" — Preprints.org, 2025 — [preprint](https://doi.org/10.20944/preprints202509.2284.v1)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.33; abstract similarity 0.30; year +0  (source: OpenAlex)
  2. "Defining LoDs to support BIM-based 3D building abstractions in GIS" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-55-2026)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori, Jantien Stoter (supervisor: Stoter), Siham El Yamani
     - title similarity 0.32; abstract similarity 0.30; year +1  (source: OpenAlex)
  3. "A Methodology to Convert Highly Detailed BIM Models into 3D Geospatial Building Models at Different LoDs" — ISPRS International Journal of Geo-Information, 2025 — [journal article](https://doi.org/10.3390/ijgi14120465)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.33; abstract similarity 0.28; year +0  (source: OpenAlex)
  4. "Creating 3D city models of Mexican cities based on open data" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-3-2026)
     - authors: Ken Arroyo Ohori, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.41; abstract similarity 0.18; year +1  (source: OpenAlex)
  … and 11 more possible candidates; re-run with --limit/--surname to see them all.
- **Yan Gao (2025)** — Labeling Vario-scale Maps
  1. "FloorPlan2Nav: Semantic-Topological Navigation from Floor Plan Images as Prior Maps" — Proceedings of the International Symposium on Automation and Robotics , 2026 — [conference paper](https://doi.org/10.22260/isarc2026/0225)
     - authors: Yan GAO (student; first author), Qian Zheng, Fuji Hu, Yiwei Weng
     - title similarity 0.32; abstract similarity n/a; year +1  (source: Crossref)
  2. "Non-recurrent rational maps with disconnected Julia set" — Nonlinearity, 2026 — [journal article](https://doi.org/10.1088/1361-6544/ae54f4)
     - authors: Yan Gao (student; first author), Lele Xu, Luxian Yang
     - title similarity 0.26; abstract similarity 0.05; year +1  (source: Crossref)
  3. "Spectral analysis of carbon concentrations in sediments at a plot scale" — ?, 2026 — [posted-content](https://doi.org/10.2139/ssrn.7031278)
     - authors: Pingping Fan, Huacheng Chi, Yang Gao (student), Yan Liu
     - title similarity 0.31; abstract similarity 0.06; year +1  (source: Crossref)
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
- **Xueheng Li (2025)** — 3D Visualization and Dissemination of Property Valuation Information Based on LA
  1. "Fire Smoke Detection Based on YOLOv11 Multi-Scale Fusion and Channel Aggregation" — 2025 4th International Conference on Robotics, Artificial Intelligence, 2025 — [conference paper](https://doi.org/10.1109/raiic65850.2025.11170188)
     - authors: Xueheng Li (student; first author), Weidong Zhao
     - title similarity 0.25; abstract similarity n/a; year +0  (source: Crossref)
  2. "Show off or hide it? Property rights and status competition shape wealth display, evil eye beliefs, and egalitarian norms" — Evolution and Human Behavior, 2026 — [journal article](https://doi.org/10.1016/j.evolhumbehav.2026.106961)
     - authors: Eric Schnell, Robin Schimmelpfennig, Xueheng Li (student), Michael Muthukrishna
     - title similarity 0.27; abstract similarity n/a; year +1  (source: Crossref)
  3. "New Edition of the Land Administration Domain Model Now Nearly Completed" — Proceedings of the FIG Working Week 20225, Brisbane, Australia, pp. 14, 2025 — [conference paper](https://www.gdmc.nl/publications/2025/LADM_ed2Ready.pdf)
     - authors: Abdullah Kara (supervisor: Kara), Peter van Oosterom (supervisor: van Oosterom), Christiaan Lemmen
     - title similarity 0.33; abstract similarity n/a; year +0  (source: GDMC)
  4. "Land administration domain model and 3D land administration" — Survey Review, 2025 — [journal article](https://doi.org/10.1080/00396265.2025.2561263)
     - authors: Peter van Oosterom (supervisor: van Oosterom), Abdullah Kara (supervisor: Kara), Eftychia Kalogianni
     - title similarity 0.31; abstract similarity n/a; year +0  (source: OpenAlex)
  … and 17 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Jessica Monahan (2025)** — Cool by Design. SOLFD: Extending SOLWEIG for Urban Design Decision-Making on Out
  1. "Shady Amsterdam: Identifying the shady places and routes of Amsterdam" — ?, 2025 — [conference paper](https://doi.org/10.5194/icuc12-345)
     - authors: Jessica Monahan (student; first author), Victoria Tsalapati, Haohua Gan, Yan Gao, Citra Andinasari, Hugo Ledoux (supervisor: Ledoux), Lukas Beuster
     - title similarity 0.31; abstract similarity 0.12; year +0  (source: OpenAlex)
  2. "Code supporting: DDL-MVS: Depth Discontinuity Learning for MVS Networks" — 4TU.ResearchData, 2026 — [software](https://doi.org/10.4121/a52925e4-21df-40ae-a030-6ff4d80086e7.v1)
     - authors: Ibrahimli, Nail, H. (Hugo) Ledoux (supervisor: Ledoux), Kooij, Julian, Nan, Liangliang
     - title similarity 0.33; abstract similarity 0.11; year +1  (source: OpenAlex)
  3. "Code supporting: DDL-MVS: Depth Discontinuity Learning for MVS Networks" — 4TU.ResearchData, 2026 — [software](https://doi.org/10.4121/a52925e4-21df-40ae-a030-6ff4d80086e7)
     - authors: Ibrahimli, Nail, H. (Hugo) Ledoux (supervisor: Ledoux), Kooij, Julian, Nan, Liangliang
     - title similarity 0.33; abstract similarity 0.11; year +1  (source: OpenAlex)
  4. "Automated Levee Detection in Digital Elevation Models" — ?, 2026 — [preprint](https://doi.org/10.31223/x57x8x)
     - authors: Maarten Pronk, Matthijs Gawehn, Marieke Eleveld, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.32; abstract similarity 0.07; year +1  (source: OpenAlex)
  … and 2 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Frederick Auer (2026)** — Testing and Enhancing the Scenario ADE in the context of building energy perform
  1. "Scenario-based energy simulation of tree planting strategies to reduce the heating and cooling demand of buildings under 2050 climate conditions" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlix-b4-2026-513-2026)
     - authors: Adhisye Rahmawati, Weixiao Gao, Camilo León Sánchez (supervisor: Sánchez), Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.39; abstract similarity 0.32; year +0  (source: OpenAlex)
  2. "Data supporting DigiTwins4PEDs - Rotterdam case study" — 4TU.ResearchData, 2026 — [dataset](https://doi.org/10.4121/47929d5e-1443-4843-aa0a-12aea4f708a1.v1)
     - authors: Camilo Alexander León Sánchez (supervisor: Sánchez), Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.31; abstract similarity 0.30; year +0  (source: OpenAlex)
  3. "Data supporting DigiTwins4PEDs - Rotterdam case study" — 4TU.ResearchData, 2026 — [dataset](https://doi.org/10.4121/47929d5e-1443-4843-aa0a-12aea4f708a1)
     - authors: Camilo Alexander León Sánchez (supervisor: Sánchez), Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.31; abstract similarity 0.30; year +0  (source: OpenAlex)
  4. "IFC and QGIS integration for the Integrated Water Service Management" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-4-2026-13-2026)
     - authors: Michele Berlato, Giorgio Agugiaro (supervisor: Agugiaro), Ken Arroyo Ohori, Carlo Zanchetta
     - title similarity 0.34; abstract similarity 0.15; year +0  (source: OpenAlex)
- **Michel Beeren (2026)** — Improving 3D alpha wrapping by preserving concave features and reducing mesh com
  1. "Invasive Meningococcal Disease in Adults Aged ≥65 Years Admitted to French Intensive Care Units: A Nationwide Comparison With Younger Adults" — Clinical Infectious Diseases, 2026 — [journal article](https://doi.org/10.1093/cid/ciag133)
     - authors: Damien Contou, Benoit Painvin, Delphine Daubin, Arthur Orieux, Hugo Pirollet, Martin Cour, Benjamine Sarton, Marie Gauvrit, Mathilde Taillantou-Candau, Paola Lepoutre, Guillaume Louis, Fabrice Bruneel, Christelle Teiten, Maud Vincendeau, Marion Giry, François Legay, Rémi Coudroy, Olivier Puig, Pierre Bay, Guillaume Schnell, Geoffrey Ledoux (supervisor: Ledoux), Romain Sonneville, Danielle Reuter, Xavier Valette, Piotr Szychowiak, Nicolas Dufour, Tomas Urbina, Gaëtan Plantefève, Nicolas de Prost
     - title similarity 0.34; abstract similarity 0.05; year +0  (source: OpenAlex)
- **Xinya Bi (2026)** — Recovering Visual Saliency from Intrinsic Properties of 3D Gaussian Splatting
  1. "Ex-Sim(3)-Reg: 2D-3D Correspondence Pruning via Extended Sim(3) Registration" — Lecture notes in computer science, 2026 — [conference paper](https://doi.org/10.1007/978-3-032-37261-1_33)
     - authors: Pei An, Muyao Peng, Junfeng Ding, Jiaqi Yang, Liangliang Nan (supervisor: Nan)
     - title similarity 0.34; abstract similarity n/a; year +0  (source: OpenAlex)
  2. "OCA: ODE-Driven Cross-Attention for Image-to-Point-Cloud Registration" — Lecture notes in computer science, 2026 — [conference paper](https://doi.org/10.1007/978-3-032-37718-0_16)
     - authors: Pei An, Jiaqi Yang, Yulong Wang, Siwen Quan, Liangliang Nan (supervisor: Nan)
     - title similarity 0.33; abstract similarity n/a; year +0  (source: OpenAlex)
- **Sara Brakelé (2026)** — Extracting building typology parameters from 3D city models for earthquake risk 
  1. "Creating 3D city models of Mexican cities based on open data" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-3-2026)
     - authors: Ken Arroyo Ohori, Jantien Stoter (supervisor: Stoter)
     - title similarity 0.47; abstract similarity 0.42; year +0  (source: OpenAlex)
  2. "Enhancing the Interpretability of 3D City Model Validation Through Web Visualization: The Case Study of the CHEK Validation Results Viewer" — ISPRS International Journal of Geo-Information, 2026 — [journal article](https://doi.org/10.3390/ijgi15070282)
     - authors: Alper Tunga Akın, Alejandro Villar, Abdoulaye Diakite, Siham El Yamani, Jantien Stoter (supervisor: Stoter), Francesca Noardo, Robert Atkinson, Piotr Zaborowski
     - title similarity 0.36; abstract similarity 0.26; year +0  (source: OpenAlex)
  3. "Conceptualising value in public sector geospatial information for digital twins" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-4-2026-331-2026)
     - authors: Jack Metcalfe, Claire Ellul, Stefano Cavazzi, Jantien Stoter (supervisor: Stoter), Jeremy Morley
     - title similarity 0.32; abstract similarity 0.11; year +0  (source: OpenAlex)
  4. "Creating and analysing a constrained TIN in a geo-DBMS: integration of point heights and parcel boundaries" — ?, 2026 — [book-chapter](https://doi.org/10.1201/9781003762638-7)
     - authors: Jantien Stoter (supervisor: Stoter), Ben Gorte
     - title similarity 0.31; abstract similarity 0.10; year +0  (source: OpenAlex)
  … and 1 more possible candidates; re-run with --limit/--surname to see them all.
- **Alexandre Bry (2026)** — From points to prints -- Generating building roofprints and footprints from airb
  1. "Roadmap on singular optics and its applications" — Applied Physics B, 2026 — [journal article](https://doi.org/10.1007/s00340-026-08645-w)
     - authors: Ganesh M. Balasubramaniam, Srinivasa Rao Allam, Vijayakumar Anand, Md. Haider Ansari, Francis Gracy Arockiaraj, Shlomi Arnon, Purnesh Singh Badavath, Mansi Baliyan, Petr Bouchal, Sakshi Choudhary, Ahmed H. Dorrah, Yuxiang Duan, Kelsey Everts, Andrew Forbes, Matthew R. Foreman, Darius Gailevičius, Akanksha Gautam, Greg Gbur, Shivasubramanian Gopinath, Narmada Joshi, Saulius Juodkazis, Olga Korotkova, Kaupo Kukli, Judy Kupferman, Praveen Kumar, Gokul Manavalan, Ayush Mehra, Naveen K. Nishchal, Takashige Omatsu, Cade Peters (supervisor: Peters), Andra Naresh Kumar Reddy, Valeria Rodríguez-Fajardo, Carmelo Rosales-Guzmán, Joseph Rosen, Sarita, Allarakha Shikder, Rakesh Kumar Singh, Xinzhou Su, Aile Tamm, Ganesh Velagala, Petr Viewegh, Eulàlia Puig Vilardell, Alan E. Willner, Agnes Pristy Ignatius Xavier, Amit Yadav, Huibin Zhou
     - title similarity 0.42; abstract similarity 0.05; year +0  (source: OpenAlex)
  2. "From field photos to microscope images: a low-cost toolbox for glacier surface darkening and biological impurity analysis" — ?, 2026 — [conference paper](https://doi.org/10.5194/egusphere-egu26-16858)
     - authors: Alexandre Anesio, Shunan Feng, Beatriz Gill Olivas, Emily Louise Mary Broadwell, Ravi Sven Peters (supervisor: Peters), Liane G. Benning, Martyn Tranter
     - title similarity 0.32; abstract similarity 0.06; year +0  (source: OpenAlex)
- **Carlo Cordes (2026)** — Spatio-temporal Transformers for Wildfire Risk Prediction
  1. "Cloud-based application for indoor daylight performance analysis through BIM-GIS Integration" — Building and Environment, Elsevier BV, 293, pp. 114376, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2026.114376)
     - authors: Yangyu Liu, Eleonora Brembilla, Azarakhsh Rafiee (supervisor: Rafiee)
     - title similarity 0.39; abstract similarity n/a; year +0  (source: GDMC)
  2. "A High-Performance Game Engine-GIS-CFD System for Interactive Urban Wind Decision Support" — Proceedings AGILE: GIScience Series (Tartu, Estonia), pp. 8, 2026 — [conference paper](https://agile-giss.copernicus.org/articles/7/49/2026/)
     - authors: Xuanchen Zhou, Azarakhsh Rafiee (supervisor: Rafiee), Peter van Oosterom
     - title similarity 0.31; abstract similarity n/a; year +0  (source: GDMC)
- **Ming-Chieh Hu (2026)** — Adaptive Plane Splatting for 3D Building Reconstruction
  1. "Enhanced Photoelectric Response in MoS 2 /Graphene Heterostructures via Surface Plasmon Resonance" — ACS Applied Nano Materials, 2026 — [journal article](https://doi.org/10.1021/acsanm.5c04964)
     - authors: Xingyu Zhou, Zhengjin Weng, Jian Li, Zhihao Wang, Qianqian Wu, Liangliang Lin, Jialing Jian, Xiaofeng Gu, Peng Xiao, Haiyan Nan (supervisor: Nan)
     - title similarity 0.33; abstract similarity 0.05; year +0  (source: OpenAlex)
  2. "Ex-Sim(3)-Reg: 2D-3D Correspondence Pruning via Extended Sim(3) Registration" — Lecture notes in computer science, 2026 — [conference paper](https://doi.org/10.1007/978-3-032-37261-1_33)
     - authors: Pei An, Muyao Peng, Junfeng Ding, Jiaqi Yang, Liangliang Nan (supervisor: Nan)
     - title similarity 0.31; abstract similarity n/a; year +0  (source: OpenAlex)
  3. "RrLHY regulates arginine biosynthesis by activating RrNAGS1 in Rosa roxburghii fruit" — Plant Cell Reports, 2026 — [journal article](https://doi.org/10.1007/s00299-025-03701-9)
     - authors: Xufeng Yang, Nanyu Li, Richard Ludlow, Qianmin Huang, Zhaoxin Wu, Hong Nan (supervisor: Nan), Huaming An, Min Lu
     - title similarity 0.31; abstract similarity n/a; year +0  (source: OpenAlex)
- **Giorgos Iliopoulos (2026)** — (Semi-)automatic modeling of indoor building 3D models for daylight simulation w
  1. "Automatic 3D Building Model Generation for Energy Digital Twins" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-1-2026-447-2026)
     - authors: Oscar Roman, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Maarten Bassier, Elisa Mariarosaria Farella, Fabio Remondino
     - title similarity 0.48; abstract similarity 0.09; year +0  (source: OpenAlex)
  2. "Semi-automated indoor geometry reconstruction for daylight simulation" — Building and Environment, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2025.114045)
     - authors: Nima Forouzandeh, Jin Huang, Liangliang Nan, Eleonora Brembilla (supervisor: Brembilla), Jantien Stoter
     - title similarity 0.54; abstract similarity n/a; year +0  (source: Crossref)
  3. "Defining LoDs to support BIM-based 3D building abstractions in GIS" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-55-2026)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter, Siham El Yamani
     - title similarity 0.37; abstract similarity 0.14; year +0  (source: OpenAlex)
  4. "Cloud-based application for indoor daylight performance analysis through BIM-GIS Integration" — Building and Environment, Elsevier BV, 293, pp. 114376, 2026 — [journal article](https://doi.org/10.1016/j.buildenv.2026.114376)
     - authors: Yangyu Liu, Eleonora Brembilla (supervisor: Brembilla), Azarakhsh Rafiee
     - title similarity 0.35; abstract similarity n/a; year +0  (source: GDMC)
- **Luc Jonker (2026)** — Automated generation of tree-aware urban shade maps using deep learning
  1. "Automated Levee Detection in Digital Elevation Models" — ?, 2026 — [preprint](https://doi.org/10.31223/x57x8x)
     - authors: Maarten Pronk, Matthijs Gawehn, Marieke Eleveld, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.39; abstract similarity 0.10; year +0  (source: OpenAlex)
  2. "Code supporting: DDL-MVS: Depth Discontinuity Learning for MVS Networks" — 4TU.ResearchData, 2026 — [software](https://doi.org/10.4121/a52925e4-21df-40ae-a030-6ff4d80086e7.v1)
     - authors: Ibrahimli, Nail, H. (Hugo) Ledoux (supervisor: Ledoux), Kooij, Julian, Nan, Liangliang
     - title similarity 0.31; abstract similarity 0.13; year +0  (source: OpenAlex)
  3. "Code supporting: DDL-MVS: Depth Discontinuity Learning for MVS Networks" — 4TU.ResearchData, 2026 — [software](https://doi.org/10.4121/a52925e4-21df-40ae-a030-6ff4d80086e7)
     - authors: Ibrahimli, Nail, H. (Hugo) Ledoux (supervisor: Ledoux), Kooij, Julian, Nan, Liangliang
     - title similarity 0.31; abstract similarity 0.13; year +0  (source: OpenAlex)
  4. "Complement augments antibody neutralization of SARS-CoV-2 variants" — Science Translational Medicine, 2026 — [journal article](https://doi.org/10.1126/scitranslmed.aec6027)
     - authors: Martin Jungbauer-Groznica, Pierre Rosenbaum, Isabelle Staropoli, Florence Guivel-Benhassine, Pierre-Henri Commere, Tom Perisse, Lily Bruyère, Aura Fantin Rengifo, Alejandro De Cruz, Andrea Cottignies-Calamarte, Sabina Andreu, Laurent Hocqueloux, Thierry Prazuck, Cyril Planchais, Michael White, Sophie Novault, Sophie Trouillet-Assant, SEVARVIR investigators, Slim Fourati, Nicolas de Prost, Martin Killian, Stéphane Paul, Olivier Schwartz, Hugo Mouquet, Timothée Bruel, Pierre Bay, Keyvan Razazi, Armand Mekontso Dessap, Lucile Picard, Nicolas Mongardon, Alexandre Soulier, Melissa N'debi, Sarah Seng, Mohamed Ader, Pierre Cappy, Christophe Rodriguez, Jean-Michel Pawlotsky, Etienne Audureau, Pierre-Andre Natella, Frederic Pene, Anne-Sophie L'honneur, Adrien Joseph, Elie Azoulay, Megan Fraisse, Maud Salmona, Marie-Laure Chaix, Charles-Edouard Luyt, David Levy, Julien Mayaux, Stephane Marot, Juliette Bernier, Vincent Bonny, Tomas Urbina, Hafid Ait-Oufella, Eric Maury, Laurence Morand-Joubert, Djeneba Bocar Fofana, Jean-Francois Timsit, Diane Descamps, Quentin Le Hingrat, Guillaume Voiriot, Nina De Montmollin, Mathieu Turpin, Stéphane Gaudry, Ségolène Brichler, Fabrice Uhel, Damien Roux, Luce Landraud, Anne-Claire Maherault, Tài Olivier Pham, Amal Chaghouri, Anne-Marie Roque-Alfonso, Nicholas Heming, Djillali Annane, Marie-Alice Bovy, Sylvie Meireles, Antoine Vieillard-Baron, Elyanne Gault, Sébastien Jochmans, Aurélia Pitsch, Guillaume Chevrel, Céline Clergue, Kubab Sabah, Damien Contou, Amandine Henry, Malo Emery, Claudio Garcia-Sanchez, Ferhat Meziani, Louis-Marie Jandeaux, Samira Fafi-Kremer, Elodie Laugel, Sébastien Preau, Raphaël Favory, Claire Bourel, Côme Bureau, Estelle Danche, Alexandre Gaudet, Geoffrey Ledoux (supervisor: Ledoux), Aurélie Guigon, Antoine Kimmoun
     - title similarity 0.34; abstract similarity 0.02; year +0  (source: OpenAlex)
  … and 1 more possible candidates; re-run with --limit/--surname to see them all.
- **Julia Pille (2026)** — Seabed Fingerprinting for Maritime Navigation in GNSS-Denied Environments
  1. "Permanent terrestrial laser scanning for environmental monitoring" — ?, 2026 — [conference paper](https://doi.org/10.5194/egusphere-egu26-17484)
     - authors: Roderik Lindenbergh (supervisor: Lindenbergh), Sander Vos, Daan Hulskemper
     - title similarity 0.35; abstract similarity 0.11; year +0  (source: OpenAlex)
  2. "Coastal process understanding through automated identification of recurring surface dynamics in permanent laser scanning data of a sandy beach" — Earth Surface Dynamics, 2026 — [journal article](https://doi.org/10.5194/esurf-14-329-2026)
     - authors: Daan Cornelis Hulskemper, José A. Á. Antolínez, Roderik Lindenbergh (supervisor: Lindenbergh), Katharina Anders
     - title similarity 0.33; abstract similarity 0.13; year +0  (source: OpenAlex)
  3. "Salt march Leaf Area Index determination with AI driven aerial lidar and multispectral data fusion" — ?, 2026 — [conference paper](https://doi.org/10.5194/egusphere-egu26-12569)
     - authors: Sander Vos, Tegan Blount, Roderik Lindenbergh (supervisor: Lindenbergh), José Antolinez, Marco Marani
     - title similarity 0.34; abstract similarity 0.06; year +0  (source: OpenAlex)
  4. "The Effect of Beach Buildings on Decadal Dune Volume Development" — Coastal research library, 2026 — [conference paper](https://doi.org/10.1007/978-3-032-15473-6_26)
     - authors: Sander Vos, Daan Hulskemper, Christa IJzendoorn, Alain de Wulf, Roderik Lindenbergh (supervisor: Lindenbergh), José A. A. Antolinez
     - title similarity 0.35; abstract similarity 0.04; year +0  (source: OpenAlex)
  … and 7 more possible candidates; re-run with --limit/--surname to see them all.
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
- **Heiko Rotteveel (2026)** — Automatic water detection using ICESat-2 measurements
  1. "Automated Levee Detection in Digital Elevation Models" — ?, 2026 — [preprint](https://doi.org/10.31223/x57x8x)
     - authors: Maarten Pronk (supervisor: Pronk), Matthijs Gawehn, Marieke Eleveld, Hugo Ledoux (supervisor: Ledoux)
     - title similarity 0.57; abstract similarity 0.19; year +0  (source: OpenAlex)
- **Daan Schlosser (2026)** — Investigation on the data model requirements for Building Renovation Passports
  1. "Scenario-based energy simulation of tree planting strategies to reduce the heating and cooling demand of buildings under 2050 climate conditions" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlix-b4-2026-513-2026)
     - authors: Adhisye Rahmawati, Weixiao Gao, Camilo León Sánchez, Giorgio Agugiaro (supervisor: Agugiaro)
     - title similarity 0.41; abstract similarity 0.25; year +0  (source: OpenAlex)
  2. "IFC and QGIS integration for the Integrated Water Service Management" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-4-2026-13-2026)
     - authors: Michele Berlato, Giorgio Agugiaro (supervisor: Agugiaro), Ken Arroyo Ohori, Carlo Zanchetta
     - title similarity 0.34; abstract similarity 0.29; year +0  (source: OpenAlex)
  3. "Automatic 3D Building Model Generation for Energy Digital Twins" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-1-2026-447-2026)
     - authors: Oscar Roman, Giorgio Agugiaro (supervisor: Agugiaro), Ken Arroyo Ohori, Maarten Bassier, Elisa Mariarosaria Farella, Fabio Remondino
     - title similarity 0.39; abstract similarity 0.18; year +0  (source: OpenAlex)
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
     - title similarity 0.38; abstract similarity 0.21; year +0  (source: GDMC)
  2. "Salt march Leaf Area Index determination with AI driven aerial lidar and multispectral data fusion" — ?, 2026 — [conference paper](https://doi.org/10.5194/egusphere-egu26-12569)
     - authors: Sander Vos, Tegan Blount, Roderik Lindenbergh (supervisor: Lindenbergh), José Antolinez, Marco Marani
     - title similarity 0.31; abstract similarity 0.15; year +0  (source: OpenAlex)
  3. "From Static to Dynamic: Modernizing the Sharing of HistoricalPhotogrammetry Datasets" — ?, 2026 — [conference paper](https://doi.org/10.5194/egusphere-egu26-19445)
     - authors: Felix Dahle, Roderik Lindenbergh (supervisor: Lindenbergh), Bert Wouters
     - title similarity 0.36; abstract similarity 0.07; year +0  (source: OpenAlex)
  4. "Spatial Aerodynamic Roughness of Forested Landscapes from Airborne LiDAR" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-3-2026-695-2026)
     - authors: Mahmoud H. Ahmed, Roderik Lindenbergh (supervisor: Lindenbergh), Massimo Menenti, Joris Timmermans
     - title similarity 0.32; abstract similarity 0.11; year +0  (source: OpenAlex)
  … and 5 more possible candidates; re-run with --limit/--surname to see them all.
- **Vincent Vanderheeren (2026)** — Pillar of Morphology – Enhancing point-based mathematical morphology for applica
  1. "Defining LoDs to support BIM-based 3D building abstractions in GIS" — The international archives of the photogrammetry, remote sensing and, 2026 — [journal article](https://doi.org/10.5194/isprs-archives-xlviii-3-w4-2025-55-2026)
     - authors: Jasper van der Vaart, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter, Siham El Yamani
     - title similarity 0.36; abstract similarity 0.09; year +0  (source: OpenAlex)
  2. "IFC and QGIS integration for the Integrated Water Service Management" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-4-2026-13-2026)
     - authors: Michele Berlato, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Carlo Zanchetta
     - title similarity 0.32; abstract similarity 0.08; year +0  (source: OpenAlex)
  3. "Automatic 3D Building Model Generation for Energy Digital Twins" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-1-2026-447-2026)
     - authors: Oscar Roman, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Maarten Bassier, Elisa Mariarosaria Farella, Fabio Remondino
     - title similarity 0.33; abstract similarity 0.06; year +0  (source: OpenAlex)
- **Sue Wang (2026)** — From IFC BIM to Semantically Enriched 2.5D Indoor Navigation Graphs for Congesti
  1. "Automatic 3D Building Model Generation for Energy Digital Twins" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-1-2026-447-2026)
     - authors: Oscar Roman, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Maarten Bassier, Elisa Mariarosaria Farella, Fabio Remondino
     - title similarity 0.35; abstract similarity 0.19; year +0  (source: OpenAlex)
  2. "IFC and QGIS integration for the Integrated Water Service Management" — ISPRS annals of the photogrammetry, remote sensing and spatial informa, 2026 — [journal article](https://doi.org/10.5194/isprs-annals-xi-4-2026-13-2026)
     - authors: Michele Berlato, Giorgio Agugiaro, Ken Arroyo Ohori (supervisor: Ohori), Carlo Zanchetta
     - title similarity 0.31; abstract similarity 0.21; year +0  (source: OpenAlex)
  3. "Visualization of Urban Digital Twins on the web with attribute-driven adaptive tiling" — Environmental Modelling & Software, 2026 — [journal article](https://doi.org/10.1016/j.envsoft.2026.106863)
     - authors: Ziya Usta, Alper Tunga Akın, Ken Arroyo Ohori (supervisor: Ohori), Jantien Stoter
     - title similarity 0.31; abstract similarity 0.05; year +0  (source: OpenAlex)
  4. "Hierarchical Polygon-to-Point Collapsing for Multi-Scale Representation Based on the Straight Skeleton" — ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Informa, 2026 — [conference paper](https://doi.org/10.5194/isprs-annals-xi-4-2026-21-2026)
     - authors: Amin Gholami, Pawel Boguslawski, Martijn Meijers (supervisor: Meijers)
     - title similarity 0.33; abstract similarity n/a; year +0  (source: GDMC)

## No candidates (29)

de Koning (2010), Boersma (2019), Moscholaki (2020), Staring (2020), Alhoz (2021), de Jongh (2021), Hobeika (2021), van Heerden (2021), Fratzeskou (2022), Fu (2022), Papakostas (2022), Prihanggo (2022), Dong (2023), Meschin (2023), Panagiotidou (2023), Dinklo (2024), Hengelmolen (2024), Monté (2024), Zhang (2024)

No candidates found for 10 theses from 2025–2026 either, but those rarely have papers yet: Chontos (2025), Manden (2025), Tew (2025), Aalders (2026), den Hartog (2026), Félix Aires (2026), Hutama (2026), Joh (2026), Singh (2026), Ye (2026)

## Calibration

Of the 25 entries that already link a paper and can be checked automatically, the search surfaced 23 as a candidate (the rest had a title too far from the thesis's, or were not in the sources for this run); 8 more have a paper link this script cannot verify automatically:

- **missed** — Rao (2024): doi 10.5281/zenodo.21605442 (not among the candidates)
- surfaced — Xu (2024): record title (best similarity 1.00) — title 0.67, abstract n/a, student co-author: yes (first author: yes), supervisors among authors: 0/0
- surfaced — Roy (2022): doi 10.1080/13658816.2022.2160454 — title 0.65, abstract 0.63, student co-author: yes (first author: yes), supervisors among authors: 1/1
- surfaced — Tufan (2022): doi 10.5194/isprs-archives-xlviii-4-w4-2022-169-2022 — title 1.00, abstract 0.86, student co-author: no (first author: no), supervisors among authors: 0/1
- surfaced — Chen (2021): doi 10.1016/j.isprsjprs.2022.09.017 — title 0.72, abstract 0.71, student co-author: yes (first author: yes), supervisors among authors: 2/2
- **missed** — Doan (2021): doi 10.5194/isprs-annals-v-4-2021-169-2021 (not among the candidates)
- surfaced — Giannelli (2021): doi 10.5194/isprs-annals-v-4-2022-275-2022 — title 0.47, abstract 0.28, student co-author: yes (first author: yes), supervisors among authors: 1/1
- surfaced — Lumban Gaol (2021): doi 10.1080/01490419.2022.2091696 — title 0.36, abstract 0.72, student co-author: no (first author: no), supervisors among authors: 1/1
- surfaced — Morlighem (2021): doi 10.1007/s44212-022-00011-3 — title 0.55, abstract 0.60, student co-author: yes (first author: yes), supervisors among authors: 1/1
- not automatically checkable — Dahle (2020): non-DOI, non-record link
- not automatically checkable — Zhang (2020): non-DOI, non-record link
- surfaced — Bouzas (2019): doi 10.1016/j.isprsjprs.2020.07.010 — title 0.80, abstract 0.61, student co-author: yes (first author: yes), supervisors among authors: 1/1
- surfaced — Du (2019): doi 10.3390/rs11182074 — title 0.71, abstract 0.81, student co-author: yes (first author: yes), supervisors among authors: 2/2
- not automatically checkable — Flikweert (2019): non-DOI, non-record link
- not automatically checkable — Salheb (2019): non-DOI, non-record link
- surfaced — Wang (2018): doi 10.1080/19401493.2020.1729862 — title 0.47, abstract 0.63, student co-author: yes (first author: yes), supervisors among authors: 4/4
- surfaced — Broersen (2016): doi 10.1016/j.cageo.2017.06.003 — title 0.73, abstract n/a, student co-author: yes (first author: yes), supervisors among authors: 2/2
- surfaced — Rook (2016): doi 10.5194/isprs-annals-iv-2-w1-23-2016 — title 0.68, abstract 0.49, student co-author: yes (first author: yes), supervisors among authors: 2/2
- surfaced — van der Ham (2015): doi 10.5194/isprs-annals-iv-4-w1-105-2016 — title 0.98, abstract 0.64, student co-author: yes (first author: yes), supervisors among authors: 2/2
- surfaced — Krūminaitė (2014): doi 10.1145/2676528.2676529 — title 1.00, abstract 0.46, student co-author: yes (first author: yes), supervisors among authors: 1/1
- surfaced — van Winden (2014): doi 10.1111/tgis.12186 — title 0.50, abstract 0.62, student co-author: yes (first author: yes), supervisors among authors: 2/2
- surfaced — Boeters (2013): doi 10.1080/13658816.2015.1072201 — title 0.58, abstract 0.54, student co-author: yes (first author: yes), supervisors among authors: 2/3
- surfaced — Donkers (2013): doi 10.1111/tgis.12162 — title 0.50, abstract 0.58, student co-author: yes (first author: yes), supervisors among authors: 3/3
- surfaced — Biljecki (2010): record title (best similarity 1.00) — title 1.00, abstract n/a, student co-author: yes (first author: yes), supervisors among authors: 2/2
- not automatically checkable — Bloemsma (2010): non-DOI, non-record link
- surfaced — Kalpoe (2010): doi 10.1117/12.889440 — title 1.00, abstract 0.55, student co-author: yes (first author: yes), supervisors among authors: 2/3
- not automatically checkable — Possel (2010): linked repository record unreadable
- not automatically checkable — Widiastuti (2009): non-DOI, non-record link
- not automatically checkable — Hofman (2008): non-DOI, non-record link
- surfaced — de Boer (2007): doi 10.1007/978-3-540-68566-1_20 — title 0.58, abstract n/a, student co-author: yes (first author: yes), supervisors among authors: 2/3
- surfaced — Pluymaekers (2007): doi 10.1109/oceanse.2007.4302305 — title 0.47, abstract 0.21, student co-author: yes (first author: yes), supervisors among authors: 1/1
- surfaced — Slobbe (2007): doi 10.1111/j.1365-246x.2008.03978.x — title 0.40, abstract n/a, student co-author: yes (first author: yes), supervisors among authors: 2/2
- surfaced — Kodde (2006): doi 10.11588/heidok.00036925 — title 0.67, abstract n/a, student co-author: yes (first author: yes), supervisors among authors: 1/4
