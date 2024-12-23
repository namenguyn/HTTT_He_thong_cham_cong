import random

dates = ('2024-10-21', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-25', '2024-10-28', '2024-10-29', '2024-10-30', '2024-10-31', '2024-11-01', '2024-11-04', '2024-11-05', '2024-11-06', '2024-11-07', '2024-11-08', '2024-11-11', '2024-11-12', '2024-11-13', '2024-11-14', '2024-11-15', '2024-11-18', '2024-11-19', '2024-11-20', '2024-11-21', '2024-11-22', '2024-11-25', '2024-11-26', '2024-11-27', '2024-11-28', '2024-11-29', '2024-12-02', '2024-12-03', '2024-12-04', '2024-12-05', '2024-12-06', '2024-12-09', '2024-12-10', '2024-12-11', '2024-12-12', '2024-12-13', '2024-12-16', '2024-12-17', '2024-12-18', '2024-12-19', '2024-12-20', '2024-12-23', '2024-12-24', '2024-12-25', '2024-12-26', '2024-12-27')
ft_emp_ids = ('NV1234', 'NV1271', 'NV1282', 'NV1371', 'NV1404', 'NV1452', 'NV1472', 'NV1492', 'NV1778', 'NV1816', 'NV1967', 'NV2034', 'NV2105', 'NV2124', 'NV2137', 'NV2357', 'NV2368', 'NV2494', 'NV2551', 'NV2569', 'NV2582', 'NV2825', 'NV2959', 'NV2994', 'NV3027', 'NV3058', 'NV3171', 'NV3189', 'NV3205', 'NV3214', 'NV3265', 'NV3287', 'NV3290', 'NV3308', 'NV3325', 'NV3577', 'NV3587', 'NV3614', 'NV3678', 'NV3692', 'NV3709', 'NV3795', 'NV3857', 'NV3984', 'NV3993', 'NV4036', 'NV4052', 'NV4112', 'NV4225', 'NV4257', 'NV4286', 'NV4355', 'NV4526', 'NV4590', 'NV4602', 'NV4739', 'NV4867', 'NV4906', 'NV5031', 'NV5136', 'NV5170', 'NV5194', 'NV5594', 'NV5604', 'NV5718', 'NV5775', 'NV5849', 'NV5918', 'NV6036', 'NV6406', 'NV6411', 'NV6419', 'NV6510', 'NV6562', 'NV6643', 'NV6713', 'NV6786', 'NV6789', 'NV7040', 'NV7171', 'NV7197', 'NV7288', 'NV7466', 'NV7528', 'NV7556', 'NV7597', 'NV7743', 'NV7788', 'NV7803', 'NV7947', 'NV8058', 'NV8112', 'NV8120', 'NV8207', 'NV8278', 'NV8291', 'NV8481', 'NV8680', 'NV8703', 'NV8795', 'NV8815', 'NV8937', 'NV8938', 'NV8971', 'NV9119', 'NV9225', 'NV9229', 'NV9405', 'NV9433', 'NV9548', 'NV9574', 'NV9606', 'NV9648', 'NV9676', 'NV9714', 'NV9750', 'NV9858', 'NV9885', 'NV9964', 'NV9979')
states = ('Có mặt', 'Vắng có phép', 'Vắng không phép')
# bangchamcong(`MaNV`, `Ngay`, `TrangThai`)
# for ft_emp_id in ft_emp_ids:
#     for date in dates:
#         if random.randint(0, 9) == 8:
#             print(f'(\'{ft_emp_id}\', \'{date}\', \'Vắng không phép\'),')
#         elif random.randint(0, 9) == 9:
#             print(f'(\'{ft_emp_id}\', \'{date}\', \'Vắng có phép\'),')
#         else:
#             print(f'(\'{ft_emp_id}\', \'{date}\', \'Có mặt\'),')
            

# print(len(dates_2))

# print("Vắng không phép")
pt_emp_ids = (
    'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1108', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1252', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV1540', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2099', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2231', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2553', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2689', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2790', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV2977', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3140', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3184', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3300', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3728', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV3981', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV4620', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5192', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5235', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5324', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5474', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5494', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5858', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5859', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV5896', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6043', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6160', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6164', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6256', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6452', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV6475', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7327', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7733', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7938', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV7994', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8049', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8084', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8232', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8348', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8519', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8594', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8801', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV8929', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9007', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9022', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9115', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9199', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9240', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9273', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9375', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9741', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983', 'NV9983')

date_2 = (
    '2024-10-22', '2024-10-29', '2024-11-01', '2024-11-04', '2024-11-05', '2024-11-07', '2024-11-11', '2024-11-14', '2024-11-15', '2024-11-18', '2024-11-19', '2024-11-20', '2024-11-21', '2024-11-26', '2024-11-27', '2024-11-28', '2024-12-06', '2024-12-09', '2024-12-10', '2024-12-11', '2024-12-16', '2024-12-17', '2024-12-19', '2024-12-23', '2024-12-24', '2024-12-25', '2024-10-21', '2024-10-23', '2024-10-24', '2024-10-29', '2024-11-01', '2024-11-04', '2024-11-06', '2024-11-08', '2024-11-12', '2024-11-15', '2024-11-18', '2024-11-19', '2024-11-22', '2024-11-25', '2024-11-26', '2024-11-27', '2024-11-28', '2024-12-02', '2024-12-04', '2024-12-10', '2024-12-12', '2024-12-16', '2024-12-18', '2024-12-24', '2024-12-25', '2024-12-26', '2024-12-27', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-29', '2024-10-30', '2024-11-04', '2024-11-07', '2024-11-08', '2024-11-11', '2024-11-12', '2024-11-13', '2024-11-14', '2024-11-25', '2024-11-26', '2024-11-28', '2024-11-29', '2024-12-03', '2024-12-05', '2024-12-06', '2024-12-09', '2024-12-10', '2024-12-11', '2024-12-13', '2024-12-16', '2024-12-17', '2024-12-19', '2024-12-23', '2024-12-24', '2024-12-26', '2024-10-25', '2024-10-28', '2024-11-04', '2024-11-08', '2024-11-11', '2024-11-12', '2024-11-13', '2024-11-15', '2024-11-27', '2024-11-29', '2024-12-09', '2024-12-10', '2024-12-11', '2024-12-17', '2024-12-19', '2024-12-20', '2024-12-25', '2024-12-26', '2024-10-22', '2024-10-23', '2024-10-28', '2024-10-30', '2024-10-31', '2024-11-04', '2024-11-05', '2024-11-11', '2024-11-13', '2024-11-15', '2024-11-18', '2024-11-20', '2024-11-21', '2024-11-22', '2024-11-26', '2024-11-29', '2024-12-02', '2024-12-03', '2024-12-04', '2024-12-06', '2024-12-10', '2024-12-16', '2024-12-17', '2024-12-20', '2024-12-23', '2024-12-25', '2024-12-27', '2024-10-24', '2024-10-28', '2024-11-04', '2024-11-05', '2024-11-06', '2024-11-07', '2024-11-08', '2024-11-12', '2024-11-14', '2024-11-15', '2024-11-18', '2024-11-19', '2024-11-21', '2024-11-26', '2024-11-27', '2024-12-03', '2024-12-05', '2024-12-10', '2024-12-12', '2024-12-13', '2024-12-16', '2024-12-17', '2024-12-18', '2024-12-19', '2024-12-20', '2024-12-27', '2024-10-22', '2024-10-24', '2024-10-25', '2024-10-30', '2024-10-31', '2024-11-01', '2024-11-04', '2024-11-05', '2024-11-08', '2024-11-11', '2024-11-14', '2024-11-19', '2024-11-20', '2024-11-21', '2024-11-22', '2024-11-25', '2024-11-28', '2024-12-02', '2024-12-03', '2024-12-05', '2024-12-06', '2024-12-09', '2024-12-10', '2024-12-11', '2024-12-16', '2024-12-23', '2024-12-25', '2024-12-27', '2024-10-21', '2024-10-23', '2024-10-28', '2024-10-30', '2024-10-31', '2024-11-01', '2024-11-05', '2024-11-06', '2024-11-08', '2024-11-11', '2024-11-13', '2024-11-18', '2024-11-21', '2024-11-25', '2024-11-27', '2024-11-28', '2024-11-29', '2024-12-03', '2024-12-06', '2024-12-09', '2024-12-12', '2024-12-17', '2024-12-18', '2024-12-20', '2024-12-24', '2024-12-26', '2024-10-22', '2024-10-31', '2024-11-01', '2024-11-06', '2024-11-07', '2024-11-11', '2024-11-14', '2024-11-18', '2024-11-20', '2024-11-22', '2024-11-25', '2024-11-28', '2024-12-04', '2024-12-12', '2024-12-18', '2024-12-19', '2024-12-20', '2024-12-24', '2024-12-26', '2024-12-27', '2024-10-21', '2024-10-24', '2024-10-25', '2024-10-31', '2024-11-07', '2024-11-12', '2024-11-14', '2024-11-19', '2024-11-21', '2024-11-22', '2024-11-25', '2024-11-26', '2024-11-27', '2024-12-04', '2024-12-05', '2024-12-09', '2024-12-12', '2024-12-16', '2024-12-17', '2024-12-23', '2024-12-24', '2024-12-27', '2024-10-22', '2024-10-30', '2024-10-31', '2024-11-01', '2024-11-05', '2024-11-06', '2024-11-14', '2024-11-15', '2024-11-20', '2024-11-22', '2024-11-27', '2024-11-29', '2024-12-02', '2024-12-03', '2024-12-05', '2024-12-12', '2024-12-13', '2024-12-16', '2024-12-17', '2024-12-23', '2024-12-24', '2024-12-25', '2024-12-27', '2024-10-21', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-25', '2024-10-28', '2024-10-29', '2024-10-30', '2024-10-31', '2024-11-01', '2024-11-04', '2024-11-05', '2024-11-07', '2024-11-08', '2024-11-12', '2024-11-14', '2024-11-21', '2024-11-22', '2024-11-25', '2024-11-27', '2024-11-29', '2024-12-05', '2024-12-06', '2024-12-13', '2024-12-17', '2024-12-18', '2024-12-19', '2024-12-24', '2024-12-25', '2024-10-23', '2024-10-24', '2024-11-04', '2024-11-06', '2024-11-12', '2024-11-13', '2024-11-19', '2024-11-20', '2024-11-21', '2024-11-25', '2024-11-26', '2024-11-27', '2024-11-28', '2024-11-29', '2024-12-09', '2024-12-13', '2024-12-16', '2024-12-18', '2024-12-20', '2024-12-23', '2024-12-24', '2024-12-26', '2024-12-27', '2024-10-22', '2024-10-24', '2024-10-25', '2024-10-29', '2024-10-30', '2024-10-31', '2024-11-01', '2024-11-04', '2024-11-06', '2024-11-12', '2024-11-13', '2024-11-18', '2024-11-19', '2024-11-22', '2024-11-25', '2024-11-26', '2024-12-03', '2024-12-04', '2024-12-05', '2024-12-06', '2024-12-10', '2024-12-11', '2024-12-12', '2024-12-13', '2024-12-17', '2024-12-19', '2024-12-20', '2024-12-24', '2024-12-26', '2024-10-21', '2024-10-28', '2024-10-29', '2024-10-30', '2024-11-01', '2024-11-05', '2024-11-07', '2024-11-11', '2024-11-14', '2024-11-15', '2024-11-18', '2024-11-19', '2024-11-20', '2024-11-22', '2024-11-27', '2024-11-28', '2024-12-02', '2024-12-09', '2024-12-10', '2024-12-13', '2024-12-16', '2024-12-19', '2024-12-25', '2024-10-21', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-25', '2024-10-28', '2024-10-30', '2024-10-31', '2024-11-05', '2024-11-06', '2024-11-12', '2024-11-13', '2024-11-14', '2024-11-15', '2024-11-18', '2024-11-26', '2024-11-27', '2024-12-03', '2024-12-09', '2024-12-12', '2024-12-13', '2024-12-16', '2024-12-23', '2024-12-24', '2024-12-26', '2024-10-21', '2024-10-22', '2024-10-23', '2024-10-30', '2024-10-31', '2024-11-01', '2024-11-05', '2024-11-08', '2024-11-12', '2024-11-13', '2024-11-14', '2024-11-18', '2024-11-20', '2024-11-22', '2024-11-25', '2024-11-26', '2024-11-27', '2024-11-28', '2024-12-05', '2024-12-09', '2024-12-10', '2024-12-13', '2024-12-24', '2024-12-27', '2024-10-21', '2024-10-22', '2024-10-24', '2024-10-30', '2024-10-31', '2024-11-04', '2024-11-05', '2024-11-08', '2024-11-12', '2024-11-14', '2024-11-15', '2024-11-19', '2024-11-27', '2024-12-02', '2024-12-06', '2024-12-09', '2024-12-10', '2024-12-13', '2024-12-17', '2024-12-20', '2024-12-23', '2024-12-24', '2024-12-25', '2024-12-27', '2024-10-21', '2024-10-23', '2024-10-24', '2024-10-30', '2024-10-31', '2024-11-01', '2024-11-05', '2024-11-06', '2024-11-08', '2024-11-12', '2024-11-19', '2024-11-20', '2024-11-21', '2024-11-29', '2024-12-02', '2024-12-05', '2024-12-06', '2024-12-09', '2024-12-17', '2024-12-18', '2024-12-24', '2024-12-25', '2024-12-26', '2024-12-27', '2024-10-21', '2024-10-25', '2024-10-28', '2024-10-29', '2024-10-31', '2024-11-01', '2024-11-05', '2024-11-08', '2024-11-14', '2024-11-27', '2024-11-29', '2024-12-02', '2024-12-05', '2024-12-06', '2024-12-09', '2024-12-11', '2024-12-16', '2024-12-20', '2024-12-23', '2024-10-21', '2024-10-23', '2024-10-24', '2024-10-28', '2024-10-29', '2024-11-01', '2024-11-05', '2024-11-06', '2024-11-08', '2024-11-11', '2024-11-14', '2024-11-18', '2024-11-19', '2024-11-21', '2024-11-25', '2024-11-26', '2024-12-02', '2024-12-03', '2024-12-04', '2024-12-06', '2024-12-10', '2024-12-13', '2024-12-24', '2024-12-25', '2024-12-27', '2024-10-21', '2024-10-24', '2024-10-28', '2024-11-04', '2024-11-05', '2024-11-08', '2024-11-11', '2024-11-12', '2024-11-18', '2024-11-19', '2024-11-20', '2024-11-21', '2024-11-22', '2024-11-25', '2024-11-26', '2024-11-27', '2024-11-29', '2024-12-03', '2024-12-04', '2024-12-05', '2024-12-06', '2024-12-09', '2024-12-13', '2024-12-16', '2024-12-20', '2024-12-24', '2024-12-26', '2024-10-21', '2024-10-23', '2024-10-25', '2024-10-28', '2024-10-29', '2024-10-30', '2024-11-01', '2024-11-04', '2024-11-06', '2024-11-08', '2024-11-11', '2024-11-12', '2024-11-13', '2024-11-14', '2024-11-15', '2024-11-18', '2024-11-19', '2024-11-20', '2024-12-09', '2024-12-12', '2024-12-13', '2024-12-16', '2024-12-19', '2024-12-23', '2024-12-25', '2024-12-26', '2024-12-27', '2024-10-21', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-28', '2024-10-29', '2024-10-30', '2024-10-31', '2024-11-05', '2024-11-13', '2024-11-14', '2024-11-18', '2024-11-21', '2024-11-25', '2024-11-27', '2024-11-28', '2024-11-29', '2024-12-03', '2024-12-04', '2024-12-05', '2024-12-06', '2024-12-10', '2024-12-18', '2024-12-19', '2024-12-20', '2024-12-26', '2024-12-27', '2024-10-21', '2024-10-22', '2024-10-23', '2024-10-25', '2024-10-29', '2024-11-01', '2024-11-04', '2024-11-06', '2024-11-08', '2024-11-11', '2024-11-15', '2024-11-18', '2024-11-19', '2024-11-21', '2024-11-22', '2024-11-27', '2024-11-28', '2024-12-02', '2024-12-03', '2024-12-05', '2024-12-09', '2024-12-11', '2024-12-13', '2024-12-17', '2024-12-19', '2024-12-25', '2024-12-27', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-25', '2024-10-28', '2024-10-29', '2024-10-31', '2024-11-01', '2024-11-04', '2024-11-05', '2024-11-07', '2024-11-08', '2024-11-12', '2024-11-13', '2024-11-14', '2024-11-20', '2024-11-22', '2024-11-26', '2024-11-27', '2024-12-02', '2024-12-04', '2024-12-05', '2024-12-11', '2024-12-12', '2024-12-13', '2024-12-17', '2024-12-18', '2024-12-24', '2024-12-26', '2024-10-22', '2024-10-28', '2024-11-04', '2024-11-05', '2024-11-11', '2024-11-15', '2024-11-19', '2024-11-25', '2024-11-27', '2024-12-03', '2024-12-06', '2024-12-10', '2024-12-13', '2024-12-19', '2024-12-20', '2024-12-23', '2024-12-25', '2024-12-26', '2024-10-22', '2024-10-23', '2024-10-25', '2024-10-28', '2024-10-30', '2024-11-01', '2024-11-04', '2024-11-08', '2024-11-14', '2024-11-15', '2024-11-18', '2024-11-22', '2024-11-26', '2024-11-29', '2024-12-02', '2024-12-04', '2024-12-05', '2024-12-06', '2024-12-10', '2024-12-11', '2024-12-12', '2024-12-13', '2024-12-18', '2024-12-27', '2024-10-22', '2024-10-23', '2024-10-25', '2024-10-29', '2024-10-30', '2024-10-31', '2024-11-04', '2024-11-07', '2024-11-12', '2024-11-13', '2024-11-14', '2024-11-19', '2024-11-28', '2024-11-29', '2024-12-03', '2024-12-05', '2024-12-06', '2024-12-09', '2024-12-11', '2024-12-16', '2024-12-18', '2024-12-20', '2024-12-23', '2024-12-24', '2024-12-25', '2024-10-23', '2024-10-28', '2024-10-29', '2024-10-30', '2024-10-31', '2024-11-05', '2024-11-06', '2024-11-08', '2024-11-15', '2024-11-18', '2024-11-20', '2024-11-21', '2024-11-22', '2024-11-25', '2024-11-26', '2024-11-27', '2024-12-02', '2024-12-04', '2024-12-10', '2024-12-12', '2024-12-16', '2024-12-17', '2024-12-23', '2024-12-25', '2024-12-26', '2024-10-21', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-30', '2024-11-01', '2024-11-04', '2024-11-05', '2024-11-06', '2024-11-07', '2024-11-08', '2024-11-12', '2024-11-13', '2024-11-18', '2024-11-19', '2024-11-20', '2024-11-21', '2024-11-22', '2024-11-27', '2024-11-29', '2024-12-04', '2024-12-05', '2024-12-06', '2024-12-09', '2024-12-11', '2024-12-16', '2024-12-17', '2024-12-18', '2024-12-24', '2024-12-27', '2024-10-21', '2024-10-22', '2024-10-28', '2024-11-01', '2024-11-04', '2024-11-07', '2024-11-11', '2024-11-13', '2024-11-14', '2024-11-15', '2024-11-21', '2024-11-25', '2024-11-27', '2024-12-03', '2024-12-05', '2024-12-10', '2024-12-13', '2024-12-16', '2024-12-17', '2024-12-18', '2024-12-19', '2024-12-27', '2024-10-21', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-25', '2024-10-31', '2024-11-01', '2024-11-05', '2024-11-06', '2024-11-07', '2024-11-11', '2024-11-13', '2024-11-21', '2024-11-25', '2024-11-29', '2024-12-09', '2024-12-11', '2024-12-16', '2024-12-17', '2024-12-18', '2024-12-20', '2024-10-22', '2024-10-23', '2024-10-28', '2024-10-29', '2024-10-30', '2024-10-31', '2024-11-06', '2024-11-07', '2024-11-11', '2024-11-20', '2024-11-25', '2024-11-27', '2024-12-02', '2024-12-11', '2024-12-13', '2024-12-17', '2024-12-20', '2024-12-23', '2024-12-27', '2024-10-21', '2024-10-22', '2024-10-23', '2024-10-25', '2024-10-31', '2024-11-01', '2024-11-06', '2024-11-08', '2024-11-11', '2024-11-12', '2024-11-15', '2024-11-18', '2024-11-19', '2024-11-21', '2024-11-22', '2024-11-25', '2024-11-28', '2024-11-29', '2024-12-03', '2024-12-04', '2024-12-05', '2024-12-11', '2024-12-17', '2024-12-18', '2024-12-20', '2024-12-25', '2024-12-27', '2024-10-25', '2024-10-29', '2024-10-31', '2024-11-01', '2024-11-05', '2024-11-06', '2024-11-11', '2024-11-21', '2024-11-25', '2024-11-26', '2024-11-27', '2024-12-02', '2024-12-03', '2024-12-06', '2024-12-12', '2024-12-13', '2024-12-17', '2024-12-18', '2024-12-20', '2024-12-24', '2024-12-25', '2024-12-26', '2024-10-23', '2024-10-24', '2024-10-28', '2024-10-29', '2024-10-30', '2024-11-04', '2024-11-05', '2024-11-08', '2024-11-11', '2024-11-12', '2024-11-15', '2024-11-18', '2024-11-22', '2024-11-25', '2024-11-29', '2024-12-02', '2024-12-03', '2024-12-05', '2024-12-09', '2024-12-16', '2024-12-18', '2024-12-19', '2024-12-24', '2024-12-25', '2024-12-27', '2024-10-22', '2024-10-24', '2024-10-25', '2024-10-28', '2024-10-30', '2024-11-04', '2024-11-05', '2024-11-07', '2024-11-13', '2024-11-14', '2024-11-15', '2024-11-19', '2024-11-26', '2024-11-27', '2024-12-02', '2024-12-05', '2024-12-06', '2024-12-11', '2024-12-13', '2024-12-16', '2024-12-18', '2024-12-19', '2024-12-20', '2024-12-23', '2024-12-24', '2024-12-26', '2024-10-23', '2024-10-24', '2024-10-25', '2024-10-28', '2024-10-29', '2024-11-01', '2024-11-05', '2024-11-07', '2024-11-08', '2024-11-11', '2024-11-15', '2024-11-19', '2024-11-21', '2024-11-22', '2024-11-28', '2024-11-29', '2024-12-02', '2024-12-05', '2024-12-06', '2024-12-10', '2024-12-12', '2024-12-17', '2024-12-19', '2024-12-20', '2024-12-23', '2024-12-26', '2024-10-25', '2024-10-30', '2024-11-01', '2024-11-05', '2024-11-06', '2024-11-08', '2024-11-19', '2024-11-21', '2024-11-27', '2024-12-02', '2024-12-03', '2024-12-04', '2024-12-09', '2024-12-10', '2024-12-11', '2024-12-12', '2024-12-13', '2024-12-17', '2024-12-18', '2024-12-20', '2024-12-23', '2024-12-24', '2024-12-27', '2024-10-21', '2024-10-22', '2024-10-23', '2024-10-31', '2024-11-01', '2024-11-04', '2024-11-11', '2024-11-12', '2024-11-14', '2024-11-15', '2024-11-18', '2024-11-25', '2024-11-29', '2024-12-02', '2024-12-04', '2024-12-09', '2024-12-11', '2024-12-13', '2024-12-16', '2024-12-17', '2024-12-18', '2024-12-20', '2024-12-24', '2024-12-25', '2024-12-27', '2024-10-21', '2024-10-23', '2024-10-28', '2024-10-29', '2024-10-30', '2024-11-04', '2024-11-05', '2024-11-06', '2024-11-12', '2024-11-15', '2024-11-18', '2024-11-19', '2024-11-26', '2024-11-28', '2024-11-29', '2024-12-02', '2024-12-03', '2024-12-05', '2024-12-10', '2024-12-11', '2024-12-12', '2024-12-13', '2024-12-16', '2024-12-17', '2024-12-18', '2024-12-19', '2024-12-20', '2024-12-24', '2024-12-25', '2024-12-26', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-25', '2024-10-30', '2024-10-31', '2024-11-04', '2024-11-11', '2024-11-13', '2024-11-19', '2024-11-20', '2024-11-22', '2024-11-26', '2024-11-29', '2024-12-04', '2024-12-06', '2024-12-09', '2024-12-13', '2024-12-18', '2024-12-19', '2024-12-23', '2024-12-25', '2024-10-21', '2024-10-22', '2024-10-25', '2024-10-28', '2024-10-29', '2024-10-31', '2024-11-01', '2024-11-04', '2024-11-06', '2024-11-07', '2024-11-11', '2024-11-12', '2024-11-13', '2024-11-14', '2024-11-15', '2024-11-21', '2024-11-26', '2024-11-27', '2024-11-29', '2024-12-02', '2024-12-03', '2024-12-06', '2024-12-09', '2024-12-11', '2024-12-13', '2024-12-16', '2024-12-18', '2024-12-19', '2024-12-20', '2024-12-25', '2024-12-26', '2024-12-27', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-25', '2024-10-30', '2024-11-04', '2024-11-05', '2024-11-06', '2024-11-12', '2024-11-13', '2024-11-20', '2024-11-21', '2024-11-22', '2024-11-26', '2024-11-27', '2024-12-02', '2024-12-04', '2024-12-09', '2024-12-11', '2024-12-12', '2024-12-16', '2024-12-17', '2024-12-23', '2024-12-25', '2024-10-21', '2024-11-01', '2024-11-06', '2024-11-07', '2024-11-11', '2024-11-12', '2024-11-14', '2024-11-15', '2024-11-20', '2024-11-26', '2024-11-28', '2024-11-29', '2024-12-03', '2024-12-06', '2024-12-09', '2024-12-11', '2024-12-12', '2024-12-16', '2024-12-17', '2024-12-20', '2024-12-26', '2024-10-22', '2024-10-23', '2024-10-24', '2024-10-31', '2024-11-01', '2024-11-04', '2024-11-05', '2024-11-08', '2024-11-11', '2024-11-13', '2024-11-14', '2024-11-15', '2024-11-18', '2024-11-19', '2024-11-20', '2024-11-25', '2024-11-26', '2024-12-04', '2024-12-05', '2024-12-09', '2024-12-16', '2024-12-17', '2024-12-18', '2024-12-20', '2024-12-23', '2024-12-25', '2024-12-27', '2024-10-22', '2024-10-25', '2024-10-28', '2024-10-29', '2024-10-30', '2024-10-31', '2024-11-05', '2024-11-06', '2024-11-08', '2024-11-12', '2024-11-18', '2024-11-22', '2024-11-27', '2024-11-28', '2024-12-04', '2024-12-06', '2024-12-10', '2024-12-16', '2024-12-17', '2024-12-18', '2024-12-19', '2024-12-23', '2024-12-24', '2024-12-25', '2024-12-26', '2024-12-27', '2024-10-21', '2024-10-22', '2024-11-01', '2024-11-04', '2024-11-13', '2024-11-15', '2024-11-21', '2024-12-03', '2024-12-06', '2024-12-09', '2024-12-10', '2024-12-16', '2024-12-17', '2024-12-23', '2024-12-25', '2024-12-26', '2024-10-22', '2024-10-23', '2024-10-25', '2024-10-31', '2024-11-04', '2024-11-07', '2024-11-11', '2024-11-13', '2024-11-14', '2024-11-15', '2024-11-19', '2024-11-20', '2024-11-21', '2024-11-22', '2024-11-26', '2024-11-27', '2024-11-28', '2024-11-29', '2024-12-02', '2024-12-04', '2024-12-05', '2024-12-09', '2024-12-11', '2024-12-13', '2024-12-17', '2024-12-20', '2024-12-27')

with open('./out.txt', 'w', encoding='utf-8') as f:
    for pt_emp_id, date in zip(pt_emp_ids, date_2):
        if random.randint(0, 9) == 8:
            f.write(f'(\'{pt_emp_id}\', \'{date}\', \'Vắng không phép\'),\n')
        elif random.randint(0, 9) == 9:
            f.write(f'(\'{pt_emp_id}\', \'{date}\', \'Vắng có phép\'),\n')
        else:
            f.write(f'(\'{pt_emp_id}\', \'{date}\', \'Có mặt\'),\n')
    