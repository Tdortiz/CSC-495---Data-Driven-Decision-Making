from __future__ import unicode_literals
from django.db import models
import json

'''
    A map to easily get/change values of priorities
    Example Access:
        priorityMap['Low'] => .75
        priorityMap['Medium'] => 1.0
        priorityMap['High'] => 1.25
'''
priorityMap = {
    'Low': .75,
    'Medium': 1,
    'High': 1.25,
}

'''
    The hospital ranking algorithm
'''
class HospitalRankingAlgorithm:
    filters = {}

    def __init__(self, filters):
        self.filters = filters
    
    '''
        Using the filters (Low = .75, Med = 1, High = 1.25) weight the 
        given metrics to create a weighted sum.

        Using that weighted sum, order the hospital list by it from [highest, ..., lowest] 
    '''
    def rank_hospitals_by_filters(self):

        # All hospitals in NC
        hospitals_nc = Hospital.objects.filter(state='NC').all()

        # Setup ranking dictionary
        ranking_dict = dict()
        for hospital in hospitals_nc:
            ranking_dict[hospital.provider_id] = {
                "name": hospital.hospital_name,
                "score": 0,
                "address": hospital.address,
                "city": hospital.city,
                "state": hospital.state,
                "zip_code": hospital.zip_code,
                "county_name": hospital.county_name,
                "phone_number": hospital.phone_number,
            }

        print(str(json.dumps(ranking_dict, indent=4, sort_keys=True)))

        for current_hospital in hospitals_nc:
            '''
            hospitals_nc_dict[current_hospital.provider_id] = current_hospital


            # Ranking it
            hospitals_payment_sorted = self.payment_rank(hospitals_nc)

            # Return it

            for hospital_sorted in hospitals_payment_sorted:
                self.hospital_ranked_list.append(
                    str(hospitals_nc_dict.get(hospital_sorted[0])) + "-" + str(hospital_sorted[1]))
            '''

        return ranking_dict

    def payment_rank(self, hospitals_nc):
        # dict use to sort
        hospitals_rating_dict = dict()


        # Not available value in database
        na = 0
        # if all values are not available set it as
        all_na = 9999999

        for current_hospital in hospitals_nc:

            # all payment_measurements for given provider_id
            payment_measurements = PaymentAndValueOfCare_Hospital.objects.filter(
                provider_id=current_hospital.provider_id)
            payment_sum = 0
            payment_count = 0
            for measurement in payment_measurements:
                # conver $xx,xxx string to int
                measurement_int = int(measurement.payment.replace('$', '').replace(',', ''))
                # if measurement value is available
                if (measurement_int != na):
                    payment_sum += measurement_int
                    payment_count += 1

            if payment_count != 0:
                hospitals_rating_dict[current_hospital.provider_id] = payment_sum / payment_count

            # if all measurements are not available
            else:
                hospitals_rating_dict[current_hospital.provider_id] = all_na

        # Sort
        hospitals_rating_dict_sorted = sorted(hospitals_rating_dict.iteritems(), key=lambda d: d[1])
        return hospitals_rating_dict_sorted




class Footnotes(models.Model):
    footnote = models.CharField(primary_key=True, max_length=6)
    footnote_text = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Footnotes'


class Hospital(models.Model):
    provider_id = models.IntegerField(primary_key=True)
    hospital_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField(blank=True, null=True)
    county_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    hospital_type = models.CharField(max_length=50, blank=True, null=True)
    hospital_ownership = models.CharField(max_length=50, blank=True, null=True)
    emergency_services = models.BooleanField()
    meets_criteria_for_meaningful_use_of_ehrs = models.CharField(max_length=5)
    hospital_overall_rating = models.IntegerField(blank=True, null=True)
    hospital_overall_rating_footnote = models.CharField(max_length=50, blank=True, null=True)
    mortality_national_comparison = models.CharField(max_length=50, blank=True, null=True)
    mortality_national_comparison_footnote = models.CharField(max_length=50, blank=True, null=True)
    safety_of_care_national_comparison = models.CharField(max_length=50, blank=True, null=True)
    safety_of_care_national_comparison_footnote = models.CharField(max_length=50, blank=True, null=True)
    readmission_national_comparison = models.CharField(max_length=50, blank=True, null=True)
    readmission_national_comparison_footnote = models.CharField(max_length=50, blank=True, null=True)
    patient_experience_national_comparison = models.CharField(max_length=50, blank=True, null=True)
    patient_experience_national_comparison_footnote = models.CharField(max_length=50, blank=True, null=True)
    effectiveness_of_care_national_comparison = models.CharField(max_length=50, blank=True, null=True)
    effectiveness_of_care_national_comparison_footnote = models.CharField(max_length=50, blank=True, null=True)
    timeliness_of_care_national_comparison = models.CharField(max_length=50, blank=True, null=True)
    timeliness_of_care_national_comparison_footnote = models.CharField(max_length=50, blank=True, null=True)
    efficient_use_of_medical_imaging_national_comparison = models.CharField(max_length=50, blank=True, null=True)
    efficient_use_of_medical_imaging_national_comparison_footnote = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.provider_id) + " - " + str(self.hospital_name)

    class Meta:
        managed = True
        db_table = 'Hospital'


