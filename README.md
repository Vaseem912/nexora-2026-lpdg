# NEXORA 2026 – LPDG Gateway Visit Prioritization

## Overview

This project addresses the LPDG gateway field-visit prioritization problem.

The system generates a ranked list of 15 gateways to visit for each scored week using the provided baseline 3-sigma approach.

## Part 1 – Gateway Prioritization

The baseline analyzes recent gateway telemetry and identifies gateways showing unusual:

- Offline duration
- Disconnection count
- Reboot count

For each week, the system produces the top 15 gateways with a score and explanation.

The generated submission contains 120 rows covering 8 weeks.

## Part 2 – Software Development

A lightweight Flask API was developed around the prediction output.

### API Endpoints

`GET /health`

Returns:

```json
{"status": "ok"}