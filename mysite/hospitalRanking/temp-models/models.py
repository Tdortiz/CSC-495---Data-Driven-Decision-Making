from django.db import models

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Ambulatory Surgical Measures-State.csv
class AmbulatorySurgicalMeasures_State(models.Model):
    state = models.CharField(default='', max_length=2, null=False, primary_key=True, blank=False)
    year = models.IntegerField(default=0, null=True, blank=True)
    asc1_measure_state_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    asc2_measure_state_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    asc3_measure_state_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    asc4_measure_state_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    asc5_measure_state_rate = models.DecimalField(default=0, null=True, max_digits=6, decimal_places=3, blank=True)
    asc_6_state_pct = models.IntegerField(default=0, null=True, blank=True)
    avg_asc_7_state = models.IntegerField(default=0, null=True, blank=True)
    avg_gastrointestinal_state = models.IntegerField(default=0, null=True, blank=True)
    avg_eye_state = models.IntegerField(default=0, null=True, blank=True)
    avg_genitourinary_state = models.IntegerField(default=0, null=True, blank=True)
    avg_multi_system_state = models.IntegerField(default=0, null=True, blank=True)
    avg_musculoskeletal_state = models.IntegerField(default=0, null=True, blank=True)
    avg_nervous_system_state = models.IntegerField(default=0, null=True, blank=True)
    avg_respiratory_state = models.IntegerField(default=0, null=True, blank=True)
    avg_skin_state = models.IntegerField(default=0, null=True, blank=True)
    avg_asc_8_state_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    avg_asc_9_state_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    avg_asc_10_state_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    avg_asc_11_state_rate = models.DecimalField(default=0, null=True, max_digits=7, decimal_places=3, blank=True)
    median_asc_7_state = models.IntegerField(default=0, null=True, blank=True)
    median_gastrointestinal_state = models.IntegerField(default=0, null=True, blank=True)
    median_eye_state = models.IntegerField(default=0, null=True, blank=True)
    median_genitourinary_state = models.IntegerField(default=0, null=True, blank=True)
    median_multi_system_state = models.IntegerField(default=0, null=True, blank=True)
    median_musculoskeletal_state = models.IntegerField(default=0, null=True, blank=True)
    median_nervous_system_state = models.IntegerField(default=0, null=True, blank=True)
    median_respiratory_state = models.IntegerField(default=0, null=True, blank=True)
    median_skin_state = models.IntegerField(default=0, null=True, blank=True)
    median_asc_8_state_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    median_asc_9_state_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    median_asc_10_state_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    median_asc_11_state_rate = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"AmbulatorySurgicalMeasures_State"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HOSPITAL_QUARTERLY_QUALITYMEASURE_PCH_HCAHPS_NATIONAL.csv
