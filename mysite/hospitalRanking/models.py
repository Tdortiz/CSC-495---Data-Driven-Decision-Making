from __future__ import unicode_literals
from django.db import models
import json
from random import *
from pprint import pprint

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
                "provider_id": hospital.provider_id,
                "name": hospital.hospital_name,
                "score": 0,
                "address": hospital.address,
                "city": hospital.city,
                "state": hospital.state,
                "zip_code": hospital.zip_code,
                "county_name": hospital.county_name,
                "phone_number": hospital.phone_number,
                "n_payment": 0,
                "n_md": 0,
                "n_timely": 0,
                "n_complications": 0,
                "n_returns": 0
            }

        # Run algorithm per hospital
        for current_hospital in hospitals_nc:
            '''
            Run algorithm and set score(s)
            '''

        # Save dict items into an array that is sorted by item.score
        # Sort by putting [ Higher Scores, ..., Lower Scores ]

        # print self.filters['Complications and Death']
        # 'Complications and Death': '1',
        #  'Doctor Ranking': '1',
        #  'Timely and Effective Care': '1',
        #  'Cost of Care': '1',
        #  'Hospital Returns': '1'

        hospitals_payment = self.payment_rank(hospitals_nc)
        for hsp in hospitals_payment:
            ranking_dict[hsp[0]]['score'] += (float(hsp[1])*float(self.filters['Cost of Care']))
            ranking_dict[hsp[0]]['n_payment'] = float(hsp[1])

        hospitals_md = self.md_rank(hospitals_nc)
        for hsp in hospitals_md:
            ranking_dict[hsp[0]]['score'] += (float(hsp[1])*float(self.filters['Doctor Ranking']))
            ranking_dict[hsp[0]]['n_md'] = float(hsp[1])

        hospitals_timely = self.timely_rank(hospitals_nc)
        for hsp in hospitals_timely:
            ranking_dict[hsp[0]]['score'] += (float(hsp[1])*float(self.filters['Timely and Effective Care']))
            ranking_dict[hsp[0]]['n_timely'] = float(hsp[1])

        hospitals_complications = self.complications_rank(hospitals_nc)
        for hsp in hospitals_complications:
            ranking_dict[hsp[0]]['score'] += (float(hsp[1])*float(self.filters['Complications and Death']))
            ranking_dict[hsp[0]]['n_complications'] = float(hsp[1])

        hospitals_returns = self.returns_rank(hospitals_nc)
        for hsp in hospitals_returns:
            ranking_dict[hsp[0]]['score'] += (float(hsp[1])*float(self.filters['Hospital Returns']))
            ranking_dict[hsp[0]]['n_returns'] = float(hsp[1])

        print ranking_dict

        # Normalize final results for display 0-1, higher score is better
        max_score=0
        min_score=1
        for key in ranking_dict.iterkeys():
            if max_score<ranking_dict[key]['score']:
                max_score=ranking_dict[key]['score']
            if min_score>ranking_dict[key]['score']:
                min_score=ranking_dict[key]['score']

        for key in ranking_dict.iterkeys():
            ranking_dict[key]['score'] = (ranking_dict[key]['score']-min_score)/(max_score-min_score)

        # ENd Normalization


        ranked_list = list()
        for key, value in ranking_dict.items():
            ranked_list.append(value)

        # Return the ranked list
        ranked_list.sort(key=lambda item: item['score'], reverse=True)
        return ranked_list

    def payment_rank(self, hospitals_nc):
        # dict use to sort
        hospitals_rating_dict = dict()

        for current_hospital in hospitals_nc:

            # all payment_measurements for given provider_id
            payment_measurements = Normalized_Payment.objects.filter(
                provider_id=current_hospital.provider_id)
            n_score_sum = 0
            n_score_count = 0
            for measurement in payment_measurements:
                # conver $xx,xxx string to int

                n_score_sum += measurement.n_score
                n_score_count += 1

                hospitals_rating_dict[current_hospital.provider_id] = n_score_sum / n_score_count

        # Sort
        # hospitals_rating_dict_sorted = sorted(hospitals_rating_dict.iteritems(), key=lambda d: d[1])
        return hospitals_rating_dict.iteritems()

    def md_rank(self, hospitals_nc):
        # dict use to sort
        hospitals_rating_dict = dict()

        for current_hospital in hospitals_nc:

            # all payment_measurements for given provider_id
            md_score = MD_Score.objects.filter(
                provider_id=current_hospital.provider_id)
            n_score_sum = 0
            n_score_count = 0
            for score in md_score:
                # conver $xx,xxx string to int

                n_score_sum += score.score
                n_score_count += 1

                hospitals_rating_dict[current_hospital.provider_id] = n_score_sum / n_score_count

        # Sort
        # hospitals_rating_dict_sorted = sorted(hospitals_rating_dict.iteritems(), key=lambda d: d[1])
        return hospitals_rating_dict.iteritems()


    def timely_rank(self, hospitals_nc):
        # dict use to sort
        hospitals_rating_dict = dict()

        for current_hospital in hospitals_nc:

            # all payment_measurements for given provider_id
            payment_measurements = Normalized_Timely.objects.filter(
                provider_id=current_hospital.provider_id)
            n_score_sum = 0
            n_score_count = 0
            for measurement in payment_measurements:
                # conver $xx,xxx string to int

                n_score_sum += measurement.n_score
                n_score_count += 1

                hospitals_rating_dict[current_hospital.provider_id] = n_score_sum / n_score_count

        # Sort
        # hospitals_rating_dict_sorted = sorted(hospitals_rating_dict.iteritems(), key=lambda d: d[1])
        return hospitals_rating_dict.iteritems()

    def complications_rank(self, hospitals_nc):
        # dict use to sort
        hospitals_rating_dict = dict()

        for current_hospital in hospitals_nc:

            # all payment_measurements for given provider_id
            payment_measurements = Normalized_Complications.objects.filter(
                provider_id=current_hospital.provider_id)
            n_score_sum = 0
            n_score_count = 0
            for measurement in payment_measurements:
                # conver $xx,xxx string to int

                n_score_sum += measurement.n_score
                n_score_count += 1

                hospitals_rating_dict[current_hospital.provider_id] = n_score_sum / n_score_count

        # Sort
        # hospitals_rating_dict_sorted = sorted(hospitals_rating_dict.iteritems(), key=lambda d: d[1])
        return hospitals_rating_dict.iteritems()

    def returns_rank(self, hospitals_nc):
        # dict use to sort
        hospitals_rating_dict = dict()

        for current_hospital in hospitals_nc:

            # all payment_measurements for given provider_id
            payment_measurements = Normalized_Returns.objects.filter(
                provider_id=current_hospital.provider_id)
            n_score_sum = 0
            n_score_count = 0
            for measurement in payment_measurements:
                # conver $xx,xxx string to int

                n_score_sum += measurement.n_score
                n_score_count += 1

                hospitals_rating_dict[current_hospital.provider_id] = n_score_sum / n_score_count

        # Sort
        # hospitals_rating_dict_sorted = sorted(hospitals_rating_dict.iteritems(), key=lambda d: d[1])
        return hospitals_rating_dict.iteritems()


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

