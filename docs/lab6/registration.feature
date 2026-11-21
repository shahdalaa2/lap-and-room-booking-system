Feature: Lab and Room Booking Registration and Drop

  Scenario: Drop a booked lab or room session before deadline
    Given a registered user has an active booking for "Lab 101" tomorrow
    And the current time is before the drop deadline
    When the user drops the booking
    Then the booking status becomes "Dropped"
    And "Lab 101" becomes available for other users

  Scenario: Register for an available lab slot
    Given a registered user is logged into the booking system
    And "Lab 202" is available at "10:00 AM"
    When the user registers for "Lab 202" at "10:00 AM"
    Then a confirmed booking is created for the user

  Scenario: Reject registration when slot is already booked
    Given "Room 305" is already booked at "02:00 PM"
    When another user attempts to book "Room 305" at "02:00 PM"
    Then the registration is rejected with a conflict message

  Scenario: Reject drop after the allowed cutoff time
    Given a user has an active booking that started already
    When the user tries to drop the booking
    Then the drop request is denied
