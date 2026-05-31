# Glass Dataset Schema

Dataset: **Glass Samples Chemical Composition**

Description: 214 forensic glass samples with chemical composition labeled by glass type.

## Columns

| Column | Type | Role | Unit | Description |
|---|---:|---|---|---|
| sample_id | integer | identifier | integer ID | Unique identifier for each glass sample. |
| refractive_index | number | feature | RI | Refractive index (RI) of the glass sample. |
| sodium | number | feature | weight percent | Sodium oxide content as weight percent. |
| magnesium | number | feature | weight percent | Magnesium oxide content as weight percent. |
| aluminum | number | feature | weight percent | Aluminum oxide content as weight percent. |
| silicon | number | feature | weight percent | Silicon dioxide content as weight percent. |
| potassium | number | feature | weight percent | Potassium oxide content as weight percent. |
| calcium | number | feature | weight percent | Calcium oxide content as weight percent. |
| barium | number | feature | weight percent | Barium oxide content as weight percent. |
| iron | number | feature | weight percent | Iron oxide content as weight percent. |
| glass_type | integer | target | class code | Target class label indicating the forensic glass type. |

## Glass Type Mapping

- 1: building_windows_float_processed
- 2: building_windows_non_float_processed
- 3: vehicle_windows_float_processed
- 4: vehicle_windows_non_float_processed
- 5: containers
- 6: tableware
- 7: headlamps

## Class Counts

- Type 1: 70
- Type 2: 76
- Type 3: 17
- Type 5: 13
- Type 6: 9
- Type 7: 29
