from __future__ import annotations


def campaign_payload(name: str, marketplace: str) -> dict[str, object]:
    return {
        "adProduct": "SPONSORED_PRODUCTS",
        "autoCreationSettings": {"autoCreateTargets": False},
        "budgets": [
            {
                "budgetType": "MONETARY",
                "budgetValue": {
                    "monetaryBudgetValue": {
                        "monetaryBudget": {"value": 10.0},
                    },
                },
                "recurrenceTimePeriod": "DAILY",
            },
        ],
        "marketplaceScope": "SINGLE_MARKETPLACE",
        "marketplaces": [marketplace],
        "name": name,
        "startDateTime": "2026-06-09T00:00:00Z",
        "state": "ENABLED",
    }


def campaign_query_body(campaign_id: str, *, state: str | None = None) -> dict[str, object]:
    body: dict[str, object] = {
        "adProductFilter": {"include": ["SPONSORED_PRODUCTS"]},
        "campaignIdFilter": {"include": [campaign_id]},
    }
    if state is not None:
        body["stateFilter"] = {"include": [state]}
    return body


def ad_group_payload(name: str, campaign_id: str) -> dict[str, object]:
    return {
        "adProduct": "SPONSORED_PRODUCTS",
        "bid": {"defaultBid": 1.0},
        "campaignId": campaign_id,
        "name": name,
        "state": "ENABLED",
    }
