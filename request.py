import requests

url = "http://127.0.0.1:5000/api/analyse"
response = requests.post(url, json={"wbc_count": 2.4, "rbc_count": 3.7, "hb_level": 3.7, "hematocrit": 3.7, "mean_cell_volume": 3.7, "mean_corp_hb": 3.7, "mean_cell_hb_conc": 3.7, "platelet_count": 3.7, "platelet_distr_width": 3.7, "mean_platelet_vl": 3.7, "neutrophils_percent": 3.7, "lymphocytes_percent": 3.7, "mixed_cells_percent": 3.7, "neutrophils_count": 3.7, "lymphocytes_count": 3.7, "mixed_cells_count": 3.7, "RBC_dist_width_Percent": 3.7})
print(response.json())