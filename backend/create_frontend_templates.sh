#!/bin/bash

set -e

echo "Creating Solar ERP frontend templates..."

mkdir -p templates/core
mkdir -p templates/sales
mkdir -p templates/customers
mkdir -p templates/projects
mkdir -p templates/inventory
mkdir -p templates/finance
mkdir -p templates/technicians
mkdir -p templates/reports

cat > templates/base.html <<'BASE_HTML'
<!DOCTYPE html>
<html>
<head>
    <title>Solar ERP</title>

    https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css

    <style>
        body {
            background-color: #f4f6f9;
        }

        .sidebar {
            min-height: 100vh;
            background-color: #111827;
        }

        .sidebar h4 {
            color: #ffffff;
            padding: 20px;
        }

        .sidebar a {
            color: #d1d5db;
            text-decoration: none;
            display: block;
            padding: 12px 20px;
        }

        .sidebar a:hover {
            background-color: #1f2937;
            color: #ffffff;
        }

        .content {
            padding: 25px;
        }

        .topbar {
            background-color: #ffffff;
            padding: 15px 25px;
            border-bottom: 1px solid #e5e7eb;
        }

        .card-box {
            border-radius: 10px;
            border: none;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
    </style>
</head>

<body>

<div class="container-fluid">
    <div class="row">

        <div class="col-md-2 sidebar p-0">

            <h4>Solar ERP</h4>

            /dashboard/Dashboard</a>
            /dashboard/sales/Sales Dashboard</a>
            /dashboard/finance/Finance Dashboard</a>
            /dashboard/technician/Technician Dashboard</a>
            /dashboard/management/Management Dashboard</a>

            <hr style="border-color: #374151;">

            /api/crm/leads/Leads</a>
            /api/quotation/quotations/Quotations</a>
            /api/customers/customers/Customers</a>
            /api/projects/projects/Projects</a>
            /api/inventory/items/Inventory</a>
            /api/finance/invoices/Invoices</a>
            /api/technicians/workorders/Work Orders</a>

            <hr style="border-color: #374151;">

            /logout/Logout</a>

        </div>

        <div class="col-md-10 p-0">

            <div class="topbar">
                <strong>Welcome, {{ request.user.username }}</strong>
            </div>

            <div class="content">
                {% block content %}
                {% endblock %}
            </div>

        </div>

    </div>
</div>

https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js</script>

</body>
</html>
BASE_HTML

cat > templates/core/login.html <<'LOGIN_HTML'
<!DOCTYPE html>
<html>
<head>
    <title>Solar ERP Login</title>

    https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css

    <style>
        body {
            background-color: #f4f6f9;
        }

        .login-box {
            max-width: 400px;
            margin: 100px auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.1);
        }
    </style>
</head>

<body>

<div class="login-box">

    <h3 class="text-center mb-4">
        Solar ERP Login
    </h3>

    {% if error_message %}
        <div class="alert alert-danger">
            {{ error_message }}
        </div>
    {% endif %}

    <form method="post">
        {% csrf_token %}

        <div class="mb-3">
            <label>Username</label>
            <input
                type="text"
                name="username"
                class="form-control"
                required
            >
        </div>

        <div class="mb-3">
            <label>Password</label>
            <input
                type="password"
                name="password"
                class="form-control"
                required
            >
        </div>

        <button class="btn btn-primary w-100" type="submit">
            Login
        </button>
    </form>

</div>

</body>
</html>
LOGIN_HTML

cat > templates/core/sales_dashboard.html <<'SALES_HTML'
{% extends "base.html" %}

{% block content %}

<h2>Sales Dashboard</h2>

<p class="text-muted">
    Sales and marketing team dashboard.
</p>

<div class="row">

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Total Leads</h5>
                <h3 id="total_leads">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Won Leads</h5>
                <h3 id="won_leads">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Lost Leads</h5>
                <h3 id="lost_leads">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>New Leads</h5>
                <h3 id="new_leads">-</h3>
            </div>
        </div>
    </div>

</div>

<div class="mt-4">
    /api/crm/leads/
        Manage Leads
    </a>

    /api/quotation/quotations/
        Manage Quotations
    </a>

    /api/reports/sales-dashboard/
        View Sales API
    </a>
</div>

<script>
fetch("/api/reports/sales-dashboard/")
    .then(response => response.json())
    .then(data => {
        document.getElementById("total_leads").innerText = data.total_leads ?? 0;
        document.getElementById("won_leads").innerText = data.won_leads ?? 0;
        document.getElementById("lost_leads").innerText = data.lost_leads ?? 0;
        document.getElementById("new_leads").innerText = data.new_leads ?? 0;
    })
    .catch(error => {
        console.log("Sales dashboard API error", error);
    });
</script>

{% endblock %}
SALES_HTML

cat > templates/core/finance_dashboard.html <<'FINANCE_HTML'
{% extends "base.html" %}

{% block content %}

<h2>Finance Dashboard</h2>

<p class="text-muted">
    Finance team dashboard.
</p>

<div class="row">

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Total Invoices</h5>
                <h3 id="total_invoices">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Payments Received</h5>
                <h3 id="payments_received">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Paid Invoices</h5>
                <h3 id="paid_invoices">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Pending Invoices</h5>
                <h3 id="pending_invoices">-</h3>
            </div>
        </div>
    </div>