class HospitalReturns_Hospital(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey(Hospital, models.DO_NOTHING, blank=True, null=True)
    measure_name = models.CharField(max_length=50, blank=True, null=True)
    measure_id = models.CharField(max_length=231, blank=True, null=True)
    compared_to_national = models.CharField(max_length=242, blank=True, null=True)
    denominator = models.IntegerField(blank=True, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    lower_estimate = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    higher_estimate = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    footnote = models.ForeignKey(Footnotes, models.DO_NOTHING, db_column='footnote', blank=True, null=True)
    measure_start_date = models.DateTimeField(blank=True, null=True)
    measure_end_date = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'HospitalReturns_Hospital'


class MedicareSpendingPerPatient_Hospital(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey(Hospital, models.DO_NOTHING)
    measure_name = models.CharField(max_length=100, blank=True, null=True)
    measure_id = models.CharField(max_length=6)
    score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    footnote = models.ForeignKey(Footnotes, models.DO_NOTHING, db_column='footnote')
    measure_start_date = models.DateTimeField(blank=True, null=True)
    measure_end_date = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'MedicareSpendingPerPatient_Hospital'


class OutpatientImagingEfficiency_Hospital(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey(Hospital, models.DO_NOTHING)
    measure_id = models.CharField(max_length=5)
    measure_name = models.CharField(max_length=100, blank=True, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    footnote = models.ForeignKey(Footnotes, models.DO_NOTHING, db_column='footnote')
    measure_start_date = models.DateTimeField(blank=True, null=True)
    measure_end_date = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'OutpatientImagingEfficiency_Hospital'


class PaymentAndValueOfCare_Hospital(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey(Hospital, models.DO_NOTHING)
    payment_measure_name = models.CharField(max_length=243)
    payment_measure_id = models.CharField(max_length=221)
    payment_category = models.CharField(max_length=248)
    denominator = models.IntegerField(blank=True, null=True)
    payment = models.CharField(max_length=143)
    lower_estimate = models.CharField(max_length=143)
    higher_estimate = models.CharField(max_length=143)
    payment_footnote = models.CharField(max_length=184)
    value_of_care_display_name = models.CharField(max_length=244)
    value_of_care_display_id = models.CharField(max_length=226)
    value_of_care_category = models.CharField(max_length=245)
    value_of_care_footnote = models.CharField(max_length=190)
    measure_start_date = models.DateTimeField(blank=True, null=True)
    measure_end_date = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'PaymentAndValueOfCare_Hospital'

class Timely_And_Effective(models.Model):

    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey(Hospital, models.DO_NOTHING)
    measure_id = models.CharField(null=True, blank=True,max_length=243)
    measure_name = models.CharField(null=True, blank=True,max_length=243)
    score = models.IntegerField(default=0, null=True, blank=True)
    sample = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'Timely_And_Effective'

class StructuralMeasures_Hospital(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey(Hospital, models.DO_NOTHING)
    measure_name = models.CharField(max_length=100, blank=True, null=True)
    measure_id = models.CharField(max_length=216)
    measure_response = models.BooleanField()
    footnote = models.ForeignKey(Footnotes, models.DO_NOTHING, db_column='footnote')
    measure_start_date = models.DateTimeField(blank=True, null=True)
    measure_end_date = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'StructuralMeasures_Hospital'

class MeasureInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    measure_id = models.CharField(max_length=255, blank=True, null=True)
    measure_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.measure_id) + " - " + str(self.measure_name)

    class Meta:
        managed = False
        db_table = 'Measure_info'


class ComplicationsAndDeathsHospital(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey('Hospital', models.DO_NOTHING)
    measure_name = models.CharField(max_length=125)
    measure_id = models.CharField(max_length=83)
    compared_to_national = models.CharField(max_length=110)
    denominator = models.IntegerField(blank=True, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    lower_estimate = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    higher_estimate = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    footnote = models.ForeignKey('Footnotes', models.DO_NOTHING, db_column='footnote')
    measure_start_date = models.DateTimeField(blank=True, null=True)
    measure_end_date = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'ComplicationsAndDeaths_Hospital'


class Normalized_Payment(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey(Hospital, models.DO_NOTHING)
    payment_measure_name = models.CharField(max_length=243,blank=True, null=True)
    payment_measure_id = models.CharField(max_length=221,blank=True, null=True)
    payment_category = models.CharField(max_length=248,blank=True, null=True)
    payment = models.CharField(max_length=143,blank=True, null=True)
    n_score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    value_of_care_display_name = models.CharField(max_length=244,blank=True, null=True)
    value_of_care_display_id = models.CharField(max_length=226,blank=True, null=True)
    value_of_care_category = models.CharField(max_length=245,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Normalized_Payment'


class Normalized_Timely(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey(Hospital, models.DO_NOTHING)
    measure_id = models.CharField(null=True, blank=True, max_length=243)
    measure_name = models.CharField(null=True, blank=True, max_length=243)
    score = models.IntegerField(default=0, null=True, blank=True)
    n_score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    sample = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'Normalized_Timely'


class Normalized_Returns(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey(Hospital, models.DO_NOTHING, blank=True, null=True)
    measure_name = models.CharField(max_length=50, blank=True, null=True)
    measure_id = models.CharField(max_length=231, blank=True, null=True)
    compared_to_national = models.CharField(max_length=242, blank=True, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    n_score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'Normalized_Returns'

class Normalized_Complications(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey('Hospital', models.DO_NOTHING)
    measure_name = models.CharField(max_length=125)
    measure_id = models.CharField(max_length=83)
    compared_to_national = models.CharField(max_length=110)
    score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    n_score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'Normalized_Complications'