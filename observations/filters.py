"""Filters for WAStD Observations."""
from django_filters import FilterSet
from django_filters.filters import (  # noqa
    DateFilter,  # DateTimeFilter,
    BooleanFilter,
    CharFilter,
    RangeFilter,
    ChoiceFilter,
    MultipleChoiceFilter,
    ModelChoiceFilter,
    ModelMultipleChoiceFilter,
)
from shared.filters import FILTER_OVERRIDES
from .models import (
    HEALTH_CHOICES,
    Area,
    Survey,
    Encounter,
    AnimalEncounter,
    TurtleNestEncounter,
    # LoggerEncounter,
    LineTransectEncounter,
)


class SurveyFilter(FilterSet):
    """Survey Filter.

    https://django-filter.readthedocs.io/en/latest/usage.html
    """

    no_start = BooleanFilter(
        label="Start Point reconstructed", field_name="source_id", lookup_expr="isnull"
    )

    no_end = BooleanFilter(
        label="End Point reconstructed",
        field_name="end_source_id",
        lookup_expr="isnull",
    )

    area = ModelChoiceFilter(
        label="Locality",
        queryset=Area.objects.filter(
            area_type__in=[
                Area.AREATYPE_LOCALITY,
            ]
        ).order_by("-northern_extent", "name"),
    )

    site = ModelChoiceFilter(
        label="Site",
        queryset=Area.objects.filter(
            area_type__in=[
                Area.AREATYPE_SITE,
            ]
        ).order_by("-northern_extent", "name"),
        # method='taxa_occurring_in_area'
    )

    survey_date = DateFilter(
        field_name="start_time",
        lookup_expr="date",
        label="Exact survey date (YYYY-mm-dd)",
    )

    # duplicates = BooleanFilter(
    #     label="Duplicates",
    #     field_name='has_duplicates',
    # )

    class Meta:
        """Options for SurveyFilter."""

        model = Survey
        filter_overrides = FILTER_OVERRIDES
        fields = [
            "campaign__owner",
            "area",
            "site",
            "no_start",
            "no_end",
            "production",
            "source",
            "source_id",
            "device_id",
            "reporter",
            "start_location",
            "start_location_accuracy_m",
            "start_time",
            "start_comments",
            "end_source_id",
            "end_device_id",
            "end_location",
            "end_location_accuracy_m",
            "end_time",
            "end_comments",
            # 'team', # m2m
            # 'label',
            "transect",
        ]


class EncounterFilter(FilterSet):
    """Encounter Filter.

    https://django-filter.readthedocs.io/en/latest/usage.html
    """

    area = ModelChoiceFilter(
        label="Locality",
        queryset=Area.objects.filter(
            area_type__in=[
                Area.AREATYPE_LOCALITY,
            ]
        ).order_by("-northern_extent", "name"),
        # method='taxa_occurring_in_area'
    )
    site = ModelChoiceFilter(
        label="Site",
        queryset=Area.objects.filter(
            area_type__in=[
                Area.AREATYPE_SITE,
            ]
        ).order_by("-northern_extent", "name"),
        # method='taxa_occurring_in_area'
    )

    encounter_date = DateFilter(
        field_name="when", lookup_expr="date", label="Exact encounter date (YYYY-mm-dd)"
    )

    class Meta:
        """Options for EncounterFilter."""

        model = Encounter
        filter_overrides = FILTER_OVERRIDES
        fields = [
            "campaign__owner",
            "area",
            "site",
            "when",
            "where",
            "reporter",
            "observer",
            "encounter_type",
            "source",
        ]


class AnimalEncounterFilter(EncounterFilter):

    health = MultipleChoiceFilter(choices=HEALTH_CHOICES)

    class Meta(EncounterFilter.Meta):

        model = AnimalEncounter
        fields = EncounterFilter._meta.fields + [
            "identifiers",
            "taxon",
            "species",
            "sex",
            "maturity",
            "health",
            "activity",
            "habitat",
            "sighting_status",
            "sighting_status_reason",
            "datetime_of_last_sighting",
            "site_of_first_sighting",
            "site_of_last_sighting",
            "nesting_event",
            "nesting_disturbed",
            "laparoscopy",
            "checked_for_injuries",
            "scanned_for_pit_tags",
            "checked_for_flipper_tags",
            "cause_of_death",
        ]


class TurtleNestEncounterFilter(EncounterFilter):
    class Meta(EncounterFilter.Meta):

        model = TurtleNestEncounter
        fields = EncounterFilter._meta.fields + [
            "species",
            "nest_type",
            "nest_age",
            "habitat",
            "disturbance",
            "nest_tagged",
            "logger_found",
            "eggs_counted",
            "hatchlings_measured",
            "fan_angles_measured",
        ]


# class LoggerEncounterFilter(EncounterFilter):

#     class Meta(EncounterFilter.Meta):

#         model = LoggerEncounter
#         fields = EncounterFilter._meta.fields + [
#             'logger_type',
#             'deployment_status',
#             'logger_id',
#         ]


class LineTransectEncounterFilter(EncounterFilter):
    class Meta(EncounterFilter.Meta):

        model = LineTransectEncounter
        fields = EncounterFilter._meta.fields + [
            "transect",
        ]