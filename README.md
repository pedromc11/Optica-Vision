# Optica Vision: Optical Store Management System 👁️‍🗨️

Optica Vision is an Odoo-based management system designed specifically for optical stores. It streamlines various operations, from managing product warranties and repairs to scheduling customer revisions and maintaining store information.

## Features ✨

### 1. Warranty Management (`garantia.py`)
This module handles the lifecycle of product warranties.
* **Unique Warranty Numbers**: Ensures each warranty has a unique identifier.
* **Purchase Date Tracking**: Records the date of product purchase.
* **Product and Customer Linking**: Associates warranties with specific products and customers.
* **Warranty Types**: Supports different types of warranties (e.g., manufacturer, store).
* **Coverage Period**: Defines the duration of warranty coverage in months.
* **Problem Description**: Allows detailed descriptions of issues covered by the warranty.
* **Status Tracking**: Monitors the status of warranties (Active, Expired, Claimed).
* **Dynamic Status Description**: Automatically updates the warranty's validity period.
* **Actions**:
    * **Claim Warranty**: Marks a warranty as "reclamada" (claimed).
    * **Extend Warranty**: Allows extension of active warranties by 12 months.

<hr/>

### 2. Replacement Management (`reemplazo.py`)
Manages product replacements under warranty.
* **Replacement Date**: Records the date when a replacement occurs.
* **Reason for Replacement**: Details the justification for the replacement.
* **Status**: Tracks the status of replacements (In Progress, Completed).
* **Warranty Link**: Directly links replacements to their corresponding warranty.

<hr/>

### 3. Repair Management (`reparacion.py`)
Manages the repair process for products under warranty.
* **Repair Date**: Records the date of the repair.
* **Work Description**: Provides a detailed account of the work performed.
* **Responsible Technician**: Assigns a specific technician to the repair.
* **Repair Cost**: Tracks the cost associated with the repair.
* **Status**: Indicates the current state of the repair (In Progress, Completed).
* **Warranty Link**: Connects repairs to the relevant product warranty.

<hr/>

### 4. Revision Management (`revision.py`)
Handles customer appointments and revisions.
* **Date and Time**: Schedules specific dates and times for revisions.
* **Revision Type**: Categorizes revisions (e.g., Optometrist for "Vista" (Sight), ENT for "Audición" (Hearing)).
* **Professional**: Assigns the professional conducting the revision.
* **Observations**: Stores notes and observations from the revision.
* **Rating**: Allows rating the revision (Bad, Normal, Very Good).
* **Client and Store Association**: Links revisions to specific clients and stores.
* **Status**: Manages the status of revisions (Pending, Done, Rejected, Postponed).

<hr/>

### 5. Store Management (`tienda.py`)
Manages information for each physical store location.
* **Store Name**: Unique name for each store.
* **Address and City**: Physical location details.
* **Province Calculation**: Automatically determines the province based on the city.
* **Phone Number Validation**: Ensures phone numbers adhere to a valid Spanish format (e.g., 999-999-999 or 999999999).
* **Opening Days**: Specifies the days of the week the store is open.
* **Description**: Provides a brief description of the store.
* **Actions**:
    * **Open Weekend**: Adds Saturday and Sunday to the store's opening days.
    * **Close Weekend**: Removes Saturday and Sunday from the store's opening days.

<hr/>

### 6. Day Management (`dia.py`)
A simple model to define days of the week, used for store opening hours.
* **Day Name**: Stores the name of the day (e.g., Monday, Tuesday).
* **Unique Constraint**: Ensures each day name is unique.

<hr/>

## Installation 💻

1.  **Clone the Repository**:
    ```bash
    git clone <repository_url>
    ```
2.  **Add to Odoo Addons Path**: Place the cloned `optica_vision` folder within your Odoo instance's `addons` path.
3.  **Update Odoo Modules List**:
    * Go to `Apps` in Odoo.
    * Click on `Update Apps List`.
4.  **Install the Module**:
    * Search for "Optica Vision" (or the technical name of the module if different) in the Apps list.
    * Click `Install`.

## Usage 🚀

Once installed, you can access the various modules from your Odoo dashboard.

* **Warranties**: Create and manage product warranties.
* **Revisions**: Schedule and track customer appointments.
* **Stores**: Set up and manage your optical store locations.
* **Repairs**: Log and track product repairs.
* **Replacements**: Record product replacements.

## Contributing 🤝

Contributions are welcome! If you'd like to improve Optica Vision, please feel free to submit pull requests or open issues.

## License 📄

This project is licensed under the MIT License.