class HCAHPS_National(models.Model):
    hcahps_measure_id = models.CharField(default='', max_length=222, null=False, primary_key=True, blank=False)
    hcahps_question = models.CharField(null=True, blank=True, max_length=200)
    hcahps_answer_description = models.CharField(default='', max_length=247, blank=True)
    hcahps_answer_percent = models.IntegerField(default=0, null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"HCAHPS_National"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/FY2015_Percent_Change_in_Medicare_Payments.csv
class Percent_Change_in_Medicare_Payments(models.Model):
    percent_change_in_base_operating_drg_payment_amount = models.CharField(default='', max_length=235, null=False, primary_key=True, blank=False)
    number_of_hospitals_receiving_this_change = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"Percent_Change_in_Medicare_Payments"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Ambulatory Surgical Measures-National.csv
class AmbulatorySurgicalMeasures_National(models.Model):
    year = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    asc1_measure_nat_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    asc2_measure_nat_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    asc3_measure_nat_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    asc4_measure_nat_rate = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    asc5_measure_nat_rate = models.DecimalField(default=0, null=True, max_digits=6, decimal_places=3, blank=True)
    asc_6_nat_pct = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    avg_asc_7_nat = models.IntegerField(default=0, null=True, blank=True)
    avg_gastrointestinal_nat = models.IntegerField(default=0, null=True, blank=True)
    avg_eye_nat = models.IntegerField(default=0, null=True, blank=True)
    avg_genitourinary_nat = models.IntegerField(default=0, null=True, blank=True)
    avg_multi_system_nat = models.IntegerField(default=0, null=True, blank=True)
    avg_musculoskeletal_nat = models.IntegerField(default=0, null=True, blank=True)
    avg_nervous_system_nat = models.IntegerField(default=0, null=True, blank=True)
    avg_respiratory_nat = models.IntegerField(default=0, null=True, blank=True)
    avg_skin_nat = models.IntegerField(default=0, null=True, blank=True)
    avg_asc_8_nat_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    avg_asc_9_nat_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    avg_asc_10_nat_rate = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    avg_asc_11_nat_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    median_asc_7_nat = models.IntegerField(default=0, null=True, blank=True)
    median_gastrointestinal_nat = models.IntegerField(default=0, null=True, blank=True)
    median_eye_nat = models.IntegerField(default=0, null=True, blank=True)
    median_genitourinary_nat = models.IntegerField(default=0, null=True, blank=True)
    median_multi_system_nat = models.IntegerField(default=0, null=True, blank=True)
    median_musculoskeletal_nat = models.IntegerField(default=0, null=True, blank=True)
    median_nervous_system_nat = models.IntegerField(default=0, null=True, blank=True)
    median_respiratory_nat = models.IntegerField(default=0, null=True, blank=True)
    median_skin_nat = models.IntegerField(default=0, null=True, blank=True)
    median_asc_8_nat_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    median_asc_9_nat_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    median_asc_10_nat_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    median_asc_11_nat_rate = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"AmbulatorySurgicalMeasures_National"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/GLOBAL_July2017_05092017.csv
class Csvimport(models.Model):
    provider_id = models.CharField(default='', max_length=6, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=113, blank=True)
    address = models.CharField(default='', max_length=101, blank=True)
    city = models.CharField(default='', max_length=7, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=8, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    condition = models.CharField(default='', max_length=124, blank=True)
    measure_id = models.CharField(default='', max_length=6, blank=True)
    measure_name = models.CharField(default='', max_length=158, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)
    sample = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.CharField(default='', max_length=146, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=9, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Outpatient Imaging Efficiency - Hospital.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:15:38 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.(null=True, blank=True)
    address = models.CharField(default='', max_length=245, blank=True)
    city = models.CharField(default='', max_length=10, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=8, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    measure_id = models.CharField(default='', max_length=5, blank=True)
    measure_name = models.(null=True, blank=True)
    score = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    footnote = models.CharField(default='', max_length=10, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HOSPITAL_QUARTERLY_QUALITYMEASURE_PCH_OCM_HOSPITAL.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:15:43 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=6, blank=True)
    hospital_name = models.(null=True, blank=True)
    hospital_type = models.CharField(default='', max_length=10, blank=True)
    address = models.CharField(default='', max_length=248, blank=True)
    city = models.CharField(default='', max_length=191, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=241, blank=True)
    measure_description = models.(null=True, blank=True)
    hospital_performance = models.IntegerField(default=0, null=True, blank=True)
    denominator = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.IntegerField(default=0, null=True, blank=True)
    rptg_prd_start_dt = models.DateTimeField(null=True, blank=True)
    rptg_prd_end_dt = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Complications and Deaths - Hospital.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:15:45 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=107, blank=True)
    address = models.CharField(default='', max_length=85, blank=True)
    city = models.CharField(default='', max_length=7, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=8, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    measure_name = models.CharField(default='', max_length=125, blank=True)
    measure_id = models.CharField(default='', max_length=83, blank=True)
    compared_to_national = models.CharField(default='', max_length=105, blank=True)
    denominator = models.IntegerField(default=0, null=True, blank=True)
    score = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    lower_estimate = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    higher_estimate = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    footnote = models.CharField(default='', max_length=10, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/hvbp_safety_11_10_2016.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:16:06 2017 '''

    provider_number = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=202, blank=True)
    address = models.CharField(default='', max_length=192, blank=True)
    city = models.CharField(default='', max_length=10, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=10, blank=True)
    psi_90_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    psi_90_benchmark = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    psi_90_baseline_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    psi_90_performance_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    psi_90_achievement_points = models.CharField(default='', max_length=182, blank=True)
    psi_90_improvement_points = models.CharField(default='', max_length=10, blank=True)
    psi_90_measure_score = models.CharField(default='', max_length=182, blank=True)
    hai_1_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    hai_1_benchmark = models.IntegerField(default=0, null=True, blank=True)
    hai_1_baseline_rate = models.DecimalField(default=0, null=True, max_digits=153, decimal_places=10, blank=True)
    hai_1_performance_rate = models.DecimalField(default=0, null=True, max_digits=153, decimal_places=10, blank=True)
    hai_1_achievement_points = models.CharField(default='', max_length=181, blank=True)
    hai_1_improvement_points = models.CharField(default='', max_length=153, blank=True)
    hai_1_measure_score = models.CharField(default='', max_length=181, blank=True)
    hai_2_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    hai_2_benchmark = models.IntegerField(default=0, null=True, blank=True)
    hai_2_baseline_rate = models.DecimalField(default=0, null=True, max_digits=153, decimal_places=10, blank=True)
    hai_2_performance_rate = models.DecimalField(default=0, null=True, max_digits=153, decimal_places=10, blank=True)
    hai_2_achievement_points = models.CharField(default='', max_length=181, blank=True)
    hai_2_improvement_points = models.CharField(default='', max_length=153, blank=True)
    hai_2_measure_score = models.CharField(default='', max_length=181, blank=True)
    combined_ssi_measure_score = models.CharField(default='', max_length=181, blank=True)
    hai_3_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    hai_3_benchmark = models.IntegerField(default=0, null=True, blank=True)
    hai_3_baseline_rate = models.DecimalField(default=0, null=True, max_digits=153, decimal_places=10, blank=True)
    hai_3_performance_rate = models.DecimalField(default=0, null=True, max_digits=153, decimal_places=10, blank=True)
    hai_3_achievement_points = models.CharField(default='', max_length=181, blank=True)
    hai_3_improvement_points = models.CharField(default='', max_length=153, blank=True)
    hai_3_measure_score = models.CharField(default='', max_length=181, blank=True)
    hai_4_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    hai_4_benchmark = models.IntegerField(default=0, null=True, blank=True)
    hai_4_baseline_rate = models.DecimalField(default=0, null=True, max_digits=183, decimal_places=10, blank=True)
    hai_4_performance_rate = models.DecimalField(default=0, null=True, max_digits=173, decimal_places=10, blank=True)
    hai_4_achievement_points = models.CharField(default='', max_length=182, blank=True)
    hai_4_improvement_points = models.CharField(default='', max_length=183, blank=True)
    hai_4_measure_score = models.CharField(default='', max_length=182, blank=True)
    hai_5_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    hai_5_benchmark = models.IntegerField(default=0, null=True, blank=True)
    hai_5_baseline_rate = models.DecimalField(default=0, null=True, max_digits=153, decimal_places=10, blank=True)
    hai_5_performance_rate = models.DecimalField(default=0, null=True, max_digits=153, decimal_places=10, blank=True)
    hai_5_achievement_points = models.CharField(default='', max_length=181, blank=True)
    hai_5_improvement_points = models.CharField(default='', max_length=153, blank=True)
    hai_5_measure_score = models.CharField(default='', max_length=181, blank=True)
    hai_6_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    hai_6_benchmark = models.IntegerField(default=0, null=True, blank=True)
    hai_6_baseline_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    hai_6_performance_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    hai_6_achievement_points = models.CharField(default='', max_length=181, blank=True)
    hai_6_improvement_points = models.CharField(default='', max_length=10, blank=True)
    hai_6_measure_score = models.CharField(default='', max_length=181, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Medicare Hospital Spending per Patient - Hospital.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:16:11 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=250, blank=True)
    address = models.CharField(default='', max_length=225, blank=True)
    city = models.CharField(default='', max_length=163, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=10, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    measure_name = models.(null=True, blank=True)
    measure_id = models.CharField(default='', max_length=6, blank=True)
    score = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    footnote = models.CharField(default='', max_length=10, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HOSPITAL_QUARTERLY_IPFQR_MEASURES_STATE.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:16:20 2017 '''

    state = models.CharField(default='', max_length=2, null=False, primary_key=True, blank=False)
    s_hbips_2_measure_description = models.CharField(default='', max_length=221, blank=True)
    s_hbips_2_overall_rate_per_1000 = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    s_hbips_2_overall_num = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    s_hbips_2_overall_den = models.IntegerField(default=0, null=True, blank=True)
    s_hbips_3_measure_description = models.CharField(default='', max_length=208, blank=True)
    s_hbips_3_overall_rate_per_1000 = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    s_hbips_3_overall_num = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    s_hbips_3_overall_den = models.IntegerField(default=0, null=True, blank=True)
    s_hbips_5_measure_description = models.(null=True, blank=True)
    s_hbips_5_of_total = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_hbips_5_overall_num = models.IntegerField(default=0, null=True, blank=True)
    s_hbips_5_overall_den = models.IntegerField(default=0, null=True, blank=True)
    s_hbips_6_measure_description = models.CharField(default='', max_length=233, blank=True)
    s_hbips_6_of_total = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_hbips_6_overall_num = models.IntegerField(default=0, null=True, blank=True)
    s_hbips_6_overall_den = models.IntegerField(default=0, null=True, blank=True)
    s_hbips_7_measure_description = models.(null=True, blank=True)
    s_hbips_7_overall_of_total = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_hbips_7_overall_num = models.IntegerField(default=0, null=True, blank=True)
    s_hbips_7_overall_den = models.IntegerField(default=0, null=True, blank=True)
    s_sub_1_measure_description = models.CharField(default='', max_length=211, blank=True)
    s_sub_1_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_sub_1_numerator = models.IntegerField(default=0, null=True, blank=True)
    s_sub_1_denominator = models.IntegerField(default=0, null=True, blank=True)
    s_tob_1_measure_description = models.CharField(default='', max_length=211, blank=True)
    s_tob_1_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_tob_1_numerator = models.IntegerField(default=0, null=True, blank=True)
    s_tob_1_denominator = models.IntegerField(default=0, null=True, blank=True)
    s_tob_2_2a_measure_desc = models.CharField(default='', max_length=231, blank=True)
    s_tob_2_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_tob_2_numerator = models.IntegerField(default=0, null=True, blank=True)
    s_tob_2_2a_denominator = models.IntegerField(default=0, null=True, blank=True)
    s_tob_2a_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_tob_2a_numerator = models.IntegerField(default=0, null=True, blank=True)
    s_tob_2_2a_denominator = models.IntegerField(default=0, null=True, blank=True)
    s_peoc_measure_description = models.CharField(default='', max_length=230, blank=True)
    s_peoc_yes_count = models.IntegerField(default=0, null=True, blank=True)
    s_peoc_no_count = models.IntegerField(default=0, null=True, blank=True)
    s_peoc_yes_ = models.DecimalField(default=0, null=True, max_digits=6, decimal_places=3, blank=True)
    s_peoc_no_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_ehr_use_measure_description = models.CharField(default='', max_length=232, blank=True)
    s_ehr_paper_count = models.IntegerField(default=0, null=True, blank=True)
    s_ehr_non_certified_count = models.IntegerField(default=0, null=True, blank=True)
    s_ehr_certified_count = models.IntegerField(default=0, null=True, blank=True)
    s_ehr_paper_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_ehr_non_certified_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_ehr_certified_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_hie_measure_description = models.CharField(default='', max_length=242, blank=True)
    s_hie_yes_count = models.IntegerField(default=0, null=True, blank=True)
    s_hie_no_count = models.IntegerField(default=0, null=True, blank=True)
    s_hie_yes_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_hie_no_ = models.DecimalField(default=0, null=True, max_digits=6, decimal_places=3, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.CharField(default='', max_length=10, blank=True)
    s_fuh_measure_description = models.(null=True, blank=True)
    s_fuh_30_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_fuh_30_numerator = models.IntegerField(default=0, null=True, blank=True)
    s_fuh_30_denominator = models.IntegerField(default=0, null=True, blank=True)
    s_fuh_7_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_fuh_7_numerator = models.IntegerField(default=0, null=True, blank=True)
    s_fuh_7_denominator = models.IntegerField(default=0, null=True, blank=True)
    s_fuh_measure_start_date = models.DateTimeField(null=True, blank=True)
    s_fuh_measure_end_date = models.CharField(default='', max_length=10, blank=True)
    s_imm_2_measure_description = models.CharField(default='', max_length=212, blank=True)
    s_imm_2_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    s_imm_2_numerator = models.IntegerField(default=0, null=True, blank=True)
    s_imm_2_denominator = models.IntegerField(default=0, null=True, blank=True)
    s_hcp_measure_description = models.CharField(default='', max_length=232, blank=True)
    s_hcp_ = models.IntegerField(default=0, null=True, blank=True)
    s_hcp_numerator = models.IntegerField(default=0, null=True, blank=True)
    s_hcp_denominator = models.IntegerField(default=0, null=True, blank=True)
    s_flu_season_start_date = models.DateTimeField(null=True, blank=True)
    s_flu_season_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Timely and Effective Care - Hospital.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:16:26 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=220, blank=True)
    address = models.CharField(default='', max_length=209, blank=True)
    city = models.CharField(default='', max_length=8, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=201, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    condition = models.CharField(default='', max_length=225, blank=True)
    measure_id = models.CharField(default='', max_length=162, blank=True)
    measure_name = models.CharField(default='', max_length=254, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)
    sample = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.(null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/hvbp_imm2_11_10_2016.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:16:32 2017 '''

    provider_number = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=219, blank=True)
    address = models.CharField(default='', max_length=215, blank=True)
    city = models.CharField(default='', max_length=211, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=214, blank=True)
    imm_2_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    imm_2_benchmark = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    imm_2_baseline_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    imm_2_performance_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    imm_2_achievement_points = models.CharField(default='', max_length=211, blank=True)
    imm_2_improvement_points = models.CharField(default='', max_length=10, blank=True)
    imm_2_measure_score = models.CharField(default='', max_length=211, blank=True)
    imm_2_preventive_condition_procedure_score = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/FY2015_Distribution_of_Net_Change_in_Base_Op_DRG_Payment_Amt.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:16:32 2017 '''

    percentile = models.CharField(default='', max_length=4, null=False, primary_key=True, blank=False)
    net_change_in_base_operating_drg_payment_amount = models.CharField(default='', max_length=141, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HOSPITAL_QUARTERLY_MSPB_6_DECIMALS.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:16:32 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=6, blank=True)
    value = models.DecimalField(default=0, null=True, max_digits=9, decimal_places=4, blank=True)
    footnote = models.CharField(default='', max_length=10, blank=True)
    start_date = models.IntegerField(default=0, null=True, blank=True)
    end_date = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/VA_IPSHEP_Jul2017CMS_08MAY17.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:16:38 2017 '''

    provider_id = models.CharField(default='', max_length=6, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=253, blank=True)
    s_add2 = models.CharField(default='', max_length=241, blank=True)
    s_city = models.CharField(default='', max_length=140, blank=True)
    s_state = models.CharField(default='', max_length=2, blank=True)
    s_zip = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=9, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    measure_id = models.CharField(default='', max_length=245, blank=True)
    measure_name = models.(null=True, blank=True)
    survey_question = models.(null=True, blank=True)
    answer_description = models.CharField(default='', max_length=254, blank=True)
    answerpercent = models.IntegerField(default=0, null=True, blank=True)
    numbercompleted = models.IntegerField(default=0, null=True, blank=True)
    responserate = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.IntegerField(default=0, null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Ambulatory Surgical Measures-Facility.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:16:44 2017 '''

    asc_name = models.CharField(default='', max_length=117, null=False, primary_key=True, blank=False)
    provider_id = models.CharField(default='', max_length=10, blank=True)
    npi = models.IntegerField(default=0, null=True, blank=True)
    city = models.CharField(default='', max_length=9, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    year = models.IntegerField(default=0, null=True, blank=True)
    asc_1_measure_rate = models.IntegerField(default=0, null=True, blank=True)
    asc_1_footnote = models.CharField(default='', max_length=10, blank=True)
    asc_2_measure_rate = models.IntegerField(default=0, null=True, blank=True)
    asc_2_footnote = models.CharField(default='', max_length=10, blank=True)
    asc_3_measure_rate = models.IntegerField(default=0, null=True, blank=True)
    asc_3_footnote = models.CharField(default='', max_length=10, blank=True)
    asc_4_measure_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    asc_4_footnote = models.CharField(default='', max_length=10, blank=True)
    asc_5_measure_rate = models.IntegerField(default=0, null=True, blank=True)
    asc_5_footnote = models.CharField(default='', max_length=10, blank=True)
    asc_1_5_encounter_start_date = models.DateTimeField(null=True, blank=True)
    asc_1_5_encounter_end_date = models.CharField(default='', max_length=10, blank=True)
    asc6_sschecklist = models.BooleanField(default=False, null=True, blank=True)
    asc_6_footnote = models.CharField(default='', max_length=7, blank=True)
    asc_7_volume = models.IntegerField(default=0, null=True, blank=True)
    asc_7_gastrointestinal = models.IntegerField(default=0, null=True, blank=True)
    asc_7_eye = models.IntegerField(default=0, null=True, blank=True)
    asc_7_skin = models.IntegerField(default=0, null=True, blank=True)
    asc_7_genitourinary = models.IntegerField(default=0, null=True, blank=True)
    asc_7_musculoskeletal = models.IntegerField(default=0, null=True, blank=True)
    asc_7_multi_system = models.IntegerField(default=0, null=True, blank=True)
    asc_7_nervous_system = models.IntegerField(default=0, null=True, blank=True)
    asc_7_respiratory = models.IntegerField(default=0, null=True, blank=True)
    asc_7_footnote = models.CharField(default='', max_length=7, blank=True)
    asc_6_7_encounter_start_date = models.DateTimeField(null=True, blank=True)
    asc_6_7_encounter_end_date = models.CharField(default='', max_length=10, blank=True)
    asc_8_rate = models.DecimalField(default=0, null=True, max_digits=10, decimal_places=5, blank=True)
    asc_8_footnote = models.CharField(default='', max_length=7, blank=True)
    asc_8_encounter_date = models.CharField(default='', max_length=9, blank=True)
    asc_9_rate = models.DecimalField(default=0, null=True, max_digits=10, decimal_places=5, blank=True)
    asc_9_footnote = models.CharField(default='', max_length=7, blank=True)
    asc_10_rate = models.DecimalField(default=0, null=True, max_digits=10, decimal_places=5, blank=True)
    asc_10_footnote = models.CharField(default='', max_length=7, blank=True)
    asc_9_10_encounter_start_date = models.DateTimeField(null=True, blank=True)
    asc_9_10_encounter_end_date = models.CharField(default='', max_length=10, blank=True)
    asc_11_rate = models.IntegerField(default=0, null=True, blank=True)
    asc_11_footnote = models.CharField(default='', max_length=7, blank=True)
    asc_11_encounter_start_date = models.DateTimeField(null=True, blank=True)
    asc_11_encounter_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HOSPITAL_QUARTERLY_IPFQR_MEASURES_HOSPITAL.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:16:56 2017 '''

    provider_number = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=244, blank=True)
    address = models.CharField(default='', max_length=249, blank=True)
    city = models.CharField(default='', max_length=10, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=10, blank=True)
    hbips_2_measure_description = models.CharField(default='', max_length=251, blank=True)
    hbips_2_overall_rate_per_1000 = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    hbips_2_overall_num = models.BooleanField(default=False, null=True, blank=True)
    hbips_2_overall_den = models.IntegerField(default=0, null=True, blank=True)
    hbips_2_overall_footnote = models.CharField(default='', max_length=10, blank=True)
    hbips_3_measure_description = models.CharField(default='', max_length=238, blank=True)
    hbips_3_overall_rate_per_1000 = models.IntegerField(default=0, null=True, blank=True)
    hbips_3_overall_num = models.BooleanField(default=False, null=True, blank=True)
    hbips_3_overall_den = models.IntegerField(default=0, null=True, blank=True)
    hbips_3_overall_footnote = models.CharField(default='', max_length=10, blank=True)
    hbips_5_measure_description = models.(null=True, blank=True)
    hbips_5_overall_of_total = models.CharField(default='', max_length=213, blank=True)
    hbips_5_overall_num = models.IntegerField(default=0, null=True, blank=True)
    hbips_5_overall_den = models.IntegerField(default=0, null=True, blank=True)
    hbips_5_overall_footnote = models.BooleanField(default=False, null=True, blank=True)
    hbips_6_measure_description = models.(null=True, blank=True)
    hbips_6_overall_of_total = models.CharField(default='', max_length=7, blank=True)
    hbips_6_overall_num = models.IntegerField(default=0, null=True, blank=True)
    hbips_6_overall_den = models.IntegerField(default=0, null=True, blank=True)
    hbips_6_overall_footnote = models.CharField(default='', max_length=10, blank=True)
    hbips_7_measure_description = models.(null=True, blank=True)
    hbips_7_overall_of_total = models.CharField(default='', max_length=7, blank=True)
    hbips_7_overall_num = models.IntegerField(default=0, null=True, blank=True)
    hbips_7_overall_den = models.IntegerField(default=0, null=True, blank=True)
    hbips_7_overall_footnote = models.CharField(default='', max_length=10, blank=True)
    sub_1_measure_description = models.CharField(default='', max_length=241, blank=True)
    sub_1_ = models.CharField(default='', max_length=7, blank=True)
    sub_1_numerator = models.IntegerField(default=0, null=True, blank=True)
    sub_1_denominator = models.IntegerField(default=0, null=True, blank=True)
    sub_1_footnote = models.CharField(default='', max_length=10, blank=True)
    tob_1_measure_description = models.CharField(default='', max_length=241, blank=True)
    tob_1_ = models.CharField(default='', max_length=7, blank=True)
    tob_1_numerator = models.IntegerField(default=0, null=True, blank=True)
    tob_1_denominator = models.IntegerField(default=0, null=True, blank=True)
    tob_1_footnote = models.CharField(default='', max_length=10, blank=True)
    tob_2_2a_measure_desc = models.(null=True, blank=True)
    tob_2_ = models.CharField(default='', max_length=7, blank=True)
    tob_2_numerator = models.IntegerField(default=0, null=True, blank=True)
    tob_2_2a_denominator = models.IntegerField(default=0, null=True, blank=True)
    tob_2_footnote = models.CharField(default='', max_length=10, blank=True)
    tob_2a_ = models.CharField(default='', max_length=183, blank=True)
    tob_2a_numerator = models.IntegerField(default=0, null=True, blank=True)
    tob_2_2a_denominator = models.IntegerField(default=0, null=True, blank=True)
    tob_2a_footnote = models.BooleanField(default=False, null=True, blank=True)
    peoc_measure_description = models.(null=True, blank=True)
    peoc_assessed_response = models.BooleanField(default=False, null=True, blank=True)
    peoc_assessed_footnote = models.CharField(default='', max_length=10, blank=True)
    ehr_use_measure_description = models.CharField(default='', max_length=254, blank=True)
    ehr_use_response = models.CharField(default='', max_length=244, blank=True)
    ehr_use_footnote = models.CharField(default='', max_length=10, blank=True)
    hie_measure_description = models.(null=True, blank=True)
    hie_response = models.BooleanField(default=False, null=True, blank=True)
    hie_footnote = models.CharField(default='', max_length=10, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.CharField(default='', max_length=10, blank=True)
    fuh_measure_description = models.(null=True, blank=True)
    fuh_30_ = models.CharField(default='', max_length=233, blank=True)
    fuh_30_numerator = models.IntegerField(default=0, null=True, blank=True)
    fuh_30_denominator = models.IntegerField(default=0, null=True, blank=True)
    fuh_30_footnote = models.BooleanField(default=False, null=True, blank=True)
    fuh_7_ = models.CharField(default='', max_length=233, blank=True)
    fuh_7_numerator = models.IntegerField(default=0, null=True, blank=True)
    fuh_7_denominator = models.IntegerField(default=0, null=True, blank=True)
    fuh_7_footnote = models.BooleanField(default=False, null=True, blank=True)
    fuh_measure_start_date = models.DateTimeField(null=True, blank=True)
    fuh_measure_end_date = models.CharField(default='', max_length=10, blank=True)
    imm_2_measure_description = models.CharField(default='', max_length=242, blank=True)
    imm_2_ = models.CharField(default='', max_length=113, blank=True)
    imm_2_numerator = models.IntegerField(default=0, null=True, blank=True)
    imm_2_denominator = models.IntegerField(default=0, null=True, blank=True)
    imm_2_footnote = models.BooleanField(default=False, null=True, blank=True)
    hcp_measure_description = models.(null=True, blank=True)
    hcp_ = models.IntegerField(default=0, null=True, blank=True)
    hcp_numerator = models.IntegerField(default=0, null=True, blank=True)
    hcp_denominator = models.IntegerField(default=0, null=True, blank=True)
    hcp_footnote = models.BooleanField(default=False, null=True, blank=True)
    flu_season_start_date = models.DateTimeField(null=True, blank=True)
    flu_season_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/hvbp_ami_11_14_2016.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:16:58 2017 '''

    provider_number = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=230, blank=True)
    address = models.CharField(default='', max_length=221, blank=True)
    city = models.CharField(default='', max_length=132, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=141, blank=True)
    ami_7a_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    ami_7a_benchmark = models.IntegerField(default=0, null=True, blank=True)
    ami_7a_baseline_rate = models.CharField(default='', max_length=213, blank=True)
    ami_7a_performance_rate = models.CharField(default='', max_length=203, blank=True)
    ami_7a_achievement_points = models.CharField(default='', max_length=213, blank=True)
    ami_7a_improvement_points = models.CharField(default='', max_length=213, blank=True)
    ami_7a_measure_score = models.CharField(default='', max_length=213, blank=True)
    ami_condition_procedure_score = models.CharField(default='', max_length=213, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Healthcare Associated Infections - Hospital.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:01 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=117, blank=True)
    address = models.CharField(default='', max_length=95, blank=True)
    city = models.CharField(default='', max_length=7, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=8, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    measure_name = models.CharField(default='', max_length=110, blank=True)
    measure_id = models.CharField(default='', max_length=94, blank=True)
    compared_to_national = models.CharField(default='', max_length=93, blank=True)
    score = models.CharField(default='', max_length=93, blank=True)
    footnote = models.CharField(default='', max_length=132, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/VA_PSI_July2017_05092017.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:05 2017 '''

    ccn_ = models.CharField(default='', max_length=6, null=False, primary_key=True, blank=False)
    vha_facility = models.(null=True, blank=True)
    address = models.(null=True, blank=True)
    city = models.CharField(default='', max_length=10, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    measureid = models.CharField(default='', max_length=6, blank=True)
    technical_measure_title = models.(null=True, blank=True)
    measure_as_reported_on_hospital_compare = models.(null=True, blank=True)
    numerator = models.IntegerField(default=0, null=True, blank=True)
    denominator = models.IntegerField(default=0, null=True, blank=True)
    observed_rate_per_1_000 = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    footnotes = models.CharField(default='', max_length=161, blank=True)
    date_range = models.(null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HOSPITAL_QUARTERLY_IPFQR_MEASURES_NATIONAL.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:06 2017 '''

    n_hbips_2_measure_description = models.CharField(default='', max_length=41, null=False, primary_key=True, blank=False)
    n_hbips_2_overall_rate_per_1000 = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    n_hbips_2_overall_num = models.DecimalField(default=0, null=True, max_digits=9, decimal_places=4, blank=True)
    n_hbips_2_overall_den = models.IntegerField(default=0, null=True, blank=True)
    n_hbips_3_measure_description = models.CharField(default='', max_length=28, blank=True)
    n_hbips_3_overall_rate_per_1000 = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    n_hbips_3_overall_num = models.DecimalField(default=0, null=True, max_digits=9, decimal_places=4, blank=True)
    n_hbips_3_overall_den = models.IntegerField(default=0, null=True, blank=True)
    n_hbips_5_measure_description = models.CharField(default='', max_length=98, blank=True)
    n_hbips_5_overall_of_total = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_hbips_5_overall_num = models.IntegerField(default=0, null=True, blank=True)
    n_hbips_5_overall_den = models.IntegerField(default=0, null=True, blank=True)
    n_hbips_6_measure_description = models.CharField(default='', max_length=53, blank=True)
    n_hbips_6_overall_of_total = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_hbips_6_overall_num = models.IntegerField(default=0, null=True, blank=True)
    n_hbips_6_overall_den = models.IntegerField(default=0, null=True, blank=True)
    n_hbips_7_measure_description = models.CharField(default='', max_length=107, blank=True)
    n_hbips_7_overall_of_total = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_hbips_7_overall_num = models.IntegerField(default=0, null=True, blank=True)
    n_hbips_7_overall_den = models.IntegerField(default=0, null=True, blank=True)
    n_sub_1_measure_description = models.CharField(default='', max_length=31, blank=True)
    n_sub_1_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_sub_1_numerator = models.IntegerField(default=0, null=True, blank=True)
    n_sub_1_denominator = models.IntegerField(default=0, null=True, blank=True)
    n_tob_1_measure_description = models.CharField(default='', max_length=31, blank=True)
    n_tob_1_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_tob_1_numerator = models.IntegerField(default=0, null=True, blank=True)
    n_tob_1_denominator = models.IntegerField(default=0, null=True, blank=True)
    n_tob_2_2a_measure_desc = models.CharField(default='', max_length=58, blank=True)
    n_tob_2_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_tob_2_numerator = models.IntegerField(default=0, null=True, blank=True)
    n_tob_2_2a_denominator = models.IntegerField(default=0, null=True, blank=True)
    n_tob_2a_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_tob_2a_numerator = models.IntegerField(default=0, null=True, blank=True)
    n_tob_2_2a_denominator = models.IntegerField(default=0, null=True, blank=True)
    n_peoc_measure_description = models.CharField(default='', max_length=50, blank=True)
    n_peoc_yes_count = models.IntegerField(default=0, null=True, blank=True)
    n_peoc_no_count = models.IntegerField(default=0, null=True, blank=True)
    n_peoc_yes_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_peoc_no_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_ehr_use_measure_description = models.CharField(default='', max_length=52, blank=True)
    n_ehr_paper_count = models.IntegerField(default=0, null=True, blank=True)
    n_ehr_non_certified_count = models.IntegerField(default=0, null=True, blank=True)
    n_ehr_certified_count = models.IntegerField(default=0, null=True, blank=True)
    n_ehr_paper_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_ehr_non_certified_ = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    n_ehr_certified_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_hie_measure_description = models.CharField(default='', max_length=62, blank=True)
    n_hie_yes_count = models.IntegerField(default=0, null=True, blank=True)
    n_hie_no_count = models.IntegerField(default=0, null=True, blank=True)
    n_hie_yes_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_hie_no_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.CharField(default='', max_length=10, blank=True)
    n_fuh_measure_description = models.CharField(default='', max_length=144, blank=True)
    n_fuh_30_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_fuh_30_numerator = models.IntegerField(default=0, null=True, blank=True)
    n_fuh_30_denominator = models.IntegerField(default=0, null=True, blank=True)
    n_fuh_7_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_fuh_7_numerator = models.IntegerField(default=0, null=True, blank=True)
    n_fuh_7_denominator = models.IntegerField(default=0, null=True, blank=True)
    n_fuh_measure_start_date = models.DateTimeField(null=True, blank=True)
    n_fuh_measure_end_date = models.CharField(default='', max_length=10, blank=True)
    n_imm_2_measure_description = models.CharField(default='', max_length=32, blank=True)
    n_imm_2_ = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    n_imm_2_numerator = models.IntegerField(default=0, null=True, blank=True)
    n_imm_2_denominator = models.IntegerField(default=0, null=True, blank=True)
    n_hcp_measure_description = models.CharField(default='', max_length=52, blank=True)
    n_hcp_ = models.IntegerField(default=0, null=True, blank=True)
    n_hcp_numerator = models.IntegerField(default=0, null=True, blank=True)
    n_hcp_denominator = models.IntegerField(default=0, null=True, blank=True)
    n_flu_season_start_date = models.DateTimeField(null=True, blank=True)
    n_flu_season_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HCAHPS - State.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:09 2017 '''

    state = models.CharField(default='', max_length=2, null=False, primary_key=True, blank=False)
    hcahps_question = models.CharField(default='', max_length=224, blank=True)
    hcahps_measure_id = models.CharField(default='', max_length=165, blank=True)
    hcahps_answer_description = models.CharField(default='', max_length=177, blank=True)
    hcahps_answer_percent = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.CharField(default='', max_length=216, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/hvbp_efficiency_11_10_2016.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:22 2017 '''

    provider_number = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.(null=True, blank=True)
    address = models.(null=True, blank=True)
    city = models.(null=True, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=131, blank=True)
    mspb_1_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mspb_1_benchmark = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mspb_1_baseline_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mspb_1_performance_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mspb_1_achievement_points = models.(null=True, blank=True)
    mspb_1_improvement_points = models.CharField(default='', max_length=10, blank=True)
    mspb_1_measure_score = models.(null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Healthcare Associated Infections - National.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:24 2017 '''

    measure_name = models.CharField(default='', max_length=140, null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=9, blank=True)
    score = models.BooleanField(default=False, null=True, blank=True)
    footnote = models.CharField(default='', max_length=180, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Outpatient Imaging Efficiency - State.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:29 2017 '''

    state = models.CharField(default='', max_length=2, null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=5, blank=True)
    measure_name = models.(null=True, blank=True)
    score = models.DecimalField(default=0, null=True, max_digits=53, decimal_places=10, blank=True)
    footnote = models.(null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/FY2015_Value_Based_Incentive_Payment_Amount.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:30 2017 '''

    incentive_payment_range = models.(null=False, primary_key=True, blank=False)
    number_of_hospitals_receiving_this_range = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HBIPS_July2017_05092017.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:34 2017 '''

    provider_id = models.CharField(default='', max_length=6, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=193, blank=True)
    address = models.CharField(default='', max_length=181, blank=True)
    city = models.CharField(default='', max_length=100, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=8, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    condition = models.CharField(default='', max_length=209, blank=True)
    measure_id = models.CharField(default='', max_length=185, blank=True)
    measure_name = models.CharField(default='', max_length=238, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)
    sample = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.(null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/hvbp_clinical_care_outcomes_11_10_2016.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:48 2017 '''

    provider_number = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=252, blank=True)
    address = models.CharField(default='', max_length=242, blank=True)
    city = models.CharField(default='', max_length=10, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=10, blank=True)
    mort_30_ami_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_ami_benchmark = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_ami_baseline_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_ami_performance_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_ami_achievement_points = models.CharField(default='', max_length=231, blank=True)
    mort_30_ami_improvement_points = models.CharField(default='', max_length=223, blank=True)
    mort_30_ami_measure_score = models.CharField(default='', max_length=231, blank=True)
    mort_30_hf_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_hf_benchmark = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_hf_baseline_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_hf_performance_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_hf_achievement_points = models.CharField(default='', max_length=231, blank=True)
    mort_30_hf_improvement_points = models.CharField(default='', max_length=143, blank=True)
    mort_30_hf_measure_score = models.CharField(default='', max_length=231, blank=True)
    mort_30_pn_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_pn_benchmark = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_pn_baseline_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_pn_performance_rate = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    mort_30_pn_achievement_points = models.CharField(default='', max_length=231, blank=True)
    mort_30_pn_improvement_points = models.CharField(default='', max_length=10, blank=True)
    mort_30_pn_measure_score = models.CharField(default='', max_length=231, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:49 2017 '''

    hospital_name = models.(null=False, primary_key=True, blank=False)
    provider_id = models.IntegerField(default=0, null=True, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    fiscal_year = models.IntegerField(default=0, null=True, blank=True)
    domain_1_score = models.IntegerField(default=0, null=True, blank=True)
    domain_1_score_footnote = models.IntegerField(default=0, null=True, blank=True)
    domain_1_start_date = models.IntegerField(default=0, null=True, blank=True)
    domain_1_end_date = models.IntegerField(default=0, null=True, blank=True)
    ahrq_psi_90_score = models.IntegerField(default=0, null=True, blank=True)
    ahrq_psi_90_score_footnote = models.IntegerField(default=0, null=True, blank=True)
    domain_2_score = models.DecimalField(default=0, null=True, max_digits=7, decimal_places=3, blank=True)
    domain_2_score_footnote = models.IntegerField(default=0, null=True, blank=True)
    clabsi_score = models.IntegerField(default=0, null=True, blank=True)
    clabsi_score_footnote = models.IntegerField(default=0, null=True, blank=True)
    cauti_score = models.IntegerField(default=0, null=True, blank=True)
    cauti_score_footnote = models.IntegerField(default=0, null=True, blank=True)
    ssi_score = models.IntegerField(default=0, null=True, blank=True)
    ssi_score_footnote = models.IntegerField(default=0, null=True, blank=True)
    mrsa_score = models.IntegerField(default=0, null=True, blank=True)
    mrsa_footnote = models.IntegerField(default=0, null=True, blank=True)
    cdi_score = models.IntegerField(default=0, null=True, blank=True)
    cdi_footnote = models.IntegerField(default=0, null=True, blank=True)
    domain_2_start_date = models.IntegerField(default=0, null=True, blank=True)
    domain_2_end_date = models.IntegerField(default=0, null=True, blank=True)
    total_hac_score = models.DecimalField(default=0, null=True, max_digits=6, decimal_places=3, blank=True)
    total_hac_score_footnote = models.IntegerField(default=0, null=True, blank=True)
    payment_reduction = models.BooleanField(default=False, null=True, blank=True)
    payment_reduction_footnote = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Hospital Returns - National.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:53 2017 '''

    measure_name = models.CharField(default='', max_length=157, null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=112, blank=True)
    national_rate = models.DecimalField(default=0, null=True, max_digits=33, decimal_places=10, blank=True)
    number_of_hospitals_worse = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_same = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_better = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_too_few = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.CharField(default='', max_length=166, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)
    number_of_hospitals_fewer = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_average = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_more = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_too_small = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Medicare Hospital Spending by Claim.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:55 2017 '''

    hospital_name = models.CharField(default='', max_length=211, null=False, primary_key=True, blank=False)
    provider_id = models.IntegerField(default=0, null=True, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    period = models.CharField(default='', max_length=253, blank=True)
    claim_type = models.CharField(default='', max_length=175, blank=True)
    avg_spending_per_episode_hospital = models.IntegerField(default=0, null=True, blank=True)
    avg_spending_per_episode_state = models.IntegerField(default=0, null=True, blank=True)
    avg_spending_per_episode_nation = models.IntegerField(default=0, null=True, blank=True)
    percent_of_spending_hospital = models.CharField(default='', max_length=6, blank=True)
    percent_of_spending_state = models.CharField(default='', max_length=6, blank=True)
    percent_of_spending_nation = models.CharField(default='', max_length=6, blank=True)
    start_date = models.IntegerField(default=0, null=True, blank=True)
    end_date = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/FINAL CJR Quality PR - PY1 File Values_Updated.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:17:59 2017 '''

    hospital_name = models.CharField(default='', max_length=122, null=False, primary_key=True, blank=False)
    provider_id = models.IntegerField(default=0, null=True, blank=True)
    msa = models.IntegerField(default=0, null=True, blank=True)
    msa_title = models.CharField(default='', max_length=94, blank=True)
    hcahps_hlmr = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    hcahps_start_date = models.CharField(default='', max_length=8, blank=True)
    hcahps_end_date = models.CharField(default='', max_length=9, blank=True)
    hcahps_footnote = models.CharField(default='', max_length=10, blank=True)
    comp_hip_knee = models.DecimalField(default=0, null=True, max_digits=3, decimal_places=1, blank=True)
    comp_start_date = models.CharField(default='', max_length=8, blank=True)
    comp_end_date = models.CharField(default='', max_length=9, blank=True)
    comp_footnote = models.IntegerField(default=0, null=True, blank=True)
    pro = models.CharField(default='', max_length=1, blank=True)
    pro_start_date = models.CharField(default='', max_length=8, blank=True)
    pro_end_date = models.CharField(default='', max_length=9, blank=True)
    pro_footnote_ = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Timely and Effective Care - National.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:18:06 2017 '''

    measure_name = models.(null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=214, blank=True)
    condition = models.CharField(default='', max_length=230, blank=True)
    category = models.(null=True, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.(null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HOSPITAL_ANNUAL_QUALITYMEASURE_PCH_EBRT_HOSPITAL.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:18:08 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=6, blank=True)
    hospital_name = models.CharField(default='', max_length=157, blank=True)
    hospital_type = models.CharField(default='', max_length=10, blank=True)
    address = models.CharField(default='', max_length=128, blank=True)
    city = models.CharField(default='', max_length=111, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=121, blank=True)
    measure_description = models.CharField(default='', max_length=156, blank=True)
    hospital_performance = models.IntegerField(default=0, null=True, blank=True)
    denominator = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.IntegerField(default=0, null=True, blank=True)
    rptg_prd_start_dt = models.DateTimeField(null=True, blank=True)
    rptg_prd_end_dt = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Outpatient Procedures - Volume.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:18:13 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=252, blank=True)
    measure_id = models.CharField(default='', max_length=5, blank=True)
    gastrointestinal = models.IntegerField(default=0, null=True, blank=True)
    eye = models.IntegerField(default=0, null=True, blank=True)
    nervous_system = models.IntegerField(default=0, null=True, blank=True)
    musculoskeletal = models.IntegerField(default=0, null=True, blank=True)
    skin = models.IntegerField(default=0, null=True, blank=True)
    genitourinary = models.IntegerField(default=0, null=True, blank=True)
    cardiovascular = models.IntegerField(default=0, null=True, blank=True)
    respiratory = models.IntegerField(default=0, null=True, blank=True)
    other = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.CharField(default='', max_length=10, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Medicare Hospital Spending per Patient - National.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:18:13 2017 '''

    measure_name = models.CharField(default='', max_length=84, null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=6, blank=True)
    score = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    footnote_score = models.IntegerField(default=0, null=True, blank=True)
    national_median = models.CharField(default='', max_length=10, blank=True)
    footnote_national_median = models.IntegerField(default=0, null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/MORT_READM_July2017.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:18:15 2017 '''

    provider_id = models.CharField(default='', max_length=6, null=False, primary_key=True, blank=False)
    vha_facility = models.CharField(default='', max_length=218, blank=True)
    address = models.CharField(default='', max_length=211, blank=True)
    city = models.CharField(default='', max_length=10, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county = models.CharField(default='', max_length=10, blank=True)
    county_code = models.IntegerField(default=0, null=True, blank=True)
    measure_id = models.CharField(default='', max_length=204, blank=True)
    technical_measure_title = models.CharField(default='', max_length=245, blank=True)
    measure_as_posted_on_hospital_compare = models.CharField(default='', max_length=241, blank=True)
    95_confidence_lower_limit = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    95_confidence_lower_upper_limit = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    risk_adjusted_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    vha_national_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    hospital_rating = models.CharField(default='', max_length=229, blank=True)
    number_observations = models.IntegerField(default=0, null=True, blank=True)
    number_deaths_readmissions = models.IntegerField(default=0, null=True, blank=True)
    footnotes = models.CharField(default='', max_length=151, blank=True)
    date_range = models.CharField(default='', max_length=219, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/hvbp_hcahps_11_10_2016.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:18:40 2017 '''

    provider_number = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=153, blank=True)
    address = models.CharField(default='', max_length=146, blank=True)
    city = models.CharField(default='', max_length=131, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=121, blank=True)
    communication_with_nurses_floor = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_with_nurses_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_with_nurses_benchmark = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_with_nurses_baseline_rate = models.DecimalField(default=0, null=True, max_digits=113, decimal_places=10, blank=True)
    communication_with_nurses_performance_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_with_nurses_achievement_points = models.CharField(default='', max_length=141, blank=True)
    communication_with_nurses_improvement_points = models.CharField(default='', max_length=113, blank=True)
    communication_with_nurses_dimension_score = models.CharField(default='', max_length=141, blank=True)
    communication_with_doctors_floor = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_with_doctors_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_with_doctors_benchmark = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_with_doctors_baseline_rate = models.DecimalField(default=0, null=True, max_digits=113, decimal_places=10, blank=True)
    communication_with_doctors_performance_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_with_doctors_achievement_points = models.CharField(default='', max_length=141, blank=True)
    communication_with_doctors_improvement_points = models.CharField(default='', max_length=113, blank=True)
    communication_with_doctors_dimension_score = models.CharField(default='', max_length=141, blank=True)
    responsiveness_of_hospital_staff_floor = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    responsiveness_of_hospital_staff_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    responsiveness_of_hospital_staff_benchmark = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    responsiveness_of_hospital_staff_baseline_rate = models.DecimalField(default=0, null=True, max_digits=113, decimal_places=10, blank=True)
    responsiveness_of_hospital_staff_performance_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    responsiveness_of_hospital_staff_achievement_points = models.CharField(default='', max_length=141, blank=True)
    responsiveness_of_hospital_staff_improvement_points = models.CharField(default='', max_length=113, blank=True)
    responsiveness_of_hospital_staff_dimension_score = models.CharField(default='', max_length=141, blank=True)
    pain_management_floor = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    pain_management_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    pain_management_benchmark = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    pain_management_baseline_rate = models.DecimalField(default=0, null=True, max_digits=113, decimal_places=10, blank=True)
    pain_management_performance_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    pain_management_achievement_points = models.CharField(default='', max_length=141, blank=True)
    pain_management_improvement_points = models.CharField(default='', max_length=113, blank=True)
    pain_management_dimension_score = models.CharField(default='', max_length=141, blank=True)
    communication_about_medicines_floor = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_about_medicines_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_about_medicines_benchmark = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_about_medicines_baseline_rate = models.DecimalField(default=0, null=True, max_digits=113, decimal_places=10, blank=True)
    communication_about_medicines_performance_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    communication_about_medicines_achievement_points = models.CharField(default='', max_length=141, blank=True)
    communication_about_medicines_improvement_points = models.CharField(default='', max_length=113, blank=True)
    communication_about_medicines_dimension_score = models.CharField(default='', max_length=141, blank=True)
    cleanliness_and_quietness_of_hospital_environment_floor = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    cleanliness_and_quietness_of_hospital_environment_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    cleanliness_and_quietness_of_hospital_environment_benchmark = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    cleanliness_and_quietness_of_hospital_environment_baseline_rate = models.DecimalField(default=0, null=True, max_digits=113, decimal_places=10, blank=True)
    cleanliness_and_quietness_of_hospital_environment_performance_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    cleanliness_and_quietness_of_hospital_environment_achievement_points = models.CharField(default='', max_length=141, blank=True)
    cleanliness_and_quietness_of_hospital_environment_improvement_points = models.CharField(default='', max_length=113, blank=True)
    cleanliness_and_quietness_of_hospital_environment_dimension_score = models.CharField(default='', max_length=141, blank=True)
    discharge_information_floor = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    discharge_information_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    discharge_information_benchmark = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    discharge_information_baseline_rate = models.DecimalField(default=0, null=True, max_digits=113, decimal_places=10, blank=True)
    discharge_information_performance_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    discharge_information_achievement_points = models.CharField(default='', max_length=141, blank=True)
    discharge_information_improvement_points = models.CharField(default='', max_length=113, blank=True)
    discharge_information_dimension_score = models.CharField(default='', max_length=141, blank=True)
    overall_rating_of_hospital_floor = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    overall_rating_of_hospital_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    overall_rating_of_hospital_benchmark = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    overall_rating_of_hospital_baseline_rate = models.DecimalField(default=0, null=True, max_digits=113, decimal_places=10, blank=True)
    overall_rating_of_hospital_performance_rate = models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True)
    overall_rating_of_hospital_achievement_points = models.CharField(default='', max_length=141, blank=True)
    overall_rating_of_hospital_improvement_points = models.CharField(default='', max_length=113, blank=True)
    overall_rating_of_hospital_dimension_score = models.CharField(default='', max_length=141, blank=True)
    hcahps_base_score = models.IntegerField(default=0, null=True, blank=True)
    hcahps_consistency_score = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Payment - National.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:18:42 2017 '''

    measure_name = models.CharField(default='', max_length=73, null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=51, blank=True)
    national_payment = models.CharField(default='', max_length=7, blank=True)
    number_less_than_national_payment = models.IntegerField(default=0, null=True, blank=True)
    number_same_as_national_payment = models.IntegerField(default=0, null=True, blank=True)
    number_greater_than_national_payment = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_too_few = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.CharField(default='', max_length=106, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/FY2015_Net_Change_in_Base_Op_DRG_Payment_Amt.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:18:42 2017 '''

    net_change_in_base_operating_drg_payment_amount = models.(null=False, primary_key=True, blank=False)
    number_of_hospitals_receiving_this_range = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HOSPITAL_QUARTERLY_QUALITYMEASURE_PCH_HCAHPS_HOSPITAL.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:18:47 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.(null=True, blank=True)
    address = models.CharField(default='', max_length=228, blank=True)
    city = models.CharField(default='', max_length=6, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=221, blank=True)
    phone_number = models.CharField(default='', max_length=224, blank=True)
    hcahps_measure_id = models.CharField(default='', max_length=225, blank=True)
    hcahps_question = models.(null=True, blank=True)
    hcahps_answer_description = models.CharField(default='', max_length=237, blank=True)
    patient_survey_star_rating = models.IntegerField(default=0, null=True, blank=True)
    patient_survey_star_rating_footnote = models.CharField(default='', max_length=10, blank=True)
    hcahps_answer_percent = models.IntegerField(default=0, null=True, blank=True)
    hcahps_answer_percent_footnote = models.CharField(default='', max_length=10, blank=True)
    hcahps_linear_mean_value = models.IntegerField(default=0, null=True, blank=True)
    number_of_completed_surveys = models.IntegerField(default=0, null=True, blank=True)
    number_of_completed_surveys_footnote = models.CharField(default='', max_length=10, blank=True)
    survey_response_rate_percent = models.IntegerField(default=0, null=True, blank=True)
    survey_response_rate_percent_footnote = models.CharField(default='', max_length=10, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HOSPITAL_QUARTERLY_QUALITYMEASURE_PCH_HCAHPS_STATE.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:18:50 2017 '''

    state = models.CharField(default='', max_length=2, null=False, primary_key=True, blank=False)
    hcahps_measure_id = models.CharField(default='', max_length=215, blank=True)
    hcahps_question = models.(null=True, blank=True)
    hcahps_answer_description = models.CharField(default='', max_length=227, blank=True)
    hcahps_answer_percent = models.IntegerField(default=0, null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Complications and Deaths - National.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:18:55 2017 '''

    measure_name = models.CharField(default='', max_length=234, null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=189, blank=True)
    national_rate = models.DecimalField(default=0, null=True, max_digits=6, decimal_places=3, blank=True)
    number_of_hospitals_worse = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_same = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_better = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_too_few = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.CharField(default='', max_length=236, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HCAHPS - National.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:03 2017 '''

    hcahps_measure_id = models.(null=False, primary_key=True, blank=False)
    hcahps_question = models.(null=True, blank=True)
    hcahps_answer_description = models.(null=True, blank=True)
    hcahps_answer_percent = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.(null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Payment - State.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:08 2017 '''

    state = models.CharField(default='', max_length=2, null=False, primary_key=True, blank=False)
    measure_name = models.CharField(default='', max_length=233, blank=True)
    measure_id = models.CharField(default='', max_length=211, blank=True)
    number_less_than_national_payment = models.IntegerField(default=0, null=True, blank=True)
    number_same_as_national_payment = models.IntegerField(default=0, null=True, blank=True)
    number_greater_than_national_payment = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_too_few = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.(null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/hvbp_pc_11_10_2016.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:12 2017 '''

    provider_number = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=215, blank=True)
    address = models.CharField(default='', max_length=212, blank=True)
    city = models.CharField(default='', max_length=191, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=174, blank=True)
    pc_01_achievement_threshold = models.DecimalField(default=0, null=True, max_digits=8, decimal_places=4, blank=True)
    pc_01_benchmark = models.IntegerField(default=0, null=True, blank=True)
    pc_01_baseline_rate = models.DecimalField(default=0, null=True, max_digits=173, decimal_places=10, blank=True)
    pc_01_performance_rate = models.DecimalField(default=0, null=True, max_digits=173, decimal_places=10, blank=True)
    pc_01_achievement_points = models.CharField(default='', max_length=202, blank=True)
    pc_01_improvement_points = models.CharField(default='', max_length=173, blank=True)
    pc_01_measure_score = models.CharField(default='', max_length=202, blank=True)
    pc_01_preventive_condition_procedure_score = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/VHA provider level data.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:15 2017 '''

    provider_id = models.CharField(default='', max_length=6, null=False, primary_key=True, blank=False)
    hospital_name = models.(null=True, blank=True)
    address = models.(null=True, blank=True)
    city = models.CharField(default='', max_length=242, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=211, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    hospital_type = models.(null=True, blank=True)
    hospital_ownership = models.(null=True, blank=True)
    emergency_services = models.BooleanField(default=False, null=True, blank=True)
    hospital_overall_rating = models.(null=True, blank=True)
    hospital_overall_rating_footnote = models.(null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HOSPITAL_QUARTERLY_QUALITYMEASURE_PCH_HOSPITAL.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:20 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=5, blank=True)
    hospital_name = models.CharField(default='', max_length=247, blank=True)
    hospital_type = models.CharField(default='', max_length=10, blank=True)
    address = models.CharField(default='', max_length=218, blank=True)
    city = models.CharField(default='', max_length=181, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=211, blank=True)
    measure_description = models.CharField(default='', max_length=238, blank=True)
    numerator = models.IntegerField(default=0, null=True, blank=True)
    denominator = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.BooleanField(default=False, null=True, blank=True)
    rptg_prd_start_dt = models.DateTimeField(null=True, blank=True)
    rptg_prd_end_dt = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Hospital Returns - State.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:25 2017 '''

    state = models.CharField(default='', max_length=2, null=False, primary_key=True, blank=False)
    measure_name = models.(null=True, blank=True)
    measure_id = models.CharField(default='', max_length=242, blank=True)
    number_of_hospitals_worse = models.BooleanField(default=False, null=True, blank=True)
    number_of_hospitals_same = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_better = models.BooleanField(default=False, null=True, blank=True)
    number_of_hospitals_too_few = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.(null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)
    number_of_hospitals_fewer = models.CharField(default='', max_length=244, blank=True)
    number_of_hospitals_average = models.CharField(default='', max_length=244, blank=True)
    number_of_hospitals_more = models.CharField(default='', max_length=244, blank=True)
    number_of_hospitals_too_small = models.CharField(default='', max_length=244, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/hvbp_tps_11_10_2016.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:27 2017 '''

    provider_number = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=214, blank=True)
    address = models.CharField(default='', max_length=213, blank=True)
    city = models.CharField(default='', max_length=132, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=10, blank=True)
    unweighted_normalized_clinical_care_process_domain_score = models.IntegerField(default=0, null=True, blank=True)
    weighted_clinical_care_process_domain_score = models.DecimalField(default=0, null=True, max_digits=204, decimal_places=10, blank=True)
    unweighted_normalized_clinical_care_outcomes_domain_score = models.DecimalField(default=0, null=True, max_digits=205, decimal_places=10, blank=True)
    weighted_normalized_clinical_care_outcomes_domain_score = models.DecimalField(default=0, null=True, max_digits=205, decimal_places=10, blank=True)
    unweighted_patient_and_caregiver_centered_experience_of_care_care_coordination_domain_score = models.IntegerField(default=0, null=True, blank=True)
    weighted_patient_and_caregiver_centered_experience_of_care_care_coordination_domain_score = models.DecimalField(default=0, null=True, max_digits=204, decimal_places=10, blank=True)
    unweighted_normalized_safety_domain_score = models.DecimalField(default=0, null=True, max_digits=205, decimal_places=10, blank=True)
    weighted_safety_domain_score = models.DecimalField(default=0, null=True, max_digits=204, decimal_places=10, blank=True)
    unweighted_normalized_efficiency_and_cost_reduction_domain_score = models.IntegerField(default=0, null=True, blank=True)
    weighted_efficiency_and_cost_reduction_domain_score = models.DecimalField(default=0, null=True, max_digits=204, decimal_places=10, blank=True)
    total_performance_score = models.DecimalField(default=0, null=True, max_digits=205, decimal_places=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/HCAHPS - Hospital.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:30 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=177, blank=True)
    address = models.CharField(default='', max_length=155, blank=True)
    city = models.CharField(default='', max_length=7, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=8, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    hcahps_measure_id = models.CharField(default='', max_length=153, blank=True)
    hcahps_question = models.CharField(default='', max_length=204, blank=True)
    hcahps_answer_description = models.CharField(default='', max_length=159, blank=True)
    patient_survey_star_rating = models.IntegerField(default=0, null=True, blank=True)
    patient_survey_star_rating_footnote = models.CharField(default='', max_length=10, blank=True)
    hcahps_answer_percent = models.IntegerField(default=0, null=True, blank=True)
    hcahps_answer_percent_footnote = models.CharField(default='', max_length=10, blank=True)
    hcahps_linear_mean_value = models.IntegerField(default=0, null=True, blank=True)
    number_of_completed_surveys = models.IntegerField(default=0, null=True, blank=True)
    number_of_completed_surveys_footnote = models.CharField(default='', max_length=10, blank=True)
    survey_response_rate_percent = models.IntegerField(default=0, null=True, blank=True)
    survey_response_rate_percent_footnote = models.CharField(default='', max_length=10, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Value of Care - National.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:34 2017 '''

    value_of_care_measure_name = models.CharField(default='', max_length=253, null=False, primary_key=True, blank=False)
    value_of_care_measure_id = models.CharField(default='', max_length=219, blank=True)
    number_of_hospitals = models.IntegerField(default=0, null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/VHA measure dates.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:34 2017 '''

    measure_name = models.(null=False, primary_key=True, blank=False)
    measure_id = models.CharField(default='', max_length=6, blank=True)
    measure_start_quarter = models.CharField(default='', max_length=6, blank=True)
    measure_start_date = models.IntegerField(default=0, null=True, blank=True)
    measure_end_quarter = models.CharField(default='', max_length=6, blank=True)
    measure_end_date = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Payment and Value of Care - Hospital.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:40 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(default='', max_length=247, blank=True)
    address = models.CharField(default='', max_length=225, blank=True)
    city = models.CharField(default='', max_length=10, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=8, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    payment_measure_name = models.CharField(default='', max_length=243, blank=True)
    payment_measure_id = models.CharField(default='', max_length=221, blank=True)
    payment_category = models.CharField(default='', max_length=248, blank=True)
    denominator = models.IntegerField(default=0, null=True, blank=True)
    payment = models.CharField(default='', max_length=143, blank=True)
    lower_estimate = models.CharField(default='', max_length=143, blank=True)
    higher_estimate = models.CharField(default='', max_length=143, blank=True)
    payment_footnote = models.CharField(default='', max_length=184, blank=True)
    value_of_care_display_name = models.CharField(default='', max_length=244, blank=True)
    value_of_care_display_id = models.CharField(default='', max_length=226, blank=True)
    value_of_care_category = models.CharField(default='', max_length=245, blank=True)
    value_of_care_footnote = models.CharField(default='', max_length=190, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/READMISSION REDUCTION.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:43 2017 '''

    hospital_name = models.CharField(default='', max_length=252, null=False, primary_key=True, blank=False)
    provider_number = models.IntegerField(default=0, null=True, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    measure_name = models.CharField(default='', max_length=237, blank=True)
    number_of_discharges = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.CharField(default='', max_length=1, blank=True)
    excess_readmission_ratio = models.DecimalField(default=0, null=True, max_digits=163, decimal_places=10, blank=True)
    predicted_readmission_rate = models.DecimalField(default=0, null=True, max_digits=163, decimal_places=10, blank=True)
    expected_readmission_rate = models.DecimalField(default=0, null=True, max_digits=163, decimal_places=10, blank=True)
    number_of_readmissions = models.IntegerField(default=0, null=True, blank=True)
    start_date = models.CharField(default='', max_length=9, blank=True)
    end_date = models.CharField(default='', max_length=9, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Timely and Effective Care - State.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:49 2017 '''

    state = models.CharField(default='', max_length=2, null=False, primary_key=True, blank=False)
    condition = models.(null=True, blank=True)
    measure_name = models.(null=True, blank=True)
    measure_id = models.CharField(default='', max_length=5, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.(null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Medicare Hospital Spending per Patient - State.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:19:55 2017 '''

    state = models.CharField(default='', max_length=2, null=False, primary_key=True, blank=False)
    measure_name = models.(null=True, blank=True)
    measure_id = models.CharField(default='', max_length=6, blank=True)
    score = models.DecimalField(default=0, null=True, max_digits=193, decimal_places=10, blank=True)
    footnote = models.(null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Measure Dates.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:20:20 2017 '''

    measure_name = models.(null=False, primary_key=True, blank=False)
    measure_id = models.(null=True, blank=True)
    measure_start_quarter = models.CharField(default='', max_length=6, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_quarter = models.CharField(default='', max_length=6, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'

#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Healthcare Associated Infections - State.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:20:28 2017 '''

    state = models.CharField(default='', max_length=2, null=False, primary_key=True, blank=False)
    measure_name = models.(null=True, blank=True)
    measure_id = models.CharField(default='', max_length=9, blank=True)
    score = models.(null=True, blank=True)
    footnote = models.(null=True, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Outpatient Imaging Efficiency - National.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:20:30 2017 '''

    measure_id = models.CharField(default='', max_length=5, null=False, primary_key=True, blank=False)
    measure_name = models.CharField(default='', max_length=123, blank=True)
    score = models.DecimalField(default=0, null=True, max_digits=4, decimal_places=2, blank=True)
    footnote = models.CharField(default='', max_length=126, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Complications and Deaths - State.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:20:33 2017 '''

    state = models.CharField(default='', max_length=2, null=False, primary_key=True, blank=False)
    measure_name = models.CharField(default='', max_length=165, blank=True)
    measure_id = models.CharField(default='', max_length=121, blank=True)
    number_of_hospitals_worse = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_same = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_better = models.IntegerField(default=0, null=True, blank=True)
    number_of_hospitals_too_few = models.IntegerField(default=0, null=True, blank=True)
    footnote = models.CharField(default='', max_length=176, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'


#Imported from : /home/thomas/Github/CSC-495-Data-Driven-Decision-Making/mysite/csv/shortened/Structural Measures - Hospital.csv
class Csvimport(models.Model):
    ''' Autogenerated model file csvimport Thu Oct 26 06:20:39 2017 '''

    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.(null=True, blank=True)
    address = models.CharField(default='', max_length=245, blank=True)
    city = models.CharField(default='', max_length=10, blank=True)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(default='', max_length=8, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    measure_name = models.(null=True, blank=True)
    measure_id = models.CharField(default='', max_length=216, blank=True)
    measure_response = models.BooleanField(default=False, null=True, blank=True)
    footnote = models.CharField(default='', max_length=10, blank=True)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"csvimport_"'