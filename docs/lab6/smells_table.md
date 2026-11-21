# Code Smells & Refactoring Table (invoice.py)

| Smell | Location / Context | Refactoring Applied |
|---|---|---|
| Duplicated Discount / Policy Logic | Repeated discount/policy rules across invoice calculation (SiblingPolicy) | Extracted SiblingPolicy with a clean apply(subtotal) method |
| Long / Complex Invoice Calculation | Mixing item totals, policy checks, and formatting in one block | Split responsibilities into small helper functions/methods |
| Magic Numbers | Hardcoded discount percentages and tax rates | Replaced with named constants (SIBLING_DISCOUNT_RATE, TAX_RATE) |
