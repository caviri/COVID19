Database
========

The Covid Tracking Project: Data API. It contains 2 main categories:
National Data, and State & Territories Data.

National Data
-------------

-  Historic US values:

   -  field_definitions

      -  Total test results
      -  Hospital discharges
      -  Confirmed Cases
      -  Cumulative hospitalized/Ever hospitalized
      -  Cumulative in ICU/Ever in ICU
      -  Cumulative on ventilator/Ever on ventilator
      -  Currently hospitalized/Now hospitalized
      -  Currently in ICU/Now in ICU
      -  Currently on ventilator/Now on ventilator
      -  Deaths (probable)
      -  Deaths (confirmed)
      -  Deaths (confirmed and probable)
      -  Probable Cases
      -  Last Update (ET)
      -  New deaths
      -  Date
      -  States (**Non reported**)

Every field is organized in 3 categories: cases, testing, and outcomes.
Then, every field can be accessed with aq dot after the category.

-  Single Day of data:

   -  Same information but you don’t need to download the whole dataset.
      This can be useful in order to make the dataretrieval parallel.

State & Terrtories Data
-----------------------

-  All state metadata: Basic information about all states, including
   notes about our methodology and the websites we use to check for
   data.

   -  field_definitions

      -  state_code
      -  COVID Tracking Project preferred total test units
      -  COVID Tracking Project preferred total test field
      -  State population (2019 census)
      -  Tertiary source for state COVID data
      -  Secondary source for state COVID data
      -  Primary source for state COVID data
      -  FIPS code
      -  State (or territory)

-  Single State Metadata: Same but per state

   -  field_definitions

      -  state_code
      -  COVID Tracking Project preferred total test units
      -  COVID Tracking Project preferred total test field
      -  State population (2019 census)
      -  Tertiary source for state COVID data
      -  Secondary source for state COVID data
      -  Primary source for state COVID data
      -  FIPS code
      -  State (or territory)

-  Historic data for a state or

   -  field_definitions

      -  Total test results
      -  Hospital discharges
      -  Confirmed Cases
      -  Cumulative hospitalized/Ever hospitalized
      -  Cumulative in ICU/Ever in ICU
      -  Cumulative on ventilator/Ever on ventilator
      -  Currently hospitalized/Now hospitalized
      -  Currently in ICU/Now in ICU
      -  Currently on ventilator/Now on ventilator
      -  Deaths (probable)
      -  Deaths (confirmed)
      -  Deaths (confirmed and probable)
      -  Probable Cases
      -  Last Update (ET)
      -  New deaths
      -  Date

-  Single day of data for a state or territory

   -  field_definitions

      -  Total test results
      -  Hospital discharges
      -  Confirmed Cases
      -  Cumulative hospitalized/Ever hospitalized
      -  Cumulative in ICU/Ever in ICU
      -  Cumulative on ventilator/Ever on ventilator
      -  Currently hospitalized/Now hospitalized
      -  Currently in ICU/Now in ICU
      -  Currently on ventilator/Now on ventilator
      -  Deaths (probable)
      -  Deaths (confirmed)
      -  Deaths (confirmed and probable)
      -  Probable Cases
      -  Last Update (ET)
      -  New deaths
      -  Date

