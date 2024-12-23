import random

pt_emp_ids = ('NV1252', 'NV9375', 'NV2099', 'NV6452', 'NV6043', 'NV9741', 'NV3184', 'NV7938', 'NV9007', 'NV3140', 'NV6160', 'NV7994', 'NV5474', 'NV3728', 'NV6256', 'NV6475', 'NV8594', 'NV8801', 'NV2689', 'NV8929', 'NV3981', 'NV9273', 'NV1108', 'NV5192', 'NV1540', 'NV8519', 'NV2790', 'NV3300', 'NV9022', 'NV2231', 'NV5858', 'NV8084', 'NV4620', 'NV5859', 'NV6164', 'NV8049', 'NV8348', 'NV2977', 'NV7327', 'NV9983', 'NV7733', 'NV8232', 'NV9199', 'NV2553', 'NV5235', 'NV5494', 'NV9115', 'NV5324', 'NV5896', 'NV9240')

shifts = (('08:00', '12:00'), ('13:00', '17:00'))

dates = ('2024-10-21', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-25', '2024-10-28', '2024-10-29', '2024-10-30', '2024-10-31', '2024-11-01', '2024-11-04', '2024-11-05', '2024-11-06', '2024-11-07', '2024-11-08', '2024-11-11', '2024-11-12', '2024-11-13', '2024-11-14', '2024-11-15', '2024-11-18', '2024-11-19', '2024-11-20', '2024-11-21', '2024-11-22', '2024-11-25', '2024-11-26', '2024-11-27', '2024-11-28', '2024-11-29', '2024-12-02', '2024-12-03', '2024-12-04', '2024-12-05', '2024-12-06', '2024-12-09', '2024-12-10', '2024-12-11', '2024-12-12', '2024-12-13', '2024-12-16', '2024-12-17', '2024-12-18', '2024-12-19', '2024-12-20', '2024-12-23', '2024-12-24', '2024-12-25', '2024-12-26', '2024-12-27')

# random.randint(1, 100)

# (`MaNV`, `Ngay`, `GioBatDau`, `GioKetThuc`)
for pt_emp_id in pt_emp_ids:
    for date in dates:
        if random.randint(1, 100) % 2 == 0:
            continue
        else:
            shift = random.choice(shifts)
            print(f'(\'{pt_emp_id}\', \'{date}\', \'{shift[0]}\', \'{shift[1]}\'),')
