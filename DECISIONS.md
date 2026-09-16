\# NEXORA 2026 – Decisions



\## 1. How gateways are prioritized



I used the provided 3-sigma baseline approach for Part 1.



For each scoring week, the system looks at recent telemetry and identifies unusual gateway behaviour using:



\- `offline\_duration\_sec`

\- `disconnection\_cnt`

\- `reboot\_cnt`



The gateways are ranked by the number of recent hours that exceed their own historical 3-sigma baseline.



\## 2. Why 15 gateways



The operations team has a hard limit of 15 site visits per week.



Therefore, the system selects exactly 15 gateways and assigns ranks from 1 to 15.



\## 3. Why use a gateway's own baseline



Gateway behaviour can differ between sites.



Using each gateway's own 28-day baseline makes the comparison relative to its normal behaviour rather than assuming that all gateways have the same normal operating level.



\## 4. Alternatives considered



\### Machine Learning model



A machine learning model was considered, but I did not replace the provided baseline because Part 1 does not require a new ML model.



The available time was instead used to make the solution easier to run, test and explain.



\### Using all available datasets



Gateway master data, field visits, meter-read success and engineer reviews could potentially provide additional information.



However, the baseline provides a clear telemetry-based starting point, and introducing additional signals without enough validation could make the decision logic harder to justify.



\## 5. Part 2 choice – Software Development



I selected Software Development for Part 2.



The goal was to make the prediction output usable through a simple API rather than only as a CSV file.



The API provides:



\- A health check endpoint

\- Weekly gateway predictions

\- Input validation

\- Error responses

\- Automated tests



This keeps the ranking logic separate from the way the results are consumed.



\## What the solution cannot do



The current solution is based mainly on telemetry anomalies.



It does not establish that every selected gateway is actually faulty, and an anomaly may have another explanation.



It also does not explicitly optimize the €380 site-visit cost versus the €600 cost of leaving a faulty gateway for another week.



With additional development time, I would evaluate historical field-visit outcomes and meter-read success to test whether the ranking better identifies gateways that actually require a visit.

