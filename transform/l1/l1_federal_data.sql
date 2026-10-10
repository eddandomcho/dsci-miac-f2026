CREATE TABLE dsci_miac_2026.l1_federal_data
WITH (
  format = 'PARQUET',
  external_location = 's3://miac-2026/l1/l1_federal_data/'
) AS
SELECT *
FROM dsci_miac_2026.l0_federal_data