# Lab & Room Booking System — User Stories

## Project overview
The Lab & Room Booking System is a web-based system for university students and instructors. Users can browse rooms and labs, check when they are free, send booking requests, and follow the status of their requests. Administrators are responsible for managing the spaces and their schedules, and for approving or rejecting requests.

## Team
| Member | Role | GitHub |
|---|---|---|
| Shahd Alaa | Product Owner | Shahdalaa2 |
| Dareen Wael | Developer | Dareen278 |
| Reem Taher | Developer | Reem taher |
| Youstina Nady | Scrum Master | youstinanady555-droid |

## User stories

### US01 — Log in
As a user, I want to log in so that I can use the system with my own account.
- Acceptance criteria:
  - When I enter valid credentials, the system signs me in and takes me to the main page.
  - When I enter incorrect credentials, the system shows an error and keeps me on the login page.
  - The system does not allow access to user pages before login.

### US02 — Browse rooms and labs
As a student or instructor, I want to browse the available rooms and labs so that I can find a space that suits my needs.
- Acceptance criteria:
  - The system displays the rooms and labs that can currently be booked.
  - Each result shows the space name and whether it is a room or a lab.
  - Deactivated spaces are not shown as available options.

### US03 — Search and filter
As a user, I want to search and filter rooms and labs so that I can narrow down the list.
- Acceptance criteria:
  - I can search using a room or lab name.
  - I can filter the results by space type and capacity.
  - The results update to match the search text and selected filters.

### US04 — View space details
As a user, I want to view the details of a room or lab so that I can decide whether it is suitable for my booking.
- Acceptance criteria:
  - The details page shows the space name, type, capacity, location, and available equipment.
  - The details shown belong to the space I selected.
  - If a detail is not available, the system does not display misleading information.

### US05 — Check availability
As a user, I want to check the available dates and time slots so that I can choose a suitable time.
- Acceptance criteria:
  - I can select a date for the space I want to book.
  - The system shows which time slots are available and which are already taken or blocked.
  - Availability is updated when a booking or schedule change affects that space.

### US06 — Submit a booking request
As a student or instructor, I want to submit a booking request so that I can request a room or lab for a specific purpose.
- Acceptance criteria:
  - I can choose a space, date, time slot, and enter the purpose of the booking.
  - The system checks that the required information has been entered.
  - After submission, I see a message confirming that the request was received.
  - The request appears in my bookings with a pending status until an administrator makes a decision.

### US07 — Prevent double booking
As a user, I want the system to prevent overlapping booking requests so that the same space is not requested by two users for the same time.
- Acceptance criteria:
  - Before saving a request, the system checks for another pending or approved booking for the same space and overlapping time.
  - If there is a conflict, the system does not save the request and explains why.
  - Requests for different spaces or non-overlapping time slots can still be submitted.

### US08 — View my bookings
As a user, I want to view my booking requests so that I can keep track of their details and statuses.
- Acceptance criteria:
  - I can see the booking requests submitted from my account.
  - Each booking shows the space, date, time, and current status.
  - I cannot see another user's private booking list.

### US09 — Cancel a booking
As a user, I want to cancel a booking when cancellation is allowed so that the time slot can be made available to others.
- Acceptance criteria:
  - I can cancel a booking only when it meets the system's cancellation rules.
  - The system asks for confirmation before completing the cancellation.
  - After cancellation, the booking status is updated and the time slot is made available if no other booking blocks it.

### US10 — Approve or reject requests
As an administrator, I want to review booking requests and approve or reject them so that bookings are managed properly.
- Acceptance criteria:
  - I can view the requests that are waiting for a decision.
  - I can approve or reject a pending request.
  - The system updates the request status and makes the new status visible to the requester.
  - A request that has already been decided cannot be approved or rejected again.

### US11 — Manage rooms and labs
As an administrator, I want to add, edit, and deactivate rooms and labs so that the information shown to users stays up to date.
- Acceptance criteria:
  - I can add a space with its name, type, capacity, location, and equipment details.
  - I can edit the information of an existing space.
  - I can deactivate a space so it is no longer offered for new bookings.
  - The system keeps existing booking records when a space is deactivated.

### US12 — Manage schedules
As an administrator, I want to manage the schedules of rooms and labs so that users see the correct available time slots.
- Acceptance criteria:
  - I can set the normal operating days and hours for a space.
  - I can block a date or time slot when the space cannot be used.
  - Blocked times are shown as unavailable when users check availability.
  - The system warns me if a schedule change conflicts with an existing booking.

### US13 — Receive booking notifications
As a user, I want to receive an update when a decision is made on my booking request so that I know what happened.
- Acceptance criteria:
  - The system creates a notification when the status of my request changes to approved or rejected.
  - The notification identifies the booking and shows its new status.
  - I can access the notification from my account.

## MVP suggestion
For the first usable version, focus on login, browsing and searching, viewing space details and availability, submitting requests, preventing conflicting bookings, administrator decisions, and viewing booking statuses. Notifications and further administration improvements can be added in a later release.