</div>

<div class="mt-4">
    /api/finance/invoices/
        Manage Invoices
    </a>

    /api/finance/payments/
        Manage Payments
    </a>

    /api/reports/finance-dashboard/
        View Finance API
    </a>
</div>

<script>
fetch("/api/reports/finance-dashboard/")
    .then(response => response.json())
    .then(data => {
        document.getElementById("total_invoices").innerText = data.total_invoices ?? 0;
        document.getElementById("payments_received").innerText = data.payments_received ?? 0;
        document.getElementById("paid_invoices").innerText = data.paid_invoices ?? 0;
        document.getElementById("pending_invoices").innerText = data.pending_invoices ?? 0;
    })
    .catch(error => {
        console.log("Finance dashboard API error", error);
    });
</script>

{% endblock %}
FINANCE_HTML

cat > templates/core/technician_dashboard.html <<'TECH_HTML'
{% extends "base.html" %}

{% block content %}

<h2>Technician Dashboard</h2>

<p class="text-muted">
    Technician work order dashboard.
</p>

<div class="row">

    <div class="col-md-4">
        <div class="card card-box">
            <div class="card-body">
                <h5>Technicians</h5>
                <h3 id="technicians">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-4">
        <div class="card card-box">
            <div class="card-body">
                <h5>Open Work Orders</h5>
                <h3 id="open_work_orders">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-4">
        <div class="card card-box">
            <div class="card-body">
                <h5>Completed Work Orders</h5>
                <h3 id="completed_work_orders">-</h3>
            </div>
        </div>
    </div>

</div>

<div class="mt-4">
    /api/technicians/workorders/
        Work Orders
    </a>

    /api/projects/projects/
        Projects
    </a>

    /api/reports/technician-dashboard/
        View Technician API
    </a>
</div>

<script>
fetch("/api/reports/technician-dashboard/")
    .then(response => response.json())
    .then(data => {
        document.getElementById("technicians").innerText = data.technicians ?? 0;
        document.getElementById("open_work_orders").innerText = data.open_work_orders ?? 0;
        document.getElementById("completed_work_orders").innerText = data.completed_work_orders ?? 0;
    })
    .catch(error => {
        console.log("Technician dashboard API error", error);
    });
</script>

{% endblock %}
TECH_HTML

cat > templates/core/management_dashboard.html <<'MANAGEMENT_HTML'
{% extends "base.html" %}

{% block content %}

<h2>Management Dashboard</h2>

<p class="text-muted">
    Overall Solar ERP business summary.
</p>

<div class="row">

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Leads</h5>
                <h3 id="leads">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Customers</h5>
                <h3 id="customers">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Projects</h5>
                <h3 id="projects">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Inventory Items</h5>
                <h3 id="inventory_items">-</h3>
            </div>
        </div>
    </div>

</div>

<div class="row mt-4">

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Payments</h5>
                <h3 id="payments">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Technicians</h5>
                <h3 id="technicians">-</h3>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card card-box">
            <div class="card-body">
                <h5>Work Orders</h5>
                <h3 id="work_orders">-</h3>
            </div>
        </div>
    </div>

</div>

<script>
fetch("/api/reports/management-dashboard/")
    .then(response => response.json())
    .then(data => {
        document.getElementById("leads").innerText = data.leads ?? 0;
        document.getElementById("customers").innerText = data.customers ?? 0;
        document.getElementById("projects").innerText = data.projects ?? 0;
        document.getElementById("inventory_items").innerText = data.inventory_items ?? 0;
        document.getElementById("payments").innerText = data.payments ?? 0;
        document.getElementById("technicians").innerText = data.technicians ?? 0;
        document.getElementById("work_orders").innerText = data.work_orders ?? 0;
    })
    .catch(error => {
        console.log("Management dashboard API error", error);
    });
</script>

{% endblock %}
MANAGEMENT_HTML

cat > templates/core/admin_dashboard.html <<'ADMIN_HTML'
{% extends "base.html" %}

{% block content %}

<h2>Admin Dashboard</h2>

<p class="text-muted">
    Admin control centre.
</p>

<div class="row">

    <div class="col-md-4">
        <div class="card card-box">
            <div class="card-body">
                <h5>Django Admin</h5>
                <p>Manage users, roles and backend data.</p>
                <a class="btn btn-primary" href="/admin/">
                    Open Admin
                </a>
            </div>
        </div>
    </div>

    <div class="col-md-4">
        <div class="card card-box">
            <div class="card-body">
                <h5>Management Dashboard</h5>
                <p>View full ERP summary.</p>
                /dashboard/management/
                    View Dashboard
                </a>
            </div>
        </div>
    </div>

</div>

{% endblock %}
ADMIN_HTML

cat > templates/core/no_access.html <<'NO_ACCESS_HTML'
{% extends "base.html" %}

{% block content %}

<h2>No Access Assigned</h2>

<p>
    Your user account does not belong to any ERP role group.
</p>

<p>
    Please contact Admin to assign one of these groups:
</p>

<ul>
    <li>ADMIN</li>
    <li>SALES</li>
    <li>FINANCE</li>
    <li>TECHNICIAN</li>
    <li>MANAGEMENT</li>
</ul>

/logout/
    Logout
</a>

{% endblock %}
NO_ACCESS_HTML

echo "Frontend templates created successfully."
