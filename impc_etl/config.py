"""
Config file
"""


class SparkConfig:
    SPARK_JAR_PACKAGES = "com.databricks:spark-xml_2.11:0.6.0"


class OntologySchema:
    LABEL_ANNOTATION = ""
    ALT_ID = ""
    X_REF = ""
    REPLACEMENT = ""
    CONSIDER = ""
    TERM_REPLACED_BY = ""
    IS_OBSOLETE = ""
    SYNONYM_ANNOTATIONS = [
        "http://www.geneontology.org/formats/oboInOwl#hasExactSynonym",
        "http://www.geneontology.org/formats/oboInOwl#hasNarrowSynonym",
        "http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym",
        "http://www.geneontology.org/formats/oboInOwl#hasBroadSynonym",
    ]
    DEFINITION_ANNOTATION = "http://purl.obolibrary.org/obo/IAO_0000115"
    PART_OF = ""


class Constants:
    SKIPPED_PROCEDURES = {
        "SLM_SLM",
        "SLM_AGS",
        "TRC_TRC",
        "DSS_DSS",
        "MGP_ANA",
        "MGP_BCI",
        "MGP_BMI",
        "MGP_EEI",
        "MGP_MLN",
        "MGP_PBI",
        "MGP_IMM",
    }
    VALID_PROJECT_IDS = {
        "BaSH",
        "DTCC",
        "EUMODIC",
        "EUCOMM-EUMODIC",
        "Helmholtz GMC",
        "JAX",
        "NING",
        "MARC",
        "MGP",
        "MGP Legacy",
        "MRC",
        "NorCOMM2",
        "Phenomin",
        "RIKEN BRC",
        "KMPC",
        "Kmpc",
        "3i",
        "IMPC",
    }
    EUROPHENOME_VALID_COLONIES = {
        "EPD0013_1_G11_10613",
        "EPD0019_1_A05_10494",
        "EPD0023_1_F07_10481",
        "EPD0033_3_F04_10955",
        "EPD0037_1_E07_10471",
        "EPD0037_3_G01_10533",
        "EPD0039_1_B01_10470",
        "EPD0057_2_C02_10474",
        "EPD0065_2_E04_10968",
        "EPD0089_4_F11_10538",
        "EPD0100_4_A06_10472",
        "EPD0135_1_A05_10967",
        "EPD0156_1_B01_10970",
        "EPD0242_4_B03_10958",
        "EPD0011_3_B08_10331",
        "EPD0017_3_E02_71",
        "EPD0019_1_A05_10574",
        "EPD0023_1_F07_10553",
        "EPD0033_3_F04_10514",
        "EPD0037_1_B03_10395",
        "EPD0037_1_E07_10554",
        "EPD0038_2_B10_10557",
        "EPD0057_1_H01_10556",
        "EPD0057_2_C02_10549",
        "EPD0065_2_E04_10515",
        "EPD0065_5_A04_10523",
        "EPD0089_4_F11_320",
        "EPD0100_4_A06_10380",
        "EPD0135_1_A05_10581",
        "EPD0145_4_B09_10343",
        "EPD0156_1_B01_10099",
        "EPD0242_4_B03_10521",
        "EPD0023_1_F07_10594",
        "EPD0037_1_B03_10632",
        "EPD0037_1_E07_10595",
        "EPD0038_2_B10_10026",
        "EPD0046_2_F02_216",
        "EPD0057_1_H01_134",
        "EPD0057_2_C02_10630",
        "EPD0065_2_E04_10028",
        "EPD0065_5_A04_141",
        "EPD0089_4_F11_10578",
        "EPD0100_4_A06_10519",
        "EPD0135_1_A05_10631",
        "EPD0156_1_B01_10517",
        "EPD0242_4_B03_10579",
        "EPD0011_3_B08_28",
        "EPD0013_1_G11_10560",
        "EPD0017_3_E02_10220",
        "EPD0019_1_A05_73",
        "EPD0033_3_F04_10232",
        "EPD0037_1_B03_10234",
        "EPD0037_3_G01_10649",
        "EPD0039_1_B01_157",
        "EPD0046_2_F02_10658",
        "EPD0135_1_A05_10562",
        "EPD0145_4_B09_10826",
        "EPD0242_4_B03_10233",
        "Dll1_C3H_113",
        "Dll1_C3H_10333",
        "EPD0059_2_C08_10660",
    }

    WEIGHT_PARAMETERS = [
        "IMPC_GRS_003_001",
        "IMPC_CAL_001_001",
        "IMPC_DXA_001_001",
        "IMPC_HWT_007_001",
        "IMPC_PAT_049_001",
        "IMPC_BWT_001_001",
        "IMPC_ABR_001_001",
        "IMPC_CHL_001_001",
        "TCP_CHL_001_001",
        "HMGU_ROT_004_001",
        "ESLIM_001_001_001",
        "ESLIM_002_001_001",
        "ESLIM_003_001_001",
        "ESLIM_004_001_001",
        "ESLIM_005_001_001",
        "ESLIM_020_001_001",
        "ESLIM_022_001_001",
        "ESLIM_009_001_003",
        "ESLIM_010_001_003",
        "ESLIM_011_001_011",
        "ESLIM_012_001_005",
        "ESLIM_013_001_018",
        "ESLIM_022_001_001",
        "GMC_916_001_022",
        "GMC_908_001_001",
        "GMC_900_001_001",
        "GMC_926_001_003",
        "GMC_922_001_002",
        "GMC_923_001_001",
        "GMC_921_001_002",
        "GMC_902_001_003",
        "GMC_912_001_018",
        "GMC_917_001_001",
        "GMC_920_001_001",
        "GMC_909_001_002",
        "GMC_914_001_001",
    ]

    CENTRE_ID_MAP = {
        "bcm": "BCM",
        "gmc": "HMGU",
        "h": "MRC Harwell",
        "harwell": "MRC Harwell",
        "hmgu": "HMGU",
        "ics": "ICS",
        "j": "JAX",
        "jax": "JAX",
        "ncom": "CMHD",
        "ning": "MARC",
        "marc": "MARC",
        "rbrc": "RBRC",
        "tcp": "TCP",
        "ucd": "UC Davis",
        "wtsi": "WTSI",
        "wsi": "WTSI",
        "kmpc": "KMPC",
        "biat": "BIAT",
        "ph": "PH",
        "cdta": "CDTA",
        "crl": "Crl",
        "riken brc": "RBRC",
        "ccp-img": "CCP-IMG",
        "monterotondo": "Monterotondo",
        "narlabs": "NARLabs",
    }

    PROJECT_ID_MAP = {
        "bash": "BaSH",
        "dtcc": "DTCC",
        "eumodic": "EUMODIC",
        "eucomm-eumodic": "EUMODIC",
        "eucomm-eucomm-eumodic": "EUMODIC",
        "helmholtz gmc": "Helmholtz GMC",
        "jax": "JAX",
        "ning": "MARC",
        "marc": "MARC",
        "mgp": "MGP",
        "mgp legacy": "MGP Legacy",
        "mrc": "MRC",
        "norcomm2": "NorCOMM2",
        "phenomin": "Phenomin",
        "riken brc": "RBRC",
        "kmpc": "KMPC",
        "3i": "3i",
        "impc": "IMPC",
        "ccp-img": "CCP-IMG",
        "norcomm": "NorCOMM",
        "ucd-komp": "UC Davis",
        "eucommtoolscre": "EUCOMMToolsCre",
        "monterotondo": "Monterotondo",
        "infrafrontier-i3": "Infrafrontier-I3",
        "komp": "KOMP",
        "narlabs": "NARLabs",
        "tobeloadedfromimits": "tobeloadedfromimits",
    }

    EXPERIMENTER_IDS = {
        "LHl": "131",
        "OH": "132",
        "jiangman, wangchenhao": "jiangman,wangchenhao",
        "jiangman wangchenhao": "jiangman,wangchenhao",
        "jianman  wangchenhao": "jiangman,wangchenhao",
        "JMC_301_304": "JMC301,JMC304",
        "JMC601,JMC602JMC603": "JMC601,JMC602,JMC603",
        "JCM601,JCM602,JCM603": "JMC601,JMC602,JMC603",
        "JCM601,JCM603": "JMC601,JMC603",
        "JMC601,JCM603": "JMC601,JMC603",
        "JCM602,JCM603": "JMC602,JMC603",
        "JMC602,JCM603": "JMC602,JMC603",
        "JCM603": "JMC603",
        "qixin;jiangman": "qixin,jiangman",
        "Chenhao Wang": "wangchenhao",
        "wangchenhao  jiangman": "wangchenhao,jiangman",
    }

    EFO_EMBRYONIC_STAGES = {
        "8.25": "EFO:0002561",
        "9": "EFO:0002561",
        "9.5": "EFO:0007641",
        "10.5": "EFO:0007643",
        "11.5": "EFO:0002562",
        "12": "EFO:0007640",
        "12.5": "EFO:0002563",
        "13": "EFO:0007642",
        "13.5": "EFO:0002564",
        "14.5": "EFO:0002565",
        "15.5": "EFO:0002566",
        "16.5": "EFO:0002567",
        "17.5": "EFO:0002568",
        "18": "EFO:0002569",
        "18.5": "EFO:0002570",
    }
