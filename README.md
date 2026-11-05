# warehouse-inventory-system
Warehouse Inventory Management System – Week 11 CI/CD Lab
## Deployment and Infrastructure Assumptions

The application will run as a web-based system.

The system will use a separate database for products, inventory, sales orders, purchasing, users, and transaction data.

Users will access the system through a web interface.

The Financial System will communicate with the Warehouse Inventory Management System through an API.

GitHub is used for source-code version control.

GitHub Actions is used for Continuous Integration.

Every code change should pass the automated tests before it is merged.

Production deployment should happen only after the CI pipeline passes successfully.

Sensitive information such as passwords and API keys should not be stored directly in the source code.

## Monitoring and Feedback Signals

The system should be monitored after deployment using the following signals:

Latency: Monitor how quickly the system responds to product searches, stock checks, and inventory updates.

Traffic: Monitor the number of users and requests using the system.

Errors: Monitor failed logins, unsuccessful inventory updates, database errors, and Financial System integration errors.

Saturation: Monitor whether the server, database, memory, or other system resources are reaching their capacity.

These monitoring signals will help identify problems quickly and improve system reliability and performance.
