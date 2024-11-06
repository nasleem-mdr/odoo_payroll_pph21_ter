def calculate_result(gross, brackets):
    for lower_bound, upper_bound, factor in brackets:
        if lower_bound <= gross <= upper_bound:
            return gross * factor
    return gross * 0.35 if gross > 1400000000 else 0

brackets_single = [
    (5400001, 5650000, 0.0025),
    (5650001, 5950000, 0.0050),
    (5950001, 6300000, 0.0075),
    # Tambahkan rentang berikutnya sesuai kebutuhan...
]

if (employee.marital == 'single' and employee.children < 2) or (employee.marital == 'married' and employee.children < 1):
    result = calculate_result(categories.GROSS, brackets_single)
# Tambahkan kondisi elif lain sesuai kebutuhan...
