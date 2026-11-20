# Lab & Room Booking System — Estimation

We estimated the user stories using a relative Fibonacci-style scale: 1, 2, 3, 5, and 8 points. Story points are used to compare the effort, complexity, and uncertainty of stories. They do not represent a number of hours or days.

| Story ID | User story (short name) | Story points | Reason |
|---|---|---:|---|
| US01 | Log in | 3 | Includes credential checking, validation, and handling incorrect login details. |
| US02 | Browse rooms and labs | 3 | Retrieves and displays the list of bookable spaces, excluding deactivated ones. |
| US03 | Search and filter | 2 | Basic search and filtering by a small number of fields. |
| US04 | View space details | 2 | Displays information already stored for the selected space. |
| US05 | Check availability | 5 | Needs date and time selection, plus logic to identify free and occupied slots. |
| US06 | Submit a booking request | 5 | Booking form with required-field validation and saving the request with a pending status. |
| US07 | Prevent double booking | 5 | Conflict checking against pending and approved bookings, including overlapping time edge cases. |
| US08 | View my bookings | 3 | Retrieves the current user's requests and displays their statuses. |
| US09 | Cancel a booking | 2 | Applies cancellation rules, asks for confirmation, and updates the booking status and slot. |
| US10 | Approve or reject requests | 5 | Includes an administrator workflow and updates to booking statuses. |
| US11 | Manage rooms and labs | 5 | Supports adding, editing, and deactivating spaces. |
| US12 | Manage schedules | 5 | Includes setting operating hours and blocking dates or time slots. |
| US13 | Receive booking notifications | 3 | Creates and displays a notification when a booking decision changes. |
| | **Total** | **48** | |

## Estimation assumptions
- These are initial estimates. The team should review and agree on the points together.
- We use the same scale for all stories so that their relative effort can be compared.
- A story may need to be estimated again if its requirements or scope change.
- The points are estimates of relative work, not a promise about how long implementation will take.
