# Mini Fleet - Fleet Management Module for Odoo 16

## Module Description
**Mini Fleet** is a lightweight module developed for Odoo 16 designed to manage a company vehicle fleet. It tracks technical vehicle characteristics, operational states, assigned drivers, and intervention histories (logs).

## Key Features
* **Vehicle Form:** Tracking for license plate, brand, model, year, color, chassis number, and mileage.
* **Status Management:** Vehicle lifecycle managed via states (`Stock`, `Running`, `Maintenance`, `Scrapped`) with dedicated action buttons.
* **Uniqueness Constraints:** Database-level security preventing duplicate license plates and chassis numbers.
* **Intervention Tracking:** One2many relationship linking to a maintenance and service history (`mini.vehicle.log`).
* **Security & Strict Roles:** 
  * *Reader*: Read-only access.
  * *Fleet Manager*: Creation and modification, with no deletion rights.
  * *Manager*: Full access (including deletion and archiving).

## File Structure
```text
mini_fleet/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── vehicle.py
│   └── vehicle_log.py
├── security/
│   ├── security.xml
│   └── ir.model.access.csv
├── views/
│   ├── vehicle_views.xml
│   └── fleet_menus.xml
└── demo/
    └── vehicle_demo.xml
```

## Installation Instructions

1. **Clone or place the module** into your Odoo custom addons directory (e.g., `/mnt/extra-addons/addons/`).
2. **Update the app list** from the Odoo interface (with Developer Mode enabled) or via the Docker command line:
   ```bash
   docker exec -it <odoo_container_name> odoo -d <database_name> -u mini_fleet --without-demo=False --stop-after-init
3. **The module will install with its demonstration data (vehicles with various statuses and associated logs).