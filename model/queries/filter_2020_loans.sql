select *
from dsci_miac_2026.l1_federal_data
where 1=1
	and productionyear = 2020
	and origloanamt between 100000 and 110000;