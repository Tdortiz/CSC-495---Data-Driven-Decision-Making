from __future__ import unicode_literals
from django.db import models


'''
    The hospital ranking algorithm
'''
class HospitalRankingAlgorithm:

    filters = {}
    hospital_ranked_list = []

    def __init__(self, filters):
        self.filters = filters
        self.hospital_ranked_list = []
    
    '''
        Using the filters (Low = .75, Med = 1, High = 1.25) weight the 
        given metrics to create a weighted sum.

        Using that weighted sum, order the hospital list by it from [highest, ..., lowest] 
    '''
    def rank_hospitals_by_filters(self):
        # Pull sql data
        hospital = Hospital.objects.filter(provider_id=10001)

        # Ranking it

        # Return it
        self.hospital_ranked_list.append("Hospital 1")
        self.hospital_ranked_list.append("Hospital 2")
        self.hospital_ranked_list.append("Hospital 3")
        return self.hospital_ranked_list


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
        managed = True
        db_table = 'PaymentAndValueOfCare_Hospital'


class StructuralMeasures_Hospital(models.Model):
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