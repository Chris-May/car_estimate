from random import randint, sample

from fastapi import APIRouter

sample_entries = [
    {
        'type': 'ServiceCheck',
        'date': '2022-03-15',
        'details': {
            'service_center': 'QuickFix Auto',
            'services_performed': ['Oil change', 'Tire rotation'],
            'mileage': 15000,
        },
    },
    {
        'type': 'OwnershipTransfer',
        'date': '2021-09-01',
        'details': {
            'previous_owner': 'Jane Doe',
            'new_owner': 'John Smith',
            'location': 'New York, NY',
        },
    },
    {
        'type': 'AccidentReport',
        'date': '2023-07-04',
        'details': {
            'description': 'Rear-end collision',
            'severity': 'Moderate',
            'repairs_needed': ['Rear bumper replacement', 'Trunk alignment'],
            'reported_to_insurance': True,
        },
    },
    {
        'type': 'RegistrationChange',
        'date': '2024-01-10',
        'details': {
            'state': 'California',
            'plate_number': 'ABC1234',
            'registration_status': 'Renewed',
        },
    },
    {
        'type': 'InspectionNote',
        'date': '2023-11-20',
        'details': {
            'inspection_type': 'Annual safety check',
            'passed': True,
            'notes': 'Brakes and tires in good condition.',
        },
    },
    {
        'type': 'RepairLog',
        'date': '2022-05-18',
        'details': {
            'shop_name': 'Auto Masters',
            'repairs': ['Replaced battery', 'Fixed air conditioning'],
            'mileage': 18000,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2023-05-15',
        'details': {
            'service_center': 'AutoPro Services',
            'services_performed': ['Brake fluid replacement', 'Engine tune-up'],
            'mileage': 25000,
        },
    },
    {
        'type': 'OwnershipTransfer',
        'date': '2018-06-12',
        'details': {
            'previous_owner': 'Mike Johnson',
            'new_owner': 'Jane Doe',
            'location': 'Los Angeles, CA',
        },
    },
    {
        'type': 'AccidentReport',
        'date': '2019-10-22',
        'details': {
            'description': 'Side-swipe collision',
            'severity': 'Minor',
            'repairs_needed': ['Passenger-side mirror replacement'],
            'reported_to_insurance': True,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2020-03-01',
        'details': {
            'service_center': 'Express Auto Care',
            'services_performed': ['Oil change', 'Battery check'],
            'mileage': 12000,
        },
    },
    {
        'type': 'RepairLog',
        'date': '2021-08-14',
        'details': {
            'shop_name': "Joe's Garage",
            'repairs': ['Replaced alternator', 'Adjusted alignment'],
            'mileage': 22000,
        },
    },
    {
        'type': 'RegistrationChange',
        'date': '2020-07-15',
        'details': {
            'state': 'Nevada',
            'plate_number': 'NV54321',
            'registration_status': 'Transferred',
        },
    },
    {
        'type': 'InspectionNote',
        'date': '2022-12-02',
        'details': {
            'inspection_type': 'Emissions test',
            'passed': True,
            'notes': 'Passed with no issues.',
        },
    },
    {
        'type': 'AccidentReport',
        'date': '2021-01-29',
        'details': {
            'description': 'Fender bender in parking lot',
            'severity': 'Minor',
            'repairs_needed': ['Front bumper repaint'],
            'reported_to_insurance': False,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2022-04-10',
        'details': {
            'service_center': 'Prestige Auto',
            'services_performed': ['Replaced air filter', 'Brake pad replacement'],
            'mileage': 20000,
        },
    },
    {
        'type': 'RepairLog',
        'date': '2023-09-05',
        'details': {
            'shop_name': 'City Auto Repair',
            'repairs': ['Fixed fuel pump issue'],
            'mileage': 30000,
        },
    },
    {
        'type': 'RegistrationChange',
        'date': '2023-03-12',
        'details': {
            'state': 'Arizona',
            'plate_number': 'AZ76543',
            'registration_status': 'Renewed',
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2020-06-20',
        'details': {
            'service_center': 'Quick Lube Center',
            'services_performed': ['Oil change', 'Tire rotation', 'Fluid top-off'],
            'mileage': 5000,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2021-02-15',
        'details': {
            'service_center': 'Main Street Auto',
            'services_performed': ['Brake pad inspection', 'Battery test'],
            'mileage': 10000,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2021-10-30',
        'details': {
            'service_center': 'Autoworks Pro',
            'services_performed': ['Oil change', 'Transmission fluid replacement'],
            'mileage': 17000,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2022-08-01',
        'details': {
            'service_center': 'Premier Auto Care',
            'services_performed': [
                'Coolant system flush',
                'Cabin air filter replacement',
            ],
            'mileage': 23000,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2023-02-18',
        'details': {
            'service_center': 'Downtown Mechanics',
            'services_performed': ['Oil change', 'Power steering fluid replacement'],
            'mileage': 27000,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2023-10-10',
        'details': {
            'service_center': 'Green Valley Auto',
            'services_performed': ['Tire replacement', 'Alignment check'],
            'mileage': 32000,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2024-04-05',
        'details': {
            'service_center': 'Auto King',
            'services_performed': ['Spark plug replacement', 'Engine diagnostics'],
            'mileage': 37000,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2024-12-22',
        'details': {
            'service_center': 'Highway Mechanics',
            'services_performed': ['Oil change', 'Timing belt inspection'],
            'mileage': 42000,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2025-06-01',
        'details': {
            'service_center': 'Performance Auto',
            'services_performed': ['Brake fluid replacement', 'Tire rotation'],
            'mileage': 47000,
        },
    },
    {
        'type': 'ServiceCheck',
        'date': '2026-01-15',
        'details': {
            'service_center': 'Express Service',
            'services_performed': ['Battery replacement', 'Oil change', 'Inspection'],
            'mileage': 52000,
        },
    },
]

other = APIRouter(include_in_schema=False, prefix='/data')


@other.get('/')
def main():
    return sorted(
        sample(sample_entries, randint(1, len(sample_entries))),  # noqa: S311
        key=lambda entry: entry['date'],
    )


@other.get('/estimate')
def estimate():
    return dict(estimate=randint(5101, 32890))  # noqa: S311
