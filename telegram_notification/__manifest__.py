{
    "name": "Telegram Notification Center",
    "version": "19.0.1.0.0",
    "summary": "Send Telegram alerts for key business events",
    "category": "Tools",
    "author": "thetzin",
    "license": "LGPL-3",
    "description": """
                        <p>
                            Telegram Notification Center sends Telegram alerts for key Odoo business events
                            such as sales, purchases, invoices, stock, CRM leads, and attendance.
                        </p>
                        <ul>
                            <li>Sale and purchase order notifications</li>
                            <li>Invoice payment alerts</li>
                            <li>Scheduled reminders for due invoices and low stock</li>
                            <li>CRM lead assignment notifications</li>
                            <li>Attendance alerts</li>
                        </ul>
                   """,
    "images": ["static/description/cover.png"],
    "external_dependencies": {"python": ["requests"]},
    "depends": [
        "base",
        "mail",
        "sale_management",
        "purchase",
        "account",
        "stock",
        "crm",
        "hr_attendance",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_cron.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
    "application": False,
}