class MD_Score(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey('Hospital', models.DO_NOTHING)
    score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    class Meta:
        managed = True
        db_table = 'MD_Score'

class MD_Hospital(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey('Hospital', models.DO_NOTHING)
    name = models.CharField(max_length=255,null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    education_1 = models.CharField(max_length=255,null=True, blank=True)
    education_2 = models.CharField(max_length=255,null=True, blank=True)
    education_3 = models.CharField(max_length=255,null=True, blank=True)
    education_4 = models.CharField(max_length=255,null=True, blank=True)
    education_5 = models.CharField(max_length=255,null=True, blank=True)
    education_6 = models.CharField(max_length=255,null=True, blank=True)
    field_1 = models.CharField(max_length=255,null=True, blank=True)
    field_2 = models.CharField(max_length=255,null=True, blank=True)
    field_3 = models.CharField(max_length=255,null=True, blank=True)
    field_4 = models.CharField(max_length=255,null=True, blank=True)
    field_5 = models.CharField(max_length=255,null=True, blank=True)
    field_6 = models.CharField(max_length=255,null=True, blank=True)
    hospital_1 = models.CharField(max_length=255,null=True, blank=True)
    hospital_2 = models.CharField(max_length=255,null=True, blank=True)
    hospital_3 = models.CharField(max_length=255,null=True, blank=True)
    hospital_4 = models.CharField(max_length=255,null=True, blank=True)
    hospital_5 = models.CharField(max_length=255,null=True, blank=True)
    hospital_6 = models.CharField(max_length=255,null=True, blank=True)
    phone = models.CharField(max_length=255,null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'MD_Hospital'
