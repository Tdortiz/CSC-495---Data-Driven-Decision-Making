from __future__ import unicode_literals
from django.db import models


class Footnote(models.Model):
    footnote = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    footnote_text = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        managed = True
        db_table = u'"Footnotes"'

class Hospital(models.Model):
    provider_id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    hospital_name = models.CharField(null=True, blank=True, max_length=50)
    address = models.CharField(null=True, blank=True, max_length=50)
    city = models.CharField(null=True, blank=True, max_length=50)
    state = models.CharField(default='', max_length=2, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    county_name = models.CharField(null=True, blank=True, max_length=50)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    hospital_type = models.CharField(null=True, blank=True, max_length=50)
    hospital_ownership = models.CharField(null=True, blank=True, max_length=50)
    emergency_services = models.BooleanField(default=False, blank=True, max_length=50)
    meets_criteria_for_meaningful_use_of_ehrs = models.CharField(default='', max_length=1, blank=True)
    hospital_overall_rating = models.IntegerField(default=0, null=True, blank=True)
    hospital_overall_rating_footnote = models.CharField(null=True, blank=True, max_length=50)
    mortality_national_comparison = models.CharField(null=True, blank=True, max_length=50)
    mortality_national_comparison_footnote = models.CharField(null=True, blank=True, max_length=50)
    safety_of_care_national_comparison = models.CharField(null=True, blank=True, max_length=50)
    safety_of_care_national_comparison_footnote = models.CharField(null=True, blank=True, max_length=50)
    readmission_national_comparison = models.CharField(null=True, blank=True, max_length=50)
    readmission_national_comparison_footnote = models.CharField(null=True, blank=True, max_length=50)
    patient_experience_national_comparison = models.CharField(null=True, blank=True, max_length=50)
    patient_experience_national_comparison_footnote = models.CharField(null=True, blank=True, max_length=50)
    effectiveness_of_care_national_comparison = models.CharField(null=True, blank=True, max_length=50)
    effectiveness_of_care_national_comparison_footnote = models.CharField(null=True, blank=True, max_length=50)
    timeliness_of_care_national_comparison = models.CharField(null=True, blank=True, max_length=50)
    timeliness_of_care_national_comparison_footnote = models.CharField(null=True, blank=True, max_length=50)
    efficient_use_of_medical_imaging_national_comparison = models.CharField(null=True, blank=True, max_length=50)
    efficient_use_of_medical_imaging_national_comparison_footnote = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        managed = True
        db_table = u'"Hospital"'

class HospitalReturns_Hospital(models.Model):
    provider_id = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    measure_name = models.CharField(null=True, blank=True, max_length=50)
    measure_id = models.CharField(default='', max_length=231, blank=True)
    compared_to_national = models.CharField(default='', max_length=242, blank=True)
    denominator = models.IntegerField(default=0, null=True, blank=True)
    score = models.DecimalField(default=0, null=True, max_digits=33, decimal_places=10, blank=True)
    lower_estimate = models.DecimalField(default=0, null=True, max_digits=33, decimal_places=10, blank=True)
    higher_estimate = models.DecimalField(default=0, null=True, max_digits=33, decimal_places=10, blank=True)
    footnote = models.ForeignKey('Footnote', on_delete=models.CASCADE)
    measure_start_date = models.DateTimeField(null=True, blank=True)
    measure_end_date = models.CharField(default='', max_length=10, blank=True)

    class Meta:
        managed = True
        db_table = u'"HospitalReturns_Hospital"'

