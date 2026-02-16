
import os
import shutil

rename_map = {
    "43-荒地.py": "wasteland.py",
    "44-数组连续和.py": "continuous_subarray_sum.py",
    "45-完美走位.py": "perfect_move.py",
    "46-垃圾短信识别.py": "spam_sms_identification.py",
    "47-挑选字符串.py": "pick_strings.py",
    "48-敏感字段加密.py": "sensitive_field_encryption.py",
    "49-水库溃坝填补.py": "dam_filling.py",
    "50-单核 CPU 调度.py": "single_core_cpu_scheduling.py",
    "51-网上商城优惠活动.py": "online_mall_promotions.py",
    "52-异常的打卡记录.py": "abnormal_attendance_records.py",
    "53-挑选宝石.py": "picking_gems.py",
    "54-任务编排系统.py": "task_orchestration_system.py",
    "55-分苹果.py": "splitting_apples.py",
    "56-统计设计比赛成绩.py": "calculate_competition_score.py",
    "57-热点网站统计.py": "hot_website_statistics.py",
    "58-组装新数组.py": "assemble_new_array.py",
    "59-最长的密码.py": "longest_password.py",
    "60-停车场费用统计.py": "parking_lot_fee_calculation.py",
    "61-国际移动用户识别码(IMSI)匹配.py": "imsi_matching.py",
    "62-去除多余空格.py": "remove_extra_spaces.py",
    "63-恢复数字序列.py": "restore_numeric_sequence.py",
    "64-机器人活动区域.py": "robot_activity_area.py",
    "65-图像坏点矫正.py": "image_defect_correction.py",
    "66-计算误码率.py": "calculate_error_rate.py",
    "67-流水线调度.py": "pipeline_scheduling.py",
    "68-风险投资计划.py": "venture_capital_plan.py",
    "69-最佳升级时间窗.py": "optimal_upgrade_window.py",
    "70-贪吃的猴子.py": "greedy_monkey.py",
    "71-零食奖励.py": "snack_reward.py",
    "72-跳格子1.py": "jump_grid_1.py",
    "73-结对编程.py": "pair_programming.py",
    "74-幸存数之和.py": "surviving_numbers_sum.py",
    "75-分解正整数.py": "integer_factorization.py",
    "76-部门人力分配.py": "department_manpower_allocation.py",
    "77-阿里巴巴找黄金宝箱.py": "alibaba_find_golden_chest.py",
    "78-约瑟夫问题.py": "josephus_problem.py",
    "79-分月饼.py": "distribute_mooncakes.py",
    "80-流量波峰.py": "traffic_peak_80.py",
    "两个字符串间的最短路径问题.py": "shortest_path_between_strings.py",
    "二维伞的雨滴效应.py": "raindrop_effect_2d_umbrella.py",
    "优雅子数组.py": "elegant_subarray.py",
    "卡牌游戏.py": "card_game.py",
    "压缩查询日志.py": "compress_query_logs.py",
    "叠积木.py": "stack_blocks.py",
    "员工派遣.py": "employee_dispatch.py",
    "垂直四子棋.py": "vertical_connect_four.py",
    "字符串计数匹配.py": "string_count_matching.py",
    "宜居星球改造计划.py": "habitable_planet_terraforming.py",
    "小明减肥.py": "xiaoming_weight_loss.py",
    "微服务的集成测试.py": "microservice_integration_test.py",
    "总最快检测效率.py": "total_fastest_detection_efficiency.py",
    "手机app防沉迷系统.py": "app_addiction_prevention.py",
    "打印机队列.py": "printer_queue.py",
    "推荐多样性.py": "recommendation_diversity.py",
    "整数编码.py": "integer_encoding.py",
    "文件存储系统的排序.py": "file_storage_system_sorting.py",
    "最佳信号覆盖.py": "optimal_signal_coverage.py",
    "最大社交距离.py": "maximum_social_distance.py",
    "最小矩阵宽度.py": "minimum_matrix_width.py",
    "最长的顺子.py": "longest_sequence.py",
    "朋友圈个数.py": "number_of_friend_circles.py",
    "构成正方形的数量.py": "count_squares.py",
    "查找接口成功率最优时间段.py": "find_optimal_interface_success_rate_period.py",
    "模拟目录管理.py": "simulate_directory_management.py",
    "水库蓄水.py": "reservoir_water_storage.py",
    "版本管理.py": "version_management.py",
    "猜数字.py": "guess_number.py",
    "矩形绘制.py": "rectangle_drawing.py",
    "符号运算.py": "symbolic_arithmetic.py",
    "组装最大可靠性装备.py": "assemble_max_reliability_equipment.py",
    "绘图机器.py": "drawing_machine.py",
    "编程能力提升计划.py": "coding_skill_improvement_plan.py",
    "网格红绿灯最短路径.py": "grid_traffic_light_shortest_path.py",
    "螺旋数字矩阵.py": "spiral_number_matrix.py",
    "补种未存活胡杨.py": "replant_unsurvived_poplar_trees.py",
    "评委评分_比赛.PY": "judge_scoring_competition.py",
    "运维日志排序.py": "ops_log_sorting.py",
    "连续数组和.py": "continuous_array_sum.py",
    "采购订单.py": "purchase_order.py",
    "高矮个子排队.py": "tall_short_people_queue.py"
}

base_dir = "Group-C"
if not os.path.exists(base_dir):
    print(f"Directory {base_dir} not found.")
    exit(1)

for old_name, new_name in rename_map.items():
    old_path = os.path.join(base_dir, old_name)
    new_path = os.path.join(base_dir, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found: {old_name}")
