CREATE TABLE dsci_miac_2026.l1_conventional_data
WITH (
  format = 'PARQUET',
  external_location = 's3://miac-2026/l1/l1_conventional_data/'
) AS
SELECT *
FROM dsci_miac_2026.l0_conventional_data