Fundraising Platform:-

Overview of the Application
This Flask application is a simple web app that allows users to:

Register their details on the send.html page.

Provide additional information (e.g., donation amount) on the information.html page.

View a success message with their submitted data on the success.html page.

The application uses Flask for routing and rendering HTML templates, and it passes data between pages using URL parameters.



Routing:

The application has three routes:

/ (root route) for the registration page (send.html).

/information for the donation information page (information.html).

/success for the success page (success.html).

Form Handling:

Forms are used to collect user input on both send.html and information.html.

The form data is passed between pages using URL parameters (e.g., ?name=John&email=john@example.com).

Dynamic Data Rendering:

The information.html page dynamically displays the data submitted on the send.html page.

The success.html page displays all the submitted data (from both forms).

Styling:

Each page has a background image and basic CSS styling for a clean and user-friendly interface.


1. Registration Page (send.html):
The user enters their details (name, email, phone, and message) and clicks the "Next" button.

The form submits a POST request to the / route (handled by the register function in app.py).

The register function collects the form data and redirects the user to the /information route, passing the data as URL parameters.

2. Information Page (information.html):
The user sees their previously submitted data (name, email, phone, and message) displayed as read-only fields.

The user enters additional information (e.g., donation amount) and clicks the "Submit" button.

The form submits a POST request to the /information route (handled by the information function in app.py).

The information function collects the form data and redirects the user to the /success route, passing all the data as URL parameters.

3. Success Page (success.html):
The user sees a success message along with all the data they submitted (from both forms).

The data is displayed dynamically using Jinja2 templating (e.g., {{ name }}, {{ email }}).


Flask Application (app.py):
register Function:

Handles the registration form submission.

Redirects to the /information route with the form data as URL parameters.

information Function:

Handles the donation form submission.

Redirects to the /success route with all the form data as URL parameters.

success Function:

Displays the submitted data on the success page.

HTML Templates:
send.html:

Contains a form for user registration.

Submits data to the / route.

information.html:

Displays the registration data as read-only fields.

Contains a form for additional information (e.g., donation amount).

Submits data to the /information route.

success.html:

Displays all the submitted data dynamically using Jinja2 templating.

Data Flow
User Submits Registration Form:

Data flows from send.html → app.py (register function) → information.html.

User Submits Donation Form:

Data flows from information.html → app.py (information function) → success.html.

User Views Success Page:

All submitted data is displayed on success.html.



![Screenshot 2025-02-19 165445](https://github.com/user-attachments/assets/5fa10057-e258-4d96-848f-06a7593c97c7)



![Screenshot 2025-02-19 165508](https://github.com/user-attachments/assets/52a19e74-86f2-4242-b465-d1d340736c03)



![Screenshot 2025-02-19 165534](https://github.com/user-attachments/assets/558d63e4-fd1a-409c-a26c-a884c254ff42)



