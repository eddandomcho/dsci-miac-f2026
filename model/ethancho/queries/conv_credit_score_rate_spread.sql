select loan_sequence_number
	, pool_issue_date
	, cusip
	, original_note_rate
	, note_rate
	, pmms_30yr_origination
	, original_note_rate - pmms_30yr_origination as rate_spread
	, original_loan_amt
	, credit_score
	, case when credit_score <= 579 then 'Poor'
		when credit_score >= 580 and credit_score <= 669 then 'Fair'
		when credit_score >= 670 and credit_score <= 739 then 'Good'
		when credit_score >= 740 and credit_score <= 799 then 'Very Good'
		when credit_score >= 800 and credit_score <= 850 then 'Exceptional'
		end as credit_score_category
	, pmms_30yr_origination
from l2_conventional_data
where 1=1
	and year(cast(pool_issue_date as date)) = 2024
	and property_state = 'NC';